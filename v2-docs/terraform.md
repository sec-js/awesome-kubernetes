---
description: "Curated, AI-ranked Terraform resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Hardened Infrastructure)."
---
# Hashicorp Terraform and Packer. Kubernetes Boilerplates

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/terraform/).

!!! info "Architectural Context"
    Detailed reference for Hashicorp Terraform and Packer. Kubernetes Boilerplates in the context of Hardened Infrastructure.

## AWS

### Container Registry

#### Monitoring

  - **(2023)** [porscheofficial/terraform-aws-ecr-watch](https://github.com/porscheofficial/terraform-aws-ecr-watch) <span class='md-tag md-tag--info'>⭐ 70</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0e8000d6" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 10 L 20 11 L 30 11 L 40 7 L 50 10" fill="none" stroke="url(#spark-grad-0e8000d6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source Terraform automation module constructed to monitor AWS Elastic Container Registry (ECR) push actions. It facilitates automated security audits, vulnerability tracking, and dynamic alert dispatches to external systems during image push phases.
### EKS

#### Networking

  - **(2023)** [dev.to/aws-builders: Navigating AWS EKS with Terraform: Understanding VPC Essentials for EKS Cluster Management](https://dev.to/aws-builders/navigating-aws-eks-with-terraform-understanding-vpc-essentials-for-eks-cluster-management-51e3) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This architectural guide details the creation of secure, high-availability VPC networks tailored for AWS Elastic Kubernetes Service (EKS). It provides systematic designs for public/private subnet distribution, NAT Gateways, and route table controls to achieve optimal isolation. The author emphasizes standard modular Terraform paradigms for constructing multi-AZ network topographies.
#### Security

  - **(2023)** [dev.to/verifacrew: How to assume an AWS IAM role from a Service Account in EKS with Terraform](https://dev.to/verifacrew/how-to-assume-an-aws-iam-role-from-a-service-account-in-eks-with-terraform-28gd) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walks through implementing AWS IAM Roles for Service Accounts (IRSA) inside EKS using Terraform configuration templates. Explains federated identity mapping via OpenID Connect (OIDC) to enable native Kubernetes service accounts to assume precise IAM roles. This guide enforces the Principle of Least Privilege for pod execution environments.
## Azure

### AKS

#### Artificial Intelligence

  - **(2024)** [techcommunity.microsoft.com: Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit chat app in AKS using Terraform](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/create-an-azure-openai-langchain-chromadb-and-chainlit-chat-app-in-aks-using-ter/4024070) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An innovative blueprint outlining how to build a generative AI application on Azure Kubernetes Service (AKS) using Terraform. It walks through orchestration of LangChain pipelines, ChromaDB vector storage, Chainlit interfaces, and secure integration with Azure OpenAI endpoints.
### App Service

#### Security (1)

  - **(2023)** [build5nines.com: Terraform: Deploy Azure App Service with Key Vault Secret Integration](https://build5nines.com/terraform-deploy-azure-app-service-with-key-vault-secret-integration) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Highlights secure integration methods for linking Azure Key Vault to App Service. Shows how to avoid storing plain-text credentials in code by leveraging Managed System Identities to read parameters.
### Serverless

#### Function App

  - **(2023)** [build5nines.com: Terraform: Deploy Azure Function App with Consumption Plan](https://build5nines.com/terraform-deploy-azure-function-app-with-consumption-plan) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical reference showing how to provision an Azure Function App under a Consumption Plan. It outlines infrastructure parameters such as storage dependencies, App Service Plans, and runtime environments in standard HCL code.
## Cloud Infrastructure

### AWS (1)

#### Compute and Serverless

  - **(2023)** [dev.to/aws-builders: Deploying a Containerized App to ECS Fargate Using a Private ECR Repo & Terragrunt](https://dev.to/aws-builders/deploying-a-containerized-app-to-ecs-fargate-using-a-private-ecr-repo-terragrunt-5b8a) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A container orchestration blueprint demonstrating ECS Fargate deployment via Terragrunt. Uses secure private ECR registries, ECS Task definitions, and automated cloud network isolation patterns to run enterprise-grade microservices.
#### EKS and Container Orchestration

  - **(2023)** [dev.to/aws-builders: My Service Mesh journey with Terraform on AWS Cloud - Part 1](https://dev.to/aws-builders/my-service-mesh-journey-with-terraform-on-aws-cloud-part-1-3hee) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Part 1 of a structured technical series exploring AWS App Mesh infrastructure configured via Terraform. Establishes core service mesh primitives, including virtual routers, nodes, and transport-layer TLS certificates.
### Platform Engineering

#### Application Operations

  - **(2021)** [shipa.io: Terraform meets AppOps 🌟](https://shipa.io/terraform-meets-appops-2)  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details how integrating Shipa's AppOps architecture with declarative Terraform plans bridges the gap between infrastructure deployment and application runtime operations, giving application developers direct deployment capabilities.
## Cloud Native

### Kubernetes

#### AWS EKS

  - **(2024)** [spacelift.io: How to Provision an AWS EKS Kubernetes Cluster with Terraform](https://spacelift.io/blog/terraform-eks) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A production-focused Spacelift tutorial for deploying AWS EKS using modern terraform-aws-eks modules. Details critical path definitions including VPC setups, IAM OIDC providers, KMS encryption keys, and node group autoscaling profiles.
#### Anti-Patterns

  - **(2020)** [itnext.io: Terraform: don’t use kubernetes provider with your cluster resource! 🌟](https://itnext.io/terraform-dont-use-kubernetes-provider-with-your-cluster-resource-d8ec5319d14a) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An essential warning on a common architectural anti-pattern: configuring the Terraform Kubernetes provider to authenticate dynamically with a cluster declared inside the same workspace execution run. Explains why dynamic provider instantiation causes state locking errors and plan-time dependency loops.
#### Application Delivery

  - **(2021)** [opensource.com: How I use Terraform and Helm to deploy the Kubernetes Dashboard 🌟](https://opensource.com/article/21/8/terraform-deploy-helm) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates deploy automation patterns combining Terraform with Helm. Demonstrates the mechanics of deploying cluster-level operational workloads like the Kubernetes Dashboard by using the Terraform Helm provider, aligning underlying platform provisioning with packaging patterns.
#### Cluster Provisioning

  - **(2023)** [learnk8s.io/kubernetes-terraform: Creating Kubernetes clusters with Terraform](https://learnkube.com/kubernetes-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed LearnK8s tutorial demonstrating cloud cluster provisioning with Terraform. Focuses on orchestrating clean IAM hierarchies, underlying storage provisions, network definitions, and secure worker node groups.
  - **(2023)** [thenewstack.io: A Better Way to Provision Kubernetes Using Terraform](https://thenewstack.io/a-better-way-to-provision-kubernetes-using-terraform) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Proposes decoupling patterns that separate underlying Kubernetes structural provisioning from inner-cluster configurations. Recommends utilizing GitOps agents (like ArgoCD or Flux) once the cluster plane is initialized by Terraform to handle target container manifests.
  - **(2022)** [releasehub.com: Terraform Kubernetes Deployment: A Detailed Walkthrough](https://release.com/blog/terraform-kubernetes-deployment-a-detailed-walkthrough) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed walk-through demonstrating the creation and bootstrap process of managed cloud container environments, illustrating resource sequencing requirements and control loop structures.
#### Cost Management

  - **(2022)** [hodovi.cc: Creating a Low Cost Managed Kubernetes Cluster for Personal Development using Terraform](https://hodovi.cc/blog/creating-low-cost-managed-kubernetes-cluster-personal-development-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide detailing how to build a highly cost-effective managed Kubernetes environment for engineering sandbox testing. Emphasizes small node configurations, pool autoscaling, and minimal state profiles to reduce infrastructure costs.
#### Federated Architectures

  - **(2024)** [learn.hashicorp.com: Deploy Federated Multi-Cloud Kubernetes Clusters](https://developer.hashicorp.com/terraform/tutorials/networking/multicloud-kubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official HashiCorp tutorial illustrating how to configure and deploy federated Kubernetes clusters across multi-cloud environments. Leverages Consul Service Mesh alongside Terraform for secure cross-network discovery and communication routing.
#### Kubernetes Operators

  - **(2025)** [hashicorp/terraform-k8s: Terraform Cloud Operator for Kubernetes](https://github.com/hashicorp/terraform-k8s) <span class='md-tag md-tag--info'>⭐ 449</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-da8d2cfe" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 12 L 20 13 L 30 3 L 40 11 L 50 6" fill="none" stroke="url(#spark-grad-da8d2cfe)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official HashiCorp Terraform Cloud Operator for Kubernetes. Implements a controller pattern inside the cluster, allowing platform teams to manage external cloud resources via Custom Resource Definitions (CRDs) which coordinate plans and applies in Terraform Cloud.
#### Official Integration

  - **(2022)** [architect.io: Get started with the Terraform Kubernetes provider](https://loopholelabs.io) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured introduction to the official Kubernetes provider. Outlines how to define namespaces, secrets, configmaps, and simple microservice deployments using HCL declaratives rather than raw YAML resource files.
  - **(2020)** [kubernetes.io blog: Working with Terraform and Kubernetes](https://kubernetes.io/blog/2020/06/working-with-terraform-and-kubernetes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official Kubernetes blog review describing operational integration patterns using Terraform to configure cloud network spaces alongside bare-metal node sets. Explores deployment hand-offs to local scheduling operators.
## Container Orchestration

### Kubernetes (1)

#### Bare Metal and Cloud Hosting

  - **(2023)** [==terraform-hcloud-dualstack-k8s: Hetzner Dual-Stack Kubernetes Cluster==](https://github.com/tibordp/terraform-hcloud-dualstack-k8s) <span class='md-tag md-tag--info'>⭐ 34</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-20c0afdc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 13 L 20 7 L 30 4 L 40 3 L 50 10" fill="none" stroke="url(#spark-grad-20c0afdc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community-led open-source project automating the deployment of dual-stack (IPv4/IPv6) Kubernetes clusters on Hetzner Cloud. Provides dynamic network routing, instance configuration, and cluster orchestration out of the box.
#### Edge Computing

  - **(2023)** [==K3s Private Cluster 🌟==](https://github.com/inscapist/terraform-k3s-private-cloud) <span class='md-tag md-tag--info'>⭐ 121</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f6b6c247" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 13 L 20 6 L 30 9 L 40 8 L 50 10" fill="none" stroke="url(#spark-grad-f6b6c247)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source code repository outlining how to automate secure, private K3s Kubernetes cluster installations using Terraform scripts. Illustrates resource definitions and networking setups for edge deployments.
## Infrastructure as Code

### AWS (2)

#### Arch Study

  - **(2017)** [The Segment AWS Stack](https://segment.com/blog/the-segment-aws-stack) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Segment's historic architectural deep dive discussing their infrastructure orchestration models over AWS. Captures early evolution of high-volume container deployments prior to widespread EKS standards.
#### Legacy Tooling

  - **(2021)** [**segmentio/stack**](https://github.com/segmentio/stack) <span class='md-tag md-tag--info'>⭐ 2091</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2b2c8331" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 7 L 20 12 L 30 7 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-2b2c8331)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Segment's production-proven infrastructure baseline template codebase for AWS workloads. Standardized on ECS, Auto-scaling, and foundational network controls, but now archived in favor of native Kubernetes/EKS methodologies.
### Ansible

#### Image Provisioning

  - **(2021)** [getbetterdevops.io: Build Docker Images Using Ansible and Packer](https://www.empowersurvivors.net) <span class='md-tag md-tag--warning'>[YAML/HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical blueprint demonstrating how to integrate Ansible playbooks as provisioning engines inside HashiCorp Packer build runs. Outlines processes to construct audited, standardized, and security-hardened Docker images.
### Best Practices

#### Case Studies

  - **(2023)** [blog.coderco.io: Terraform Best Practices Series - Lessons from the Battlefield: Part 1](https://blog.coderco.io/p/terraform-best-practices-series-lessons) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A two-part real-world post-mortem analysis exploring system breakdowns when operating large IaC topologies. Details technical remediation steps for corrupted states, uncoordinated dynamic lock releases, and scaling boundary patterns for high-frequency microservice backbones.
### Curation

#### Cloud Posse Modules

  - **(2025)** [==github.com/cloudposse?q=terraform-==](https://github.com/cloudposse?q=terraform-) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier repository suite of highly modular, enterprise-tested blueprints authored by Cloud Posse. These patterns are widely adopted for orchestrating complex AWS and Kubernetes infrastructure layers using declarative conventions.
### Enterprise Platforms

#### Catalogs and Blueprints

  - **(2023)** [blog.gruntwork.io: Introducing: The Gruntwork Module, Service, and Architecture Catalogs](https://www.gruntwork.io/blog/introducing-the-gruntwork-module-service-and-architecture-catalogs) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The Gruntwork Service Catalog provides structured templates to accelerate developer self-service workflows inside enterprise environments. By decoupling infrastructure blueprints from daily application releases, developers can safely deploy scalable databases or microservices. It balances developer velocity with rigorous platform engineering standards.
### GitOps

#### Push-Based Workflows

  - **(2023)** [**about.gitlab.com: How to use a push-based approach for GitOps with Terraform and AWS ECS and EC2**](https://about.gitlab.com/blog/how-to-agentless-gitops-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Evaluates push-based GitOps strategies using GitLab CI/CD pipelines to manage Terraform states targeted at AWS ECS and EC2. Contrasts agentless runner-driven pushes with pull-based execution models to help architects choose the ideal strategy.
### Kubernetes Integration

#### GitOps and Provisioning

  - **(2023)** [**blog.ogenki.io: Applying GitOps Principles to Infrastructure: An overview of tf-controller**](https://blog.ogenki.io/post/terraform-controller) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Analyzes the capabilities of Weaveworks' "tf-controller", a specialized Kubernetes operator designed to reconcile Terraform configurations following strict GitOps design loops. Details how this eliminates configuration drift by continuously comparing declared Git repository states with actual live environment structures. Live grounding confirms that despite Weaveworks' corporate restructuring, the community remains actively engaged in developing controller-driven reconciliation loops.
  - **(2022)** [**dev.to/kubestack: A Better Way to Provision Kubernetes Resources Using Terraform 🌟**](https://dev.to/kubestack/a-better-way-to-provision-kubernetes-resources-using-terraform-355n) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Highlights the architectural benefits of Kubestack, an open-source framework built on Terraform designed specifically for managing Kubernetes clusters and platform service deployments. Solves the traditional "two-stage apply" problem by separating cluster infrastructure provisioning from operational workload deployment. Live grounding underscores its utility in providing a deterministic GitOps deployment lifecycle for base platform components.
### Kubernetes Provisioning

#### GitOps Frameworks

  - **(2024)** [Kubestack: Terraform GitOps Framework 🌟](https://www.kubestack.com) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubestack is a specialized GitOps framework tailored for managing cloud-managed and bare-metal Kubernetes clusters using Terraform. Featuring a robust multi-tier environment structure, it guarantees absolute parity from local development platforms through to multi-zone production configurations. It helps platform engineers declare and provision compliant Kubernetes footprints.
### Multi-Tooling

#### Azure Integration

  - **(2023)** [devopshubproject/azure-terraform-ansible](https://github.com/devopshubproject/azure-terraform-ansible) <span class='md-tag md-tag--info'>⭐ 3</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c7fd9deb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 10 L 20 4 L 30 13 L 40 12 L 50 3" fill="none" stroke="url(#spark-grad-c7fd9deb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A functional integration project demonstrating hybrid automation on Azure. Illustrates patterns using Terraform to instantiate structural subnets and compute hosts, passing outputs directly into Ansible for fast runtime bootstrapping.
### Serverless Integration

#### Hybrid Automation

  - **(2019)** [**theburningmonk.com: Making Terraform and Serverless framework work together**](https://theburningmonk.com/2019/03/making-terraform-and-serverless-framework-work-together) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A classic, influential case study analyzing the architecture of combining HashiCorp Terraform (for heavy resources like VPCs, databases, IAM) with Serverless Framework (for ephemeral Lambdas). Explores state output handoffs, parameter store structures, and pipeline coordination protocols. Live grounding confirms that while newer tools have merged these functions, this division of labor remains highly performant and stable.
### Terraform

#### AWS Integration

  - **(2023)** [**youtube: How to Deploy an E-Commerce Website to AWS With Terraform || Terraform Hands-on Project | Tech with Helen**](https://www.youtube.com/watch?v=iLgEK6A31HM) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A hands-on, end-to-end architecture video project walking through the deployment of a highly-available, multi-tier e-commerce platform on AWS. Covers setting up application load balancers, auto-scaling groups, database subnets, and security configurations. Live grounding validates that constructing comprehensive environments like this helps engineers master real-world production interdependencies.
## Orchestration

### AKS (1)

#### CI-CD Pipelines

  - **(2022)** [thomasthornton.cloud: Building and deploying to an AKS cluster using Terraform and Azure DevOps with Kubernetes and Helm providers](https://thomasthornton.cloud/building-and-deploying-to-an-aks-cluster-using-terraform-and-azure-devops-with-kubernetes-and-helm-providers) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A tactical guide focused on end-to-end GitOps deployment. Integrates Terraform provisioning of AKS with the Helm and Kubernetes providers within Azure DevOps pipelines to automate application layer deployment.
#### Masterclass

  - **(2023)** [**github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟**](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A highly comprehensive masterclass repository containing declarative HCL files and manifests to deploy AKS with Azure Disks, Azure Files, Application Gateway ingress, and active Azure AD integration.
## Platform Engineering (1)

### AKS (2)

#### Reference Architecture

  - **(2024)** [**github.com/Azure-Samples/aks-platform-engineering Building a Platform Engineering Environment on Azure Kubernetes Service (AKS) 🌟**](https://github.com/Azure-Samples/aks-platform-engineering) <span class='md-tag md-tag--info'>⭐ 155</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4afffad1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 11 L 20 10 L 30 12 L 40 9 L 50 8" fill="none" stroke="url(#spark-grad-4afffad1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The official Microsoft reference architecture for building enterprise platform engineering environments on AKS. Demonstrates internal developer platforms, cluster bootstrapping, policy control, and automated fleet management.
## Security (2)

### Secrets Management

#### GitOps Encrypted Secrets

  - **(2026)** [==sops: Simple and flexible tool for managing secrets 🌟==](https://github.com/getsops/sops) <span class='md-tag md-tag--info'>⭐ 22092</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8b8e42fa" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 8 L 20 6 L 30 3 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-8b8e42fa)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An essential open-source tool for file-level encryption inside configuration management pipelines. SOPS supports partial file encryption for formats like YAML, JSON, and ENV, integrating natively with AWS KMS, GCP KMS, Azure Key Vault, HashiCorp Vault, age, and PGP. It is highly valued in GitOps workflows for its ability to securely commit encrypted configurations.
## Serverless (1)

### AWS (3)

#### IaC

  - **(2024)** [**serverless.tf: Doing serverless with Terraform**](https://serverless.tf) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The serverless.tf project offers structured Terraform blueprints for designing robust, production-ready serverless applications on AWS. By standardizing execution patterns for AWS Lambda, API Gateway, and Step Functions, it eliminates raw boilerplate while preserving native HCL flexibility.
## Serverless Architecture

### AWS Lambda

#### API Gateway

  - **(2024)** [learn.hashicorp.com: y Serverless Applications with AWS Lambda and API Gateway 🌟](https://developer.hashicorp.com/terraform/tutorials/aws/lambda-api-gateway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Standard HashiCorp tutorial teaching developers how to architect, deploy, and configure high-performance serverless endpoints using AWS Lambda and API Gateway, entirely declared via modular HCL files.
#### Infrastructure as Code (1)

  - **(2023)** [==AWS Lambda the Terraform Way==](https://github.com/nsriram/lambda-the-terraform-way) <span class='md-tag md-tag--info'>⭐ 1260</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8a88e588" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 13 L 20 13 L 30 3 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-8a88e588)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A widely starred open-source template repository outlining best practices for packaging, versioning, and deploying AWS Lambda functions natively using Terraform. Eliminates dependencies on external serverless frameworks by leveraging HCL zip archiving capabilities.

---
💡 **Explore Related:** [Securityascode](./securityascode.md) | [Ansible](./ansible.md) | [Devsecops](./devsecops.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

