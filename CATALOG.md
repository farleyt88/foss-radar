# FOSS Radar — Full Catalog

**350 tools** across 29 categories, sorted by relevance score.

Vendor tags: ✅ = verified support, (?) = auto-tagged, needs verification.

---


## Network Automation (219 tools)

- **[NAPALM](https://github.com/napalm-automation/napalm)** (score: 137) — `Ciena` `Nokia` ✅ — ⭐ 2,200
  > Network Automation and Programmability Abstraction Layer. Multi-vendor network device interaction via unified API.

- **[OpenConfig Feature Profiles](https://github.com/openconfig/featureprofiles)** (score: 117) — `Nokia` `Ciena` ✅ — ⭐ 250
  > OpenConfig path definitions and Ondatra test suites for validating network device behavior. Covers gNMI, gNOI, gRIBI, BGP, IS-IS feature compliance testing across vendors.

- **[OpenConfig gNMI](https://github.com/openconfig/gnmi)** (score: 116) — `Nokia` ✅ — ⭐ 572
  > gRPC Network Management Interface specification and reference implementation. The foundation for gNMI-based network automation used by Nokia, Arista, Cisco, and others.

- **[NetBox DeviceType Library](https://github.com/netbox-community/devicetype-library)** (score: 107) — `Ciena` `Nokia` ✅ — ⭐ 1,200
  > Community-sourced device type definitions for NetBox. 51 Ciena and 30 Nokia device types confirmed in library. Import directly to NetBox.

- **[pydantify](https://github.com/pydantify/pydantify)** (score: 101) — `Nokia` ✅ — ⭐ 92
  > CLI tool that transforms YANG models into Pydantic datastructures, serializable as RESTCONF payloads. Bridges YANG/NETCONF data modeling with modern Python type-safe workflows. Supports trimming to...

- **[NetGauze](https://github.com/NetGauze/NetGauze)** (score: 101) — `Nokia` ✅ — ⭐ 180
  > High-performance Rust libraries and daemons for network protocol parsing and telemetry collection. Supports BGP-4, MP-BGP (IPv4/IPv6, MPLS VPN, EVPN, BGP-LS), BMP v3/v4, IPFIX/NetFlow (with Nokia-s...

- **[gnmic](https://github.com/openconfig/gnmic)** (score: 98) — `Nokia` ✅ — ⭐ 800
  > gNMI CLI client and collector. Subscribe to telemetry streams, configure devices via gRPC.

- **[Ciena YANG Modules](https://github.com/ciena/yang)** (score: 95) — `Ciena` ✅ — ⭐ 5
  > Official Ciena YANG data models for NETCONF/RESTCONF automation of Ciena platforms (SAOS, WaveServer, etc.). Actively maintained — last updated November 2025. Essential reference for building YANG-...

- **[ncclient](https://github.com/ncclient/ncclient)** (score: 93) — `Nokia` ✅ — ⭐ 500
  > Python library for NETCONF clients. The standard NETCONF library for Python.

- **[NAPALM-SROS](https://github.com/napalm-automation-community/napalm-sros)** (score: 91) — `Nokia` ✅ — ⭐ 30
  > Community NAPALM driver for Nokia SR OS. Provides unified API for config management and operational data retrieval via NETCONF. Validated on SR OS 19.10R5+.

- **[ciena.waveserver5](https://github.com/ciena/ciena.waveserver5)** (score: 91) — `Ciena` ✅ — ⭐ 2
  > Official Ansible collection for Ciena Waveserver 5 optical transport appliances. Provides NETCONF-based modules for AAA, port, PTP, system, and transceiver configuration and operational data retrie...

- **[Nokia SR Linux Ansible Collection](https://github.com/nokia/srlinux-ansible-collection)** (score: 85) — `Nokia` ✅
  > Official Nokia Ansible collection for SR Linux device management. Provides modules for config management, state queries, and operational tasks via JSON-RPC/gNMI.

- **[Nokia SROS Ansible Collection](https://github.com/nokia/sros-ansible-collection)** (score: 85) — `Nokia` ✅
  > Official Nokia Ansible collection for SR OS routers. CLI and NETCONF plugins enabling cli_config/cli_command modules, device info, and capability discovery. BSD-3 licensed.

- **[Inmanta](https://github.com/inmanta/inmanta-core)** (score: 83) — `Nokia` ✅ — ⭐ 90
  > Infrastructure orchestration and automation tool with intent-based desired-state model. Built for network service orchestration with YANG/NETCONF support. Used by Nokia for SR Linux service managem...

- **[notconf](https://github.com/notconf/notconf)** (score: 83) — `Nokia` ✅ — ⭐ 150
  > NETCONF/RESTCONF device simulator based on Netopeer2. Pre-built images for Cisco IOS XR, Juniper JUNOS, Nokia SROS. Drop-in netsim replacement.

- **[ANX (Advanced NETCONF Explorer)](https://github.com/cisco-ie/anx)** (score: 83) — ⭐ 200
  > Graphical explorer for YANG models on NETCONF devices. Features include model retrieval, tree visualization, filtering, live operational data browsing, and GNMI/IOS XR telemetry support with GRPC. ...

- **[nokia-sros-automation](https://github.com/karneliuk-com/nokia-sros-automation)** (score: 83) — `Nokia` ✅ — ⭐ 15
  > Demo collection of Python scripts showing Nokia SR OS automation via all major interfaces: pySROS (YANG data model access), MD-CLI, config get/set, operational state retrieval, and YANG tree printi...

- **[pydantic-srlinux](https://github.com/srl-labs/pydantic-srlinux)** (score: 83) — `Nokia` ✅ — ⭐ 15
  > Experimental Pydantic model library auto-generated from Nokia SR Linux YANG schemas. Provides strongly-typed Python classes for SR Linux config payloads (interfaces, ACL, BFD, BGP, network-instance...

- **[napalm-ciena-saos](https://github.com/napalm-automation-community/napalm-ciena-saos)** (score: 83) — `Ciena` ✅ — ⭐ 15
  > NAPALM community driver for Ciena SAOS devices. Enables get_facts, get_config, save_config, and get_virtual_switch via SSH. Integrates Ciena gear into the broader NAPALM automation ecosystem alongs...

- **[pySROS](https://github.com/nokia/pysros)** (score: 81) — `Nokia` ✅
  > Python 3 library for Nokia Service Router Operating System (SR OS). Model-driven NETCONF management API for Nokia routers.

- **[nokia-netconf-yang-operations](https://github.com/karneliuk-com/nokia-netconf-yang-operations)** (score: 81) — `Nokia` ✅ — ⭐ 3
  > Practical examples for operating Nokia SR OS routers via NETCONF/YANG. Python automation demos with ncclient for Nokia network devices.

- **[SR Linux YANG Browser](https://github.com/srl-labs/yang-browser)** (score: 79) — `Nokia` ✅ — ⭐ 50
  > Web portal for browsing Nokia SR Linux YANG models. Fast path search, tree visualization, and access to source .yang files for code generation.

- **[srlinux-ndk-py](https://github.com/nokia/srlinux-ndk-py)** (score: 77) — `Nokia` ✅ — ⭐ 12
  > Python bindings for Nokia SR Linux NetOps Development Kit (NDK). Build custom agents that run natively on SR Linux — monitoring, automation, or integration agents with full access to the SR Linux s...

- **[cienasaos10ncc](https://github.com/lucasw-eng/cienasaos10ncc)** (score: 77) — `Ciena` ✅ — ⭐ 4
  > Python library for interacting with Ciena SAOS 10 devices via NETCONF/YANG. Supports querying classifiers, forwarding domains, flow points, and more. Lightweight alternative to full Ansible collect...

- **[vscode-netconf](https://github.com/nokia/vscode-netconf)** (score: 75) — `Nokia` ✅ — ⭐ 50
  > Nokia's official NETCONF client extension for Visual Studio Code. Interactive NETCONF/YANG operations for SR OS and SRLinux routers. Supports SSH jump hosts, containerlab, event notifications (RFC ...

- **[Nokia SR Linux YANG Models](https://github.com/nokia/srlinux-yang-models)** (score: 75) — `Nokia` ✅ — ⭐ 45
  > Official Nokia SR Linux YANG model repository. Source files for all SR Linux configuration and state models, tagged by release version.

- **[Nokia 7x50 YANG Models](https://github.com/nokia/7x50_YangModels)** (score: 75) — `Nokia` ✅ — ⭐ 50
  > Official Nokia SR OS YANG models for configuration and management of 7x50 series routers (7750 SR, 7450 ESS, 7950 XRS, VSR). Essential reference for NETCONF/YANG automation against Nokia SROS devices.

- **[ciena.waveserverai](https://github.com/ciena/ciena.waveserverai)** (score: 75) — `Ciena` ✅ — ⭐ 3
  > Ansible Collection for Ciena Waveserver Ai optical platforms. Supports NETCONF connection for automated management of Waveserver Ai transponders and muxponders. Includes resource modules for xcvrs ...

- **[xNMS](https://github.com/xmas-ar/xNMS)** (score: 71) — ⭐ 30
  > Active eNMS fork tailored for carrier/telecom networks. Adds VPLS E2E, EVPN-VXLAN, and MPLS link service templates on top of eNMS's workflow automation, Git-backed config backup, Netmiko/NAPALM val...

- **[moler](https://github.com/nokia/moler)** (score: 71) — `Nokia` ✅ — ⭐ 60
  > Nokia's Python library for building automated network tests. Provides reusable 'bricks' for command-as-object automation with built-in parsing, event observers, and background execution. Supports S...

- **[RibbonEdgePsRest](https://github.com/plessisa/RibbonEdgePsRest)** (score: 71) — `Ribbon` ✅ — ⭐ 15
  > PowerShell module for controlling Ribbon SBC Edge via REST API. Query transformation tables, system info, create/modify/delete resources, perform reboots and configuration backups/restores at scale...

- **[Nornir](https://github.com/nornir-automation/nornir)** (score: 69) — ⭐ 1,400
  > Python automation framework for network devices. Pluggable, multi-threaded, inventory-driven.

- **[cawk](https://github.com/cedricllorens/cawk)** (score: 69) — `Nokia` ✅ — ⭐ 8
  > Multi-supplier network configuration checker built purely on gawk, gmake, and gm4 — no databases, no additional languages. Validates network device configs across multiple vendors including Nokia S...

- **[sros-enable-netconf](https://github.com/h4ndzdatm0ld/sros-enable-netconf)** (score: 67) — `Nokia` ✅ — ⭐ 4
  > Python tool to programmatically enable NETCONF and MD-CLI on Nokia SROS devices at scale. Useful for bootstrapping automation across legacy 7750 fleets that need NETCONF enabled.

- **[yang-to-ngsi-ld](https://github.com/giros-dit/yang-to-ngsi-ld)** (score: 67) — ⭐ 4
  > Research tool that translates YANG data models to NGSI-LD format to enable Network Digital Twin (NDT) solutions. Uses pyang plugins to auto-generate NGSI-LD schemas from YANG modules, enabling gNMI...

- **[nokia-netconf-examples](https://github.com/nokia/netconf-examples)** (score: 65) — `Nokia` ✅ — ⭐ 15
  > Official Nokia NETCONF example scripts and code samples. Reference implementations for NETCONF operations on Nokia platforms.

- **[Arista OpenMgmt](https://github.com/aristanetworks/openmgmt)** (score: 65) — `Arista` (?) — ⭐ 79
  > Documentation and examples for OpenConfig, NETCONF, RESTCONF, gNMI with Arista EOS. Reference implementations for open network management.

- **[ciena.saos6](https://github.com/ciena/ciena.saos6)** (score: 65) — `Ciena` ✅
  > Official Ciena Ansible Collection for SAOS 6.x devices. Automate management of legacy Ciena carrier ethernet appliances with Ansible modules and plugins.

- **[ciena.saos8](https://github.com/ciena/ciena.saos8)** (score: 65) — `Ciena` ✅ — ⭐ 2
  > Official Ansible Collection for Ciena SAOS 8.x devices. Includes modules for running commands (saos8_command) and collecting facts (saos8_facts) via network_cli. Tested against SAOS 8.6.5.

- **[twampy](https://github.com/nokia/twampy)** (score: 65) — `Nokia` ✅ — ⭐ 103
  > Official Nokia Python implementation of TWAMP (RFC 5357) and STAMP (RFC 8762, 8972) for active network measurement. Measures latency, jitter, and packet loss with no external dependencies. Supports...

- **[Nokia Validated Designs](https://github.com/nokia/nokia-validated-designs)** (score: 63) — `Nokia` ✅ — ⭐ 34
  > Official Nokia Validated Designs (NVDs) repository with deployable digital twins using containerized Nokia SR Linux and Containerlab. Covers multi-vendor and Nokia-centric network architectures acr...

- **[Nokia YANG Tree](https://github.com/hellt/nokia-yangtree)** (score: 62) — `Nokia` ✅ — ⭐ 50
  > HTML tree and Path Browser for Nokia 7x50 YANG models. Pre-generated views for navigating SR OS YANG paths. Archived but still useful reference.

- **[Netbox](https://github.com/netbox-community/netbox)** (score: 61) — ⭐ 16,000
  > Network source of truth and IPAM. Infrastructure resource modeling for network automation.

- **[EDA Topo Builder](https://github.com/eda-labs/topo-builder)** (score: 61) — `Nokia` ✅ — ⭐ 4
  > GUI-based topology builder for creating NetworkTopology workflows in Nokia EDA. Allows network engineers to graphically design and deploy fabric topologies that feed directly into the EDA intent en...

- **[gNSI](https://github.com/openconfig/gnsi)** (score: 59) — `Nokia` (?) — ⭐ 50
  > gRPC Network Security Interface — OpenConfig specification for security infrastructure services on network devices. Covers authorization, accounting, certificate management, console access manageme...

- **[sros-anysec-macsec-lab](https://github.com/srl-labs/sros-anysec-macsec-lab)** (score: 57) — `Nokia` (?) — ⭐ 30
  > ANYSec and MACSec demo lab using Nokia SR OS FP5 vSIMs with Containerlab. Features SR-ISIS, Flex-Algo slicing, gNMIc streaming telemetry to Grafana, and a Python/Flask automation panel for live dem...

- **[ciena.saos10](https://github.com/ciena/ciena.saos10)** (score: 57) — `Ciena` ✅
  > Official Ciena Ansible Collection for SAOS 10.x devices. Modules for facts, forwarding domains, interfaces, classifiers, and flow points. Direct vendor support.

- **[Rousette](https://github.com/CESNET/rousette)** (score: 57) — ⭐ 45
  > Full RFC 8040 RESTCONF server built on top of sysrepo YANG datastore. Supports XML and JSON encoding, YANG module library, data retrieval/edits, RPC/action execution, NETCONF notification streams, ...

- **[Nautobot](https://github.com/nautobot/nautobot)** (score: 55) — ⭐ 1,200
  > Network automation platform built on NetBox. Extensible network source of truth and automation.

- **[NORFAB](https://github.com/norfablabs/NORFAB)** (score: 55)
  > Network Automations Fabric — service-oriented platform for extreme network automation. Run on laptop or server, centralized or distributed. Built-in Nornir integration for show commands, config man...

- **[lighty.io](https://github.com/PANTHEONtech/lighty)** (score: 53) — ⭐ 400
  > Lightweight OpenDaylight runtime library for SDN. NETCONF, RESTCONF, gNMI support. Java SE runtime without Karaf overhead.

- **[SR Linux Telemetry Lab](https://github.com/srl-labs/srl-telemetry-lab)** (score: 51) — `Nokia` (?) — ⭐ 200
  > Interactive Streaming Telemetry lab with Nokia SR Linux nodes in Clos topology. Includes gnmic, Prometheus, Grafana, Loki stack via containerlab.

- **[Clixon](https://github.com/clicon/clixon)** (score: 51) — ⭐ 200
  > YANG-based embedded framework for building NETCONF/RESTCONF/CLI into devices or apps. Used by vendors (Netgate, Ceragon) to add standards-based management to their products.

- **[yang.ncdiff](https://github.com/CiscoTestAutomation/yang)** (score: 51) — ⭐ 200
  > NETCONF/YANG test framework with config diff capabilities. Downloads, compiles, and diffs NETCONF configs for automation - calculate new config states from current state + edit-configs. Includes NE...

- **[NCM (Network Config Management)](https://github.com/lijianqiao/ncm)** (score: 51) — ⭐ 1
  > Enterprise network config management - Vue 3 + FastAPI. Config backup, batch deployment, asset/topology discovery. Supports H3C, Huawei, Cisco.

- **[Ondatra](https://github.com/openconfig/ondatra)** (score: 51) — `Nokia` `Arista` `Juniper` (?) — ⭐ 200
  > Open Network Device Automated Test Runner and API by OpenConfig. Write and run tests against real and containerized network devices. Supports gNMI, YANG, and multiple vendor bindings.

- **[NetDriver](https://github.com/OpenSecFlow/netdriver)** (score: 51)
  > Network device CLI automation via HTTP RESTful API. Connects to network devices and executes CLI commands through a simple REST interface, simplifying integration with network automation workflows ...

- **[Bootz](https://github.com/openconfig/bootz)** (score: 51) — `Nokia` (?) — ⭐ 24
  > OpenConfig network device bootstrap APIs and services. Defines a structured data format and gRPC service for taking devices from factory state to production — covering boot config, security config,...

- **[Holo](https://github.com/holo-routing/holo)** (score: 50) — ⭐ 800
  > Routing protocol suite in Rust with native YANG/gNMI/gRPC support. Built for automation-driven networks. Memory-safe, modular, with confirmed commits.

- **[Netmiko](https://github.com/ktbyers/netmiko)** (score: 49) — ⭐ 3,500
  > Multi-vendor SSH library for network devices. Simplifies CLI automation over SSH.

- **[pyGNMI](https://github.com/akarneliuk/pygnmi)** (score: 49) — `nokia` (?) — ⭐ 200
  > Python gNMI client. Interact with network devices via gRPC Network Management Interface.

- **[Clixon Controller](https://github.com/clicon/clixon-controller)** (score: 49) — ⭐ 150
  > Open-source NETCONF/YANG network controller for multi-vendor device management. Templates, device profiles, Python API for services.

- **[gNXI Tools](https://github.com/google/gnxi)** (score: 47) — ⭐ 283
  > Google's gRPC Network Management/Operations Interface Tools. Includes gnmi_get, gnmi_set, gnmi_subscribe, gnoi_cert, gnoi_os utilities.

- **[ConfigDrift](https://github.com/cwccie/configdrift)** (score: 47)
  > Real-time network configuration drift detector with severity scoring. Uses NAPALM/SSH to continuously poll devices, diff running configs against golden baselines, and score changes by impact: CRITI...

- **[ncdiff](https://github.com/CiscoTestAutomation/ncdiff)** (score: 47) — ⭐ 55
  > Lightweight NETCONF diff engine (open sourced by Cisco). Compares NETCONF config states, calculates edit-config deltas, and validates YANG-modeled configurations. Standalone library usable outside ...

- **[netpalm](https://github.com/tbotnz/netpalm)** (score: 45) — ⭐ 450
  > REST broker and abstraction layer for NAPALM, Netmiko, NCCLIENT. Unified API for network automation.

- **[SDC (sdctl)](https://github.com/sdcio/sdctl)** (score: 45) — ⭐ 200
  > Schema Driven Configuration - cloud-native declarative config management for network devices using YANG schemas. Idempotent API interactions.

- **[gnoic](https://github.com/karimra/gnoic)** (score: 45) — `Nokia` (?) — ⭐ 26
  > gNOI (gRPC Network Operations Interface) CLI client. Companion to gnmic for operational tasks like cert management, file ops, OS install, system reboot on gNOI-capable devices.

- **[KNE](https://github.com/openconfig/kne)** (score: 45) — `Nokia` (?) — ⭐ 400
  > Kubernetes Network Emulation - deploy multi-vendor network topologies (Arista, Cisco, Juniper, Nokia, Drivenets) as containers in k8s. Standard API for topology management with gRPC interface.

- **[Stratum](https://github.com/stratum/stratum)** (score: 45) — ⭐ 410
  > Open source silicon-independent switch operating system for software-defined networks. Exposes P4Runtime and OpenConfig/gNMI interfaces, enabling programmable forwarding and vendor-agnostic managem...

- **[ygot](https://github.com/openconfig/ygot)** (score: 43) — `Nokia` `Arista` `Cisco` `Juniper` (?) — ⭐ 350
  > YANG Go Tools - Generate Go structs from YANG models, validate data against schema, render to JSON/gNMI notifications. Core library for OpenConfig Go implementations.

- **[nautobot-app-circuit-maintenance](https://github.com/nautobot/nautobot-app-circuit-maintenance)** (score: 43) — ⭐ 45
  > Nautobot plugin for tracking circuit maintenance windows from ISP/carrier notification emails (Zayo, Verizon, Lumen, Cogent, etc.). No support for Nokia/Ciena/Ribbon equipment vendors — those are g...

- **[nautobot-app-nornir](https://github.com/nautobot/nautobot-app-nornir)** (score: 43) — ⭐ 90
  > Official Nautobot app providing a Nornir ORM-based inventory and credential manager. Acts as the foundation shim for other Nautobot automation apps (Golden Config, Network Importer). Enables Nornir...

- **[NetBox MCP Server](https://github.com/netboxlabs/netbox-mcp-server)** (score: 43) — ⭐ 100
  > Official Model Context Protocol (MCP) server for NetBox by NetBox Labs. Read-only interaction with NetBox data via LLMs supporting MCP. Query objects, get details by ID, retrieve changelogs. Enable...

- **[Jalapeno](https://github.com/cisco-open/jalapeno)** (score: 43) — ⭐ 77
  > Cloud-native infrastructure platform for network services built on BMP, GoBGP, Kafka, ArangoDB, and Kubernetes. Collects BGP-LS, BGP peering, and telemetry data to build a real-time network topolog...

- **[Sysrepo](https://github.com/sysrepo/sysrepo)** (score: 41) — ⭐ 460
  > YANG-based configuration and operational state data store for Unix/Linux applications. Integrates with Netopeer2 NETCONF server. Features YANG 1.1 support, full transaction/concurrency, commit veri...

- **[annet](https://github.com/annetutil/annet)** (score: 41) — `Cisco` `Huawei` `Juniper` (?) — ⭐ 200
  > Configuration generation and deployment utility translating config diffs into command sequences. Supports Huawei, Cisco IOS/NX-OS, Juniper, and Linux. Integrates with NetBox for Source of Truth.

- **[Network Importer](https://github.com/networktocode/network-importer)** (score: 41) — ⭐ 178
  > Tool/library to analyze and synchronize an existing network with a Network Source of Truth (SOT). Idempotent by default, shows differences between running network and remote SOT. Integrates with Ba...

- **[Validity](https://github.com/amyasnikov/validity)** (score: 41) — ⭐ 170
  > NetBox plugin for writing compliance 'auto-tests' for network devices. Define compliance tests and Validity checks device state or running configuration against them. Integrates with Nautobot-style...

- **[cnaas-nms](https://github.com/SUNET/cnaas-nms)** (score: 41) — ⭐ 120
  > Campus Network-as-a-Service NMS by SUNET. Open source software to automate campus LAN management: zero-touch provisioning, common change automation, firmware upgrades, and multi-vendor support. RES...

- **[Lemming](https://github.com/openconfig/lemming)** (score: 40) — `Nokia` (?) — ⭐ 120
  > OpenConfig reference device implementation supporting gNMI, gNOI, gRIBI, P4RT, BGP, and IS-IS. Use as a fake network device for testing automation scripts and gNMI workflows without real hardware —...

- **[BGPalerter](https://github.com/nttgin/BGPalerter)** (score: 40) — ⭐ 971
  > Self-configuring BGP and RPKI monitoring tool. Monitors prefix visibility loss, hijacks, RPKI invalid announcements, ROA misconfigurations, unexpected AS path changes, and more — all without connec...

- **[jsnac](https://github.com/commitconfirmed/jsnac)** (score: 39) — ⭐ 50
  > JSON Schema (for) Network Automation Creator. Build JSON schemas using YAML syntax with network/infrastructure templates for validating Ansible host_vars, Jinja2 data, and automation YAML files.

- **[YANCCM](https://github.com/cunningr/yanccm)** (score: 39) — ⭐ 10
  > NETCONF-based network configuration and change management tool. Uses ncclient for config-diff, commit-confirm, and compliance against a Source of Truth. Supports YAML-defined multi-device configs.

- **[Secure Cartography](https://github.com/scottpeterman/secure_cartography)** (score: 39)
  > SSH & SNMP-based network discovery and topology mapping tool. Crawls infrastructure via CDP/LLDP, auto-generates topology maps. v2 features async discovery, SNMP v2c/v3, AES-256 credential vault, e...

- **[nautobot-app-ssot](https://github.com/nautobot/nautobot-app-ssot)** (score: 39) — ⭐ 95
  > Nautobot Single Source of Truth (SSoT) app. Synchronizes data between Nautobot and external systems including SolarWinds, LibreNMS, Infoblox, IPFabric, ServiceNow, Arista CloudVision, Cisco DNA Cen...

- **[netbox-librenms-plugin](https://github.com/bonzo81/netbox-librenms-plugin)** (score: 39) — ⭐ 88
  > NetBox plugin that syncs data bidirectionally between LibreNMS and NetBox. Keeps your network source of truth and monitoring platform in sync — devices, interfaces, IPs, and more.

- **[libyang](https://github.com/CESNET/libyang)** (score: 37) — ⭐ 450
  > YANG data modeling language parser and toolkit in C. Foundation library used by sysrepo, Netopeer2, and libnetconf2. Parses/validates YANG/YIN schemas, handles XML/JSON instance data.

- **[Nautobot Golden Config](https://github.com/nautobot/nautobot-app-golden-config)** (score: 37) — ⭐ 150
  > Golden Config app for Nautobot. Network config compliance and remediation.

- **[Napalm-Ansible](https://github.com/napalm-automation/napalm-ansible)** (score: 37)
  > Ansible modules using NAPALM for multi-vendor network automation.

- **[nrx (Netreplica Exporter)](https://github.com/netreplica/nrx)** (score: 37) — ⭐ 150
  > Export NetBox topologies to Containerlab, CML, NVIDIA Air, or Graphite for network lab orchestration and visualization.

- **[Netopeer2](https://github.com/nokia/Netopeer2)** (score: 37)
  > NETCONF toolset from Nokia - server, CLI client, and keystored implementation. Second generation of the Netopeer project for NETCONF protocol development and testing.

- **[openwisp-network-topology](https://github.com/openwisp/openwisp-network-topology)** (score: 37) — ⭐ 224
  > Network topology collector and visualizer. Collects from dynamic mesh routing protocols or OpenVPN, saves daily snapshots, visualizes graphs with Django web UI.

- **[Netreplica Graphite](https://github.com/netreplica/graphite)** (score: 37) — `Nokia` (?) — ⭐ 350
  > Interactive network topology visualization for NetBox, Containerlab, and Netlab. Browser-based with WebSSH access to lab nodes.

- **[GNPy](https://github.com/Telecominfraproject/oopt-gnpy)** (score: 37) — ⭐ 250
  > Optical route planning library for DWDM networks. Gaussian noise model for SNR estimation, path computation engine, bandwidth tracking. Used to advise SDN controllers on optimal paths.

- **[nornir-srl](https://github.com/srl-labs/nornir-srl)** (score: 37) — `Nokia` (?) — ⭐ 16
  > Nornir connection plugin and CLI tool (fcli) for Nokia SR Linux. Uses gNMI via PyGNMI to fetch state and push configs. Provides network-wide show commands across SRLinux nodes with report generation.

- **[netcfgbu](https://github.com/jeremyschulman/netcfgbu)** (score: 37) — ⭐ 220
  > Async network configuration backup tool using SSH. Multi-vendor support for any NOS with monolithic config (show running-config). Git integration, config diffing, inventory from CSV/Netbox, filteri...

- **[network-mcp](https://github.com/latticio/network-mcp)** (score: 37)
  > AI-powered multi-vendor network automation MCP server with 261 purpose-built tools for Arista EOS, Cisco IOS-XE/NX-OS, and Juniper JunOS. Works with Claude, Cursor, and any MCP-compatible client. S...

- **[VyManager](https://github.com/Community-VyProjects/VyManager)** (score: 37) — ⭐ 211
  > Modern web UI for centralized configuration, deployment, and monitoring of multi-site VyOS routers. Supports all active VyOS versions including rolling releases. Open beta; useful for teams managin...

- **[Trigger](https://github.com/trigger/trigger)** (score: 36) — ⭐ 557
  > Robust network automation toolkit in Python, originally from AOL's Network Security team. Supports SSH/Telnet/JunOS XML API, async parallel command execution, ACL/firewall policy parsing and conver...

- **[Icinga](https://github.com/Icinga/icinga2)** (score: 35) — ⭐ 2,000
  > Network monitoring with real-time graphing, topology maps, bandwidth monitoring, and trend prediction.

- **[yangson](https://github.com/CZ-NIC/yangson)** (score: 35) — ⭐ 80
  > YANG data modeling language parser and validator. JSON instance validation against YANG schemas.

- **[netconf-go](https://github.com/nights99/netconf-go)** (score: 35) — ⭐ 50
  > NETCONF CLI with tab completion and dynamic YANG module download. Can compile to WebAssembly for browser-based network management.

- **[NetAI-MCP](https://github.com/pdudotdev/netaimcp)** (score: 35) — ⭐ 50
  > Network automation lab with Claude AI and MCP. Multi-vendor (Arista EOS, Cisco IOS), multi-protocol topology for troubleshooting with containerlab.

- **[meshnet-cni](https://github.com/networkop/meshnet-cni)** (score: 35) — ⭐ 400
  > Kubernetes CNI plugin to create arbitrary network topologies using point-to-point links (veth, vxlan, macvlan). Uses etcd via Custom Resources and gRPC for internal communication. Built for network...

- **[drawio-network-plot](https://github.com/amrelhusseiny/drawio_network_plot)** (score: 35) — ⭐ 30
  > Python library for programmatically creating Draw.io network topology diagrams. Generate HLDs from code with customizable nodes, labeled links, and Cisco icon sets. Export to XML for Draw.io.

- **[circuit-maintenance-parser](https://github.com/networktocode/circuit-maintenance-parser)** (score: 35) — ⭐ 80
  > Parses circuit maintenance notification emails from ISP/carrier NOC teams (Zayo, Verizon, Lumen, Cogent, etc.). No support for Nokia/Ciena/Ribbon equipment vendors.

- **[ygotsrl](https://github.com/srl-labs/ygotsrl)** (score: 35) — `Nokia` (?) — ⭐ 20
  > Go API for Nokia SR Linux Network OS generated with ygot (YANG Go Tools). Provides type-safe Go structures for SR Linux YANG models, enabling programmatic config management and validation.

- **[aiNOC](https://github.com/pdudotdev/aiNOC)** (score: 35) — ⭐ 15
  > AI-based network troubleshooting project using Claude Code, FastMCP, Python, Scrapli, and Containerlab. Multi-vendor (Cisco, Arista, MikroTik), multi-protocol topology with structured outputs via G...

- **[nautobot-app-device-onboarding](https://github.com/nautobot/nautobot-app-device-onboarding)** (score: 35) — ⭐ 55
  > Official Nautobot app for automated device onboarding. Uses netmiko and NAPALM to SSH into a device and auto-populate Nautobot with hostname, platform, manufacturer, serial number, device type, man...

- **[Netdisco](https://github.com/netdisco/netdisco)** (score: 34) — ⭐ 600
  > Web-based network management tool. Device/port discovery, MAC tracking, VLAN management.

- **[FreeZTP](https://github.com/PackeTsar/freeztp)** (score: 33) — ⭐ 150
  > Zero-Touch Provisioning for Cisco IOS campus switches and routers.

- **[GoBGP](https://github.com/osrg/gobgp)** (score: 33) — ⭐ 3,994
  > Full BGP implementation in Go. Library and CLI for building BGP-based applications — route servers, looking glasses, SDN controllers, and custom routing daemons. Supports all major AFI/SAFI familie...

- **[ansible-navigator](https://github.com/ansible/ansible-navigator)** (score: 32) — ⭐ 504
  > Text-based TUI (terminal UI) for Ansible. Browse playbooks, collections, inventories, and documentation interactively. Supports execution environments (containers with ansible-core pre-loaded) and ...

- **[containerlab](https://github.com/srl-labs/containerlab)** (score: 31) — `Nokia` (?) — ⭐ 2,200
  > Container-based networking lab tool. Spin up network topologies with Nokia SR Linux, Arista cEOS, Juniper, and more in Docker containers. Define topologies in YAML, deploy in seconds. Perfect for t...

- **[NSoT](https://github.com/dropbox/nsot)** (score: 31) — ⭐ 900
  > Network Source of Truth database by Dropbox. Track inventory and metadata of network entities.

- **[Infrahub](https://github.com/opsmill/infrahub)** (score: 31) — ⭐ 1,500
  > New approach to Infrastructure Management. Version-controlled infrastructure data.

- **[clab-api-server](https://github.com/srl-labs/clab-api-server)** (score: 31) — `nokia` (?) — ⭐ 50
  > RESTful API server for Containerlab. Programmatic lab management: deploy, destroy, inspect labs. Node SSH access, CLOS topology generation, multitenancy support. Built by Nokia SRL Labs.

- **[netoviz](https://github.com/corestate55/netoviz)** (score: 31) — ⭐ 55
  > RFC8345-based Network Topology Visualizer with multi-layer views (D3.js). Supports Batfish integration for configuration-based topology generation. Docker-ready.

- **[Intent-Based Ansible Lab](https://github.com/srl-labs/intent-based-ansible-lab)** (score: 31) — `Nokia` (?) — ⭐ 20
  > Containerlab-based lab demonstrating intent-based network automation with Ansible and Nokia SR Linux. Shows how to use Ansible for declarative, intent-driven config management on SR Linux nodes.

- **[network.backup](https://github.com/redhat-cop/network.backup)** (score: 31) — ⭐ 45
  > Ansible Validated Content for network config backup and restore. Platform-agnostic roles for backup, compare, tag, and restore operations. Supports local and remote data stores. Red Hat Community o...

- **[freeRtr](https://github.com/mc36/freeRtr)** (score: 31) — ⭐ 97
  > Free open-source router OS process written in Java. Speaks a comprehensive set of routing protocols (OSPF, IS-IS, BGP, EIGRP, RIFT, Babel) and supports MPLS, Segment Routing (SR-TE, SRv6), RSVP-TE,...

- **[nautobot-app-bgp-models](https://github.com/nautobot/nautobot-app-bgp-models)** (score: 31) — ⭐ 65
  > Official Nautobot app extending core models with BGP-specific data — AS numbers, BGP peerings, peer groups, peer endpoints, and routing policies. Enables modeling and tracking BGP peering sessions ...

- **[edit4config](https://github.com/umurarslan/edit4config)** (score: 31) — ⭐ 3
  > Python tool for parsing and editing Nokia SROS and Cisco IOS style configs (parent/child with space indent) with regex support. Supports add/delete/replace/search operations on hierarchical config ...

- **[gRIBI](https://github.com/openconfig/gribi)** (score: 31) — `Nokia` (?) — ⭐ 80
  > gRPC Routing Information Base Interface — OpenConfig protocol for programmatically injecting routing entries into a network device's RIB from an external controller. Enables SDN-style route program...

- **[acton-yang](https://github.com/orchestron-orchestrator/acton-yang)** (score: 29) — ⭐ 10
  > YANG parser and library for Acton language. Works with YANG schemas and YANG-modeled data with XML & JSON serializers. Part of the Orchestron orchestrator project.

- **[Netutils](https://github.com/networktocode/netutils)** (score: 29) — ⭐ 250
  > Network automation utility functions. IP math, config parsing, bandwidth conversions.

- **[f5-common-python](https://github.com/F5Networks/f5-common-python)** (score: 29)
  > Python SDK for F5 BIG-IP configuration and monitoring via iControl REST API.

- **[NTC Ansible](https://github.com/networktocode/ntc-ansible)** (score: 29)
  > Multi-vendor Ansible modules for Network Automation by Network to Code.

- **[netconf-rs](https://github.com/jiegec/netconf-rs)** (score: 29) — ⭐ 50
  > Rust library for NETCONF (RFC 6241). Multiple SSH backends (ssh2/russh), flexible XML parsing. Device configuration automation.

- **[clab-io-draw](https://github.com/srl-labs/clab-io-draw)** (score: 29) — `Nokia` (?) — ⭐ 180
  > Bi-directional conversion between Containerlab YAML files and Draw.io diagrams. Includes clab2drawio and drawio2clab tools for visualizing and documenting network topologies with optional Grafana s...

- **[nautobot-ai-ops](https://github.com/kvncampos/nautobot-ai-ops)** (score: 29) — ⭐ 1
  > Nautobot AI Plugin integrating Large Language Models (LLM) with Model Context Protocol (MCP) and Langchain. Enables AI-powered network operations via Nautobot with dynamic prompts and MCP middlewar...

- **[ttp_templates](https://github.com/dmulyalin/ttp_templates)** (score: 29) — `Nokia` (?) — ⭐ 130
  > Community library of TTP (Template Text Parser) templates for parsing network device CLI output into structured data. Covers Nokia SR OS, Cisco IOS/XR/NX-OS, Juniper, Arista EOS, and other platform...

- **[netbox-branching](https://github.com/netboxlabs/netbox-branching)** (score: 29) — ⭐ 132
  > Official NetBox Labs plugin implementing git-like branching functionality for NetBox. Allows creating isolated branches of the network source of truth for safe what-if planning and staged changes b...

- **[eNMS](https://github.com/eNMS-automation/eNMS)** (score: 28) — ⭐ 800
  > Vendor-agnostic NMS for carrier-grade network visualization and automation.

- **[pyribbon](https://github.com/consentfactory/pyribbon)** (score: 28) — `Ribbon` (?) — ⭐ 7
  > Python module for Sonus/Ribbon SBC REST API. Query data, create/update resources, perform reboots, and do configuration backups/restores via Ribbon's REST interface. Practical tool for automating R...

- **[libiec61850](https://github.com/mz-automation/libiec61850)** (score: 28) — `SEL` (?) — ⭐ 900
  > Open-source (GPLv3) C library implementing IEC 61850 client and server protocols including MMS, GOOSE, and Sampled Values. Highly portable — runs on Linux, Windows, MacOS, and embedded systems. Inc...

- **[Jerikan](https://github.com/jerikan-network/cmdb)** (score: 27) — ⭐ 100
  > Network CMDB with Git-based config management. Template-driven network automation.

- **[yang-comparator](https://github.com/yang-central/yang-comparator)** (score: 27) — ⭐ 30
  > Compare two YANG release versions. Identifies added/changed/deleted statements, schema tree diffs, and compatibility breaking changes between model versions.

- **[rauto](https://github.com/demohiiiii/rauto)** (score: 27) — `Cisco` `Huawei` `Juniper` (?) — ⭐ 50
  > Rust CLI for network automation using Jinja2 templates and robust SSH. Supports Cisco, Huawei, Juniper with dry-run, JSON variables, TOML device profiles, and built-in web console.

- **[shconfparser](https://github.com/network-tools/shconfparser)** (score: 27) — ⭐ 60
  > Network configuration parser that translates show command outputs from Cisco and other vendors into structured tree, table, and data formats. Useful for parsing CLI output from legacy devices.

- **[SR Linux NDK Protobufs](https://github.com/nokia/srlinux-ndk-protobufs)** (score: 27) — `Nokia` (?) — ⭐ 10
  > Official Nokia SR Linux NetOps Development Kit (NDK) protobuf definitions. Defines the gRPC APIs for building custom agents on SR Linux. Essential reference for NDK agent development.

- **[scrapli](https://github.com/carlmontanari/scrapli)** (score: 25) — ⭐ 500
  > Fast, flexible screen scraping for network devices. SSH/Telnet automation with async support.

- **[salt-nornir](https://github.com/dmulyalin/salt-nornir)** (score: 25)
  > Salt proxy minion for network management using Nornir, Netmiko, NAPALM, Scrapli, etc.

- **[NetOpsForge](https://github.com/JT-BFS/NetOpsForge)** (score: 25) — ⭐ 10
  > AI-assisted zero-code network automation platform with self-growing pack library. Aligned to Cisco AUTOCOR v2.0. Features documentation site, quick-start guides, and a visual project board. Designe...

- **[ARouteServer](https://github.com/pierky/arouteserver)** (score: 25) — ⭐ 310
  > Python tool to automatically build feature-rich, policy-driven configurations for BGP route servers (BIRD v1/v2, OpenBGPD). Reads simple YAML policy definitions and enriches them with IRR/RPKI/Peer...

- **[RadOps](https://github.com/mehrdadrad/radops)** (score: 25)
  > AI-powered multi-agent platform for NetDevOps and security automation. Uses Supervisor-Worker architecture with 3-tier cognitive memory (working, ephemeral, core knowledge). Supports multi-step ope...

- **[netbox-config-diff](https://github.com/miaow2/netbox-config-diff)** (score: 25) — ⭐ 120
  > NetBox plugin that finds diffs between rendered device configurations in NetBox and the actual running configs on devices, then pushes and applies them. Supports Cisco IOS-XE/IOS-XR/NX-OS, Juniper ...

- **[TextFSM](https://github.com/google/textfsm)** (score: 24) — ⭐ 600
  > Google's template-based state machine for parsing semi-structured CLI output.

- **[ntc-templates](https://github.com/networktocode/ntc-templates)** (score: 23) — `ciena` (?) — ⭐ 1,300
  > TextFSM templates for parsing network device CLI output. 1000+ templates for various vendors.

- **[Oxidized](https://github.com/ytti/oxidized)** (score: 23) — `ciena` `nokia` (?) — ⭐ 2,700
  > Network device configuration backup tool. Supports 130+ vendors via SSH/Telnet.

- **[YAPYANG](https://github.com/nomios-opensource/yapyang)** (score: 23)
  > Python package that helps translate YANG data models to Python.

- **[FRRouting (FRR)](https://github.com/FRRouting/frr)** (score: 23) — ⭐ 3,200
  > Open source routing protocol suite supporting BGP, OSPF, IS-IS, LDP, BFD, PIM, EIGRP, and more. Runs on Linux/BSD. Used for network labs and production routing.

- **[EDA Containerlab Connector](https://github.com/eda-labs/clab-connector)** (score: 23) — `Nokia` (?) — ⭐ 15
  > Integrates Containerlab topologies with Nokia Event-Driven Automation (EDA). Automates onboarding of container-based network labs into EDA for streamlined network automation and management. Support...

- **[jdiff](https://github.com/networktocode/jdiff)** (score: 23) — ⭐ 28
  > Python library for examining and comparing structured data (JSON). Useful for network config drift detection, pre/post change validation, and compliance checks. Compare command outputs, API respons...

- **[Nokia EDA](https://github.com/nokia-eda/docs)** (score: 23) — `Nokia` (?) — ⭐ 31
  > Nokia Event Driven Automation (EDA) documentation and examples. EDA enables intent-based, event-driven network automation for Nokia SR Linux and SR OS platforms using declarative intents and reacti...

- **[nokia-eda-playground](https://github.com/nokia-eda/playground)** (score: 23) — `Nokia` (?) — ⭐ 19
  > Official Nokia EDA (Event Driven Automation) playground environment — Makefile-driven lab setup with example topologies, configs, and scripts for experimenting with Nokia's Kubernetes-native networ...

- **[hier_config](https://github.com/netdevops/hier_config)** (score: 21) — ⭐ 200
  > Hierarchical Configuration - compare running config to intended config and build remediation steps.

- **[ANTA](https://github.com/aristanetworks/anta)** (score: 21) — ⭐ 300
  > Arista Network Test Automation - Python framework for automated device testing.

- **[pyATS](https://github.com/CiscoTestAutomation/pyats)** (score: 21) — ⭐ 250
  > Cisco's Python Automation Test System. Network test automation framework.

- **[TTP](https://github.com/dmulyalin/ttp)** (score: 21) — ⭐ 350
  > Template Text Parser - parse semi-structured text using templates. TextFSM alternative.

- **[Genie Parser](https://github.com/CiscoTestAutomation/genieparser)** (score: 21) — ⭐ 250
  > Cisco Genie device output parsers. 2000+ parsers for network device CLI output.

- **[diffsync](https://github.com/networktocode/diffsync)** (score: 21) — ⭐ 200
  > Library for synchronizing data between sources. Network data reconciliation.

- **[netlab](https://github.com/ipspace/netlab)** (score: 21)
  > Infrastructure-as-code for network labs. YAML topology to VirtualBox/libvirt/containerlab.

- **[salt-sproxy](https://github.com/mirceaulinic/salt-sproxy)** (score: 21)
  > Salt plugin for network automation at scale without running Proxy Minions.

- **[Infoblox Python Client](https://github.com/infobloxopen/infoblox-client)** (score: 21)
  > Python wrapper for Infoblox REST API.

- **[NetClaw](https://github.com/automateyournetwork/netclaw)** (score: 21)
  > CCIE-level AI network engineering agent built on OpenClaw with 82 skills and 37 MCP server backends. Covers Cisco, Juniper, Arista, F5, Meraki, SD-WAN, NSO, CML, ContainerLab, Grafana, Prometheus, ...

- **[Kubenet](https://github.com/kubenet-dev/kubenet)** (score: 21) — `Nokia` (?)
  > Nokia-backed community project using Kubernetes as a network automation engine for managing physical, virtual, or containerized NOS devices (Nokia SR Linux and multi-vendor). Declarative, event-dri...

- **[nokia-sros-maintenance-scripts](https://github.com/nleontsinis-equinix/nokia-sros-maintenance-scripts)** (score: 21) — `Nokia` (?)
  > Python automation scripts for Nokia SROS maintenance tasks: bulk filesystem cleanup and card/flash status reporting with HTML dashboards. Written by Equinix engineers to handle common day-2 SROS ma...

- **[batfish](https://github.com/batfish/batfish)** (score: 20) — ⭐ 1,000
  > Network configuration analysis. Validate configs, test changes, find bugs before deployment.

- **[ciscoconfparse](https://github.com/mpenning/ciscoconfparse)** (score: 20) — ⭐ 800
  > Parse, audit, query, build, and modify Cisco IOS-style configurations.

- **[prefixopt](https://github.com/ReuxM13/prefixopt)** (score: 19) — ⭐ 20
  > High-performance Python CLI for IP prefix list optimization. Aggregates subnets, removes duplicates/Bogons, compares lists semantically. Handles 10M+ prefixes efficiently.

- **[Netpicker](https://github.com/netpicker/netpicker)** (score: 19) — ⭐ 29
  > Network config backup, security/compliance testing, and job automation in one platform. Uses pytest for compliance checks. Supports multi-vendor config management with a web UI.

- **[Netshot](https://github.com/netfishers-onl/Netshot)** (score: 17) — ⭐ 300
  > Network configuration and compliance management. Backup, audit, and report.

- **[pan-os-ansible](https://github.com/PaloAltoNetworks/pan-os-ansible)** (score: 17)
  > Ansible modules for Palo Alto Networks PAN-OS.

- **[Rconfig](https://github.com/rconfig/rconfig)** (score: 17)
  > Free, open source network device configuration management. Customizable to your needs.

- **[Infoblox Go Client](https://github.com/infobloxopen/infoblox-go-client)** (score: 17)
  > Go wrapper for Infoblox REST API.

- **[CML virl2_client](https://github.com/CiscoDevNet/virl2-client)** (score: 17)
  > Python client for Cisco CML (VIRL 2) API. Automate lab creation and management.

- **[Posh-Ribbon](https://github.com/EgoManiac/Posh-Ribbon)** (score: 17) — `Ribbon` (?) — ⭐ 10
  > PowerShell module for controlling Ribbon SBC Edge devices via REST API. Provides cmdlets for querying state, creating/updating resources, and managing Ribbon Session Border Controllers. Complements...

- **[mcp-server-sros](https://github.com/mohamedhafez87/mcp-server-sros)** (score: 17) — ⭐ 1
  > MCP (Model Context Protocol) server for Nokia SR OS devices. Provides AI-accessible tools for viewing operational state and changing configuration using Nokia's pySROS Python SDK and FastMCP. Bridg...

- **[rdb-tool](https://github.com/danyill/rdb-tool)** (score: 17) — `SEL` ✅ — ⭐ 5
  > Python tool for manipulating Schweitzer Engineering Laboratories (SEL) relay database files (.RDB). Iterates across large folder structures of RDB files for automated processing, logic counting, se...

- **[srlinux-scrapli](https://github.com/srl-labs/srlinux-scrapli)** (score: 16) — `Nokia` (?)
  > SR Linux convenience functions for Scrapligo. Provides Go bindings for automating Nokia SR Linux devices via the Scrapli framework, enabling programmatic CLI interaction and configuration management.

- **[SEL_RDB](https://github.com/AoufNihed/SEL_RDB)** (score: 16) — `SEL` ✅ — ⭐ 2
  > Python toolkit for working with SEL (Schweitzer Engineering Laboratories) .rdb relay database files. Parses and manipulates configuration data for SEL protective relays used in power system protect...

- **[Pola PCE](https://github.com/nttcom/pola)** (score: 15) — ⭐ 85
  > Stateful Path Computation Element (PCE) implementation and PCEP library in Go. Supports SR-MPLS and SRv6 (full-SID/uSID), dynamic CSPF with GoBGP BGP-LS TED, and explicit SR policy definition. Work...

- **[Schema Enforcer](https://github.com/networktocode/schema-enforcer)** (score: 15) — ⭐ 100
  > Validate structured data against schemas. Network config data validation.

- **[Aerleon](https://github.com/aerleon/aerleon)** (score: 13) — ⭐ 200
  > Multi-platform ACL generation system. Generate Juniper/IOS/etc ACLs from single policy.

- **[fetchconfig](https://github.com/udhos/fetchconfig)** (score: 13)
  > Perl script for retrieving configuration of multiple network devices.

- **[Jazigo](https://github.com/udhos/jazigo)** (score: 13)
  > Go-based tool for retrieving network device configurations. Similar to RANCID, Oxidized.

- **[Sweet](https://github.com/AppliedTrust/sweet)** (score: 13)
  > Network device configuration backups and change alerts for the 21st century.

- **[dnacentersdk](https://github.com/cisco-en-programmability/dnacentersdk)** (score: 13)
  > Python library for Cisco DNA Center Platform API.

- **[pan-python](https://github.com/kevinsteves/pan-python)** (score: 13)
  > Multi-tool set for Palo Alto Networks PAN-OS, Panorama, WildFire and AutoFocus.

- **[pyeapi](https://github.com/arista-eosplus/pyeapi)** (score: 13)
  > Python library for Arista EOS eAPI.

- **[pyiosxr](https://github.com/fooelisa/pyiosxr)** (score: 13)
  > Python library for Cisco IOS-XR automation.

- **[py-junos-eznc](https://github.com/Juniper/py-junos-eznc)** (score: 13)
  > Python library for Junos automation (PyEZ).

- **[netconan](https://github.com/intentionet/netconan)** (score: 13)
  > Network Configuration Anonymizer - sanitize configs for sharing.

- **[NetCopa](https://github.com/cidrblock/netcopa)** (score: 13)
  > Network device configuration parser. Industry standard configs to YAML.

- **[EVE-NG](https://github.com/SmartFinn/eve-ng-integration)** (score: 13)
  > Emulated Virtual Environment for Network, Security and DevOps professionals.

- **[FakeNOS](https://github.com/fakenos/fakenos)** (score: 13)
  > Simulate network operating systems programmatically. Great for testing automation.

- **[ansible-junos-stdlib](https://github.com/Juniper/ansible-junos-stdlib)** (score: 13)
  > Junos OS modules for Ansible.

- **[ara](https://github.com/ansible-community/ara)** (score: 13)
  > Ansible Runtime Analysis. Records Ansible runs for reporting and analysis.

- **[napalm-install-formula](https://github.com/saltstack-formulas/napalm-install-formula)** (score: 13)
  > Salt formula to simplify NAPALM installation and dependencies.

- **[Infoblox Ansible](https://github.com/infobloxopen/infoblox-ansible)** (score: 13)
  > Ansible module for Infoblox integration.

- **[SR Linux Controller](https://github.com/srl-labs/srl-controller)** (score: 11) — `Nokia` (?) — ⭐ 30
  > Kubernetes controller for managing Nokia SR Linux nodes in KNE (Kubernetes Network Emulation) topologies. Native k8s integration for network labs.

- **[bond](https://github.com/srl-labs/bond)** (score: 11) — `Nokia` (?) — ⭐ 15
  > A Go package to simplify Nokia SR Linux NDK (NetOps Development Kit) app development. Provides abstractions for building custom agents that extend SR Linux functionality.

- **[Cidr](https://github.com/renard/cidr)** (score: 9)
  > Cidr Is not as Dumb as Rancid. Simple network device config backup tool.

- **[Gerty](https://github.com/ssinyagin/gerty)** (score: 9)
  > Universal framework for device management automation. RANCID replacement.

- **[Capirca](https://github.com/google/capirca)** (score: 9)
  > Google's multi-platform ACL generation system. Output Juniper/IOS/etc ACLs from same policy.

- **[netaddr](https://github.com/netaddr/netaddr)** (score: 9)
  > Network address manipulation library. Supernetting, subnetting, IP math.

- **[NUTS](https://github.com/network-unit-testing-system/nuts)** (score: 9)
  > Network Unit Testing System - Pytest plugin for writing network tests with YAML.

- **[clicrud](https://github.com/davidjohngee/clicrud)** (score: 9)
  > Brocade specific CLI driver (MLX/VDX/ICX/CER/CES) for Telnet & SSH.

- **[cvprac](https://github.com/aristanetworks/cvprac)** (score: 9)
  > Python library for Arista CloudVision Portal (CVP).

- **[pandevice](https://github.com/PaloAltoNetworks/pan-os-python)** (score: 9)
  > Device framework for interacting with Palo Alto Networks devices.

- **[pyfg](https://github.com/spotify/pyfg)** (score: 9)
  > Python library for Fortinet FortiGate.

- **[pyntc](https://github.com/networktocode/pyntc)** (score: 9)
  > Python library for device-level and OS management tasks.

- **[Network-Conditions-Emulator](https://github.com/marty90/Network-Conditions-Emulator)** (score: 9)
  > Artificially limit bandwidth, delay and loss rate on selected interfaces.

- **[GNS3](https://github.com/GNS3/gns3-server)** (score: 9)
  > Graphical Network Simulator-3. Emulate complex networks on commodity hardware.

- **[Mininet](https://github.com/mininet/mininet)** (score: 9)
  > Create realistic virtual networks with real kernel, switches, apps on single machine.

- **[nokia-basic-dci-lab](https://github.com/srl-labs/nokia-basic-dci-lab)** (score: 7) — `Nokia` (?) — ⭐ 15
  > Containerlab-based DCI lab with SR Linux leaf/spine and Nokia 7750 SR OS DC gateway and P routers. Demonstrates VXLAN/EVPN fabrics interconnected via BGP-VPN WAN.

- **[vrnetlab](https://github.com/vrnetlab/vrnetlab)** (score: 5)
  > Run virtual routers in Docker for labbing, development and testing.


## Observability (75 tools)

- **[GtExporter](https://github.com/automixer/gtexporter)** (score: 146) — `Nokia` `Ciena` ✅
  > YANG data-model-aware gNMI streaming telemetry exporter for Prometheus. Subscribes to OpenConfig-compliant devices and exports metrics with proper YANG path awareness, making it ideal for network o...

- **[gNPSI](https://github.com/openconfig/gnpsi)** (score: 97) — `Nokia` (?) — ⭐ 20
  > gRPC Network Packet Sampling Interface — OpenConfig proposal to replace sFlow/NetFlow with a gRPC-based streaming packet sampling API. Addresses UDP transport loss issues, adds encryption/authentic...

- **[Nokia OSSMediator](https://github.com/nokia/OSSMediator)** (score: 95) — `Nokia` ✅ — ⭐ 12
  > Go-based mediator that periodically collects Performance Management (PM) and Fault Management (FM) data from Nokia DAC (Digital Automation Cloud) APIs and forwards it to third-party NMS systems lik...

- **[EDA Telemetry Lab](https://github.com/eda-labs/eda-telemetry-lab)** (score: 91) — `Nokia` ✅ — ⭐ 27
  > Reference lab showing modern telemetry architecture for Nokia EDA + SR Linux data center fabrics. Deploys a full Containerlab topology integrated with Nokia Event Driven Automation and streams tele...

- **[VictoriaMetrics](https://github.com/VictoriaMetrics/VictoriaMetrics)** (score: 85) — ⭐ 13,500
  > Fast, cost-effective, and scalable time series database and monitoring solution. Prometheus-compatible (drop-in replacement) with significantly better compression and query performance at scale. Su...

- **[GoFlow2](https://github.com/netsampler/goflow2)** (score: 81) — ⭐ 1,400
  > High-performance NetFlow v5/v9, IPFIX, and sFlow collector in Go — a maintained fork of Cloudflare's original GoFlow. Ingests flow data from routers/switches, serializes to protobuf or JSON, and sh...

- **[OpenNTI](https://github.com/Juniper/open-nti)** (score: 79) — ⭐ 320
  > Containerized open network telemetry collector and visualization stack. Collects data from devices via CLI/Netconf, JTI streaming telemetry, and Statsd. Comes pre-configured with Grafana dashboards...

- **[Akvorado](https://github.com/akvorado/akvorado)** (score: 75) — ⭐ 1,200
  > Flow collector, enricher and visualizer. Receives NetFlow/IPFIX and sFlow, enriches with SNMP interface names and geo data, stores in ClickHouse, and provides a built-in web UI with Sankey diagrams...

- **[pmacct](https://github.com/pmacct/pmacct)** (score: 74) — ⭐ 900
  > Multi-purpose passive network monitoring toolset supporting NetFlow, IPFIX, sFlow, libpcap, BGP, BMP, RPKI, IGP, and Streaming Telemetry. Lightweight C-based collectors that can export to Kafka, Ra...

- **[gNMIc Operator](https://github.com/gnmic/operator)** (score: 65) — ⭐ 30
  > Kubernetes operator for deploying and managing gNMIc telemetry collectors at scale. Define telemetry infrastructure as Custom Resources — the operator handles StatefulSet creation, configuration ge...

- **[DANT (Drawer of Any Network Topology)](https://github.com/karneliuk-com/drawer-any-network-topology)** (score: 63) — ⭐ 50
  > Python tool that collects operational data from network devices via NETCONF/YANG and auto-generates topology visualizations using Nornir, Graphviz, and VisJS. Supports Nokia SR OS, Cisco NX-OS, IOS...

- **[srl-sros-telemetry-lab](https://github.com/srl-labs/srl-sros-telemetry-lab)** (score: 62) — `Nokia` (?)
  > Interactive streaming telemetry lab with Nokia SR Linux and SR OS in a Clos fabric topology. Includes gnmic, Prometheus, Grafana, and Loki. Demonstrates gNMI dial-in/dial-out telemetry with OpenCon...

- **[NetGraf](https://github.com/esnet/netgraf)** (score: 61) — ⭐ 45
  > End-to-end ML-driven network performance monitoring system from ESnet. Integrates packet, flow, and device-level data from multiple FOSS monitoring tools into a unified dashboard. Uses Ansible for ...

- **[network-observability-lab](https://github.com/network-observability/network-observability-lab)** (score: 57) — ⭐ 320
  > Reference lab for 'Modern Network Observability' book. Hands-on scenarios covering gNMI/SNMP collection, Prometheus, Grafana Loki, alerting, and AI-enhanced observability with containerlab.

- **[privacynet](https://github.com/cwccie/privacynet)** (score: 57) — ⭐ 28
  > Privacy-preserving network telemetry toolkit — IP anonymization (prefix-preserving, truncation, random), flow aggregation, and differential privacy (Laplace noise) for safely sharing NetFlow/sFlow/...

- **[mapgl](https://github.com/vaduga/mapgl)** (score: 57) — ⭐ 6
  > Grafana panel plugin that renders an interactive network node graph and geomap. Visualize network topology — nodes, links, and geographic overlays — directly in Grafana dashboards. Useful for build...

- **[Beszel](https://github.com/henrygd/beszel)** (score: 57) — ⭐ 19,934
  > Lightweight self-hosted server monitoring hub. Historical data, Docker container stats, alerting, multi-server dashboard. Simple agent-based architecture with minimal resource footprint. Great for ...

- **[Grafana Alloy](https://github.com/grafana/alloy)** (score: 57) — ⭐ 4,500
  > Open-source OpenTelemetry Collector distribution from Grafana Labs with built-in Prometheus pipelines. Unified agent for collecting and shipping metrics, logs, traces, and profiles. Replaces the de...

- **[Keep](https://github.com/keephq/keep)** (score: 56) — ⭐ 8,500
  > Open-source AIOps and alert management platform. Provides a single pane of glass for all alerts with deduplication, correlation, enrichment, and filtering. Supports bi-directional integrations with...

- **[OneUptime](https://github.com/OneUptime/oneuptime)** (score: 55) — ⭐ 4,800
  > Complete open-source monitoring and observability platform. Self-hosted alternative to Datadog/PagerDuty with status pages, incident management, on-call rotation, telemetry (OpenTelemetry-native), ...

- **[DeepFlow](https://github.com/deepflowio/deepflow)** (score: 55) — ⭐ 3,200
  > eBPF-powered zero-code observability platform. Automatically captures application, network, and infrastructure metrics/traces/logs without code instrumentation. Features distributed tracing across ...

- **[Bindplane OTel Collector](https://github.com/observIQ/bindplane-otel-collector)** (score: 54) — ⭐ 300
  > OpenTelemetry Collector distribution with built-in SNMP receiver, OpAMP management, and 100+ receivers/processors. Bridges legacy SNMP monitoring with modern OTel pipelines — ideal for transport ne...

- **[Orb Agent (NetBox Labs)](https://github.com/netboxlabs/orb-agent)** (score: 53) — ⭐ 70
  > Lightweight network observability and discovery agent from NetBox Labs, part of the NetBox Discovery solution. Pluggable backend architecture supporting SNMP discovery, network device discovery, an...

- **[clio](https://github.com/openconfig/clio)** (score: 52) — `Nokia` `Ciena` (?)
  > OpenTelemetry to gNMI bridge by OpenConfig. Converts OpenTelemetry data into gNMI format, enabling integration between OTel observability pipelines and gNMI-based network telemetry systems.

- **[Telegraf](https://github.com/influxdata/telegraf)** (score: 51) — ⭐ 15,000
  > Plugin-driven agent for collecting and reporting metrics. 300+ input plugins including SNMP.

- **[DiGSiViz](https://github.com/netlab-hfd/digsiviz)** (score: 51) — ⭐ 5
  > gNMI-powered real-time visualization of Network Digital Twin topologies running in Containerlab. A proof-of-concept frontend+backend app that connects to Containerlab-deployed devices via gNMI and ...

- **[Checkmate](https://github.com/bluewave-labs/Checkmate)** (score: 51) — ⭐ 3,200
  > Self-hosted open-source uptime and infrastructure monitoring platform. Tracks server hardware (CPU, memory, disk, network), HTTP/TCP uptime, response times, and incidents in real-time with a clean ...

- **[Kubeshark](https://github.com/kubeshark/kubeshark)** (score: 51) — ⭐ 11,817
  > Cluster-wide network observability for Kubernetes. Captures L4 packets and L7 API calls (HTTP, gRPC, Redis, Kafka, DNS) using eBPF with full Kubernetes context. Decrypts TLS traffic without managin...

- **[openGemini](https://github.com/openGemini/openGemini)** (score: 49) — ⭐ 2,100
  > CNCF sandbox project — cloud-native distributed time-series database written in Go. High concurrency, high performance, designed for IoT and observability. Compatible with InfluxDB line protocol. C...

- **[Triglav](https://github.com/brevius/Triglav)** (score: 49)
  > gNMI/JTI-based streaming telemetry collector for Juniper transport routers (ACX, MX, PTX). Uses Telegraf for gNMI collection (SSL/gRPC) and ships metrics to VictoriaMetrics. Supports per-platform T...

- **[Coroot](https://github.com/coroot/coroot)** (score: 47) — ⭐ 7,476
  > Open-source observability and APM tool with AI-powered Root Cause Analysis. Combines metrics, logs, traces, continuous profiling, and SLO-based alerting with predefined dashboards and inspections. ...

- **[NetStruct](https://github.com/IT-4-ALL/NetStruct)** (score: 45) — ⭐ 2
  > Browser-based network planning and visualization tool. Drag-and-drop interface for routers, switches, firewalls. Real-time ICMP status monitoring, alarm system with API triggers, multi-page layouts...

- **[gnmi-gateway](https://github.com/openconfig/gnmi-gateway)** (score: 45) — ⭐ 200
  > Distributed, highly available gNMI telemetry gateway from OpenConfig. Connects to multiple gNMI targets, exports to other protocols.

- **[Fluere](https://github.com/SkuldNorniern/fluere)** (score: 45) — ⭐ 60
  > Cross-platform Rust tool that captures network packets in pcap format and converts them to NetFlow v5 data. Supports live capture, offline analysis, AWS Traffic Mirroring flow logs, and includes a ...

- **[OpenObserve](https://github.com/openobserve/openobserve)** (score: 41) — ⭐ 14,000
  > Cloud-native observability platform - logs, metrics, traces. 10x lower storage cost than Elasticsearch.

- **[Prometheus SNMP Exporter](https://github.com/prometheus/snmp_exporter)** (score: 41) — ⭐ 1,500
  > SNMP Exporter for Prometheus. Expose SNMP metrics for Prometheus scraping.

- **[advanced-network-topology-mapper](https://github.com/x0VIER/advanced-network-topology-mapper)** (score: 41) — ⭐ 15
  > Extensible network discovery, visualization, and analysis framework. Uses multiple protocols (SNMP, LLDP, CDP) for auto-discovery, generates interactive topology diagrams, and provides real-time de...

- **[ServiceRadar](https://github.com/carverauto/serviceradar)** (score: 41) — ⭐ 200
  > Zero-trust distributed network monitoring platform for infrastructure in hard-to-reach or constrained environments. Features WASM plugin system (Go/Rust), GPU-native topology engine, distributed ag...

- **[Network Observability Platform](https://github.com/shankar0123/network-observability-platform)** (score: 40)
  > Open source ThousandEyes alternative. Distributed synthetic network monitoring with canary agents (Ping, DNS, HTTP, Traceroute) and BGP analysis. Results via Kafka to Prometheus metrics and Grafana...

- **[flowlogs-pipeline](https://github.com/netobserv/flowlogs-pipeline)** (score: 40)
  > Observability tool that consumes network flow logs (NetFlow v5/v9, IPFIX, eBPF), transforms them, and exports to Loki and/or Prometheus metrics. Supports Kafka input, mathematical transformations, ...

- **[NetXMS](https://github.com/netxms/netxms)** (score: 39) — ⭐ 300
  > Enterprise-grade open source network and infrastructure monitoring. Unified platform for performance/availability monitoring with SNMP, agents, flexible event processing, alerting, reporting, and g...

- **[Weathermap-NG](https://github.com/utahsaint-org/weathermap-ng)** (score: 39)
  > Modern network weathermap web application showing link utilization, optical power, and link health on logical maps. Auto-discovers links via interface descriptions, supports multiple data sources (...

- **[LibreNMS](https://github.com/librenms/librenms)** (score: 37) — ⭐ 3,800
  > Auto-discovering network monitoring with alerting. SNMP-based, PHP/MySQL.

- **[NetBox Topology Views](https://github.com/mattieserver/netbox-topology-views)** (score: 37) — ⭐ 400
  > NetBox plugin for network topology visualization. D3.js based diagrams.

- **[napalm-logs](https://github.com/napalm-automation/napalm-logs)** (score: 37)
  > Cross-vendor normalisation for network syslog messages. OpenConfig/IETF YANG models.

- **[Netprobe Lite](https://github.com/plaintextpackets/netprobe_lite)** (score: 37)
  > Self-hosted internet performance monitoring tool. Measures packet loss, latency, jitter, DNS performance, and optional bandwidth speed tests. Aggregates metrics into a health score. Docker-based wi...

- **[opennms-api-wrapper](https://github.com/cnewkirk/opennms-api-wrapper)** (score: 37) — ⭐ 5
  > Unofficial Python 3 client for the OpenNMS REST API (Horizon 35+ / Meridian 2024.3+). Covers all v1 and v2 REST endpoints with JSON-only interface (no XML required). Single dependency (requests), T...

- **[Modern-Network-Observability](https://github.com/PacktPublishing/Modern-Network-Observability)** (score: 36)
  > Reference lab and architecture from the Packt book. Covers Telegraf, Prometheus, Grafana, Logstash, Nautobot integration, Prefect alerting, and ML-enhanced observability. Practical recipes for buil...

- **[EasySNMP](https://github.com/kamakazikamikaze/easysnmp)** (score: 35) — ⭐ 250
  > Fast and easy SNMP library using Net-SNMP. Python bindings for network monitoring.

- **[Scanopy](https://github.com/scanopy/scanopy)** (score: 33) — ⭐ 200
  > Auto-discover and visualize network topology. Scans networks, identifies hosts/services, generates interactive diagrams. Docker-based with multi-VLAN scanning, scheduled discovery, and role-based a...

- **[OpenTelemetry eBPF Network](https://github.com/open-telemetry/opentelemetry-network)** (score: 33) — ⭐ 500
  > eBPF-based network telemetry collector from the OpenTelemetry project. Collects low-level network data from Linux kernel with negligible overhead. Includes kernel collector, Kubernetes collector, c...

- **[suzieq](https://github.com/netenglabs/suzieq)** (score: 32) — `Nokia` (?) — ⭐ 700
  > Software for network observability and understanding. Agentless, multi-vendor network observability platform that collects, normalizes, and enables analysis of network state data. Supports path tra...

- **[natlas](https://github.com/MJL85/natlas)** (score: 31) — ⭐ 250
  > Network Atlas - automated network discovery and SVG diagram generation using SNMP, CDP, and LLDP. Auto-discovers topology and creates visual maps from a seed device.

- **[snmp-to-otel](https://github.com/avozda/snmp-to-otel)** (score: 31) — ⭐ 5
  > SNMP gauge metric exporter for OpenTelemetry in C++. Polls SNMP agents at configurable intervals and forwards metrics via OTLP/HTTP. Supports custom OID-to-metric name mappings.

- **[inet-henge](https://github.com/codeout/inet-henge)** (score: 29) — ⭐ 300
  > Generate d3.js network diagrams from JSON. Interactive network topology visualization.

- **[NetAlertX](https://github.com/netalertx/NetAlertX)** (score: 29)
  > Centralized network visibility and continuous asset discovery. Self-hosted Docker app that monitors devices, detects changes, identifies Shadow IT, and maintains a real-time network inventory (NSoT...

- **[Orb](https://github.com/orb-community/orb)** (score: 28)
  > Dynamic network observability platform with agent fleet orchestration and OpenTelemetry data pipelines. Pushes analysis to the edge using pktvisor agents, supports L2-L3 network, DNS, and DHCP anal...

- **[Scanlyne](https://github.com/Josperdo/scanlyne)** (score: 27) — ⭐ 42
  > Lightweight network change detection built on nmap. Runs scans, stores baseline snapshots in SQLite, and diffs subsequent scans to surface new/removed hosts and port/service changes — with triage h...

- **[mermin](https://github.com/elastiflow/mermin)** (score: 27) — ⭐ 29
  > Kubernetes-native network observability tool that uses eBPF to auto-instrument network traffic and export it as Flow Traces via OpenTelemetry. Provides deep visibility into cluster communications w...

- **[Topolograph](https://github.com/Vadims06/topolograph)** (score: 25)
  > Python web tool for OSPF/ISIS topology visualization and outage prediction.

- **[LogTide](https://github.com/logtide-dev/logtide)** (score: 25) — ⭐ 347
  > Open-source, self-hosted log management platform. Privacy-first alternative to Datadog and ELK. Lightweight, easy to deploy, designed for teams that want log aggregation without sending data to thi...

- **[Nerdlog](https://github.com/dimonomid/nerdlog)** (score: 23) — ⭐ 1,452
  > Fast, remote-first, multi-host TUI log viewer with timeline histogram and no central server. SSH-based log querying from multiple machines simultaneously with pattern filtering and time range selec...

- **[drawthe.net](https://github.com/cidrblock/drawthe.net)** (score: 21) — ⭐ 450
  > Draw network diagrams from YAML. Automated network diagram generation.

- **[OpenOTDR](https://github.com/BaldrAI/OpenOTDR)** (score: 21)
  > Open source OTDR reporting tool for fiber test results. Integrates OTDR traces with GIS data, enables trace viewing/labeling, fault localization, and report generation. Cross-platform (iOS, Android...

- **[Sloggo](https://github.com/phare/sloggo)** (score: 21) — ⭐ 449
  > Minimal RFC 5424 syslog collector and viewer powered by DuckDB. Runs as a single, resource-friendly process with a clean web UI for browsing and searching syslog messages. No external database requ...

- **[Upright](https://github.com/basecamp/upright)** (score: 20)
  > Self-hosted synthetic monitoring system from 37signals (Basecamp/HEY). Playwright browser probes, HTTP checks, SMTP verification, traceroute with hop-by-hop latency, multi-site support, Prometheus ...

- **[N2G (Need To Graph)](https://github.com/dmulyalin/N2G)** (score: 17)
  > Generate network diagrams in GraphML, draw.io or JSON from structured data or CLI output.

- **[IS-IS Watcher](https://github.com/Vadims06/isiswatcher)** (score: 17)
  > Tracks IS-IS topology changes via GRE tunnel with network devices. History diagrams.

- **[OSPF Watcher](https://github.com/Vadims06/ospfwatcher)** (score: 17)
  > Tracks OSPF topology changes via GRE tunnel with network devices. History diagrams.

- **[Edgeshark](https://github.com/siemens/edgeshark)** (score: 17) — ⭐ 250
  > Discover and capture container network traffic from desktop Wireshark with a single click. Containerized service with Wireshark extcap plugin. Supports Docker, containerd, and KinD. Great companion...

- **[SEC](https://github.com/simple-evcorr/sec)** (score: 13)
  > Simple Event Correlator - Advanced event processing for log monitoring, security, fraud detection.

- **[Prometheus](https://github.com/prometheus/prometheus)** (score: 13)
  > Open-source monitoring and alerting toolkit. Cloud-native foundation project.

- **[srl-prometheus-exporter](https://github.com/karimra/srl-prometheus-exporter)** (score: 13) — `Nokia` (?) — ⭐ 9
  > Prometheus exporter that runs as a native NDK app on Nokia SR Linux. Exports metrics directly from the NOS without external polling — ideal for tight Grafana/Prometheus integration with Nokia DC fa...

- **[InfluxDB](https://github.com/influxdata/influxdb)** (score: 9)
  > Time-series database for metrics, events, and real-time analytics.

- **[D2](https://github.com/terrastruct/d2)** (score: 5)
  > Create beautiful diagrams in minutes. Simple syntax, endlessly customizable.


## Network Management (6 tools)

- **[TWSNMP FK](https://github.com/twsnmp/twsnmpfk)** (score: 69) — ⭐ 220
  > Next-generation Network Management System built with Go, Svelte, and Wails for a lightweight desktop NMS experience. Ultra-lightweight SNMP manager with real-time network maps, event logs, and gNMI...

- **[NOC Project](https://github.com/nocproject/noc)** (score: 59) — ⭐ 135
  > Open-source Operation Support System (OSS) designed for telecom companies, ISPs, and enterprise NOCs. Features fault management with root cause analysis and topology correlation, performance manage...

- **[OpenNetworkDiagram](https://github.com/jcreek/OpenNetworkDiagram)** (score: 51) — ⭐ 30
  > Declarative, self-hosted containerized tool for visualizing and managing network architecture diagrams. Stores topology in a JSON source of truth that can be version-controlled in Git. Includes net...

- **[Netipam](https://github.com/nodeplex/Netipam)** (score: 41) — ⭐ 120
  > Self-hosted IP address management (IPAM) and network visibility tool. Docker-based, easy to deploy, designed for networks from homelabs to small enterprises. Provides IP inventory, allocation track...

- **[Homelable](https://github.com/Pouzor/homelable)** (score: 39) — ⭐ 60
  > Self-hosted homelab infrastructure visualizer with interactive network diagrams and live status monitoring. TypeScript-based, generates visual maps of infrastructure with real-time health checks. D...

- **[Rackula](https://github.com/RackulaLives/Rackula)** (score: 28) — ⭐ 839
  > Open-source drag-and-drop rack layout designer that runs entirely in the browser. Supports real device images, drag-and-drop placement, and export functionality. Self-hosted via Docker or usable of...


## CLI Tools (5 tools)

- **[netconf-cli](https://github.com/CESNET/netconf-cli)** (score: 43) — `nokia` (?) — ⭐ 50
  > Interactive console for working with YANG data. Connects to NETCONF servers, standalone YANG editor, or sysrepo.

- **[Atuin](https://github.com/atuinsh/atuin)** (score: 29) — ⭐ 21,000
  > Shell history sync and search. Encrypted sync across machines, SQLite backend, fuzzy search.

- **[Zellij](https://github.com/zellij-org/zellij)** (score: 29) — ⭐ 23,000
  > Terminal multiplexer (tmux alternative) with better defaults, modern UI, plugin system, floating panes.

- **[NetTowel](https://github.com/InfrastructureAsCode-ch/nettowel)** (score: 25)
  > Collection of useful network automation functions for the CLI.

- **[sig](https://github.com/ynqa/sig)** (score: 20)
  > Interactive grep for streaming data. Real-time search through live data streams with TUI, command re-execution for missed data, archived mode for historical search. Rust-based, fast. Great for tail...


## Network Observability (4 tools)

- **[ktranslate](https://github.com/kentik/ktranslate)** (score: 81) — ⭐ 250
  > Network data collection and translation system by Kentik Labs. Pulls SNMP, flow (NetFlow/sFlow/IPFIX), and streaming telemetry data and pushes to multiple sinks (Kafka, Prometheus, New Relic, stdou...

- **[Skydive](https://github.com/skydive-project/skydive)** (score: 35) — ⭐ 2,300
  > Real-time network topology and protocols analyzer. Agents collect topology info and flows, forwarding to a central agent for analysis. SDN-agnostic with driver support. Stores in Elasticsearch. Sup...

- **[Monocle (BGPKIT)](https://github.com/bgpkit/monocle)** (score: 29) — ⭐ 167
  > Fast CLI tool for analyzing BGP data from public MRT archives (RouteViews, RIPE RIS). Written in Rust. Quickly queries historical BGP routing tables, traces prefix announcements/withdrawals, and in...

- **[GoBMP](https://github.com/sbezverk/gobmp)** (score: 25) — ⭐ 180
  > Go-based BGP Monitoring Protocol (BMP) implementation. Full SRv6 support with BGP-LS extensions (Flex Algo), multiple publishers (Kafka, NATS, file), OpenBMP compatibility, intercept/proxy mode, an...


## Infrastructure as Code (4 tools)

- **[Rundeck](https://github.com/rundeck/rundeck)** (score: 36) — ⭐ 5,500
  > Job scheduler and runbook automation. Execute Ansible playbooks and scripts at scale.

- **[Pulumi](https://github.com/pulumi/pulumi)** (score: 33) — ⭐ 22,000
  > Infrastructure as Code with real programming languages - Python, TypeScript, Go. Multi-cloud + Kubernetes.

- **[OpenTofu](https://github.com/opentofu/opentofu)** (score: 33) — ⭐ 24,000
  > Open-source fork of Terraform for declarative infrastructure management. Linux Foundation project with full Terraform compatibility, state encryption, and community-driven development. Relevant for...

- **[StackStorm](https://github.com/StackStorm/st2)** (score: 28) — ⭐ 6,000
  > Event-driven automation - IFTTT for Ops. Auto-remediation, workflows, 1800+ integrations, ChatOps.


## Self-Hosted (4 tools)

- **[NetBox Docker](https://github.com/netbox-community/netbox-docker)** (score: 35) — ⭐ 1,200
  > Docker deployment for NetBox. Easy containerized network source of truth.

- **[AFFiNE](https://github.com/toeverything/AFFiNE)** (score: 33) — ⭐ 42,000
  > Notion alternative - docs, whiteboards, databases. Local-first, fully self-hostable, offline-first.

- **[Taiga](https://github.com/kaleidos-ventures/taiga)** (score: 24) — ⭐ 7,000
  > Project management (Jira alternative) - Kanban + Scrum. Self-hosted, unlimited users, GitLab/GitHub integration.

- **[Databasus](https://github.com/databasus/databasus)** (score: 21) — ⭐ 500
  > Self-hosted database backup tool with S3, Google Drive, FTP targets and Slack/Discord notifications.


## Network Monitoring (3 tools)

- **[ntopng](https://github.com/ntop/ntopng)** (score: 86) — ⭐ 6,200
  > High-speed web-based network traffic analysis and flow monitoring tool. Supports deep packet inspection (DPI) via nDPI, NetFlow/IPFIX/sFlow ingestion, real-time host/flow/protocol dashboards, behav...

- **[Trishul SNMP Studio](https://github.com/tosumitdhaka/trishul-snmp)** (score: 43) — ⭐ 5
  > Modern web-based SNMP management platform. Simulate SNMP agents, walk/parse devices with MIB resolution, send/receive traps with real-time WebSocket push, browse MIB trees, manage MIB files. Replac...

- **[RustNet](https://github.com/domcyrus/rustnet)** (score: 31) — ⭐ 120
  > Cross-platform terminal UI network monitor written in Rust. Tracks TCP/UDP/ICMP/ARP connections in real-time with deep packet inspection (DPI) to identify HTTP, TLS/SNI, DNS, SSH, QUIC, SNMP, DHCP,...


## Network Simulation (3 tools)

- **[vscode-containerlab](https://github.com/srl-labs/vscode-containerlab)** (score: 21) — `Nokia` (?) — ⭐ 300
  > VS Code extension for containerlab. Auto-discovers .clab.yml topologies, tree view with color-coded lab states, context menu actions (deploy/destroy/SSH/logs), interface traffic capture via Wiresha...

- **[clab_mpls_frr](https://github.com/martimy/clab_mpls_frr)** (score: 17)
  > MPLS network lab implementations using FRRouting and Containerlab. Covers manual MPLS, LDP label distribution, and L3 VPN with VRF/BGP. Great for learning MPLS concepts hands-on.

- **[Clabernetes](https://github.com/srl-labs/clabernetes)** (score: 13) — `Nokia` (?) — ⭐ 105
  > Containerlab but in Kubernetes. Deploys containerlab network topologies on K8s clusters, enabling scalable multi-node network labs. Supports Nokia SR Linux, Arista cEOS, and other containerized NOSes.


## Network Testing (3 tools)

- **[BNG Blaster](https://github.com/rtbrick/bngblaster)** (score: 21) — `Nokia` `Ribbon` (?) — ⭐ 274
  > Open-source network tester for routing and access protocols. Tests IS-IS, OSPF, LDP, BGP, PPPoE, IPoE/DHCP, IPTV, and L2TP at scale. Includes a traffic generator that can simulate millions of flows...

- **[Ixia-C](https://github.com/open-traffic-generator/ixia-c)** (score: 17) — ⭐ 150
  > Open-source traffic generator based on the Open Traffic Generator API. Generates and analyzes network traffic for testing, validation, and performance benchmarking. Supports containerized deploymen...

- **[Etherate](https://github.com/jwbensley/Etherate)** (score: 16) — ⭐ 500
  > Linux CLI tool for testing layer 2 Ethernet and MPLS connectivity. Generates various Ethernet and MPLS frames for testing switches, routers, and firewalls. Supports custom VLAN tags, QoS/DSCP, and ...


## IPAM (3 tools)

- **[phpIPAM](https://github.com/phpipam/phpipam)** (score: 13)
  > Open-source web IP address management (IPAM). Light, modern, RESTful API.

- **[nipap](https://github.com/SpriteLink/NIPAP)** (score: 9)
  > Sleek, intuitive and powerful IP address management system for large-scale networks.

- **[TeemIP](https://github.com/TeemIp/teemip-standalone)** (score: 9)
  > Open source IPAM tool for IPv4 and IPv6 management with web interface.


## Uncategorized (2 tools)

- **[OpenNMS](https://github.com/OpenNMS/opennms)** (score: 68)
  > Enterprise-grade open-source network management platform. Supports SNMP, JSON, WinRM, XML, SQL, JMX, SFTP, FTP, JDBC, HTTP, HTTPS, VMware, WS-Management, Prometheus, and more — no third-party plugi...

- **[Thola](https://github.com/inexio/thola)** (score: 34)
  > Go-based tool for monitoring network devices, primarily via SNMP. Features an identify mode (auto-detects vendor/model), read mode (interfaces, CPU, memory, hardware health), and check mode (Nagios...


## Network Diagnostics (2 tools)

- **[ttl](https://github.com/lance0/ttl)** (score: 36) — ⭐ 825
  > Fast, modern traceroute with real-time TUI, per-hop stats, ASN/geo lookup, ECMP detection, and MPLS label parsing. A better mtr. Written in Rust with ratatui. Especially useful for transport engine...

- **[Trippy](https://github.com/fujiapple852/trippy)** (score: 23) — ⭐ 4,500
  > Modern network diagnostic tool combining traceroute and ping with a beautiful TUI. Written in Rust, cross-platform, supports ICMP/UDP/TCP, DNS-over-TLS, GeoIP, and chart/table views. Great alternat...


## Data Management (2 tools)

- **[Airbyte](https://github.com/airbytehq/airbyte)** (score: 33) — ⭐ 16,000
  > Open-source ELT platform with 300+ connectors. Self-hosted data integration.

- **[Dremio](https://github.com/dremio/dremio-oss)** (score: 19) — ⭐ 1,400
  > Data lakehouse query engine. SQL on data lakes without data movement, virtual datasets.


## Standards & Models (1 tools)

- **[OpenROADM MSA](https://github.com/OpenROADM/OpenROADM_MSA_Public)** (score: 65) — ⭐ 150
  > Open ROADM Multi-Source Agreement YANG models and specifications for disaggregated optical transport (DWDM/ROADM). Defines interoperable device, network, and service models for optical equipment. v...


## Lab / Testing (1 tools)

- **[multivendor-evpn-lab](https://github.com/srl-labs/multivendor-evpn-lab)** (score: 63) — `Nokia` ✅ — ⭐ 13
  > Containerlab-based multivendor EVPN lab topology. Spins up Nokia SROS (route reflectors), Nokia SR Linux (leaf), Arista cEOS, and Juniper vQFX in a two-tier Clos fabric with L2 EVPN and OSPF underl...


## Network Analysis (1 tools)

- **[nDPI](https://github.com/ntop/nDPI)** (score: 63) — ⭐ 3,800
  > Open Deep Packet Inspection library from ntop, used under the hood in ntopng, Wireshark, and dozens of commercial appliances. Identifies 500+ application protocols (including BGP, MPLS, gRPC, OpenF...


## Documentation & Diagramming (1 tools)

- **[FossFLOW](https://github.com/stan-smith/FossFLOW)** (score: 54) — ⭐ 850
  > Open-source isometric infrastructure diagramming tool for creating beautiful, hand-crafted infrastructure diagrams. Web-based editor with drag-and-drop components for servers, routers, switches, ra...


## Network OS / Infrastructure (1 tools)

- **[Infix](https://github.com/kernelkit/infix)** (score: 51) — ⭐ 320
  > Immutable, YANG-native Linux NOS that turns any ARM or x86 device (Raspberry Pi to enterprise switches) into a manageable network appliance. Auto-generates CLI from YANG models, supports NETCONF an...


## Network Inventory (1 tools)

- **[Kuwaiba](https://sourceforge.net/projects/kuwaiba/)** (score: 44)
  > Enterprise-grade open source network inventory and CMDB specifically designed for telecom and IT infrastructure. Supports all major core and access technologies, full physical layer (copper, fiber,...


## Network Discovery (1 tools)

- **[Atlas](https://github.com/karam-ajaj/atlas)** (score: 36) — ⭐ 993
  > Full-stack containerized tool to scan, analyze, and visualize network infrastructure. Go-powered scanner with FastAPI backend and React frontend. Auto-discovers Docker containers, local/neighboring...


## Network Operations (1 tools)

- **[hyperglass](https://github.com/thatmattlove/hyperglass)** (score: 36) — `Nokia` (?) — ⭐ 650
  > Self-hosted network looking glass that makes BGP route queries, community lookups, AS path queries, ping, and traceroute accessible via a modern web UI. Built-in Nokia SR OS support along with Aris...


## Network Visualization (1 tools)

- **[NetVisor](https://github.com/a2s-ai/A2S_netvisor)** (score: 33) — ⭐ 200
  > Automatic network topology discovery and interactive visualization. Scans networks, identifies hosts/services, generates interactive topology maps. Docker-based server with distributed daemon agent...


## Reference (1 tools)

- **[Awesome Network Automation](https://github.com/networktocode/awesome-network-automation)** (score: 31) — ⭐ 1,500
  > Curated list of network automation resources. Learning materials, tools, and libraries.


## Infrastructure (1 tools)

- **[OpenFTTH](https://github.com/DAXGRID/open-ftth-frontend)** (score: 29)
  > Open source FTTH (Fiber to the Home) network planning and management system. QGIS integration for route network editing and visualization, fiber splice/termination tracking, and outside plant docum...


## Timing & Synchronization (1 tools)

- **[Statime](https://github.com/pendulum-project/statime)** (score: 29) — ⭐ 286
  > A full Rust implementation of IEEE 1588 Precision Time Protocol (PTP). Supports ordinary clock, boundary clock, and transparent clock roles. Actively maintained by the Pendulum Project (which also ...


## Traffic Engineering (1 tools)

- **[LMTE](https://github.com/Y-debug-sys/LMTE)** (score: 23) — ⭐ 12
  > LLM-driven WAN Traffic Engineering framework (INFOCOM 2026). Uses language models to reason about WAN TE problems. Combines domain-aware prompts, multimodal embeddings, and a lightweight planning h...


## Self-Hosted Infrastructure (1 tools)

- **[Octelium](https://github.com/octelium/octelium)** (score: 18) — ⭐ 3,405
  > Next-gen FOSS self-hosted unified zero trust secure access platform. Operates as remote access VPN, ZTNA platform, API/AI/MCP gateway, PaaS, and ngrok-alternative. Apache-2.0/AGPL licensed.


## Network Lab (1 tools)

- **[wsl-containerlab](https://github.com/srl-labs/wsl-containerlab)** (score: 15) — `Nokia` (?) — ⭐ 37
  > Pre-configured WSL2 Linux distribution purpose-built for Containerlab network labbing on Windows. Bundles Docker, Containerlab, and all required tooling with one-click WSL install. Supports Windows...
