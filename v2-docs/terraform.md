# Terraform

!!! info "Architectural Context"
    Detailed reference for Terraform in the context of Hardened Infrastructure.

## Cloud Infrastructure

### Infrastructure as Code

#### AI Generation

  - **(2025)** [Terraform 2.0 in Practice: Using AI to Generate Infrastructure as Code](https://markaicode.com/terraform-ai-infrastructure-as-code)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on AI-driven generation of HCL infrastructure files. Covers schema checking, validating security guardrails in prompt pipelines, and continuous integration workflows for automated infrastructure verification.
#### Testing Practices

  - **(2025)** [AI Meets Terraform: Prompt Strategies for Test Generation](https://masterpoint.io/blog/ai-meets-tf-prompt-strategies-for-test-generation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines specific prompting strategies to automatically draft tests for Terraform modules. Synthesizes automated validation frameworks like `terraform test` with generative AI outputs to ensure infrastructure stability.
### Kubernetes Distributions

#### Bare-Metal and Edge

  - **(2026)** [**poseidon/typhoon**](https://github.com/poseidon/typhoon) <span class='md-tag md-tag--info'>⭐ 2042</span> <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Typhoon is a bare-metal and multi-cloud Kubernetes distribution focused on simplicity. Built entirely with Terraform and running on Flatcar Container Linux, it provides a stable setup that operates efficiently without heavy proprietary layers.
## Cloud Providers

### AWS EKS

#### Infrastructure as Code (1)

  - **(2026)** [==github.com/aws-ia/terraform-aws-eks-blueprints (examples) 🌟🌟🌟==](https://github.com/aws-ia/terraform-aws-eks-blueprints) <span class='md-tag md-tag--info'>⭐ 3021</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A highly opinionated, production-ready collection of Terraform modules designed to accelerate Amazon EKS cluster deployments. Live Grounding highlights its architecture for bootstrapping clusters with essential add-ons like Karpenter, AWS Load Balancer Controller, and Prometheus. It represents the industry standard for declarative EKS infrastructure provisioning.
## Security

### Certificates

#### TLS Automation

  - **(2021)** [getbetterdevops.io: How to Secure K8S Nginx Ingress With Let’s Encrypt and Cert Manager](https://www.empowersurvivors.net) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Rescued guide detailing the technical orchestration steps of cert-manager and Let's Encrypt certificates mapping over NGINX Ingress controllers for ingress traffic protection.

---
💡 **Explore Related:** [Iac](./iac.md) | [Kubernetes Security](./kubernetes-security.md) | [Devsecops](./devsecops.md)

