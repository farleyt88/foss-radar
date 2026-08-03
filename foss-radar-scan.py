#!/usr/bin/env python3
"""
FOSS Radar Scanner — Improved scoring engine with vendor inflation prevention.

Key design principles:
  - Vendor bonus ONLY applies to tools with MANUALLY VERIFIED vendor support
    (field: "vendor_verified": true in the JSON)
  - Auto-scanned tools with vendor keywords in description do NOT get vendor bonus
  - Generic protocol terms (netconf, yang, gnmi) are high-relevance but NOT vendor-specific
  - Deduplication by URL is enforced on every run
  - Full catalog doc regeneration (no fragile regex patching)

Scoring guide (max ~250 for a perfectly relevant tool):
  vendor_verified + vendor in list:  +40 per vendor (capped at 3 vendors = 120)
  high relevance keywords:           +8 each
  medium relevance keywords:         +4 each
  GitHub stars bonus:                +2 to +20
  Recent activity (2025/2026):       +5
"""

import json
import os
import re
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

SCRIPT_DIR = Path(__file__).resolve().parent
SECOND_BRAIN_DOC = SCRIPT_DIR / "CATALOG.md"
TOOLS_DB = SCRIPT_DIR / "data" / "tools.json"
SCAN_LOG = SCRIPT_DIR / "data" / "scan-history.json"
CATEGORIES_DIR = SCRIPT_DIR / "categories"
TOOLS_DB.parent.mkdir(parents=True, exist_ok=True)

# Target vendor names — ONLY these trigger vendor bonus (when verified=True)
VENDOR_NAMES = {"ciena", "saos", "nokia", "ribbon", "aviat", "sel icon", "sel-icon"}

# Generic protocol keywords — high relevance but NOT vendor-specific
# These were previously (wrongly) in the vendor bucket, causing inflation
PROTOCOL_KEYWORDS = {
    "netconf", "yang", "restconf", "gnmi", "grpc", "openconfig",
    "netflow", "sflow", "ipfix", "snmp", "tl1", "cli automation"
}

# High relevance — directly related to transport network engineering
HIGH_KEYWORDS = {
    "network automation", "transport", "telecom", "carrier ethernet", "mpls",
    "optical", "dwdm", "otn", "sonet", "sdh", "microwave", "fiber",
    "ansible", "nornir", "nautobot", "netbox", "napalm",
    "grafana", "observability", "monitoring", "telemetry", "streaming",
    "topology", "visualization", "inventory", "source of truth",
    "grist", "dashboard", "circuit", "provisioning",
}

# Medium relevance
MEDIUM_KEYWORDS = {
    "network", "infrastructure", "devops", "sre", "api", "rest",
    "python", "configuration", "automation", "self-hosted",
    "open source", "cli", "terminal", "pipeline", "data",
}


def load_tools_db():
    if TOOLS_DB.exists():
        with open(TOOLS_DB) as f:
            data = json.load(f)
        # Handle both list and dict formats
        return data if isinstance(data, list) else data.get("tools", [])
    return []


def atomic_write(path, content):
    """Write text atomically so interrupted weekly runs cannot corrupt data."""
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode & 0o777 if path.exists() else 0o644
    with tempfile.NamedTemporaryFile(
        "w", dir=path.parent, prefix=f".{path.name}.", delete=False
    ) as handle:
        handle.write(content)
        handle.flush()
        os.fsync(handle.fileno())
        temp_path = Path(handle.name)
    temp_path.chmod(mode)
    temp_path.replace(path)


def save_tools_db(tools):
    atomic_write(TOOLS_DB, json.dumps(tools, indent=2, default=str) + "\n")


def normalize_url(url):
    """Normalize repository URLs for stable duplicate detection."""
    value = (url or "").strip().rstrip("/")
    parts = urlsplit(value)
    scheme = "https" if parts.scheme.lower() in {"http", "https"} else parts.scheme.lower()
    host = parts.netloc.lower()
    path = parts.path.rstrip("/")
    if host in {"github.com", "www.github.com"}:
        host = "github.com"
        path = path.removesuffix(".git").lower()
    return urlunsplit((scheme, host, path, parts.query, parts.fragment))


def markdown_text(value, limit=None):
    """Keep generated Markdown tables valid when metadata contains formatting."""
    text = " ".join(str(value or "").split()).replace("|", "/")
    if limit and len(text) > limit:
        text = text[: limit - 3] + "..."
    return text


def category_slug(category):
    """Return a stable, filesystem-safe category filename."""
    slug = category.lower().replace("&", "and").replace("/", "-")
    slug = re.sub(r"[^a-z0-9-]", "", slug.replace(" ", "-"))
    return re.sub(r"-+", "-", slug).strip("-") or "uncategorized"


def deduplicate(tools):
    """Remove duplicate entries. Keep highest-scored entry per URL, then per name."""
    # By URL first
    by_url = {}
    for t in tools:
        url = normalize_url(t.get("url", ""))
        if not url:
            continue
        score = t.get("relevance_score", 0)
        if url not in by_url or score > by_url[url].get("relevance_score", 0):
            by_url[url] = t

    # Then by name (case-insensitive), prefer the URL-keyed one
    by_name = {}
    for t in by_url.values():
        key = t.get("name", "").casefold().strip()
        if key not in by_name or t.get("relevance_score", 0) > by_name[key].get("relevance_score", 0):
            by_name[key] = t

    return list(by_name.values())


def calculate_relevance_score(tool):
    """
    Calculate relevance score. Vendor bonus ONLY if vendor_verified=True.
    Prevents score inflation from generic protocol keywords.
    """
    score = 0
    text = " ".join([
        tool.get("name", ""),
        tool.get("description", ""),
        " ".join(tool.get("topics", [])),
    ]).lower()

    # --- Vendor bonus (VERIFIED ONLY) ---
    # This is the critical fix: only give vendor points when manually confirmed
    if tool.get("vendor_verified", False):
        verified_vendors = 0
        seen_vendors = set()
        for vendor in tool.get("vendors", []):
            normalized_vendor = vendor.lower().replace(" ", "")
            if normalized_vendor in seen_vendors:
                continue
            seen_vendors.add(normalized_vendor)
            if normalized_vendor in {v.replace(" ", "") for v in VENDOR_NAMES}:
                score += 40  # Strong bonus for confirmed vendor support
                verified_vendors += 1
                if verified_vendors == 3:
                    break

    # --- Protocol keyword bonus (high relevance, not vendor-specific) ---
    for kw in PROTOCOL_KEYWORDS:
        if kw in text:
            score += 10

    # --- Domain relevance ---
    for kw in HIGH_KEYWORDS:
        if kw in text:
            score += 8

    for kw in MEDIUM_KEYWORDS:
        if kw in text:
            score += 4

    # --- Stars bonus ---
    stars = tool.get("stars", 0) or 0
    if stars > 10000:
        score += 20
    elif stars > 5000:
        score += 15
    elif stars > 1000:
        score += 10
    elif stars > 500:
        score += 7
    elif stars > 100:
        score += 4
    elif stars > 10:
        score += 2

    # --- Activity bonus ---
    updated = str(tool.get("updated", ""))
    match = re.search(r"\b(20\d{2})\b", updated)
    current_year = datetime.now().year
    if match and int(match.group(1)) >= current_year - 1:
        score += 5

    return score


def generate_catalog_doc(tools):
    """Fully regenerate the FOSS Radar catalog doc from current data."""
    today = datetime.now().strftime("%m-%d-%Y")
    now = datetime.now().strftime("%m-%d-%Y %H:%M")

    sorted_tools = sorted(tools, key=lambda x: x.get("relevance_score", 0), reverse=True)

    # Category breakdown
    cats = Counter(t.get("category", "Uncategorized") for t in tools)
    cat_str = ", ".join(
        f"{k} ({v})" for k, v in sorted(cats.items(), key=lambda x: -x[1])[:8]
    )

    # Top 60 table
    rows = []
    for i, t in enumerate(sorted_tools[:60], 1):
        name = markdown_text(t.get("name", "?"))
        url = t.get("url", "#")
        cat = markdown_text(t.get("category", "—"))
        desc = markdown_text(t.get("description", "—"), 100)
        stars = t.get("stars", 0)
        stars_str = f"{stars:,}" if isinstance(stars, int) and stars > 0 else "—"
        vendors = t.get("vendors", [])
        vendor_str = ", ".join(vendors) if vendors else "—"
        verified = " ✓" if t.get("vendor_verified") else ""
        rows.append(
            f"| {i} | [{name}]({url}) | {cat} | {desc} | {vendor_str}{verified} | {stars_str} |"
        )

    table = "\n".join(rows)

    # Full catalog by category
    by_cat = {}
    for t in sorted_tools:
        cat = t.get("category", "Uncategorized")
        by_cat.setdefault(cat, []).append(t)

    cat_sections = []
    for cat in sorted(by_cat.keys(), key=lambda c: -len(by_cat[c])):
        items = by_cat[cat]
        lines = [f"\n### {cat} ({len(items)} tools)\n"]
        for t in items:
            name = markdown_text(t.get("name", "?"))
            url = t.get("url", "#")
            desc = markdown_text(t.get("description", ""), 120)
            vendors = t.get("vendors", [])
            verified = t.get("vendor_verified", False)
            vendor_badge = ""
            if vendors:
                tick = " ✓" if verified else " (?)"
                vendor_badge = f" `{'` `'.join(vendors)}`{tick}"
            lines.append(f"- **[{name}]({url})**{vendor_badge} — {desc}")
        cat_sections.append("\n".join(lines))

    full_catalog = "\n".join(cat_sections)

    doc = f"""---
title: "FOSS Radar"
category: "Reference"
tags: ["foss", "tools", "automation", "network"]
created: "02-03-2026"
updated: "{today}"
---

# FOSS Radar 📡

A continuously updated list of Free and Open Source tools relevant to Transport Network Traffic Engineering, automation, and modernization.

**Last Scan:** {now}
**Total Tools Tracked:** {len(tools)}
**Categories:** {cat_str}

> **Scoring note:** Vendor bonus (+40/vendor) applies ONLY to tools with confirmed, verified support
> for target vendors (Ciena SAOS 6x/8x/10, Nokia SR OS/SR Linux, Ribbon, Aviat). Marked with ✓ in the
> vendor column. Generic NETCONF/YANG tools are scored on utility alone — not inflated by protocol
> keywords. Scoring engine modernized: 08-03-2026.

---

## 🏆 Top 60 by Relevance Score

*Ranked by confirmed relevance. ✓ = vendor support manually verified.*

| Rank | Tool | Category | Description | Vendors | Stars |
|------|------|----------|-------------|---------|-------|
{table}

---

## 📚 Full Catalog by Category

*Vendor tags: ✓ = verified, (?) = auto-tagged, needs verification*

{full_catalog}
"""

    atomic_write(SECOND_BRAIN_DOC, doc)

    return len(tools)


def generate_category_docs(tools):
    """Regenerate per-category pages and retire stale category files."""
    grouped = {}
    for tool in tools:
        grouped.setdefault(tool.get("category") or "Uncategorized", []).append(tool)

    expected = set()
    slug_categories = {}
    for category, category_tools in grouped.items():
        slug = category_slug(category)
        if slug in slug_categories and slug_categories[slug] != category:
            raise ValueError(
                f"Category slug collision: {slug_categories[slug]!r} and {category!r}"
            )
        slug_categories[slug] = category
        filename = f"{slug}.md"
        expected.add(filename)
        lines = [
            f"# {category}",
            "",
            f"**{len(category_tools)} tools** — sorted by relevance score.",
            "",
            "[← Back to FOSS Radar](../README.md)",
            "",
            "| Score | Tool | Description | Vendors |",
            "|------:|------|-------------|---------|",
        ]
        for tool in sorted(
            category_tools,
            key=lambda item: item.get("relevance_score", 0),
            reverse=True,
        ):
            name = markdown_text(tool.get("name", "Unknown"))
            url = tool.get("url", "")
            description = markdown_text(tool.get("description", ""), 100)
            score = tool.get("relevance_score", 0)
            vendors = ", ".join(tool.get("vendors", [])) or "—"
            if tool.get("vendor_verified") and tool.get("vendors"):
                vendors += " ✅"
            link = f"[{name}]({url})" if url else name
            lines.append(f"| {score} | {link} | {description} | {vendors} |")
        lines.append("")
        atomic_write(CATEGORIES_DIR / filename, "\n".join(lines))

    for old_file in CATEGORIES_DIR.glob("*.md"):
        if old_file.name not in expected:
            old_file.unlink()

    return len(expected)


def log_scan(new=0, updated=0, total=0, deduped=0):
    scans = []
    if SCAN_LOG.exists():
        with open(SCAN_LOG) as f:
            scans = json.load(f)
    scans.append({
        "timestamp": datetime.now().astimezone().isoformat(),
        "new": new,
        "updated": updated,
        "deduped": deduped,
        "total": total,
    })
    scans = scans[-100:]
    atomic_write(SCAN_LOG, json.dumps(scans, indent=2) + "\n")


def main():
    print(f"FOSS Radar Scan — {datetime.now().strftime('%m-%d-%Y %H:%M')}")

    tools = load_tools_db()
    original_count = len(tools)

    # Step 1: Deduplicate
    tools = deduplicate(tools)
    deduped = original_count - len(tools)
    if deduped:
        print(f"  Deduplication: removed {deduped} duplicates ({original_count} → {len(tools)})")

    # Step 2: Recalculate all scores with improved logic
    updated = 0
    for t in tools:
        old = t.get("relevance_score", 0)
        new = calculate_relevance_score(t)
        if new != old:
            t["relevance_score"] = new
            updated += 1

    if updated:
        print(f"  Scores recalculated: {updated} tools updated")

    # Step 3: Save
    save_tools_db(tools)

    # Step 4: Regenerate catalog doc
    generate_catalog_doc(tools)
    print(f"  Catalog doc regenerated — {len(tools)} tools")

    category_count = generate_category_docs(tools)
    print(f"  Category docs regenerated — {category_count} categories")

    log_scan(updated=updated, total=len(tools), deduped=deduped)
    print(f"  Done.")

    # Print top 10 for confirmation
    sorted_tools = sorted(tools, key=lambda x: x.get("relevance_score", 0), reverse=True)
    print("\nTop 10:")
    for i, t in enumerate(sorted_tools[:10], 1):
        score = t.get("relevance_score", 0)
        verified = "✓" if t.get("vendor_verified") else " "
        vendors = t.get("vendors", [])
        vendor_str = f"[{', '.join(vendors)}]" if vendors else "[]"
        print(f"  {i:>2}. [{score:>3}]{verified} {t.get('name')} {vendor_str}")


if __name__ == "__main__":
    main()
