# Argo Declarative GitOps for Kubernetes

!!! info "Architectural Context"
    Detailed reference for Argo Declarative GitOps for Kubernetes in the context of Engineering Pipeline.

## Cloud Native

### Community

#### Events

##### ArgoCon

  - **(2026)** [ArgoCon North America 2026 Call for Proposals](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/co-located-events/argocon/#call-for-proposals)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Call for Proposals portal for ArgoCon North America 2026. Focuses on collecting real-world architectures, case studies, and enterprise patterns utilizing Argo CD, Argo Workflows, Argo Rollouts, and Argo Events.
### Orchestration

#### Argo Workflows

##### Reliability

  - **(2023)** [blog.argoproj.io: Architecting Workflows For Reliability](https://blog.argoproj.io/architecting-workflows-for-reliability-d33bd720c6cc) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines reliable architectural patterns for running large-scale Argo Workflows. Covers retry policies, rate-limiting configurations, and workflow controller adjustments necessary to safely sustain highly concurrent executions without experiencing system degradation.
##### Security

  - **(2023)** [blog.argoproj.io: Practical Argo Workflows Hardening 🌟](https://blog.argoproj.io/practical-argo-workflows-hardening-dd8429acc1ce) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide to security hardening for Argo Workflows deployments in enterprise environments. Focuses on minimizing RBAC permissions, configuring network policies, securing the workflow controller, and utilizing read-only file systems to mitigate risks of privilege escalation and container breakouts.
##### Templates

  - **(2023)** [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes the semantic differences and runtime boundaries between the three distinct definitions of 'template' in Argo Workflows. Distinguishes template definitions, invocations, and inline declarations within a workflow manifest, preventing common YAML structure misconfigurations in complex pipelines.
## GitOps and CD

### Argo Project Ecosystem

  - **(2021)** [**devops.com: The Argo Project: Making GitOps Practical**](https://devops.com/the-argo-project-making-gitops-practical) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Investigates the rapid industry adoption of the Argo ecosystem (Argo CD, Workflows, Rollouts, Events). Explains how the projects solve operational gaps in native Kubernetes, making declarative continuous delivery robust and enterprise-ready.
### Argo Rollouts

#### Blue-Green Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through setting up a complete Blue-Green deployment workflow with Argo Rollouts. Outlines routing controls, active/preview service handoffs, and visual UI verification configurations.
#### Canary Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Offers a practical exploration of canary rollouts configured via Argo Rollouts. Focuses on setting step-based traffic splitting, managing dynamic service mesh weights (SMI, Linkerd, Istio), and defining automated rollbacks based on analysis metrics.
#### Configuration Management

  - **(2022)** [**codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts**](https://octopus.com/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Solves the tricky challenge of managing and rolling out application configuration updates dynamically. Demonstrates how to trigger controlled, safe progressive delivery cycles for applications when only ConfigMaps or Secrets are modified.
#### Progressive Delivery

  - **(2023)** [==argoproj.github.io: Argo Rollouts - Kubernetes Progressive Delivery Controller==](https://argoproj.github.io/argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces the core concepts of Argo Rollouts, which replaces standard Kubernetes Deployment objects with custom Rollout resources. Enables automatic analysis, metrics integration (Prometheus, Datadog), and automated rollback strategies.
### Argo Workflows (1)

#### Release News

  - **(2022)** [**blog.argoproj.io: What’s new in Argo Workflows v3.3**](https://blog.argoproj.io/whats-new-in-argo-workflows-v3-3-dd051d2f1c7) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Highlights the key feature additions, execution optimizations, and performance enhancements introduced in Argo Workflows version 3.3. Discusses UI/UX developments, DAG scaling capabilities, and robust security upgrades.
### ArgoCD

#### ApplicationSets

  - **(2023)** [==argoproj-labs/applicationset: Argo CD ApplicationSet Controller==](https://github.com/argoproj/applicationset) <span class='md-tag md-tag--info'>⭐ 582</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The standard orchestrator extending Argo CD to support multi-cluster application distribution templates. Processes multi-source configurations, automates environment scaling, and drastically reduces the maintenance overhead of managing distinct Application manifests.
  - **(2024)** [**developers.redhat.com: Enhance Kubernetes deployment efficiency with Argo CD and ApplicationSet**](https://developers.redhat.com/articles/2024/06/06/enhance-kubernetes-deployment-efficiency-argo-cd-and-applicationset) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Deep technical review of optimization practices when deploying large-scale software footprints using ApplicationSets. Outlines how to maximize rendering efficiency, prevent performance bottlenecks, and design clean matrix-based generators.
#### Authentication and SSO

##### GitHub Integration

  - **(2021)** [cloud.redhat.com: How to Use ArgoCD Deployments with GitHub Tokens](https://www.redhat.com/en/blog/how-to-use-argocd-deployments-with-github-tokens) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains how to securely integrate ArgoCD with private GitHub repositories using Personal Access Tokens (PATs) and fine-grained permissions. Addresses secure secret management inside Kubernetes to safeguard credentials used during the repository fetching phase.
#### Best Practices

  - **(2022)** [**datree.io: ArgoCD Best Practices You Should Know**](https://www.datree.io/resources/argocd-best-practices-you-should-know) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Expands on essential ArgoCD best practices, emphasizing the isolation of Git repositories for source code and Kubernetes manifests, configuring auto-prune, and defining declarative sync policies to maintain platform stability.
#### Bootstrap Automation

##### Autopilot

  - **(2023)** [==argoproj-labs/argocd-autopilot: Argo-CD Autopilot==](https://github.com/argoproj-labs/argocd-autopilot) <span class='md-tag md-tag--info'>⭐ 1121</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An official Argo project opinionated tool designed to structure, install, and update Argo CD setups automatically. Uses a clean directory structure separating infrastructure from application manifests, enabling rapid multi-project bootstrap with version tracking and disaster recovery features.
#### Concepts and Practices

  - **(2022)** [**thenewstack.io: Applied GitOps with ArgoCD**](https://thenewstack.io/applied-gitops-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A comprehensive examination of GitOps workflows operationalized via ArgoCD. Highlights key practices such as declarative environment definition, pull-based synchronization, and automated drift detection to maintain cluster state parity.
  - **(2022)** [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the architectural superiority of ArgoCD as a pull-based GitOps operator. Focuses on its continuous reconciliation loop, granular cluster state visualization, and out-of-the-box self-healing capabilities that minimize human intervention.
  - **(2021)** [blog.risingstack.com: Argo CD Kubernetes Tutorial](https://blog.risingstack.com/argo-cd-kubernetes-tutorial) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A structured starter guide covering ArgoCD installation, repository connection, and application deployment. Outlines core synchronization paradigms and provides a practical walkthrough of transitioning standard manifests to GitOps.
  - **(2021)** [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Describes the conceptual pillars of GitOps and details how ArgoCD implements them on Kubernetes. Explains key mechanisms such as out-of-sync alert signaling, dry-run synchronization, and visual drift visualization.
#### Introduction

  - **(2022)** [kubebyexample.com: Argo CD Overview 🌟](https://kubebyexample.com/learning-paths/argo-cd/argo-cd-overview) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational educational overview of the ArgoCD engine, architecture, and UI dashboard. Introduces the concepts of Target State versus Live State, and details the controller-to-API communication model.
#### Multi-Cluster

##### ApplicationSets (1)

  - **(2022)** [**openshift.com: Getting Started with ApplicationSets**](https://www.redhat.com/en/blog/getting-started-with-applicationsets) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep dive into the ArgoCD ApplicationSet controller, explaining how to model and automate multi-cluster and multi-tenant application deployments. Covers generators like List, Directory, and Git to scale configurations with minimal templating boilerplate.
  - **(2022)** [**piotrminkowski.com: Manage Multiple Kubernetes Clusters with ArgoCD 🌟**](https://piotrminkowski.com/2022/12/09/manage-multiple-kubernetes-clusters-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step architectural guide on configuring a centralized ArgoCD instance to manage resources across several remote Kubernetes clusters. Covers network endpoints, remote credentials provisioning, and configuration drift auditing.
#### Patterns

##### App-of-Apps

  - **(2021)** [**opensource.com: Automatically create multiple applications in Argo CD**](https://opensource.com/article/21/7/automating-argo-cd) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates how to leverage the 'App-of-Apps' pattern in ArgoCD to construct recursive, nested application structures. Enables engineers to automate the bootstrapping of complex multi-tier platforms from a single root configuration.
#### Plugins and Extensions

  - **(2023)** [**github.com/crumbhole/argocd-lovely-plugin: argocd-lovely-plugin**](https://github.com/crumbhole/argocd-lovely-plugin) <span class='md-tag md-tag--info'>⭐ 486</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A flexible Custom Config Management Plugin (CMP) for Argo CD designed to combine Helm, Kustomize, and raw YAML. It solves the nested tooling dilemma by processing multiple template layers without requiring complex shell scripts, simplifying enterprise GitOps chains.
#### Synchronization Strategies

  - **(2022)** [**blog.argoproj.io: New sync and diff strategies in ArgoCD**](https://blog.argoproj.io/new-sync-and-diff-strategies-in-argocd-44195d3f8b8c) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explores performance optimizations and enhanced reconciliation engines introduced in ArgoCD. Details advanced diff options, custom synchronization hooks, and resource tracking methods that streamline deployment workflows in large-scale environments.
#### Tutorials

  - **(2022)** [digitalocean.com: How to Deploy to Kubernetes using Argo CD and GitOps](https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical implementation guide showcasing the deployment of containerized workloads onto DigitalOcean Kubernetes (DOKS) using ArgoCD. Establishes a complete declarative delivery pipeline driven by version-controlled manifests.
#### Workload Management

##### Demos

  - **(2023)** [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive demo repository showcasing real-world GitOps workload configurations. Provides a structural blueprint for multi-tenant environments, detailing how to cleanly decouple cluster-wide infrastructure configurations from individual application manifests.
### CICD Integration

  - **(2023)** [dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores architectural models for bridging continuous integration (CI) platforms with GitOps-driven deployment mechanisms. Emphasizes clean decoupling where CI updates target config states while Kubernetes reconcile loops execute the rollout.
### Tool Comparison

#### ArgoCD vs FluxCD

  - **(2022)** [**thenewstack.io: GitOps on Kubernetes: Deciding Between Argo CD and Flux**](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Evaluates the architectural differences, strengths, and trade-offs of the two dominant GitOps controllers: ArgoCD and FluxCD. Compares ArgoCD's powerful web UI and multi-tenancy model against Flux's lightweight, decentralized, and Kubernetes-native approach.
## Kubernetes GitOps and Packaging

### Argo Project Ecosystem (1)

#### Event-Driven Automation

  - **(2026)** [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The standard event-driven orchestration engine for Kubernetes. Argo Events integrates with sources like webhooks, S3, or pub-sub, dynamically executing serverless triggers, custom scripts, and Argo Workflows with native scalability.
#### GitOps Strategy

  - **(2026)** [argoproj.github.io: Argo CD - Declarative GitOps for Kubernetes](https://argoproj.github.io/argo-cd) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The absolute industry standard for GitOps-based continuous delivery on Kubernetes. Argo CD synchronizes active cluster states with declarative configurations stored in git repositories, providing robust drift correction, visual dashboarding, and audit controls.
  - **(2022)** [Why and when do you need Argo CD?](https://mkdev.me/posts/why-and-when-do-you-need-argo-cd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An executive guide explaining the core capabilities of GitOps and the necessity of declarative pull engines like Argo CD. It details drift management, configuration alignment, and security advantages compared to manual push deployments.
#### UI Visualization

  - **(2024)** [==feat(ui): Add AppSet to Application Resource Tree in Argo CD==](https://github.com/argoproj/argo-cd/pull/26601) <span class='md-tag md-tag--info'>⭐ 23128</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Argo CD feature enhancement that maps ApplicationSets directly inside the dashboard UI tree. This view simplifies managing multi-tenant topologies and nested application definitions for platform operators.
#### Video Guides

  - **(2022)** [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory video guide showing how to configure and run continuous deployment pipelines using Argo CD and Kubernetes. It walks through initial repository setups, synchronization configurations, and basic troubleshooting procedures.
## Platform Engineering

### ArgoCD (1)

#### Internal Developer Platforms

  - **(2023)** [**itnext.io: Build a Lightweight Internal Developer Platform with Argo CD and Kubernetes Labels**](https://itnext.io/build-a-lightweight-internal-developer-platform-with-argo-cd-and-kubernetes-labels-4c0e52c6c0f4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Demonstrates how to design a lightweight, self-service Internal Developer Platform (IDP) by leveraging Kubernetes metadata labels, admission webhooks, and ArgoCD's API to dynamically generate applications.
#### Security and Compliance

##### RBAC

  - **(2021)** [itnext.io: ArgoCD: users, access, and RBAC](https://itnext.io/argocd-users-access-and-rbac-ddf9f8b51bad) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details the configuration of user management, local accounts, and role-based access control (RBAC) in ArgoCD. Guides platform engineers through restricting access to specific applications, projects, or clusters using fine-grained policies.
### CICD Migration

#### Argo Workflows (2)

##### Jenkins

  - **(2022)** [**Migrating CI/CD from Jenkins to Argo Workflows**](https://dev.to/intuitdev/migrating-cicd-from-jenkins-to-argo-1km4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Shares practical lessons from migrating a legacy Jenkins CI pipeline stack over to container-native Argo Workflows. Compares the performance, cost efficiency, resource overhead, and maintainability of step-based DAG flows.
### GitOps

#### AWS EKS

##### Tekton

  - **(2022)** [==aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS==](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Discusses designing an end-to-end, Kubernetes-native CI/CD pipeline on AWS EKS. Uses Tekton for building and containerizing microservices, seamlessly handing off the deployment phase to ArgoCD for pull-based application delivery.
#### ArgoCD (2)

##### Architecture Topologies

  - **(2022)** [==akuity.io: How many do you need? - Argo CD Architectures Explained==](https://akuity.io/blog/argo-cd-architectures-explained) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Evaluates different topology designs for ArgoCD deployments in large organizations. Details the trade-offs between a single centralized Hub-and-Spoke cluster controller versus multiple decentralized Argo instances scattered across target clusters.
##### Terraform Integration

  - **(2022)** [seraf.dev: ArgoCD Tutorial — (with Terraform)](https://seraf.dev/argocd-tutorial-with-terraform-af77ddea2e6e) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers on bootstrapping an entire ArgoCD installation, including repositories, projects, and application instances, declaratively via the official HashiCorp Terraform provider for ArgoCD.
#### Authentication and SSO (1)

##### OpenShift

  - **(2022)** [**openshift.com: OpenShift Authentication Integration with ArgoCD**](https://www.redhat.com/en/blog/openshift-authentication-integration-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the integration of OpenShift's native OAuth server with ArgoCD. Explains how to map OpenShift user groups to ArgoCD RBAC roles, establishing a secure, unified single sign-on (SSO) experience for enterprise platforms.
#### GitHub Actions

##### AWS EKS (1)

  - **(2023)** [**dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques**](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed configuration recipe detailing how to orchestrate deployments to AWS EKS using GitHub Actions as the CI pipeline and ArgoCD as the GitOps agent. Includes IAM role assumptions, token handling, and multi-environment promotions.
#### Kubernetes Operators

##### CRD Lifecycle

  - **(2023)** [**piotrminkowski.com: Manage Kubernetes Operators with ArgoCD**](https://piotrminkowski.com/2023/05/05/manage-kubernetes-operators-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Addresses challenges and patterns for deploying Kubernetes Operators (e.g., Prometheus Operator, Cert-Manager) via ArgoCD. Analyzes solutions for Custom Resource Definition (CRD) lifecycle management during upgrades and synchronization.
#### Multi-Tenancy

##### Security and Compliance (1)

  - **(2021)** [==blog.argoproj.io: Best Practices for Multi-tenancy in Argo CD==](https://blog.argoproj.io/best-practices-for-multi-tenancy-in-argo-cd-273e25a047b0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Outlines critical architectural patterns for implementing multi-tenancy in ArgoCD. Covers AppProjects boundaries, target namespace isolation, network policies, and cluster-wide RBAC to ensure secure sharing of GitOps infrastructure.
#### Terraform Integration (1)

##### Data Infrastructure

  - **(2022)** [**piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟**](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical demonstration of deploying and managing a Kafka cluster on Kubernetes using a hybrid Terraform and ArgoCD approach. Discusses how to configure infrastructure dependencies with Terraform and declare workload states inside GitOps.
### Infrastructure as Code

#### Modular Architecture

  - **(2022)** [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Proposes a blueprint for building modular, maintainable DevOps platforms. Focuses on orchestrating infrastructure provisioners, secret engines, and GitOps engines under unified declarative frameworks to minimize vendor lock-in.
#### Terraform and AWS

##### EKS Modules

  - **(2023)** [**AWS EKS Argo CD Terraform Component**](https://github.com/cloudposse-terraform-components/aws-eks-argocd) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Enterprise-ready Terraform submodule designed to deploy, configure, and bootstrap Argo CD onto an existing AWS EKS cluster. Standardizes complex security configurations, integrates with IAM Roles for Service Accounts (IRSA), and provisions preconfigured Helm releases.
### Progressive Delivery (1)

#### DNS Routing

##### Blue-Green Deployment (1)

  - **(2022)** [**infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟**](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines advanced architectural design patterns using DNS-based routing to switch traffic for Blue-Green deployments. Discusses how to coordinate external load balancers and global DNS systems during the migration window.
### Secret Management

#### HashiCorp Vault

##### ArgoCD Plugins

  - **(2023)** [==argoproj-labs/argocd-vault-plugin==](https://github.com/argoproj-labs/argocd-vault-plugin) <span class='md-tag md-tag--info'>⭐ 967</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An indispensable Argo CD plugin built to inject secrets dynamically from HashiCorp Vault, AWS Secrets Manager, or GCP Secret Manager. Replaces custom templating hacks by decrypting and injecting secret values directly into workloads at synchronization time, ensuring zero plaintext secrets enter the Git repository.
  - **(2022)** [github.com/crumbhole/argocd-vault-replacer](https://github.com/crumbhole/argocd-vault-replacer) <span class='md-tag md-tag--info'>⭐ 109</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized replacement utility designed to pull secrets from HashiCorp Vault during the Argo CD rendering phase. Acts as a lightweight precursor/alternative to full plugin integrations, enabling targeted placeholder substitutions within native Kubernetes manifest streams.
#### Sealed Secrets

##### ArgoCD (3)

  - **(2021)** [**dev.to: Argo CD and Sealed Secrets is a perfect match**](https://dev.to/timtsoitt/argo-cd-and-sealed-secrets-is-a-perfect-match-1dbf) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Illustrates the architecture of deploying Bitnami Sealed Secrets alongside ArgoCD. Solves the core GitOps paradox by allowing users to safely commit encrypted secrets to Git, which are then decrypted inside the cluster by the controller.
## Security and Compliance (2)

### Vulnerabilities and CVEs

#### ArgoCD Security

##### Remediation

  - **(2022)** [**infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability**](https://www.infoworld.com/article/2334525/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides concrete mitigation, scanning, and patching guidelines in the wake of CVE-2022-24348. Demonstrates strategies for minimizing risks in ArgoCD, including least-privilege service account configurations and network boundaries.
  - **(2022)** [**armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes**](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Highly detailed technical breakdown of CVE-2022-24348, analyzing how Helm/Kustomize relative path resolution was bypassed. Outlines step-by-step remediation plans and security control recommendations to protect clusters.
  - **(2022)** [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — News coverage of a severe vulnerability affecting ArgoCD. Explains how the path traversal flaw (CVE-2022-24348) allowed malicious manifests to pull sensitive secrets and files from the GitOps control plane cluster.
  - **(2022)** [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how security researchers identified a critical path-traversal bug (CVE-2022-24348) within the ArgoCD repository-reconciliation component. Evaluates the potential risk exposure of configuration data and key material.
  - **(2022)** [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.com/127708/hacking/kubernetes-argo-cd-flaw.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the threat landscape exposed by vulnerability CVE-2022-24348 in multi-tenant environments. Emphasizes why prompt patching of GitOps controllers is critical when handling multi-tenant repositories on shared control planes.

---
💡 **Explore Related:** [CI/CD](./cicd.md) | [Gitops](./gitops.md) | [CI/CD Kubernetes Plugins](./cicd-kubernetes-plugins.md)

