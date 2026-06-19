# Software Delivery Pipeline. CI/CD

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/cicd/).

!!! info "Architectural Context"
    Detailed reference for Software Delivery Pipeline. CI/CD in the context of Engineering Pipeline.

## Table of Contents

1. [Cloud Engineering](#cloud-engineering)
  - [AWS](#aws)
    - [Automated Deployment](#automated-deployment)
  - [CI-CD Pipelines](#ci-cd-pipelines)
    - [Architecture](#architecture)
  - [Cloud Native](#cloud-native)
    - [CI-CD Pipelines](#ci-cd-pipelines-1)
  - [Hybrid Cloud](#hybrid-cloud)
    - [Case Studies](#case-studies)
  - [Kubernetes](#kubernetes)
    - [Best Practices](#best-practices)
    - [CI-CD Pipelines](#ci-cd-pipelines-2)
    - [Cloud Native](#cloud-native-1)
1. [Continuous Delivery](#continuous-delivery)
  - [CICD and Testing](#cicd-and-testing)
    - [Pipeline as Code](#pipeline-as-code)
  - [CICD Best Practices](#cicd-best-practices)
    - [Overview](#overview)
  - [Deployment Strategies](#deployment-strategies)
    - [Blue-Green and Canary](#blue-green-and-canary)
1. [Deployment and Delivery](#deployment-and-delivery)
  - [CICD and Delivery](#cicd-and-delivery)
    - [AWS Architecture](#aws-architecture)
    - [Kubernetes Native](#kubernetes-native)
    - [Pipeline Architecture](#pipeline-architecture)
    - [Resource Portals](#resource-portals)
  - [Deployment Strategies](#deployment-strategies-1)
    - [Blue-Green and Canary](#blue-green-and-canary-1)
    - [Education](#education)
  - [GitOps](#gitops)
    - [Red Hat OpenShift](#red-hat-openshift)
  - [Platform Engineering](#platform-engineering)
    - [Kubernetes Management](#kubernetes-management)
  - [Progressive Delivery](#progressive-delivery)
    - [Feature Flags](#feature-flags)
1. [DevOps](#devops)
  - [CI-CD Pipelines](#ci-cd-pipelines-3)
    - [Best Practices](#best-practices-1)
    - [Case Studies](#case-studies-1)
  - [Continuous Delivery](#continuous-delivery-1)
    - [Patterns](#patterns)
  - [Financial Services](#financial-services)
    - [Best Practices](#best-practices-2)
1. [Infrastructure as Code](#infrastructure-as-code)
  - [CICD and Delivery](#cicd-and-delivery-1)
    - [Security and Compliance](#security-and-compliance)
  - [GitOps](#gitops-1)
    - [Configuration Management](#configuration-management)

## Cloud Engineering

### AWS

#### Automated Deployment

  - **(2020)** [aws.amazon.com: Automating safe, hands-off deployments 🌟🌟](https://aws.amazon.com/es/builders-library/automating-safe-hands-off-deployments) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly technical AWS Builders Library analysis detailing Amazon's safe, automated deployment methodologies. Highlights pipeline design using fractional wave rollouts, automated synthetic testing, and automated rollbacks triggered by alarm thresholds.
### CI-CD Pipelines

#### Architecture

  - **(2022)** [thenewstack.io: Are Monolith CI/CD Pipelines Killing Quality in Your Software?](https://thenewstack.io/are-monolith-ci-cd-pipelines-killing-quality-in-your-software)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyses the risks of monolithic pipelines on deployment safety. Recommends aligning decoupled micro-pipelines with distinct microservice models to avoid pipeline dependency bottlenecks.
### Cloud Native

#### CI-CD Pipelines (1)

  - **(2022)** [jfrog.com: Cloud Native CI/CD: The Ultimate Checklist](https://jfrog.com/blog/cloud-native-ci-cd-the-ultimate-checklist)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents an essential checklist for establishing cloud-native CI/CD systems. Highlights immutable container registry processes, in-cluster execution mechanics, and automated shift-left security evaluations.
### Hybrid Cloud

#### Case Studies

  - **(2022)** [jfrog.com: How to Accelerate Software Delivery with Hybrid Cloud CI/CD (e-commerce) 🌟](https://jfrog.com/blog/how-to-accelerate-software-delivery-with-hybrid-cloud-ci-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural blueprint analyzing hybrid-cloud continuous delivery pipeline setups for e-commerce contexts. Discusses the coordination of on-premises assets with public cloud target clusters under strict compliance constraints.
### Kubernetes

#### Best Practices

  - **(2023)** [spacelift.io: Kubernetes CI/CD Pipelines – 7 Best Practices and Tools | James Walker 🌟](https://spacelift.io/blog/kubernetes-ci-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Covers seven best practices for running production-grade Kubernetes CI/CD pipelines. Evaluates declarative branch states, secure RBAC configurations, health check integrations, and automatic drift detection.
#### CI-CD Pipelines (2)

  - **(2023)** [thenewstack.io: Kubernetes CI/CD Pipelines Explained](https://thenewstack.io/kubernetes-ci-cd-pipelines-explained)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into Kubernetes delivery designs, analyzing how declarative resources and continuous reconcilers differ from classical build steps. Evaluates the use of Helm charts and GitOps loops.
#### Cloud Native (1)

  - **(2023)** [groundcover.com: Cloud-native CI/CD? Yeah, that’s a thing 🌟](https://www.groundcover.com/blog/ci-cd-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the shift to Kubernetes-native continuous delivery models. Compares Tekton and declarative GitOps runtimes like Argo CD and Flux to highlight the safety benefits of in-cluster loops.
## Continuous Delivery

### CICD and Testing

#### Pipeline as Code

  - **(2022)** [testguild.com: Pipeline as Code with Mohamed Labouardy](https://testguild.com/podcast/a345-mohamed) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Podcast episode reviewing the strategic transition to declarative configuration pipelines (Pipeline as Code). Emphasizes integration of automated compliance scanning, container vulnerability reports, and regression testing suites.
### CICD Best Practices

#### Overview

  - **(2023)** [**about.gitlab.com: How to keep up with CI/CD best practices**](https://about.gitlab.com/blog/how-to-keep-up-with-ci-cd-best-practices) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Synthesis of modern continuous integration frameworks, emphasizing pipeline standardization, artifact isolation, and fast feedback loops. Discusses optimization of runner resource footprints and build steps parallelization.
### Deployment Strategies

#### Blue-Green and Canary

  - **(2024)** [==harness.io: Intro to Deployment Strategies: Blue-Green, Canary, and More 🌟==](https://www.harness.io/blog/blue-green-canary-deployment-strategies) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Highly detailed structural evaluation of Kubernetes deployment paradigms. Contrasts blue-green switches, canary rollouts, and rolling deployments based on system overhead, traffic redirection latency, and blast-radius containment.
## Deployment and Delivery

### CICD and Delivery

#### AWS Architecture

  - **(2024)** [trek10.com: Enterprise CI/CD on AWS: a pragmatic approach](https://caylent.com/blog/pragmatic-enterprise-cicd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Pragmatic enterprise architecture paradigms for deploying resilient pipelines on AWS. Focuses on orchestrating CodePipeline, ECS, and EKS under high compliance boundaries, robust IAM roles, and centralized security.
#### Kubernetes Native

  - **(2024)** [harness.io: Kubernetes CI/CD Best Practices](https://www.harness.io/blog/kubernetes-ci-cd-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A professional guide detailing best practices for Kubernetes-native CI/CD. Emphasizes image tag immutability, secure namespace configuration, automated GitOps pull routines, secrets orchestration, and strict readiness validations.
  - **(2023)** [blog.sonatype.com: Achieving CI and CD With Kubernetes 🌟](https://www.sonatype.com/blog/achieving-ci/cd-with-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the fundamental technological shift of containerized compilation systems running directly inside Kubernetes. Details dynamic testing namespaces, secure builds, and GitOps engines to achieve high-frequency delivery cycles.
  - **(2023)** [thenewstack.io: 7 features that make kubernetes ideal for CI/CD](https://thenewstack.io/7-features-that-make-kubernetes-ideal-for-ci-cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of Kubernetes-native features that naturally enhance modern CI/CD architectures. Focuses on APIs, declarative container orchestrations, automatic scalability, microservice security partitioning, and resilient health checks.
  - **(2023)** [thenewstack.io: CI/CD with kubernetes 🌟](https://thenewstack.io/ebooks/kubernetes/ci-cd-with-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extensive technical eBook detailing the evolution of CI/CD systems towards native Kubernetes integrations. Covers GitOps patterns, isolated build containers, pipeline security principles, and multi-tenant resource controls.
#### Pipeline Architecture

  - **(2024)** [harness.io: Pipeline Patterns for CI/CD Pipelines 🌟](https://www.harness.io/blog/deployment-pipeline-patterns) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A systematic catalogue mapping out complex deployment pipeline topologies. Covers fail-fast designs, parallel execution structures, multi-environment progression, and automated artifact immutability to elevate overall platform engineering.
#### Resource Portals

  - **(2025)** [Awesome CI/CD 🌟](https://github.com/cicdops/awesome-ciandcd) <span class='md-tag md-tag--info'>⭐ 1999</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ccee7300" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 9 L 20 4 L 30 6 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-ccee7300)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extensive curated list capturing modern DevOps platforms, delivery engines, automated linting, security scanning, and container validation tools, acting as a foundational technical index for engineering teams.
### Deployment Strategies (1)

#### Blue-Green and Canary (1)

  - **(2023)** [blog.container-solutions.com: Deployment Strategies 🌟](https://blog.container-solutions.com/deployment-strategies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — In-depth guide comparing core deployment topologies: recreate, rolling update, blue/green, canary, and shadow. Focuses on the trade-offs of budget, state management, infrastructure replication overhead, and traffic routing mechanisms.
  - **(2023)** [opsmx.com: What is Blue Green Deployment ?](https://www.opsmx.com/blog/blue-green-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory primer defining the operational mechanics of blue-green architectures. Focuses on setting up mirrored hosting environments, routing configurations, and robust database rollback plans.
#### Education

  - **(2024)** [youtube: Kubernetes Deployment Strategies | DevOps FAQ | DevOps DevOps Interview Q&A](https://www.youtube.com/watch?v=aU-EtdEOdlM)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Educational presentation covering the standard deployment patterns in Kubernetes (Recreate, Rolling Update, Canary, Shadow). Tailored for DevOps engineers seeking solid conceptual preparation and technical interview readiness.
### GitOps

#### Red Hat OpenShift

  - **(2023)** [developers.redhat.com: The present and future of CI/CD with GitOps on Red Hat OpenShift 🌟](https://developers.redhat.com/blog/2020/09/03/the-present-and-future-of-ci-cd-with-gitops-on-red-hat-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on Red Hat OpenShift's alignment with GitOps and Pipelines frameworks (Argo CD and Tekton). Highlights architectural benefits of multi-cluster visual state synchronizations and declarative deployment pipelines.
### Platform Engineering

#### Kubernetes Management

  - **(2025)** [Devtron Labs: Devtron provides a 'seamless,’ 'implementation agnostic uniform interface' across Kubernetes Life Cycle integrated with most Opensource and commercial tools](https://devtron.ai) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source, tool-agnostic application management platform for Kubernetes. Unifies discrete CI/CD workflows, GitOps, observability tooling, and cluster resource debugging into a single visual interface, drastically lowering cognitive load.
### Progressive Delivery

#### Feature Flags

  - **(2025)** [split.io: Progressive Delivery](https://www.harness.io/harness-devops-academy/progressive-delivery) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Foundational architectural overview of progressive delivery principles. Explains decoupling deployments from business releases using smart canary gates, dynamic feature flags, and real-time monitoring of impact metrics.
## DevOps

### CI-CD Pipelines (3)

#### Best Practices (1)

  - **(2021)** [CI/CD Best Practices 🌟](https://blog.bitsrc.io/ci-cd-best-practices-bca0ef665677) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details essential strategies for optimizing continuous integration speed and reliability. Evaluates modular pipelines, build caching systems, parallelized test execution, and shift-left automated scanning.
#### Case Studies (1)

  - **(2018)** [tech.buzzfeed.com: Continuous Deployments at BuzzFeed](https://tech.buzzfeed.com/continuous-deployments-at-buzzfeed-d171f76c1ac4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural case study detailing BuzzFeed's transition to continuous deployment. Analyzes how their internal tooling structures automated container packaging and microservices management to optimize high-frequency shipping.
### Continuous Delivery (1)

#### Patterns

  - **(2020)** [continuousdelivery.com: Patterns 🌟](https://continuousdelivery.com/implementing/patterns) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A seminal reference of continuous delivery patterns. Evaluates technical blueprints for automated schema updates, blue-green environments, canary verification loops, and clean decoupling of software builds from configurations.
### Financial Services

#### Best Practices (2)

  - **(2023)** [clickittech.com: CI/CD Best Practices: Top 10 Practices for Financial Services](https://www.clickittech.com/devops/ci-cd-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines specialized continuous delivery configurations designed for high-regulation financial environments. Covers security orchestration, strict separation of duties, and audit trail automation.
## Infrastructure as Code

### CICD and Delivery (1)

#### Security and Compliance

  - **(2023)** [devops.com: 8 Security Considerations for CI/CD](https://devops.com/8-security-considerations-for-ci-cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Actionable checklist of eight vital security considerations for pipeline configurations. Addresses fundamental practices such as secure secrets injection, runner environment isolation, least-privilege RBAC, and validation processes to prevent supply-chain vulnerabilities.
### GitOps (1)

#### Configuration Management

  - **(2024)** [CI Checks Are Not Enough: Combat Configuration Drift in Kubernetes Resources](https://thenewstack.io/ci-checks-are-not-enough-combat-configuration-drift-in-kubernetes-resources) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dive analysis demonstrating why standard static CI checks are insufficient for modern cloud environments. Advocates for real-time drift detection and continuous reconciliation loops in Kubernetes to ensure active infrastructure aligns directly with repository manifests.

---
💡 **Explore Related:** [Jenkins](./jenkins.md) | [Tekton](./tekton.md) | [Argo](./argo.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

