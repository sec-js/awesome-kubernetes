---
description: "Curated, AI-ranked Kubernetes On Premise resources for the 2026 Cloud Native architect: top-tier tools, guides and references (The Container Stack)."
---
# On-Premise Production Kubernetes Cluster Installers

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-on-premise/).

!!! info "Architectural Context"
    Detailed reference for On-Premise Production Kubernetes Cluster Installers in the context of The Container Stack.

## Application Delivery

### Developer Platforms

#### VMware Tanzu

  - **(2022)** [zdnet.com: VMware brings Tanzu Application Platform into GA to ease Kubernetes adoption](https://www.zdnet.com/article/vmware-brings-tanzu-application-platform-into-ga-to-ease-kubernetes-adoption) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — News of VMware's general availability announcement of Tanzu Application Platform (TAP). TAP serves as an enterprise-grade PaaS (Platform-as-a-Service) overlay on Kubernetes, packaging cloud-native buildpacks, API portals, Cartographer supply chains, and security scanning tools to deliver a streamlined developer experience.
## Infrastructure

### Container Runtimes

#### Sandboxing

  - **(2021)** [==Kata Containers on MicroK8s==](https://github.com/didier-durand/microk8s-kata-containers) <span class='md-tag md-tag--info'>⭐ 34</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ab473c19" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 12 L 20 6 L 30 12 L 40 11 L 50 2" fill="none" stroke="url(#spark-grad-ab473c19)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community repository providing integration instructions and configurations to run Kata Containers within a Canonical MicroK8s environment. This architecture allows security teams to deploy hardware-isolated, hypervisor-sandboxed container runtimes (using QEMU or Cloud Hypervisor) inside lightweight local clusters, resolving tenant isolation concerns in multi-tenant environments.
### Kubernetes Distributions

#### Edge and IoT

  - **(2026)** [==K0s - Zero Friction Kubernetes==](https://github.com/k0sproject/k0s) <span class='md-tag md-tag--info'>⭐ 6239</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e23c48a1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 5 L 20 12 L 30 2 L 40 9 L 50 4" fill="none" stroke="url(#spark-grad-e23c48a1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official open-source repository for the k0s Kubernetes distribution. Features active enterprise-grade developer tracks, offering built-in advanced networking plugins (Calico CNI, Kube-router), support for virtualized control planes, and automated bootstrapping tools without external dependencies.
  - **(2023)** [==xiaods/k8e==](https://github.com/xiaods/k8e) <span class='md-tag md-tag--info'>⭐ 449</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-93a7dc4f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 5 L 20 9 L 30 10 L 40 13 L 50 2" fill="none" stroke="url(#spark-grad-93a7dc4f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A lightweight Kubernetes distribution (k8e, standing for "k8s easy") modeled after K3s but strictly adhering to standard upstream components. It is tailored for low-resource edge architectures, CI environments, and hobbyist networks requiring low memory profiles and simple setups.
  - **(2026)** [**Microk8s**](https://canonical.com/microk8s) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Canonical's lightweight, zero-ops Kubernetes distribution designed for developers, IoT devices, and edge computing. MicroK8s is packaged as a single snap package with automatic updates, high-availability clustering, and a modular architecture that supports one-click deployment of common add-ons like Istio, Knative, and GPU acceleration.
  - **(2026)** [k0s](https://k0sproject.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Mirantis' zero-friction, single-binary Kubernetes distribution. Designed to operate across any cloud, hybrid, or edge infrastructure, k0s packages all control plane and node dependencies in a single executable, drastically simplifying lifecycle maintenance, upgrading, and operational footprint.
## Networking

### Service Mesh

#### VMware Tanzu (1)

  - **(2020)** [blogs.vmware.com: VMware Tanzu Service Mesh, built on VMware NSX is Now Available!](https://blogs.vmware.com/networkvirtualization/2020/03/vmware-tanzu-service-mesh-built-on-vmware-nsx-is-now-available.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement of VMware Tanzu Service Mesh (TSM), an Istio-based commercial service mesh integrated with VMware NSX. TSM delivers end-to-end traffic management, zero-trust security policies, cross-cluster connectivity, and deep API observability across hybrid and multi-cloud Kubernetes deployments.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

