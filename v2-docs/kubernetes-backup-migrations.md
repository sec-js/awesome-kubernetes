---
description: "Top Kubernetes Backup Migrations resources for 2026, AI-ranked: Stash, konveyor and more — curated Cloud Native tools, guides and references."
---
# Kubernetes Backup and Migrations

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-backup-migrations/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Backup and Migrations in the context of The Container Stack.

## Application Migration

### Modernization

#### Enterprise Migration

  - **(2020)** [**konveyor 🌟**](https://konveyor.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An open-source application modernization platform that helps developers migrate legacy virtual machines, stateful services, and bare-metal workloads to Kubernetes. It provides discovery, analysis, and execution tools for large-scale container migrations.
## Infrastructure

### Control Plane

#### ETCD Administration

  - **(2025)** [**github.com/gardener/etcd-backup-restore**](https://github.com/gardener/etcd-backup-restore) <span class='md-tag md-tag--info'>⭐ 329</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0e9692b3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 8 L 20 8 L 30 10 L 40 2 L 50 12" fill="none" stroke="url(#spark-grad-0e9692b3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Developed under the Gardener project, this agent automates snapshot generation, compression, and synchronization of multi-node ETCD clusters. Continuously writes transactional delta logs to private S3 endpoints.
### Data Protection

#### GitOps Synchronizers

  - **(2023)** [kube-backup: Kubernetes resource state sync to git](https://github.com/pieterlange/kube-backup) <span class='md-tag md-tag--info'>⭐ 493</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-631d607c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 9 L 20 6 L 30 7 L 40 9 L 50 10" fill="none" stroke="url(#spark-grad-631d607c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Automates Kubernetes resource state replication directly to target Git repositories. This pattern acts as an early architectural precursor to fully fledged declarative GitOps platforms, maintaining a point-in-time configuration ledger.
#### Kubernetes Backup Operators

  - **(2026)** [==github.com/vmware-tanzu/velero==](https://github.com/velero-io/velero) <span class='md-tag md-tag--info'>⭐ 10062</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1fef8e38" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 10 L 20 7 L 30 12 L 40 5 L 50 4" fill="none" stroke="url(#spark-grad-1fef8e38)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Velero is the standard open-source utility for safely backing up and restoring entire Kubernetes cluster structures and persistent volumes. Deeply integrates with both raw cloud APIs and file-level utilities like Kopia and Restic.
  - **(2025)** [**k8up.io**](https://k8up.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — K8up uses standard CRD objects to configure high-frequency Restic backups on selected persistent volumes. Offers integrated S3 exports, backup target management, and pruning policies.
  - **(2024)** [**Stash**](https://github.com/stashed/stash) <span class='md-tag md-tag--info'>⭐ 1416</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e454a632" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 4 L 20 11 L 30 9 L 40 13 L 50 2" fill="none" stroke="url(#spark-grad-e454a632)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An advanced Kubernetes-native operator utilizing Restic underneath to back up stateful persistent volumes. Stash implements native CSI VolumeSnapshot integrations to handle application-consistent recovery processes with automated deduplication.
### Workload Mobility

#### Migration Toolkits

  - **(2025)** [**github.com/konveyor 🌟**](https://github.com/konveyor) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An open-source modernization and migration suite designed to analyze, refactor, and migrate complex application workloads to Kubernetes across multiple physical and cloud ecosystems.
  - **(2024)** [**github.com/konveyor/crane: Crane 2.0 🌟**](https://github.com/migtools/crane) <span class='md-tag md-tag--info'>⭐ 54</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-552f272c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 5 L 20 6 L 30 5 L 40 10 L 50 11" fill="none" stroke="url(#spark-grad-552f272c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Crane 2.0 provides continuous state synchronization, target resource modifications, and mock-run configurations to assist operators with real-time Kubernetes cluster replatforming campaigns.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md) | [Docker](./docker.md)

🔗 **See Also:** [Javascript](./javascript.md) | [QA](./qa.md)

