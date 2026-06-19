# Kubernetes Releases

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-releases/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Releases in the context of The Container Stack.

## Kubernetes Core

### Releases

#### v1.28 Features

  - **(2023)** [thenewstack.io: Kubernetes 1.28 Accommodates the Service Mesh, Sudden Outages](https://thenewstack.io/kubernetes-1-28-accommodates-the-service-mesh-sudden-outages)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry report covering Kubernetes 1.28's key updates, notably native support for sidecar container lifecycles to aid service mesh deployments, and automated recovery controls for sudden node failures. These updates greatly reduce the coordination code needed for robust, multi-tenant microservices clusters.
### Resource Management

#### Pod Resize

  - **(2023)** [kubernetes.io: Kubernetes 1.27: In-place Resource Resize for Kubernetes Pods (alpha)](https://kubernetes.io/blog/2023/05/12/in-place-pod-resize-alpha) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — Reviews the highly anticipated alpha feature in Kubernetes 1.27: In-place Resource Resize for Pods. This allows engineers to dynamically scale CPU and memory resources allocated to running containers without requiring a pod restart. This capability drastically improves availability and operational costs for scaling-heavy stateful applications and microservices.
## Platform Engineering

### Job Scheduling

#### Batch Workloads

  - **(2024)** [**Kueue Release v0.14.0**](https://github.com/kubernetes-sigs/kueue/releases/tag/v0.14.0) <span class='md-tag md-tag--info'>⭐ 2563</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-faaefc1e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 12 L 20 4 L 30 12 L 40 9 L 50 5" fill="none" stroke="url(#spark-grad-faaefc1e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight details the Kueue v0.14.0 release for advanced batch queuing in Kubernetes. Live engineering in 2026 highlights Kueue as the de facto standard for queuing, resource-sharing, and optimizing ML/AI compute clusters using standard scheduling components.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

