# Pulumi - Modern Infrastructure as Code

!!! info "Architectural Context"
    Detailed reference for Pulumi - Modern Infrastructure as Code in the context of Hardened Infrastructure.

## Table of Contents

1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud-Native Provisioning](#cloud-native-provisioning)
  - [Serverless Containers](#serverless-containers)
    - [AWS Fargate](#aws-fargate)
1. [Infrastructure as Code](#infrastructure-as-code)
  - [API Integration](#api-integration)
    - [Pulumi](#pulumi)
  - [CICD Integration](#cicd-integration)
    - [Pulumi](#pulumi-1)
  - [Cloud Engineering](#cloud-engineering)
    - [Pulumi](#pulumi-2)
  - [Kubernetes Provisioning](#kubernetes-provisioning)
    - [AKS](#aks)
    - [Civo Cloud](#civo-cloud)
    - [Migration](#migration)
    - [Operators](#operators)
    - [Pulumi](#pulumi-3)
  - [Multi-Cloud](#multi-cloud)
    - [Pulumi Registry](#pulumi-registry)
  - [Multi-Cloud Provisioning](#multi-cloud-provisioning)
    - [Comparisons](#comparisons)
    - [Migration](#migration-1)
    - [Pulumi](#pulumi-4)
  - [Observability](#observability)
    - [Pulumi](#pulumi-5)
  - [Package Management](#package-management)
    - [Pulumi Registry](#pulumi-registry-1)
1. [Kubernetes Developer Experience](#kubernetes-developer-experience)
  - [Graph-Based Dev and Test](#graph-based-dev-and-test)
    - [Garden Documentation](#garden-documentation)

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [DRY (Don’t Repeat Yourself) on the cloud with Pulumi](https://blog.thundra.io/dry-dont-repeat-yourself-on-the-cloud-with-pulumi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering DRY (Don’t Repeat Yourself) on the cloud with Pulumi in the Kubernetes Tools ecosystem.
## Cloud-Native Provisioning

### Serverless Containers

#### AWS Fargate

  - **(2026)** [pulumi.com: Running Containers on ECS Fargate](https://www.pulumi.com/registry/packages/aws/how-to-guides/ecs-fargate) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Architecture guide detailing how to use Pulumi to configure AWS ECS Fargate environments. Covers programmatic configuration of subnets, target groups, auto-scaling thresholds, and secure IAM policies.
## Infrastructure as Code

### API Integration

#### Pulumi

  - **(2021)** [pulumi.com: Announcing the Pulumi REST API](https://www.pulumi.com/blog/pulumi-rest-api) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical briefing on the Pulumi REST API, enabling software engineering organizations to programmatically trigger, query, and govern cloud deployments directly from custom developer platforms.
### CICD Integration

#### Pulumi (1)

  - **(2023)** [build5nines.com: Beginner’s Guide to Pulumi CI/CD Pipelines](https://build5nines.com/beginners-guide-to-pulumi-ci-cd-pipelines) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide outlining automated PR validations, policy-as-code evaluations, and deployment promotions utilizing GitHub Actions and Pulumi CLI integration.
  - **(2021)** [devops.com: Pulumi Moves to Automate Cloud Infrastructure Provisioning](https://devops.com/pulumi-moves-to-automate-cloud-infrastructure-provisioning)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of Pulumi's automated delivery engines, evaluating the platform's features for removing configuration drift and synchronizing cluster models with git-managed repositories.
### Cloud Engineering

#### Pulumi (2)

  - **(2021)** [thenewstack.io: The Next Step after DevOps and GitOps Is Cloud Engineering, Pulumi Says](https://thenewstack.io/the-next-step-after-devops-and-gitops-is-cloud-engineering-pulumi-says)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A foundational examination of the shift from legacy DevOps models to full Cloud Engineering. Highlights how Pulumi bridges application development and infrastructure via standardized code workflows.
### Kubernetes Provisioning

#### AKS

  - **(2022)** [octopus.com: Create an AKS Cluster with Pulumi and Octopus Deploy](https://octopus.com/blog/pulumi-and-aks-with-octopus-deploy) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed enterprise deployment case study highlighting the instantiation of Azure Kubernetes Service (AKS) clusters via Pulumi code coupled with Octopus Deploy continuous release orchestrations.
#### Civo Cloud

  - **(2023)** [civo.com: Manage Kubernetes clusters using the Civo Pulumi provider](https://www.civo.com/learn) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step tutorial for deploying high-performance, lightweight K3s clusters on Civo Cloud utilizing Pulumi’s native Civo API bindings, highlighting modular infrastructure design.
#### Migration

  - **(2026)** [pulumi/kube2pulumi](https://github.com/pulumi/kube2pulumi) <span class='md-tag md-tag--info'>⭐ 107</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-05f6851b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 10 L 20 6 L 30 10 L 40 12 L 50 3" fill="none" stroke="url(#spark-grad-05f6851b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Open-source command-line tool designed to convert static Kubernetes YAML templates or dynamically generated Helm outputs directly into isomorphic, compilable Pulumi configurations.
  - **(2026)** [pulumi.com: From Kubernetes or Helm YAML](https://www.pulumi.com/docs/iac/guides/migration/migrating-to-pulumi/from-kubernetes) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Technical conversion guide outlining methodologies to translate legacy, static Kubernetes YAML definitions or complex Helm charts directly into expressive, compilable Pulumi programs.
#### Operators

  - **(2020)** [thenewstack.io: Pulumi Releases a Kubernetes Operator](https://thenewstack.io/pulumi-releases-a-kubernetes-operator) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product launch overview of the Pulumi Kubernetes Operator, showing how platform engineers can configure GitOps style synchronization between Git repositories and active cloud infrastructure.
#### Pulumi (3)

  - **(2022)** [travis.media: Pulumi Tutorial: Automate Kubernetes Deployments and Operations with this Complete Guide](https://travis.media/blog/pulumi-tutorial-automate-kubernetes-operations) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — End-to-end tutorial detailing the programmatic definition of namespaces, ingress controllers, replicas, and pod affinity rules inside target Kubernetes environments using Pulumi's type-safe bindings.
### Multi-Cloud

#### Pulumi Registry

  - **(2024)** [Pulumi Cloud Providers](https://www.pulumi.com/registry/packages) <span class='md-tag md-tag--warning'>[MULTI-LANGUAGE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The central registry portal hosting official Pulumi cloud infrastructure providers. Enables multi-cloud platform declaration (AWS, Kubernetes, Azure, GCP) using modern programming languages, supporting highly parameterized microservice deployments.
### Multi-Cloud Provisioning

#### Comparisons

  - **(2026)** [Pulumi VS Terraform](https://www.pulumi.com/docs/iac/comparisons/terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A granular comparison detailing architectural differences between Pulumi's language-native, dynamic resource instantiation model and Terraform's static, declarative HCL configurations.
  - **(2022)** [packetswitch.co.uk: Terraform is Good, but I Like Pulumi](https://www.packetswitch.co.uk/terraform-is-good-but-i-like-pulumi)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A platform practitioner's case study demonstrating the developer experience advantages of using Pulumi over Terraform, specifically praising testability and modular software abstractions.
  - **(2021)** [pulumi.com: From Terraform to Infrastructure as Software](https://www.pulumi.com/blog/from-terraform-to-infrastructure-as-software) <span class='md-tag md-tag--warning'>[POLYGLOT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A thought leadership piece arguing for the transition from static declarative configuration syntax (HCL) to real-time compilable Infrastructure as Software (IAS) via Pulumi.
#### Migration (1)

  - **(2026)** [pulumi.com: Convert Your Terraform to Pulumi](https://www.pulumi.com/tf2pulumi) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Comprehensive architectural guide to using the `tf2pulumi` engine, explaining key syntax translations, dependency resolutions, and model differences when modernizing from legacy HCL files.
#### Pulumi (4)

  - **(2026)** [Pulumi](https://www.pulumi.com) <span class='md-tag md-tag--warning'>[POLYGLOT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pulumi is an industry-leading infrastructure-as-code platform enabling multi-cloud resource provisioning through standard programming languages. It provides rich testing utilities, compiler-driven schema safety, and scalable cloud state backends.
  - **(2021)** [pulumi.com: Announcing Pulumi 3.0](https://www.pulumi.com/blog/pulumi-3-0) <span class='md-tag md-tag--warning'>[POLYGLOT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Launch review of Pulumi 3.0, introducing compiled packages across languages, automated code converters, and optimized state management layers to accelerate platform engineering.
### Observability

#### Pulumi (5)

  - **(2022)** [pulumi.com: Observability with Infrastructure as Code](https://www.pulumi.com/blog/observability-with-infrastructure-as-code) <span class='md-tag md-tag--warning'>[POLYGLOT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural guide explaining how to integrate observability tooling, health checks, and tracing sidecars dynamically during the code-driven resource compilation phase inside Pulumi pipelines.
### Package Management

#### Pulumi Registry (1)

  - **(2021)** [siliconangle.com: Pulumi’s new registry aims to ease sharing and reusing cloud infrastructure building blocks](https://siliconangle.com/2021/10/18/pulumis-new-registry-makes-easy-share-reuse-cloud-infrastructure-building-blocks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed insight into the launch of the Pulumi Registry, a public marketplace supporting modular package sharing and reusability of multi-cloud components across diverse language boundaries.
## Kubernetes Developer Experience

### Graph-Based Dev and Test

#### Garden Documentation

  - **(2021)** [garden.io: cloud native devops platform](https://docs.garden.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural specifications for the Garden orchestration tool. Details graph configurations, Helm-based packaging models, pipeline test automation patterns, and enterprise testing setups inside remote clusters.

---
💡 **Explore Related:** [IaC](./iac.md) | [Terraform](./terraform.md) | [Oauth](./oauth.md)

