# Iac

!!! info "Architectural Context"
    Detailed reference for Iac in the context of Hardened Infrastructure.

## Cloud Infrastructure

### Azure

#### Enterprise Architecture

  - **(2024)** [Transitioning an Existing Azure Environment to the Azure Landing Zone Reference Architecture](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/enterprise-scale/transition) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Official Microsoft guidance outlining the migration roadmap of legacy brownfield Azure environments to the Azure Landing Zone (ALZ) conceptual architecture. It focuses on governance, subscription organization, network topology convergence, and security policy enforcement at scale.
#### Platform Engineering

  - **(2024)** [Subscription Vending Implementation Guidance](https://learn.microsoft.com/en-us/azure/architecture/landing-zones/subscription-vending) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the architectural pattern of automated subscription vending on Azure.

*   Guides cloud platform teams to construct GitOps-driven workflows.
*   Automatically provisions fully governed, secure, and networked Azure subscriptions using Bicep or Terraform.
## Platform Engineering (1)

### AI Integration

#### Agentic Engineering

  - **(2025)** [**Terraform & OpenTofu Skill for AI Agents**](https://github.com/antonbabenko/terraform-skill) <span class='md-tag md-tag--info'>⭐ 1881</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An experimental, open-source repository establishing unified Model Context Protocol (MCP) skills or AI tools for Terraform and OpenTofu. Empowers AI agents to dynamically generate, parse, validate, and execute infrastructure-as-code definitions with semantic awareness.
### CI-CD Pipelines

#### Infrastructure as Code

##### GitHub Actions

  - **(2022)** [Terraform Module Releaser GitHub Action](https://github.com/techpivot/terraform-module-releaser) <span class='md-tag md-tag--info'>⭐ 221</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized GitHub Action designed to automate the release process, version tagging, and registry publication of Terraform modules. Resolves development overhead by automatically generating release logs and enforcing Semantic Versioning.

---
💡 **Explore Related:** [Terraform](./terraform.md) | [Kubernetes Security](./kubernetes-security.md) | [Devsecops](./devsecops.md)

