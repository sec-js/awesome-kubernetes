# Flux. The GitOps operator for Kubernetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/flux/).

!!! info "Architectural Context"
    Detailed reference for Flux. The GitOps operator for Kubernetes in the context of Engineering Pipeline.

## Networking and Security

### Service Mesh and Gateway

#### Envoy

  - **(2022)** [**solo.io: The 3 best ways to use Flux and Flagger for GitOps with your Envoy Proxy API gateways**](https://www.solo.io/blog/the-3-best-ways-to-use-flux-and-flagger-for-gitops-with-your-envoy-proxy-api-gateways) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Outlines integration patterns for orchestrating progressive delivery at the ingress boundary using Flux, Flagger, and Envoy-based gateways. Evaluates traffic-shifting methodologies including canary deployments, A/B testing, and blue-green releases. Live Grounding confirms Envoy-based ingress traffic shaping remains the de facto method for automated canary analysis in cloud-native topologies.
## Platform Engineering

### GitOps and Deployment

#### Flux Ecosystem

  - **(2026)** [==github: Flux Version 2==](https://github.com/fluxcd/flux2) <span class='md-tag md-tag--info'>⭐ 8186</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6d4e9fa2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 12 L 20 11 L 30 13 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-6d4e9fa2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official active repository for Flux v2. Rebuilt from the ground up as a set of Kubernetes controllers (GitOps Toolkit) to allow decoupled, highly parallel reconciliation of Git configurations.
  - **(2021)** [==github: Flux==](https://github.com/fluxcd/flux) <span class='md-tag md-tag--info'>⭐ 6861</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-520daebf" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 13 L 20 2 L 30 12 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-520daebf)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — The deprecated and archived GitHub repository for the original Flux v1 GitOps engine. Completely succeeded by the microservice-driven, decoupled Flux v2 architecture.
  - **(2026)** [Flux](https://fluxcd.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main ecosystem page for Flux, a CNCF Graduated tool designed for GitOps continuous delivery. Keeps Kubernetes clusters synchronized with version-controlled repositories, supporting declarations via Helm, Kustomize, and native YAML.
  - **(2026)** [toolkit.fluxcd.io: GitOps Toolkit 🌟](https://fluxcd.io/flux) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the modular architecture of Flux v2 (source-controller, kustomize-controller, helm-controller, notification-controller). Allows platform teams to customize GitOps engines using dedicated custom resource definitions.
  - **(2025)** [docs.microsoft.com: Configurations and GitOps with Azure Arc enabled Kubernetes](https://learn.microsoft.com/en-us/azure/azure-arc/kubernetes/conceptual-gitops-flux2) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Microsoft's guide to deploying enterprise multi-cluster configurations using Azure Arc integrated with Flux v2 GitOps extensions. Enables unified policy-driven application deployment across hybrid cloud estates.
  - **(2022)** [thenewstack.io: GitOps at Home: Automate Code Deploys with Kubernetes and Flux](https://thenewstack.io/gitops-at-home-automate-code-deploys-with-kubernetes-and-flux) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical walkthrough for setting up self-hosted GitOps pipelines on homelabs or small clusters using Flux. Highlights automated deployment routines and resource orchestration.
  - **(2021)** [docs.fluxcd.io](https://docs.fluxcd.io/en/1.22.2) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Archived reference documentation for the legacy Flux v1 orchestrator. Left online purely as historical reference; teams must use modern Flux v2 systems for controller architectures and security controls.
  - **(2021)** [blog.sldk.de: Introduction to GitOps on Kubernetes with Flux v2 🌟](https://blog.sldk.de/2021/02/introduction-to-gitops-on-kubernetes-with-flux-v2) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A clear introduction to the fundamental architecture of Flux v2. Explains key resources including GitRepository, Kustomization, and how they combine to deploy reliable workloads.
  - **(2020)** [alicegg.tech: Managing a Kubernetes cluster with Helm and FluxCD](https://alicegg.tech/2020/11/09/helm) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed architectural analysis of managing Helm releases within Flux GitOps pipelines. Explores automated release upgrades, HelmRepository declarations, and rollback mechanisms.
## Storage and Databases

### Cloud-Native Storage

#### Stateful GitOps

  - **(2022)** [thenewstack.io: Deploy Stateful Workloads on Kubernetes with Ondat and FluxCD](https://thenewstack.io/deploy-stateful-workloads-on-kubernetes-with-ondat-and-fluxcd) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores deploying resilient, stateful microservices using Ondat (formerly StorageOS) as a persistent software-defined storage layer combined with Flux for deployment state synchronization. Live Grounding notes that while Ondat offered advanced CSI-driven capabilities, consolidation in the cloud-native storage sector has shifted focus toward alternatives like Longhorn, Rook/Ceph, or cloud-managed block storage.

---
💡 **Explore Related:** [Jenkins](./jenkins.md) | [Tekton](./tekton.md) | [Argo](./argo.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

