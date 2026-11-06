# 📡 FOSS Radar

**A curated, scored database of 600+ Free and Open Source tools for network automation, observability, and transport network modernization.**

Built for network engineers working with **Ciena, Nokia, Ribbon, Aviat, and SEL ICON** equipment — but useful for anyone in telecom/transport networking.

[![Tools Tracked](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ffarleyt88%2Ffoss-radar%2Fmain%2Fdata%2Ftools.json&query=%24.length&label=Tools%20Tracked&color=blue)]()
[![Weekly Scan](https://img.shields.io/badge/Scan-Weekly-brightgreen)]()

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
| 1 | [GtExporter](https://github.com/automixer/gtexporter) | 146 | Nokia, Ciena ✅ | — | YANG data-model-aware gNMI streaming telemetry exporter for Prometheus. Subscribes to OpenConfig-compliant devices and exports metrics with proper YANG path awareness, making it ideal for network observability pipelines. |
| 2 | [NAPALM](https://github.com/napalm-automation/napalm) | 137 | Ciena, Nokia ✅ | 2,200 | Network Automation and Programmability Abstraction Layer. Multi-vendor network device interaction via unified API. |
| 3 | [OpenConfig Feature Profiles](https://github.com/openconfig/featureprofiles) | 117 | Nokia, Ciena ✅ | 250 | OpenConfig path definitions and Ondatra test suites for validating network device behavior. Covers gNMI, gNOI, gRIBI, BGP, IS-IS feature compliance testing across vendors. |
| 4 | [OpenConfig gNMI](https://github.com/openconfig/gnmi) | 116 | Nokia ✅ | 572 | gRPC Network Management Interface specification and reference implementation. The foundation for gNMI-based network automation used by Nokia, Arista, Cisco, and others. |
| 5 | [nl6](https://github.com/labmonkeys-space/nl6) | 113 | Ciena ✅ | 3 | Scalable network simulator for SNMP, SSH, REST, NetFlow v5/v9, IPFIX, sFlow, syslog, and gNMI, including Ciena Waveserver 5 device profiles and large-fleet NMS testing. |
| 6 | [MDT Dialout Collector](https://github.com/network-analytics/mdt-dialout-collector) | 111 | Nokia, Cisco ✅ | 31 | Multi-vendor Model-Driven Telemetry (MDT) collector using gRPC dialout mode. Accepts streaming telemetry from network devices (Cisco IOS-XR/NX-OS, Nokia SROS/SRL, Juniper) via gRPC dialout, decodes protobuf/JSON payloads, and forwards to Kafka or file output. Supports OpenConfig and vendor-specific YANG-push telemetry. Written in C++ for high-throughput production deployments. |
| 7 | [NetBox DeviceType Library](https://github.com/netbox-community/devicetype-library) | 107 | Ciena, Nokia ✅ | 1,200 | Community-sourced device type definitions for NetBox. 51 Ciena and 30 Nokia device types confirmed in library. Import directly to NetBox. |
| 8 | [fcling](https://github.com/wdesmedt/fcling) | 107 | Nokia ✅ | — | Async gNMI CLI and streaming observability engine for Nokia SR Linux fabrics. Provides typed operational reports, topology and path views, health checks, incident grouping, configuration-attributed history, baselines, drift analysis, web APIs, and read-only MCP tools. |
| 9 | [pydantify](https://github.com/pydantify/pydantify) | 101 | Nokia ✅ | 92 | CLI tool that transforms YANG models into Pydantic datastructures, serializable as RESTCONF payloads. Bridges YANG/NETCONF data modeling with modern Python type-safe workflows. Supports trimming to specific YANG subtree paths, JSON schema output, and config/state filtering. Useful for building type-safe Python automation against NETCONF/RESTCONF APIs on Nokia SROS, SR Linux, and other YANG-managed devices. |
| 10 | [NetGauze](https://github.com/NetGauze/NetGauze) | 101 | Nokia ✅ | 180 | High-performance Rust libraries and daemons for network protocol parsing and telemetry collection. Supports BGP-4, MP-BGP (IPv4/IPv6, MPLS VPN, EVPN, BGP-LS), BMP v3/v4, IPFIX/NetFlow (with Nokia-specific enterprise IEs), and UDP-notif. Network telemetry collector that ingests multi-source data. Type-safe protocol parsing with invalid-state-unrepresentable guarantees via Rust's type system. |
| 11 | [Splice](https://github.com/Open-Ireland-Testbed/splice) | 99 | — | 1 | Vendor-agnostic bridge that discovers NETCONF/YANG devices and exposes their telemetry through a gNMI server, with optical-network simulation and generated Grafana dashboards. |
| 12 | [gnmic](https://github.com/openconfig/gnmic) | 98 | Nokia ✅ | 800 | gNMI CLI client and collector. Subscribe to telemetry streams, configure devices via gRPC. |
| 13 | [fcli](https://github.com/srl-labs/fcli) | 97 | Nokia ✅ | 19 | Fabric observability tool for Nokia SR Linux that uses gNMI to provide a live web UI, topology and operational reports, CLI output in table/JSON/YAML/CSV formats, snapshots and diffs, and an MCP server for AI-assisted troubleshooting. |
| 14 | [gNPSI](https://github.com/openconfig/gnpsi) | 97 | Nokia | 20 | gRPC Network Packet Sampling Interface — OpenConfig proposal to replace sFlow/NetFlow with a gRPC-based streaming packet sampling API. Addresses UDP transport loss issues, adds encryption/authentication, and uses dial-in model compatible with security requirements. Streams sampled packets over authenticated gRPC channels alongside gNMI telemetry. Early-stage but signals the future direction of packet sampling for OpenConfig platforms (Nokia, Arista, etc.). |
| 15 | [Nokia Ansible Networking Collections](https://github.com/nokia-steward/ansible-networking-collections) | 97 | Nokia ✅ | 43 | Official Nokia Ansible collections for automating SR OS and related platforms, including CLI/NETCONF workflows plus gRPC/gNMI-oriented modules. |
| 16 | [StratoWeave](https://github.com/stratoweave/stratoweave) | 97 | — | 32 | Open-source intent-based network orchestration platform contributed by Deutsche Telekom to Linux Foundation Networking. Models systems in YANG, composes layered declarative transforms, and reacts to streaming telemetry; exposes northbound NETCONF/RESTCONF APIs and applies configuration through southbound device adapters. Originally built for optical transport network automation. |
| 17 | [Nokia OSSMediator](https://github.com/nokia-steward/OSSMediator) | 95 | Nokia ✅ | 12 | Go-based mediator that periodically collects Performance Management (PM) and Fault Management (FM) data from Nokia DAC (Digital Automation Cloud) APIs and forwards it to third-party NMS systems like OpenNMS or Elasticsearch/OpenSearch. Includes Grafana dashboards for PM/FM visualization. Useful for integrating Nokia-managed networks into existing OSS/observability stacks. |
| 18 | [Ciena YANG Modules](https://github.com/ciena/yang) | 95 | Ciena ✅ | 5 | Official Ciena YANG data models for NETCONF/RESTCONF automation of Ciena platforms (SAOS, WaveServer, etc.). Actively maintained — last updated November 2025. Essential reference for building YANG-driven automation against legacy Ciena Carrier Ethernet gear. |
| 19 | [Nokia OpenConfig Ansible Collection](https://github.com/nokia-steward/openconfig-ansible-collection) | 95 | Nokia ✅ | 1 | Official Nokia Ansible collection for vendor-agnostic OpenConfig gNMI automation. Provides connection plugins and modules for devices exposing OpenConfig gRPC APIs; validated against Nokia SR OS and SR Linux. |
| 20 | [Ciena gNMI C++ Client](https://github.com/ciena/gNMI-cpp-client) | 95 | Ciena ✅ | 5 | Official sample gNMI client from Ciena written in C++. Useful as a reference implementation for building or testing gNMI/OpenConfig integrations against Ciena-managed telemetry and automation workflows. |
| 21 | [ncclient](https://github.com/ncclient/ncclient) | 93 | Nokia ✅ | 500 | Python library for NETCONF clients. The standard NETCONF library for Python. |
| 22 | [NAPALM-SROS](https://github.com/napalm-automation-community/napalm-sros) | 91 | Nokia ✅ | 30 | Community NAPALM driver for Nokia SR OS. Provides unified API for config management and operational data retrieval via NETCONF. Validated on SR OS 19.10R5+. |
| 23 | [ciena.waveserver5](https://github.com/ciena/ciena.waveserver5) | 91 | Ciena ✅ | 2 | Official Ansible collection for Ciena Waveserver 5 optical transport appliances. Provides NETCONF-based modules for AAA, port, PTP, system, and transceiver configuration and operational data retrieval. Supports Ansible 2.12+. |
| 24 | [EDA Telemetry Lab](https://github.com/eda-labs/eda-telemetry-lab) | 91 | Nokia ✅ | 27 | Reference lab showing modern telemetry architecture for Nokia EDA + SR Linux data center fabrics. Deploys a full Containerlab topology integrated with Nokia Event Driven Automation and streams telemetry to Prometheus/Grafana. Practical blueprint for setting up streaming telemetry pipelines on Nokia SR Linux deployments. |
| 25 | [NAPALM SR Linux](https://github.com/napalm-automation-community/napalm-srlinux) | 91 | Nokia ✅ | 30 | Community NAPALM driver for Nokia SR Linux OS. Uses gNMI and JSON-RPC to provide the unified NAPALM API (get_facts, get_interfaces, config management) against SR Linux devices. Leverages Nokia SRL YANG models. Validated on SRL OS 21.3.1+. Complements the existing NAPALM-SROS driver for 7750/SR OS. |
| 26 | [yang2sdk](https://github.com/ConsortiumGARR/yang2sdk) | 91 | Nokia ✅ | 6 | Generates versioned Pydantic v2 SDKs directly from device YANG modules, including RESTCONF and NETCONF clients, models, navigators, RPC/action code, and lab verification; primary documentation confirms live testing against Nokia SR Linux. |
| 27 | [telemetry-demo](https://github.com/JaakkoRautanen/telemetry-demo) | 89 | Nokia ✅ | 25 | Containerlab-based streaming telemetry demo environment using Nokia SR Linux, gNMIc, InfluxDB, and Grafana to stand up an end-to-end open-source observability lab. |
| 28 | [SR Linux SNMP Framework Lab](https://github.com/srl-labs/srl-snmp-framework-lab) | 89 | Nokia ✅ | 8 | Nokia SR Linux lab showing SNMP workflows backed by gRPC-era tooling. Useful as a practical observability reference when bridging legacy SNMP expectations with modern transport telemetry patterns. |
| 29 | [SigNoz](https://github.com/SigNoz/signoz) | 87 | — | 26,094 | Open-source OpenTelemetry-native observability platform with logs, traces, and metrics in a single application. Self-hosted alternative to Datadog and New Relic. Built on ClickHouse for fast queries at scale. Features distributed tracing, log management with pipeline processing, metrics with PromQL-compatible queries, alerting, and dashboards. Supports SNMP and syslog receivers via OTel Collector for network device monitoring. Apache 2.0 licensed. |
| 30 | [nokia-sr-skills](https://github.com/antoinekh/nokia-sr-skills) | 87 | Nokia ✅ | 8 | Claude Code skill plugin for inspecting and operating Nokia SR OS and SR Linux, including NOS/version detection, on-demand YANG models, configuration formats, NETCONF, and gNMI guidance. |

---

## 📚 Full Catalog

### By Category

| Category | Count |
|----------|-------|
| [Network Automation](categories/network-automation.md) | 223 |
| [Observability](categories/observability.md) | 76 |
| [Network Management](categories/network-management.md) | 7 |
| [CLI Tools](categories/cli-tools.md) | 5 |
| [Self-Hosted](categories/self-hosted.md) | 4 |
| [Infrastructure as Code](categories/infrastructure-as-code.md) | 4 |
| [Network Observability](categories/network-observability.md) | 4 |
| [IPAM](categories/ipam.md) | 3 |
| [Network Simulation](categories/network-simulation.md) | 3 |
| [Network Testing](categories/network-testing.md) | 3 |
| [Network Monitoring](categories/network-monitoring.md) | 3 |
| [Data Management](categories/data-management.md) | 2 |
| [Network Diagnostics](categories/network-diagnostics.md) | 2 |
| [Other Categories](categories/) | 15 |

> **Full catalog in one page:** [`CATALOG.md`](CATALOG.md) · **By category:** [`categories/`](categories/)

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
| pyribbon | — | [github.com/commitconfirm/pyribbon](https://github.com/commitconfirm/pyribbon) |
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

The deterministic scanner does not invent or auto-approve repositories. A
separate source-grounded Hermes curation job runs **Mondays at 1:00 PM Eastern**
to search current GitHub/project sources, reject duplicates and weak matches,
verify licensing and canonical URLs, and add at most a few high-confidence
tools. It then runs this scanner, validates the generated artifacts, and
publishes the update. Runs with no suitable discoveries are recorded without
forcing additions.

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
├── CATALOG.md             # Full catalog — all tools in one page
├── foss-radar-scan.py     # Scoring engine and catalog generator
├── categories/            # One file per category (auto-generated)
│   ├── network-automation.md
│   ├── observability.md
│   ├── cli-tools.md
│   └── ...
└── data/
    ├── tools.json         # Tool database
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
