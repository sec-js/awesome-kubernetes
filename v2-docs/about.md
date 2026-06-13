# About Nubenetes

!!! info "Architectural Context"
    Detailed reference for About Nubenetes in the context of Architectural Foundations.

## Standard Reference

  - [Terraform Kubernetes Boilerplates 🌟](https://nubenetes.com/terraform/)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [https://swagger.io/](https://swagger.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Jenkins Configuration as Code Plugin](https://www.jenkins.io/projects/jcasc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Jenkins CLI](https://www.jenkins.io/doc/book/managing/cli)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: GitOps vs. DevOps: What's the difference? 🌟](https://opensource.com/article/21/3/gitops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Kubernetes at Scale without GitOps Is a Bad Idea](https://thenewstack.io/kubernetes-at-scale-without-gitops-is-a-bad-idea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [DZone: Defining Day-2 Operations](https://dzone.com/articles/defining-day-2-operations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kube.careers: Kubernetes jobs market trends for 2021 (Q4)](https://kube.careers/report-2021-q4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [fairwinds.com: Never Should You Ever In Kubernetes: #1 Do K8S The Hard Way](https://www.fairwinds.com/blog/never-should-you-ever-in-kubernetes-1-do-k8s-the-hard-way)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [alexander-goida.medium.com: Thoughts about breaking silos of software engineering' teams 🌟](https://alexander-goida.medium.com/thoughts-about-breaking-silos-of-software-engineering-teams-323d1f78ef68)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devdriven.by: Promotion Driven Development](https://devdriven.by/promotion)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [reddit.com: Promotion Driven Development](https://www.reddit.com/r/ExperiencedDevs/comments/pw6vuv/promotion_driven_development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [en.wikipedia.org: Kiss up kick down](https://en.wikipedia.org/wiki/Kiss_up_kick_down)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [jinja 🌟](https://github.com/pallets/jinja) <span class='md-tag md-tag--info'>⭐ 11634</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [opensource.com: Using Ansible with REST APIs](https://opensource.com/article/21/9/ansible-rest-apis)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Infrastructure

### Systems Design

#### Operational Philosophy

  - **(2021)** [==cloudscaling.com: The History of Pets vs Cattle and How to Use the Analogy Properly==](http://cloudscaling.com/blog/cloud-computing/the-history-of-pets-vs-cattle) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Explores the history and technical framework of the classic 'Pets vs Cattle' infrastructure analogy. It contrasts the hand-managed, fragile nature of unique servers ('Pets') with automated, standardized, and easily replaced nodes designed for automated recovery ('Cattle'). This core concept underpins modern auto-scaling groups and container cluster design.
## Cloud Native

### Kubernetes Development

#### Go Client-Go

##### Generics

  - [itnext.io: Generically working with Kubernetes objects in Go](https://itnext.io/generically-working-with-kubernetes-resources-in-go-53bce678f887) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the use of Go 1.18+ generics to drastically reduce boilerplate when interacting with various Kubernetes API types. Live Grounding confirms that while standard client-go uses dynamic clients or interface{} for generic operations, integrating Go generics allows for cleaner, type-safe custom controllers. This article provides practical patterns for wrapping standard clients to streamline resource manipulation.
### Orchestration

#### Kubernetes

##### API Integration

  - **(2024)** [docs.ansible.com: kubernetes.core.k8s – Manage Kubernetes (K8s) objects](https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Core reference documentation for the 'kubernetes.core.k8s' module, allowing Ansible control planes to deploy and interact with native Kubernetes API resources directly. It integrates seamlessly with kubectl credentials to process declarative manifest payloads or inline spec configurations.
## Container Orchestration

### Kubernetes (1)

#### Infrastructure Control Planes

  - **(2021)** [nextplatform.com: KUBERNETES EXPANDS FROM CONTAINERS TO INFRASTRUCTURE MANAGEMENT 🌟](https://www.nextplatform.com/store/2021/08/02/kubernetes-expands-from-containers-to-infrastructure-management/1654000) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the transformation of Kubernetes from basic container scheduling into a complete cluster management control plane. Details how the API server can orchestrate non-container assets (VMs, database systems, physical hardware) through custom operators and CRDs.
## Development Tools

### API Testing and Design

#### Postman

  - **(2012)** [getpostman.com](https://www.postman.com) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Postman is an industry-standard API collaboration platform designed to streamline the lifecycle of API design, testing, documentation, and mock-server deployment. Architecturally, it enables cross-team collaboration via shared workspaces, automated collection runs, and seamless integration into CI/CD pipelines to validate REST, GraphQL, and gRPC endpoints.
## Operations and Reliability

### Site Reliability Engineering

#### Evolution

  - [thenewstack.io: How the SRE Experience Is Changing with Cloud Native 🌟](https://thenewstack.io/how-the-sre-experience-is-changing-with-cloud-native)  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — This high-density industry analysis examines how the rise of complex cloud-native architectures shifts SRE responsibilities. It addresses how microservices, service meshes, and dynamic scheduling require SREs to move from simple system monitoring to deep, code-level observability and platform design.

---
💡 **Explore Related:** [Demos](./demos.md) | [Cheatsheets](./cheatsheets.md) | [Kubernetes](./kubernetes.md)

