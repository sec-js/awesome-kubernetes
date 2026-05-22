# Gitops

!!! info "Architectural Context"
    Detailed reference for Gitops in the context of Engineering Pipeline.

## Application Delivery

### Helm

#### Alternative Engines

  - **(2025)** [**Nelm: A Helm Alternative for Kubernetes Deployments**](https://github.com/werf/nelm) <span class='md-tag md-tag--info'>⭐ 1072</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An innovative deployment engine integrated within the Werf workflow that functions as an alternative to native Helm release tracking. It resolves Helm's tracking limitations by ensuring strict live cluster validation and resource health monitoring.
### Infrastructure as Code

#### Terraform Components

  - **(2024)** [AWS EKS Argo CD Terraform Component](https://github.com/cloudposse-terraform-components/aws-eks-argocd) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Enterprise-ready Terraform submodule designed to deploy, configure, and bootstrap Argo CD onto an existing AWS EKS cluster. Live Grounding: Standardizes complex security configuration flags, integrates smoothly with AWS IAM roles for service accounts (IRSA), and provisions preconfigured Helm-based releases.
## Infrastructure

### GitOps

#### Cluster Provisioning

  - **(2022)** [Weave Kubernetes System Control - wksctl](https://github.com/weaveworks/wksctl) <span class='md-tag md-tag--info'>⭐ 389</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — An early GitOps-driven Kubernetes cluster manager from Weaveworks that provisioned clusters from a declared state stored in git. Following Weaveworks' operational shutdown, this project is considered legacy but remains highly influential in GitOps control-loop architecture history.
## Networking

### Container Network Interface

#### CNI Plugins

  - **(2024)** [github: Weave Net - Weaving Containers into Applications](https://github.com/weaveworks/weave) <span class='md-tag md-tag--info'>⭐ 6613</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Weave Net is a resilient container CNI designed to create peer-to-peer overlay networks without external databases or configurations. The project was officially archived by Weaveworks in 2024, prompting teams to migrate to more modern CNI plugins like Cilium and Calico.

---
💡 **Explore Related:** [Cicd](./cicd.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Jenkins](./jenkins.md)

