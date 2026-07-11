---
description: "Curated, AI-ranked Argo resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Engineering Pipeline)."
---
# Argo Declarative GitOps for Kubernetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/argo/).

!!! info "Architectural Context"
    Detailed reference for Argo Declarative GitOps for Kubernetes in the context of Engineering Pipeline.

## GitOps and CD

### Argo Rollouts

#### Blue-Green Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through setting up a complete Blue-Green deployment workflow with Argo Rollouts. Outlines routing controls, active/preview service handoffs, and visual UI verification configurations.
#### Canary Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Offers a practical exploration of canary rollouts configured via Argo Rollouts. Focuses on setting step-based traffic splitting, managing dynamic service mesh weights (SMI, Linkerd, Istio), and defining automated rollbacks based on analysis metrics.
#### Configuration Management

  - **(2022)** [**codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts**](https://octopus.com/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Solves the tricky challenge of managing and rolling out application configuration updates dynamically. Demonstrates how to trigger controlled, safe progressive delivery cycles for applications when only ConfigMaps or Secrets are modified.
#### Progressive Delivery

  - **(2023)** [==argoproj.github.io: Argo Rollouts - Kubernetes Progressive Delivery Controller==](https://argoproj.github.io/argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces the core concepts of Argo Rollouts, which replaces standard Kubernetes Deployment objects with custom Rollout resources. Enables automatic analysis, metrics integration (Prometheus, Datadog), and automated rollback strategies.
### ArgoCD

#### Patterns

##### App-of-Apps

  - **(2021)** [**opensource.com: Automatically create multiple applications in Argo CD**](https://opensource.com/article/21/7/automating-argo-cd) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates how to leverage the 'App-of-Apps' pattern in ArgoCD to construct recursive, nested application structures. Enables engineers to automate the bootstrapping of complex multi-tier platforms from a single root configuration.
#### Workload Management

##### Demos

  - **(2023)** [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive demo repository showcasing real-world GitOps workload configurations. Provides a structural blueprint for multi-tenant environments, detailing how to cleanly decouple cluster-wide infrastructure configurations from individual application manifests.
### CICD Integration

  - **(2023)** [dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores architectural models for bridging continuous integration (CI) platforms with GitOps-driven deployment mechanisms. Emphasizes clean decoupling where CI updates target config states while Kubernetes reconcile loops execute the rollout.
## Kubernetes GitOps and Packaging

### Argo Project Ecosystem

#### Event-Driven Automation

  - **(2026)** [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The standard event-driven orchestration engine for Kubernetes. Argo Events integrates with sources like webhooks, S3, or pub-sub, dynamically executing serverless triggers, custom scripts, and Argo Workflows with native scalability.
## Platform Engineering

### ArgoCD (1)

#### Internal Developer Platforms

  - **(2023)** [**itnext.io: Build a Lightweight Internal Developer Platform with Argo CD and Kubernetes Labels**](https://itnext.io/build-a-lightweight-internal-developer-platform-with-argo-cd-and-kubernetes-labels-4c0e52c6c0f4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Demonstrates how to design a lightweight, self-service Internal Developer Platform (IDP) by leveraging Kubernetes metadata labels, admission webhooks, and ArgoCD's API to dynamically generate applications.
### GitOps

#### AWS EKS

##### Tekton

  - **(2022)** [==aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS==](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Discusses designing an end-to-end, Kubernetes-native CI/CD pipeline on AWS EKS. Uses Tekton for building and containerizing microservices, seamlessly handing off the deployment phase to ArgoCD for pull-based application delivery.
#### GitHub Actions

##### AWS EKS (1)

  - **(2023)** [**dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques**](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed configuration recipe detailing how to orchestrate deployments to AWS EKS using GitHub Actions as the CI pipeline and ArgoCD as the GitOps agent. Includes IAM role assumptions, token handling, and multi-environment promotions.
#### Terraform Integration

##### Data Infrastructure

  - **(2022)** [**piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟**](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical demonstration of deploying and managing a Kafka cluster on Kubernetes using a hybrid Terraform and ArgoCD approach. Discusses how to configure infrastructure dependencies with Terraform and declare workload states inside GitOps.
### Progressive Delivery (1)

#### DNS Routing

##### Blue-Green Deployment (1)

  - **(2022)** [**infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟**](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines advanced architectural design patterns using DNS-based routing to switch traffic for Blue-Green deployments. Discusses how to coordinate external load balancers and global DNS systems during the migration window.

---
💡 **Explore Related:** [Jenkins Alternatives](./jenkins-alternatives.md) | [Keptn](./keptn.md) | [Gitops](./gitops.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

