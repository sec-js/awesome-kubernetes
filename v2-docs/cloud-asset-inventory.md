# Cloud Asset Inventory

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/cloud-asset-inventory/).

!!! info "Architectural Context"
    Detailed reference for Cloud Asset Inventory in the context of Architectural Foundations.

## Table of Contents

1. [Cloud Infrastructure and Orchestration](#cloud-infrastructure-and-orchestration)
  - [Asset Management and Governance](#asset-management-and-governance)
    - [Cloud Analytics](#cloud-analytics)
  - [Storage and Databases](#storage-and-databases)
    - [Distributed Block Storage](#distributed-block-storage)
1. [Infrastructure as Code](#infrastructure-as-code)
  - [Architecture](#architecture)
    - [Diagrams](#diagrams)

## Cloud Infrastructure and Orchestration

### Asset Management and Governance

#### Cloud Analytics

  - **(2026)** [cloudquery.io: Cloud Query: The open-source cloud asset inventory powered by SQL](https://www.cloudquery.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source high-performance security and asset discovery tool that parses cloud configuration APIs into standard SQL databases. Enables infrastructure teams to perform complex auditing, compliance mapping, and security reporting.
  - **(2023)** [cloudquery.io: Building an Open-Source Cloud Asset Inventory with CloudQuery and Grafana](https://www.cloudquery.io/learning-center/cloud-asset-management) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step implementation guide detailing how to ingest cloud infrastructure state via CloudQuery and visualize data patterns within Grafana. Outlines pipeline construction, scheduling, and database optimization.
### Storage and Databases

#### Distributed Block Storage

  - **(2026)** [==Ceph: A Distributed Object, Block, and File Storage Platform==](https://github.com/ceph/ceph) <span class='md-tag md-tag--info'>⭐ 16707</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2d010a68" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 2 L 20 3 L 30 2 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-2d010a68)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[C++ CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An enterprise-grade, highly scalable distributed storage ecosystem providing object, block, and file system storage on a single unified cluster. Widely adopted as the primary storage layer backing cloud platforms and Kubernetes orchestration (Rook-Ceph).
## Infrastructure as Code

### Architecture

#### Diagrams

  - **(2024)** [CloudCanvas - Diagramming for Cloud Infrastructure](https://cloudcanvas.co) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — CloudCanvas is an emerging interactive workspace tool tailored for designing cloud topologies and auto-generating infrastructure-as-code manifests. By linking architectural nodes directly to API-driven configurations, it helps bridge the gap between architectural diagramming and operational execution.

---
💡 **Explore Related:** [About](./about.md) | [Demos](./demos.md) | [Kubernetes](./kubernetes.md)

