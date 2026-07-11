---
description: "Curated, AI-ranked Openshift resources for the 2026 Cloud Native architect: top-tier tools, guides and references (The Container Stack)."
---
# OpenShift Container Platform

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/openshift/).

!!! info "Architectural Context"
    Detailed reference for OpenShift Container Platform in the context of The Container Stack.

## CI-CD

### GitLab

#### OpenShift

  - **(2017)** [Get started with OpenShift Origin 3 and GitLab](https://about.gitlab.com/blog/get-started-with-openshift-origin-3-and-gitlab) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical tutorial tracking early integration patterns between GitLab CI/CD and OpenShift Origin 3. Demonstrates pipeline orchestration, runner allocation, and deployment tasks. Replaced by GitOps-driven pipelines in contemporary architectures.
## Databases

### Relational

#### MariaDB

  - **(2026)** [github.com/sclorg/mariadb-container](https://github.com/sclorg/mariadb-container) <span class='md-tag md-tag--info'>⭐ 32</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1673fd96" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 10 L 20 8 L 30 8 L 40 12 L 50 13" fill="none" stroke="url(#spark-grad-1673fd96)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official SCLOrg MariaDB container image optimized specifically for Kubernetes platforms. Includes integrated security scripts, support for arbitrary non-root UID execution, and custom database initialization configurations.
## Kubernetes and OpenShift

### Networking

#### Multi-Cluster

  - **(2020)** [developers.redhat.com: Skupper.io: Let your services communicate across Kubernetes clusters](https://developers.redhat.com/blog/2020/01/01/skupper-io-let-your-services-communicate-across-kubernetes-clusters) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Skupper.io enables cross-cluster microservice communications through an application-level Virtual Application Network (VAN). Contrasting original claims of simple setups, live engineering consensus in 2026 demonstrates Skupper's high architectural value in enterprise hybrid clouds, routing traffic via AMQP without complex VPNs or firewall modifications.
### Security

#### Ingress

  - **(2019)** [itnext.io: Adding security layers to your App on OpenShift — Part 1: Deployment and TLS Ingress 🌟](https://itnext.io/adding-security-layers-to-your-app-on-openshift-part-1-deployment-and-tls-ingress-9ef752835599) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step tutorial addressing TLS edge termination and ingress security on Red Hat OpenShift. Demonstrates path-based routing configurations, SSL/TLS certificate integration, and header manipulation rules to secure microservices from perimeter ingress points.
## Performance Engineering

### Kubernetes Optimization

#### Autonomous Tuning

  - **(2025)** [**How Kruize Optimizes OpenShift Workloads**](https://developers.redhat.com/articles/2025/06/25/how-kruize-optimizes-openshift-workloads) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Technical review explaining how the Kruize Autotune project leverages prometheus metrics to autonomously profile and adjust microservices allocations on enterprise OpenShift clusters.
## Platform Engineering

### Architectural Insights

#### Personal Blog

  - **(2020)** [schabell.org: Cloud-native development - A blueprint 🌟](https://www.schabell.org/2020/05/cloud-native-development-a-blueprint.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural blueprints and patterns focusing on constructing container-native applications using modern microservices and API gateways. Written by a Red Hat technology evangelist. Extremely useful for understanding how early microservices evolved to cloud-native setups in 2026.
## Software Engineering

### Collaboration

#### Rocket.Chat

  - **(2022)** [opensource.com: Why choose Rocket.Chat for your open source chat tool](https://opensource.com/article/22/1/rocketchat-data-privacy) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical review advocating for Rocket.Chat as a privacy-focused, scalable, open-source communication application. Provides design concepts for self-hosting chat infrastructure inside sandboxed container platforms.

---
💡 **Explore Related:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md)

🔗 **See Also:** [Javascript](./javascript.md) | [QA](./qa.md)

