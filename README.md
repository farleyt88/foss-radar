# 📡 FOSS Radar

**A curated, scored database of 356+ Free and Open Source tools for network automation, observability, and transport network modernization.**

Built for network engineers working with **Ciena, Nokia, Ribbon, Aviat, and SEL ICON** equipment — but useful for anyone in telecom/transport networking.

[![Tools Tracked](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffarleyt88%2Ffoss-radar%2Fmain%2Fdata%2Ftools.json&query=%24.length&label=Tools%20Tracked&color=blue)]()
[![Vendor Verified](https://img.shields.io/badge/Vendor_Verified-45-green)]()
[![Categories](https://img.shields.io/badge/Categories-29-orange)]()
[![Last Scan](https://img.shields.io/badge/Last_Scan-03--16--2026-brightgreen)]()

---

## What Is This?

FOSS Radar is a continuously maintained database of open source tools relevant to **transport network traffic engineering**. Every tool is scored by a relevance engine that factors in:

- Vendor-specific support (Nokia, Ciena, Ribbon, Aviat, SEL ICON)
- Protocol relevance (NETCONF, YANG, gNMI, OpenConfig, etc.)
- Domain match (network automation, telecom, MPLS, optical, etc.)
- Project activity and community size

The goal: **find the right open source tool for your network problem, fast.**

---

## 📊 Scoring System

Every tool gets a **relevance score** (0–250+) based on four weighted categories:

### 1. Vendor Bonus — up to +120 points

| Condition | Points |
|-----------|--------|
| Tool has **verified** support for a target vendor | **+40 per vendor** (max 3 = 120) |
| Auto-tagged vendor keyword (unverified) | +0 (no bonus) |

**Target vendors:** Ciena (SAOS 6x/8x/10), Nokia (SR OS, SR Linux), Ribbon, Aviat, SEL ICON

> ⚠️ **Vendor bonus is integrity-protected.** Only tools with `"vendor_verified": true` in the database get vendor points. A tool mentioning "Nokia" in its description does NOT automatically score vendor points — it must be manually verified to actually support that vendor's platform. This prevents score inflation from keyword stuffing.

Tools marked with ✅ in the tables have verified vendor support. Tools marked with (?) are auto-tagged and pending verification.

### 2. Protocol Keywords — +10 each

Points awarded for each matching protocol keyword found in the tool's name, description, or topics:

| Keywords |
|----------|
| `netconf`, `yang`, `restconf`, `gnmi`, `grpc`, `openconfig` |
| `netflow`, `sflow`, `ipfix`, `snmp`, `tl1`, `cli automation` |

These are high-relevance protocols for transport network management, but they are **not treated as vendor-specific** — preventing generic NETCONF libraries from inflating into the top 10.

### 3. Domain Relevance — +4 to +8 each

**High relevance (+8 each):**

| Keywords |
|----------|
| `network automation`, `transport`, `telecom`, `carrier ethernet`, `mpls` |
| `optical`, `dwdm`, `otn`, `sonet`, `sdh`, `microwave`, `fiber` |
| `ansible`, `nornir`, `nautobot`, `netbox`, `napalm` |
| `grafana`, `observability`, `monitoring`, `telemetry`, `streaming` |
| `topology`, `visualization`, `inventory`, `source of truth` |
| `dashboard`, `circuit`, `provisioning` |

**Medium relevance (+4 each):**

| Keywords |
|----------|
| `network`, `infrastructure`, `devops`, `sre`, `api`, `rest` |
| `python`, `configuration`, `automation`, `self-hosted` |
| `open source`, `cli`, `terminal`, `pipeline`, `data` |

### 4. Community & Activity — up to +25 points

| GitHub Stars | Points |
|-------------|--------|
| 10,000+ | +20 |
| 5,000+ | +15 |
| 1,000+ | +10 |
| 500+ | +7 |
| 100+ | +4 |
| 10+ | +2 |

| Activity | Points |
|----------|--------|
| Updated in 2025 or 2026 | +5 |

### Score Examples

| Tool | Score | Breakdown |
|------|-------|-----------|
| **GtExporter** | 146 | Nokia ✅ (+40) + Ciena ✅ (+40) + gnmi/yang/openconfig (+30) + telemetry/monitoring (+16) + activity (+5) + stars (+2) + misc keywords |
| **NAPALM** | 137 | Ciena ✅ (+40) + Nokia ✅ (+40) + network automation/napalm (+16) + stars 2.2k (+10) + activity (+5) + misc keywords |
| **VictoriaMetrics** | 85 | No vendor bonus + monitoring/observability/telemetry (+24) + stars 13.5k (+20) + activity (+5) + misc keywords |
| **Netmiko** | 49 | No vendor bonus + network/automation/ssh (+12) + stars 3.5k (+10) + activity (+5) + misc keywords |

---

## 🏆 Top 30 Tools

| Rank | Tool | Score | Vendors | Stars | Description |
|------|------|-------|---------|-------|-------------|
| 1 | [GtExporter](https://github.com/automixer/gtexporter) | 146 | Nokia, Ciena ✅ | — | YANG data-model-aware gNMI streaming telemetry exporter for Prometheus |
| 2 | [NAPALM](https://github.com/napalm-automation/napalm) | 137 | Ciena, Nokia ✅ | 2,200 | Multi-vendor network device interaction via unified API |
| 3 | [OpenConfig Feature Profiles](https://github.com/openconfig/featureprofiles) | 117 | Nokia, Ciena ✅ | 250 | OpenConfig path definitions and Ondatra test suites |
| 4 | [OpenConfig gNMI](https://github.com/openconfig/gnmi) | 116 | Nokia ✅ | 572 | gRPC Network Management Interface specification and reference implementation |
| 5 | [NetBox DeviceType Library](https://github.com/netbox-community/devicetype-library) | 107 | Ciena, Nokia ✅ | 1,200 | 51 Ciena and 30 Nokia device types for NetBox |
| 6 | [pydantify](https://github.com/pydantify/pydantify) | 101 | Nokia ✅ | 92 | Transforms YANG models into Pydantic datastructures |
| 7 | [NetGauze](https://github.com/NetGauze/NetGauze) | 101 | Nokia ✅ | 180 | High-performance Rust network protocol parsing and telemetry |
| 8 | [gnmic](https://github.com/openconfig/gnmic) | 98 | Nokia ✅ | 800 | gNMI CLI client and collector for telemetry streams |
| 9 | [gNPSI](https://github.com/openconfig/gnpsi) | 97 | Nokia | 20 | gRPC Network Packet Sampling Interface proposal |
| 10 | [Nokia OSSMediator](https://github.com/nokia/OSSMediator) | 95 | Nokia ✅ | 12 | Collects PM and FM data from Nokia DAC APIs |
| 11 | [Ciena YANG Modules](https://github.com/ciena/yang) | 95 | Ciena ✅ | 5 | Official Ciena YANG data models for SAOS/WaveServer |
| 12 | [ncclient](https://github.com/ncclient/ncclient) | 93 | Nokia ✅ | 500 | Standard Python NETCONF client library |
| 13 | [NAPALM-SROS](https://github.com/napalm-automation-community/napalm-sros) | 91 | Nokia ✅ | 30 | NAPALM driver for Nokia SR OS |
| 14 | [ciena.waveserver5](https://github.com/ciena/ciena.waveserver5) | 91 | Ciena ✅ | 2 | Ansible collection for Ciena Waveserver 5 |
| 15 | [EDA Telemetry Lab](https://github.com/eda-labs/eda-telemetry-lab) | 91 | Nokia ✅ | 27 | Modern telemetry architecture for Nokia EDA + SR Linux |
| 16 | [ntopng](https://github.com/ntop/ntopng) | 86 | — | 6,200 | High-speed network traffic analysis with DPI |
| 17 | [Nokia SR Linux Ansible](https://github.com/nokia/srlinux-ansible-collection) | 85 | Nokia ✅ | — | Official Ansible collection for SR Linux |
| 18 | [Nokia SROS Ansible](https://github.com/nokia/sros-ansible-collection) | 85 | Nokia ✅ | — | Official Ansible collection for SR OS |
| 19 | [VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics) | 85 | — | 13,500 | Fast, Prometheus-compatible time series database |
| 20 | [Inmanta](https://github.com/inmanta/inmanta-core) | 83 | Nokia ✅ | 90 | Intent-based infrastructure orchestration (Nokia) |
| 21 | [notconf](https://github.com/notconf/notconf) | 83 | Nokia ✅ | 150 | NETCONF/RESTCONF device simulator |
| 22 | [ANX](https://github.com/cisco-ie/anx) | 83 | — | 200 | Graphical YANG model explorer for NETCONF devices |
| 23 | [nokia-sros-automation](https://github.com/karneliuk-com/nokia-sros-automation) | 83 | Nokia ✅ | 15 | Nokia SR OS automation demos (pySROS, NETCONF, gNMI) |
| 24 | [pydantic-srlinux](https://github.com/srl-labs/pydantic-srlinux) | 83 | Nokia ✅ | 15 | Pydantic models from Nokia SR Linux YANG schemas |
| 25 | [napalm-ciena-saos](https://github.com/napalm-automation-community/napalm-ciena-saos) | 83 | Ciena ✅ | 15 | NAPALM driver for Ciena SAOS devices |
| 26 | [pySROS](https://github.com/nokia/pysros) | 81 | Nokia ✅ | — | Python library for Nokia SR OS management |
| 27 | [nokia-netconf-yang](https://github.com/karneliuk-com/nokia-netconf-yang-operations) | 81 | Nokia ✅ | 3 | NETCONF/YANG operation examples for Nokia SR OS |
| 28 | [ktranslate](https://github.com/kentik/ktranslate) | 81 | — | 250 | Network data collection: SNMP, NetFlow, sFlow, IPFIX |
| 29 | [GoFlow2](https://github.com/netsampler/goflow2) | 81 | — | 1,400 | High-performance NetFlow/IPFIX/sFlow collector in Go |
| 30 | [SR Linux YANG Browser](https://github.com/srl-labs/yang-browser) | 79 | Nokia ✅ | 50 | Web portal for browsing Nokia SR Linux YANG models |

---

## 📚 Full Catalog

### By Category

| Category | Count |
|----------|-------|
| [Network Automation](CATALOG.md#network-automation) | 223 |
| [Observability](CATALOG.md#observability) | 76 |
| [Network Management](CATALOG.md#network-management) | 7 |
| [CLI Tools](CATALOG.md#cli-tools) | 5 |
| [Self-Hosted](CATALOG.md#self-hosted) | 4 |
| [Infrastructure as Code](CATALOG.md#infrastructure-as-code) | 4 |
| [Network Observability](CATALOG.md#network-observability) | 4 |
| [IPAM](CATALOG.md#ipam) | 3 |
| [Network Simulation](CATALOG.md#network-simulation) | 3 |
| [Network Testing](CATALOG.md#network-testing) | 3 |
| [Network Monitoring](CATALOG.md#network-monitoring) | 3 |
| [Data Management](CATALOG.md#data-management) | 2 |
| [Network Diagnostics](CATALOG.md#network-diagnostics) | 2 |
| [Other Categories](CATALOG.md) | 17 |

> **Full tool catalog with links, scores, and descriptions:** See [`CATALOG.md`](CATALOG.md)

---

## 🔍 Vendor-Specific Quick Links

### Nokia (71 tools)

Tools with confirmed or tagged Nokia support:

| Tool | Verified | Link |
|------|----------|------|
| GtExporter | ✅ | [github.com/automixer/gtexporter](https://github.com/automixer/gtexporter) |
| NAPALM | ✅ | [github.com/napalm-automation/napalm](https://github.com/napalm-automation/napalm) |
| OpenConfig Feature Profiles | ✅ | [github.com/openconfig/featureprofiles](https://github.com/openconfig/featureprofiles) |
| OpenConfig gNMI | ✅ | [github.com/openconfig/gnmi](https://github.com/openconfig/gnmi) |
| NetBox DeviceType Library | ✅ | [github.com/netbox-community/devicetype-library](https://github.com/netbox-community/devicetype-library) |
| pydantify | ✅ | [github.com/pydantify/pydantify](https://github.com/pydantify/pydantify) |
| NetGauze | ✅ | [github.com/NetGauze/NetGauze](https://github.com/NetGauze/NetGauze) |
| gnmic | ✅ | [github.com/openconfig/gnmic](https://github.com/openconfig/gnmic) |
| Nokia OSSMediator | ✅ | [github.com/nokia/OSSMediator](https://github.com/nokia/OSSMediator) |
| ncclient | ✅ | [github.com/ncclient/ncclient](https://github.com/ncclient/ncclient) |
| NAPALM-SROS | ✅ | [github.com/napalm-automation-community/napalm-sros](https://github.com/napalm-automation-community/napalm-sros) |
| EDA Telemetry Lab | ✅ | [github.com/eda-labs/eda-telemetry-lab](https://github.com/eda-labs/eda-telemetry-lab) |
| Nokia SR Linux Ansible | ✅ | [github.com/nokia/srlinux-ansible-collection](https://github.com/nokia/srlinux-ansible-collection) |
| Nokia SROS Ansible | ✅ | [github.com/nokia/sros-ansible-collection](https://github.com/nokia/sros-ansible-collection) |
| Inmanta | ✅ | [github.com/inmanta/inmanta-core](https://github.com/inmanta/inmanta-core) |
| notconf | ✅ | [github.com/notconf/notconf](https://github.com/notconf/notconf) |
| nokia-sros-automation | ✅ | [github.com/karneliuk-com/nokia-sros-automation](https://github.com/karneliuk-com/nokia-sros-automation) |
| pydantic-srlinux | ✅ | [github.com/srl-labs/pydantic-srlinux](https://github.com/srl-labs/pydantic-srlinux) |
| pySROS | ✅ | [github.com/nokia/pysros](https://github.com/nokia/pysros) |
| nokia-netconf-yang-operations | ✅ | [github.com/karneliuk-com/nokia-netconf-yang-operations](https://github.com/karneliuk-com/nokia-netconf-yang-operations) |
| SR Linux YANG Browser | ✅ | [github.com/srl-labs/yang-browser](https://github.com/srl-labs/yang-browser) |
| srlinux-ndk-py | ✅ | [github.com/nokia/srlinux-ndk-py](https://github.com/nokia/srlinux-ndk-py) |
| vscode-netconf | ✅ | [github.com/nokia/vscode-netconf](https://github.com/nokia/vscode-netconf) |
| Nokia SR Linux YANG Models | ✅ | [github.com/nokia/srlinux-yang-models](https://github.com/nokia/srlinux-yang-models) |
| Nokia 7x50 YANG Models | ✅ | [github.com/nokia/7x50_YangModels](https://github.com/nokia/7x50_YangModels) |
| moler | ✅ | [github.com/nokia/moler](https://github.com/nokia/moler) |
| cawk | ✅ | [github.com/cedricllorens/cawk](https://github.com/cedricllorens/cawk) |
| sros-enable-netconf | ✅ | [github.com/h4ndzdatm0ld/sros-enable-netconf](https://github.com/h4ndzdatm0ld/sros-enable-netconf) |
| nokia-netconf-examples | ✅ | [github.com/nokia/netconf-examples](https://github.com/nokia/netconf-examples) |
| twampy | ✅ | [github.com/nokia/twampy](https://github.com/nokia/twampy) |
| Nokia Validated Designs | ✅ | [github.com/nokia/nokia-validated-designs](https://github.com/nokia/nokia-validated-designs) |
| Nokia YANG Tree | ✅ | [github.com/hellt/nokia-yangtree](https://github.com/hellt/nokia-yangtree) |
| EDA Topo Builder | ✅ | [github.com/eda-labs/topo-builder](https://github.com/eda-labs/topo-builder) |
| multivendor-evpn-lab | ✅ | [github.com/srl-labs/multivendor-evpn-lab](https://github.com/srl-labs/multivendor-evpn-lab) |
| Netopeer2 | — | [github.com/nokia/Netopeer2](https://github.com/nokia/Netopeer2) |

### Ciena (13 tools)

| Tool | Verified | Link |
|------|----------|------|
| GtExporter | ✅ | [github.com/automixer/gtexporter](https://github.com/automixer/gtexporter) |
| NAPALM | ✅ | [github.com/napalm-automation/napalm](https://github.com/napalm-automation/napalm) |
| OpenConfig Feature Profiles | ✅ | [github.com/openconfig/featureprofiles](https://github.com/openconfig/featureprofiles) |
| NetBox DeviceType Library | ✅ | [github.com/netbox-community/devicetype-library](https://github.com/netbox-community/devicetype-library) |
| Ciena YANG Modules | ✅ | [github.com/ciena/yang](https://github.com/ciena/yang) |
| ciena.waveserver5 | ✅ | [github.com/ciena/ciena.waveserver5](https://github.com/ciena/ciena.waveserver5) |
| napalm-ciena-saos | ✅ | [github.com/napalm-automation-community/napalm-ciena-saos](https://github.com/napalm-automation-community/napalm-ciena-saos) |
| cienasaos10ncc | ✅ | [github.com/lucasw-eng/cienasaos10ncc](https://github.com/lucasw-eng/cienasaos10ncc) |
| ciena.waveserverai | ✅ | [github.com/ciena/ciena.waveserverai](https://github.com/ciena/ciena.waveserverai) |
| ciena.saos6 | ✅ | [github.com/ciena/ciena.saos6](https://github.com/ciena/ciena.saos6) |
| ciena.saos8 | ✅ | [github.com/ciena/ciena.saos8](https://github.com/ciena/ciena.saos8) |
| ciena.saos10 | ✅ | [github.com/ciena/ciena.saos10](https://github.com/ciena/ciena.saos10) |
| clio | — | [github.com/openconfig/clio](https://github.com/openconfig/clio) |

### Ribbon (4 tools)

| Tool | Verified | Link |
|------|----------|------|
| RibbonEdgePsRest | ✅ | [github.com/plessisa/RibbonEdgePsRest](https://github.com/plessisa/RibbonEdgePsRest) |
| Posh-Ribbon | — | [github.com/EgoManiac/Posh-Ribbon](https://github.com/EgoManiac/Posh-Ribbon) |
| pyribbon | — | [github.com/consentfactory/pyribbon](https://github.com/consentfactory/pyribbon) |
| BNG Blaster | — | [github.com/rtbrick/bngblaster](https://github.com/rtbrick/bngblaster) |

### SEL / ICON (3 tools)

| Tool | Verified | Link |
|------|----------|------|
| rdb-tool | ✅ | [github.com/danyill/rdb-tool](https://github.com/danyill/rdb-tool) |
| SEL_RDB | ✅ | [github.com/AoufNihed/SEL_RDB](https://github.com/AoufNihed/SEL_RDB) |
| libiec61850 | — | [github.com/mz-automation/libiec61850](https://github.com/mz-automation/libiec61850) |

---

## 🛠️ Scanner

The [`foss-radar-scan.py`](foss-radar-scan.py) script:

1. **Deduplicates** the database (by URL, then by name)
2. **Recalculates** all relevance scores using the scoring engine above
3. **Regenerates** a formatted markdown catalog
4. **Logs** scan history to `data/scan-history.json`

```bash
python3 foss-radar-scan.py
```

### Adding Tools

Add entries to `data/tools.json` with this schema:

```json
{
  "name": "Tool Name",
  "url": "https://github.com/org/repo",
  "description": "What it does",
  "category": "Network Automation",
  "stars": 500,
  "topics": ["netconf", "yang", "automation"],
  "vendors": ["Nokia"],
  "vendor_verified": true,
  "updated": "2026-03-01",
  "discovered": "2026-03-15"
}
```

- Set `vendor_verified: true` **only** after confirming the tool actually works with that vendor's platform
- `vendors` without `vendor_verified: true` are treated as unverified tags (no score bonus)

---

## 📂 Repository Structure

```
foss-radar/
├── README.md              # This file
├── CATALOG.md             # Full catalog — all 350 tools with links and scores
├── foss-radar-scan.py     # Scoring engine and catalog generator
└── data/
    ├── tools.json         # Tool database (350 entries)
    └── scan-history.json  # Scan run log
```

---

## 🎯 Use Cases

- **Finding vendor-specific tools** — Filter by Nokia, Ciena, Ribbon, etc.
- **Evaluating automation options** — Compare NAPALM vs Nornir vs Netmiko by relevance
- **Discovering observability tools** — Flow collectors, telemetry exporters, monitoring stacks
- **Transport network modernization** — Tools for MPLS, DWDM, carrier ethernet, optical
- **Lab environments** — Containerlab, simulators, test generators

---

## 📝 Context

This project was born out of a real need: modernizing a large utility telecom network using open source tools. The equipment spans Ciena carrier ethernet (legacy), Nokia and Ribbon (new deployments), Aviat microwave, and SEL ICON fiber optic terminals.

The FOSS Radar helps surface the most relevant tools from the massive open source ecosystem, with scoring that reflects what actually matters for transport network engineering.

---

## Contributing

Found a tool that should be here? Open an issue or PR with:
- Tool name and GitHub/source URL
- Brief description
- Category
- Vendor support (if any) — include evidence (docs, README mentions, tested)

---

## License

MIT
