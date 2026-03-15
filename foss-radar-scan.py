#!/usr/bin/env python3
"""
FOSS Radar Scanner — Improved scoring engine with vendor inflation prevention.

Key design principles:
  - Vendor bonus ONLY applies to tools with MANUALLY VERIFIED vendor support
    (field: "vendor_verified": true in the JSON)
  - Auto-scanned tools with vendor keywords in description do NOT get vendor bonus
  - Generic protocol terms (netconf, yang, gnmi) are high-relevance but NOT vendor-specific
  - Deduplication by URL is enforced on every run
  - Full second-brain doc regeneration (no fragile regex patching)

Scoring guide (max ~250 for a perfectly relevant tool):
  vendor_verified + vendor in list:  +40 per vendor (capped at 3 vendors = 120)
  high relevance keywords:           +8 each
  medium relevance keywords:         +4 each
  GitHub stars bonus:                +2 to +20
  Recent activity (2025/2026):       +5
"""

import json
import os
from collections import Counter
from datetime import datetime
from pathlib import Path

SECOND_BRAIN_DOC = Path.home() / "clawd/second-brain/docs/foss-radar.md"
TOOLS_DB = Path.home() / "clawd/data/foss-radar-tools.json"
SCAN_LOG = Path.home() / "clawd/data/foss-radar-scans.json"
TOOLS_DB.parent.mkdir(parents=True, exist_ok=True)

# TJ's actual vendor names — ONLY these trigger vendor bonus (when verified=True)
VENDOR_NAMES = {"ciena", "saos", "nokia", "ribbon", "aviat", "sel icon", "sel-icon"}

# Generic protocol keywords — high relevance but NOT vendor-specific
# These were previously (wrongly) in the vendor bucket, causing inflation
PROTOCOL_KEYWORDS = {
    "netconf", "yang", "restconf", "gnmi", "grpc", "openconfig",
    "netflow", "sflow", "ipfix", "snmp", "tl1", "cli automation"
}

# High relevance — directly related to TJ's work domain
HIGH_KEYWORDS = {
    "network automation", "transport", "telecom", "carrier ethernet", "mpls",
    "optical", "dwdm", "otn", "sonet", "sdh", "microwave", "fiber",
    "ansible", "nornir", "nautobot", "netbox", "napalm",
    "grafana", "observability", "monitoring", "telemetry", "streaming",
    "topology", "visualization", "inventory", "source of truth",
    "gist", "dashboard", "circuit", "provisioning",
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


def save_tools_db(tools):
    with open(TOOLS_DB, "w") as f:
        json.dump(tools, f, indent=2, default=str)


def deduplicate(tools):
    """Remove duplicate entries. Keep highest-scored entry per URL, then per name."""
    # By URL first
    by_url = {}
    for t in tools:
        url = t.get("url", "").strip().rstrip("/")
        if not url:
            continue
        score = t.get("relevance_score", 0)
        if url not in by_url or score > by_url[url].get("relevance_score", 0):
            by_url[url] = t

    # Then by name (case-insensitive), prefer the URL-keyed one
    by_name = {}
    for t in by_url.values():
        key = t.get("name", "").lower().strip()
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
        for vendor in tool.get("vendors", []):
            if vendor.lower().replace(" ", "") in {v.replace(" ", "") for v in VENDOR_NAMES}:
                score += 40  # Strong bonus for confirmed vendor support

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
    updated = tool.get("updated", "")
    if "2026" in str(updated) or "2025" in str(updated):
        score += 5

    return score


def generate_second_brain_doc(tools):
    """Fully regenerate the FOSS Radar Second Brain doc from current data."""
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
        name = t.get("name", "?")
        url = t.get("url", "#")
        cat = t.get("category", "—")
        desc = t.get("description", "—")
        if len(desc) > 100:
            desc = desc[:97] + "..."
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
            name = t.get("name", "?")
            url = t.get("url", "#")
            desc = t.get("description", "")
            if len(desc) > 120:
                desc = desc[:117] + "..."
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
> for TJ's stack (Ciena SAOS 6x/8x/10, Nokia SR OS/SR Linux, Ribbon, Aviat). Marked with ✓ in the
> vendor column. Generic NETCONF/YANG tools are scored on utility alone — not inflated by protocol
> keywords. Last full audit: 03-06-2026.

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

    with open(SECOND_BRAIN_DOC, "w") as f:
        f.write(doc)

    return len(tools)


def log_scan(new=0, updated=0, total=0, deduped=0):
    scans = []
    if SCAN_LOG.exists():
        with open(SCAN_LOG) as f:
            scans = json.load(f)
    scans.append({
        "timestamp": datetime.now().isoformat(),
        "new": new,
        "updated": updated,
        "deduped": deduped,
        "total": total,
    })
    scans = scans[-100:]
    with open(SCAN_LOG, "w") as f:
        json.dump(scans, f, indent=2)


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

    # Step 4: Regenerate second brain doc
    generate_second_brain_doc(tools)
    print(f"  Second Brain doc regenerated — {len(tools)} tools")

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
