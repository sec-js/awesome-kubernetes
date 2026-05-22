# Kubernetes

!!! info "Architectural Context"
    Detailed reference for Kubernetes in the context of Architectural Foundations.

## Agentic Engineering

### Agentic Frameworks

#### Skills Integration

  - **(2024)** [Level Up Your Agents: Announcing Google's Official Skills Repository](https://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing-googles-official-skills-repository) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Curator Insight: Google's official skills repository and toolkit for modular agentic development.
Live Grounding: Delivers pre-integrated capabilities and action templates allowing Enterprise Gemini Agents to dynamically execute API operations, retrieve structured data, and handle multi-step workflows.

</div></details>
## Cloud Infrastructure

### Orchestration

#### Cluster Resource Management

  - **(2022)** [Allocatable memory and CPU in Kubernetes Nodes 🌟](https://learnkube.com/allocatable-resources) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Technical breakdown of node allocatable resources in Kubernetes. Explains how `kube-reserved`, `system-reserved`, and eviction thresholds reduce physical capacity available for user pods.

</div></details>
#### Managed Kubernetes

  - **(2022)** [**learnk8s.io/research:  Comparison of Kubernetes managed services 🌟**](https://learnkube.com/research) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Comprehensive comparison matrix evaluating key metrics of major managed Kubernetes engines, mapping out scalability limits, upgrade strategies, and CNI setups.

</div></details>
### Service Mesh

#### Istio Mesh

  - **(2026)** [==Istio.io==](https://istio.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The premier open-source service mesh providing advanced traffic management, end-to-end security, and granular observability. Uses Envoy proxies (via sidecars or Ambient mode) to secure and manage microservice fabrics.

</div></details>
## Cloud Native

### Kubernetes (1)

#### Fleet Management

  - **(2025)** [Limitless Kubernetes Scaling for AI and Data-intensive Workloads: The AKS Fleet Strategy](http://blog.aks.azure.com/2025/04/02/Scaling-Kubernetes-for-AI-and-Data-intensive-Workloads) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Deep dives into Azure Kubernetes Service (AKS) Fleet Manager strategies to run multi-cluster AI workloads. Outlines global routing, high-density scheduling optimizations, and cross-cluster resource synchronization required for distributed training.

</div></details>
## Cloud Native Architecture

### Orchestration (1)

#### Kubernetes Pod Lifecycle

  - **(2021)** [**K8s prevent queue worker Pod from being killed during deployment**](https://itnext.io/k8s-prevent-queue-worker-pod-from-being-killed-during-deployment-4252ea7c13f6) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Provides concrete technical implementation strategies to prevent abrupt termination of active queue worker Pods during rolling Kubernetes updates. It details the effective utilization of `preStop` hooks and graceful shutdown signals within Pod specifications. It ensures zero-loss processing of long-running asynchronous messages.

</div></details>
## Cloud-Native Infrastructure

### GitOps and Declarative Delivery

#### Argo Project Ecosystem

  - **(2026)** [ArgoCon North America 2026 Call for Proposals](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/#call-for-proposals) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Curator Insight: Direct portal to community sessions, submissions, and emerging patterns for the Argo GitOps suite in 2026. Live Grounding: Acts as the primary standard gathering point for Kubernetes GitOps continuous delivery. Keeps teams abreast of cutting-edge development paths in orchestration.

</div></details>
## GitOps and Continuous Delivery

### Deployment Strategies

#### Blue-Green

  - **(2022)** [==semaphoreci.com: Continuous Blue-Green Deployments With Kubernetes 🌟==](https://semaphore.io/blog/continuous-blue-green-deployments-with-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A highly-rated technical guide illustrating step-by-step implementation of automated Blue-Green deployments within a Kubernetes cluster. Details traffic switching using Kubernetes Services and ingress resources, highlighting rollback procedures and pipeline workflow integration.

</div></details>
### Progressive Delivery

#### Theory

  - **(2024)** [**harness.io: Progressive Delivery: Everything You Need to Know**](https://www.harness.io/blog) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A masterclass resource explaining the evolutionary shift from standard continuous delivery to progressive delivery. Explains integration of automated canary releases with advanced deployment patterns, metrics monitoring, and developer self-service.

</div></details>
## Infrastructure

### Cluster Provisioning

#### Canonical Juju

  - **(2026)** [**Conjure up**](https://canonical.com/juju) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The canonical toolset for automating cloud operations using Juju charms. Simplifies the installation of Charmed Kubernetes clusters across various clouds. Note: Conjure-up has been fully integrated and evolved directly into Canonical Juju's primary modeling environment.

</div></details>
### Containerization

#### Kernel Internals

  - **(2023)** [**Controlling Process Resources with Linux Control Groups (cgroups)**](https://labs.iximiuz.com/tutorials/controlling-process-resources-with-cgroups) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A deep, interactive laboratory walk-through demonstrating how Linux Control Groups (cgroups) throttle and isolate system resources. Crucial baseline knowledge for understanding container limits in Kubernetes.

</div></details>
## Networking

### Ingress

#### Azure AGC

##### Istio Integration

  - **(2025)** [**Application Gateway for Containers: Istio Integration**](https://blog.cloudtrooper.net/2025/11/21/application-gateway-for-containers-istio-integration) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A modern engineering analysis detailing the integration of Azure Application Gateway for Containers (AGC) with an internal Istio service mesh topology. Focuses on seamless north-south traffic routing and end-to-end TLS bridging configurations inside Azure cloud architectures.

</div></details>
## Platform Engineering

### CI-CD Security

#### Azure DevOps

  - **(2025)** [Dependabot Version Updates in Azure DevOps](https://www.returngis.net/2025/02/dependabot-updates-en-azure-devops) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A practical guide explaining the installation and automated orchestration of Dependabot-style dependency scanning and automated PR version updates within Azure DevOps repositories. Written in Spanish. [SPANISH CONTENT]

</div></details>
## Security

### Identity Management

#### Cloud Integration

  - **(2025)** [**From Zero to Hero with Identity and Access Control in Azure Kubernetes Service**](https://techcommunity.microsoft.com/blog/startupsatmicrosoftblog/from-zero-to-hero-with-identity-and-access-control-in-azure-kubernetes-service/4386350) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Curator Insight: Architect blueprint for managing Microsoft Entra ID integration in Azure Kubernetes Service. Live Grounding: Walks through configuring fine-grained identity federation and replacing Kubernetes cluster roles with enterprise Azure AD mappings.

</div></details>

***
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Cheatsheets](./cheatsheets.md) | [Linux](./linux.md)

