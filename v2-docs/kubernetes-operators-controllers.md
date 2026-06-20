---
description: "Top Kubernetes Operators Controllers resources for 2026, AI-ranked: Kueue Release v0.14.0, Kubernetes Gateway API and more — curated Cloud Native tools, guides."
---
# Kubernetes Operators and Controllers

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-operators-controllers/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Operators and Controllers in the context of The Container Stack.

## CICD Pipeline

### Kubernetes and Containers

#### Self-Hosted Infrastructure

  - **(2020)** [==github.com/actions/actions-runner-controller 🌟==](https://github.com/actions/actions-runner-controller) <span class='md-tag md-tag--info'>⭐ 6298</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-69d3828b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 11 L 20 3 L 30 4 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-69d3828b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official Kubernetes operator designed to manage self-hosted GitHub Actions runner infrastructure dynamically. Integrates natively with Horizontal Pod Autoscaler (HPA) targets to scale runner deployments in response to webhook event metrics.
## Cloud Native Infrastructure

### Kubernetes Extension

#### Operators Go

  - **(2022)** [dev.to/hkhelil: Building a Kubernetes Operator with an NGINX CRD](https://dev.to/hkhelil/building-a-kubernetes-operator-with-an-nginx-crd-3lil) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A step-by-step developer tutorial building an NGINX web server operator from scratch. It guides the reader through CRD definitions and controller structures, making it an excellent practical entry point for understanding the reconciliation model in a hands-on way.
## Data and Databases

### Lifecycle Management

#### Schema Migrations

  - **(2024)** [==coderanger/migrations-operator: Migrations-Operator==](https://github.com/coderanger/migrations-operator) <span class='md-tag md-tag--info'>⭐ 136</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ece28878" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 11 L 20 10 L 30 6 L 40 4 L 50 7" fill="none" stroke="url(#spark-grad-ece28878)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — This controller coordinates database schema migration jobs relative to active deployment rollouts. By intercepting deployment events, it executes schema changes as blocking preparatory steps, ensuring application microservices only start up once target database structures align.
## Infrastructure

### Container Orchestration

#### Kubernetes Operators

  - **(2023)** [itnext.io: Operator Lifecycle Manager](https://itnext.io/wth-is-a-operator-lifecycle-manager-873cf1661b04) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains Operator Lifecycle Manager (OLM) as part of the Operator Framework. Highlights catalog management, automated dependency resolution, security upgrades, and dynamic operator scaling across production enterprise clusters.
## Networking

### Ingress and Gateway

#### Controllers

  - **(2021)** [InGate: Ingress & Gateway API Controller (Archived)](https://github.com/kubernetes-sigs/ingate) <span class='md-tag md-tag--info'>⭐ 728</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-80365125" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 11 L 20 10 L 30 12 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-80365125)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — Architectural prototype designed to test Ingress integration patterns. Live engineering truth confirms this repository is archived by SIG-Network, as development has shifted entirely toward the standardized Gateway API.
#### Gateway API

  - **(2023)** [**Kubernetes Gateway API**](https://github.com/kubernetes-sigs/gateway-api) <span class='md-tag md-tag--info'>⭐ 2885</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-223c2abf" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 3 L 20 7 L 30 4 L 40 9 L 50 5" fill="none" stroke="url(#spark-grad-223c2abf)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Official GitHub repository for the standard Kubernetes Gateway API. This next-generation specification supersedes standard Ingress, offering expressive, role-oriented, and extensible routing APIs (Gateway, GatewayClass, and Route resources).
## Observability

### Distributed Tracing

#### OpenTelemetry Operator

  - **(2021)** [==github.com/open-telemetry/opentelemetry-operator==](https://github.com/open-telemetry/opentelemetry-operator) <span class='md-tag md-tag--info'>⭐ 1717</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f7fd3211" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 4 L 20 5 L 30 7 L 40 8 L 50 5" fill="none" stroke="url(#spark-grad-f7fd3211)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kubernetes operator for automating the deployment and management of the OpenTelemetry Collector. Simplifies application instrumentation via automated inject mechanisms for Java, NodeJS, Python, and Dotnet, facilitating declarative telemetry pipeline management across clusters.
## Platform Engineering

### Job Scheduling

#### Batch Workloads

  - **(2024)** [**Kueue Release v0.14.0**](https://github.com/kubernetes-sigs/kueue/releases/tag/v0.14.0) <span class='md-tag md-tag--info'>⭐ 2563</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-faaefc1e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 12 L 20 4 L 30 12 L 40 9 L 50 5" fill="none" stroke="url(#spark-grad-faaefc1e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight details the Kueue v0.14.0 release for advanced batch queuing in Kubernetes. Live engineering in 2026 highlights Kueue as the de facto standard for queuing, resource-sharing, and optimizing ML/AI compute clusters using standard scheduling components.
## Security and Identity

### Secrets Management

#### External Secrets Sync

  - **(2021)** [contentful-labs/kube-secret-syncer 🌟](https://github.com/contentful-labs/kube-secret-syncer) <span class='md-tag md-tag--info'>⭐ 194</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-cf2e5f56" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 12 L 20 9 L 30 9 L 40 8 L 50 13" fill="none" stroke="url(#spark-grad-cf2e5f56)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A targeted operator designed to synchronize secrets securely from external services (specifically AWS Parameter Store) directly into native Kubernetes Secrets, ensuring cloud-hosted secrets stay continuously aligned with active workloads.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

