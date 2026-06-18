# About Nubenetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/about/).

!!! info "Architectural Context"
    Detailed reference for About Nubenetes in the context of Architectural Foundations.

## Table of Contents

1. [Automation and Orchestration](#automation-and-orchestration)
  - [API Orchestration](#api-orchestration)
    - [Postman](#postman)
    - [Swagger Codegen](#swagger-codegen)
  - [CICD and Pipelines](#cicd-and-pipelines)
    - [Azure Pipelines](#azure-pipelines)
    - [GitLab CI](#gitlab-ci)
    - [Jenkins CLI](#jenkins-cli)
    - [Jenkins JCasC](#jenkins-jcasc)
    - [Jenkins REST API](#jenkins-rest-api)
  - [Configuration Management](#configuration-management)
    - [Ansible AWX](#ansible-awx)
    - [Ansible Kubernetes Module](#ansible-kubernetes-module)
  - [GitOps](#gitops)
    - [Argo CD](#argo-cd)
  - [Infrastructure as Code](#infrastructure-as-code)
    - [Terraform Boilerplates](#terraform-boilerplates)
    - [Terraform Provider](#terraform-provider)
  - [Package Management](#package-management)
    - [Helm](#helm)
  - [Templating Engine](#templating-engine)
    - [Jinja](#jinja)
1. [Cloud Native](#cloud-native)
  - [Kubernetes Development](#kubernetes-development)
    - [Go Client-Go](#go-client-go)
      - [Generics](#generics)
1. [Kubernetes Tools](#kubernetes-tools)
  - [General Reference](#general-reference)

## The Nubenetes Engineering Manifest

!!! quote "The Positive Sum Game"
    ==*"Open Source is most successful when is played as a positive sum game" (Sarah Novotny)*==

<div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; margin: 24px 0;">
  <iframe width="480" height="270" src="https://www.youtube.com/embed/GZl7N8sXyEo" title="Cowboy Bebop - Tank!" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
  <iframe width="480" height="270" src="https://www.youtube.com/embed/t_hdOVsdRSE" title="Jimmy Sax - Time" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

### 1. The Genesis: Munich 2018
Nubenetes was forged in the internals of a massive Cloud Native transformation for a **major multinational car manufacturer** in Munich. Coordinating hundreds of microservices, thousands of developers, and millions of end-users taught us a fundamental truth: **Standardization, Automation, and GitOps are not "best practices"—they are survival requirements.**

### 2. Our Engineering Philosophy
We reject technical obfuscation as a competitive advantage. Solutions that are "the hard way" by design do not scale and create fragile, person-dependent silos. 

!!! abstract "2.1. Correctness by Design"
    We believe in doing DevOps correctly through the **GitOps pattern**. Automation without correctness is just faster failure. This architectural rigor ensures enterprise-grade stability at scale.

!!! abstract "2.2. The Scientific Method"
    We build bridges based on **evidence**, not politics or hype. If a solution cannot be empirically verified and automated, it is a liability. Engineers rely on evidence to solve problems.

#### 2.3. Anti-Bikeshining: Abstractions over Reinvention
We prioritize established frameworks and enterprise standards over ad-hoc, unmaintainable tooling. Reinventing the wheel is often a symptom of misaligned incentives in the IT sector.

#### 2.4. Avoiding Engineering Anti-Patterns
We combat the culture of **Promotion-Based Development (PBD)**, where complexity is manufactured for personal career visibility rather than business value. 

  - [Promotion-Based Development: A Fast Track to Mediocrity](https://vadimkravcenko.com/shorts/promotion-based-development/) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Dissects how rewarding "shiny new things" over battle-tested stability leads to fragile architectures.
  - [Reddit: The Reality of Promotion-Driven Development](https://www.reddit.com/r/ExperiencedDevs/comments/pw6vuv/promotion_driven_development) <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A raw, evidence-based discussion from senior engineers on the industry's most common misaligned incentives.

### 3. The Architectural North Star
We advocate for decoupled, maintainable architectures that survive the test of time and organizational growth.

  - [Domain-Driven Design (DDD) for Microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The foundational blueprint for defining service boundaries based on business domains rather than technical layers.
  - [Hexagonal Architecture (Ports and Adapters)](https://medium.com/@sandeepsharmaster/modernize-your-cloud-microservices-apps-hexagonal-architecture-769696494c0) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Decoupling the application core from external infrastructure (Databases, APIs, UI) to ensure high testability and vendor neutrality.

### 4. Comparative Maturity Framework

| Principle | Strategic Focus | Primary Toolset | Architectural Impact |
| :--- | :--- | :--- | :--- |
| **DevOps** | Automation & Frequency | CI/CD Pipelines | Operational Speed |
| **GitOps** | ==Correctness & Drift Control== | Git + Kubernetes | ==Enterprise Stability== |
| **SRE** | Reliability & Prevention | Observability | Scalable Quality |

#### 4.1. SRE vs. DevOps Responsibility Matrix

| **Site Reliability Engineer (SRE) team** | **Developers** | **Operations team** |
| :--- | :--- | :--- |
| Provide and teach effective use of platform tooling to empower developers to be self-sufficient | Treat SREs as application operation partners, not only as first responders to incidents | Provide self-service platform deployment and observability, and enable visibility into ramifications of actions |
| Document clear escalation paths for developers struggling in production | Turn to ops teams for the "paved path" or centralized developer control plane | Provide opinionated "paved path" platform or developer control plane (DCP), but allow developers to swap platform components if they also want to be accountable |

### 5. Strategic Standards and Cultural Shifts
Engineering excellence is as much about **culture** as it is about code. These foundational resources define the strategic landscape of modern Cloud Native organizations:

  - [The Agile Manifesto](https://agilemanifesto.org) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The primary root of modern iterative development and the shift away from monolithic planning.
  - [Google: SRE vs. DevOps — Competing Standards or Close Friends?](https://cloud.google.com/blog/products/gcp/sre-vs-devops-competing-standards-or-close-friends) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An essential blueprint for understanding the symbiotic relationship between reliability engineering and delivery speed.
  - [The 4 Levels of GitOps Maturity](https://cloudnativenow.com/features/the-4-levels-of-gitops-maturity) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A roadmap for evolving from manual deployments to a fully automated, self-healing state.
  - [Necessary Culture Change with GitOps](https://itnext.io/necessary-culture-change-with-gitops-2c63f4fe9604) <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> — Dissects the organizational friction and the necessary mindset shift required to adopt declarative infrastructure.

### 6. Scaling with Evidence: DORA and Value Streams
We advocate for data-driven engineering management to avoid the trap of "gut-feeling" decision making.

  - [Driving DevOps with Value Stream Management](https://www.infoq.com/articles/DevOps-value-stream) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Dissects how to align microservice delivery with business outcomes through flow metrics.
  - [Better Metrics for Building High Performance Teams](https://www.infoq.com/articles/better-metrics-team-performance) <span class='md-tag md-tag--warning'>[EMERGING]</span> — Beyond LOC and commits: using DORA metrics to cultivate a culture of systemic stability.

### 7. Technical Leadership and The 'Glue' Factor
True seniority is measured by the ability to hold teams together through communication and shared context.

  - [Being Glue](https://noidea.dog/glue) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An industry-standard analysis of the essential, non-coding technical tasks that ensure project success.
  - [How Big Tech Runs Tech Projects](https://blog.pragmaticengineer.com/project-management-at-big-tech) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A seminal critique of ceremonial Scrum versus result-oriented engineering pragmatism.
  - [Martin Fowler: Retrospectives Antipatterns](https://martinfowler.com/articles/retrospective-antipatterns.html) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Essential guide for transforming team feedback loops from blame games into architectural improvement cycles.

### 8. Meritocracy and Careers in 2026
We advocate for a technical sector where quality and evidence-based decisions take precedence over corporate politics.

  - [HBR: Stop Hiring for Culture Fit](https://hbr.org/2019/11/stop-hiring-for-culture-fit) <span class='md-tag md-tag--warning'>[EMERGING]</span> — A critical perspective on how "culture fit" often hides bias and hinders technical innovation.
  - [Defining Day-2 Operations](https://dzone.com/articles/defining-day-2-operations) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Shifts the focus from the excitement of the first deployment to the long-term reality of maintaining production stability.

### 9. The 2026 Vision: Agentic Intelligence
Nubenetes has evolved from a historical manual archive into an **Agentic Knowledge Graph**. 

#### 9.1. V1 Archive (Exhaustive)
Preserves historical context, the original curator's voice, and every technically valid link discovered since 2018. It serves as the foundational truth for the entire ecosystem.

#### 9.2. V2 Elite Portal (Distilled)
An O'Reilly-style technical library where 18k+ resources are filtered, ranked by impact, and enriched with AI-driven architectural summaries for high-speed reference.

### 10. DevOps Demystified: Role Ambiguity and the OpsDev Pivot
DevOps has suffered significant semantic dilution, often misused as a catch-all role. We define DevOps as the engineering of pipelines and Infrastructure as Code (IaC) using standard tooling under a **cattle service model**, rather than ad-hoc script-writing or monitoring development. A DevOps specialist is not a general full-stack developer who handles QA and Ops on the side. To eliminate confusion, the term **OpsDev** is often a more accurate representation of this infrastructure-first engineering discipline.

### 11. The Certification Trap vs. Empirical Skill
While certifications like CKA are prominent on CVs, they are frequently utilized by recruiters as an artificial filter. True engineering value is built by doing—writing automated, testable, and declarative GitOps pipelines, rather than mastering manual CLI execution. Relying purely on certifications often encourages memorizing exam patterns over learning design abstractions. Seniority is measured by empirical evidence and day-2 operational stability, not exam certificates.

> *"I am a big fan of the scientific method. Engineers do not build bridges from a right or left perspective... hello! I have a problem, can you help me? Engineers rely on evidence."* — **Mark Stevenson**

---

## Automation and Orchestration

### API Orchestration

#### Postman

??? note "Postman"
    **[Access Resource](https://www.postman.com)** 🌟🌟🌟🌟🌟 | Level: Intermediate
    
    Postman remains a prominent API collaboration platform. It offers developers comprehensive tools to design, mock, test, document, and monitor APIs within an intuitive, team-oriented development lifecycle workspace.

#### Swagger Codegen

??? note "Swagger Codegen"
    **[Access Resource](https://github.com/swagger-api/swagger-codegen)** 🌟🌟🌟🌟 | Level: Intermediate
    
    Automatic generation of API client libraries and server stubs from OpenAPI/Swagger specifications.

### CICD and Pipelines

#### Azure Pipelines

??? note "Azure Pipelines"
    **[Access Resource](https://learn.microsoft.com/en-us/azure/devops/pipelines)** 🌟🌟🌟🌟 | Level: Beginner
    
    Cloud-hosted CI/CD pipeline service by Microsoft, supporting both Windows, Linux, and macOS environments.

#### GitLab CI

??? note "GitLab CI/CD"
    **[Access Resource](https://docs.gitlab.com/ee/ci)** 🌟🌟🌟🌟🌟 | Level: Beginner
    
    Built-in continuous integration and delivery engine of GitLab, supporting declarative YAML pipeline specifications.

#### Jenkins CLI

??? note "Jenkins CLI"
    **[Access Resource](https://www.jenkins.io/doc/book/managing/cli)** 🌟🌟🌟🌟 | Level: Intermediate
    
    The official command-line runtime interface for administering remote Jenkins controller servers. Allows automated shell execution of administrative tasks, plugin updates, diagnostic tracing, and build queue interventions.

#### Jenkins JCasC

??? note "Jenkins Configuration as Code"
    **[Access Resource](https://www.jenkins.io/projects/jcasc)** 🌟🌟🌟🌟🌟 | Level: Advanced
    
    Core configuration portal resource emphasizing JCasC's role in establishing single-source-of-truth configuration files. It eliminates configuration drift through central, repeatable environments.

#### Jenkins REST API

??? note "Jenkins Remote Access API"
    **[Access Resource](https://www.jenkins.io/doc/book/using/remote-access-api)** 🌟🌟🌟🌟 | Level: Beginner
    
    Official documentation for Jenkins RESTful API integration, enabling remote control, status querying, and programmatic pipeline orchestration.

### Configuration Management

#### Ansible AWX

??? note "AWX"
    **[Access Resource](https://github.com/ansible/awx)** 🌟🌟🌟🌟🌟 | Level: Advanced
    
    AWX serves as the open-source upstream project for Ansible Automation Platform/Tower. Written in Django and React, it provides a web-based user interface, REST API, and task engine to centrally manage Ansible inventories, credentials, playbooks, and scheduling in containerized environments.

#### Ansible Kubernetes Module

??? note "docs.ansible.com: kubernetes.core.k8s – Manage Kubernetes objects"
    **[Access Resource](https://docs.ansible.com/projects/ansible/latest/collections/kubernetes/core/k8s_module.html)** 🌟🌟🌟🌟 | Level: Intermediate
    
    Official documentation for the cornerstone `kubernetes.core.k8s` module. It allows direct, declarative definition of Kubernetes objects inside Ansible playbooks using native YAML manifest definitions, enabling a blended hybrid orchestration pattern.

### GitOps

#### Argo CD

??? note "Argo CD"
    **[Access Resource](https://argoproj.github.io/argo-cd)** 🌟🌟🌟🌟🌟 | Level: Intermediate
    
    The absolute industry standard for GitOps-based continuous delivery on Kubernetes. Argo CD synchronizes active cluster states with declarative configurations stored in git repositories, providing robust drift correction, visual dashboarding, and audit controls.

### Infrastructure as Code

#### Terraform Boilerplates

??? note "Terraform Kubernetes Boilerplates 🌟"
    **[Access Resource](https://nubenetes.com/terraform)** 🌟🌟🌟🌟🌟 | Level: Advanced
    
    A library of enterprise-stable Terraform templates configured specifically for modern Kubernetes environments (EKS, GKE, AKS). Includes pre-tested infrastructure specifications for VPC topologies, private nodes, and dynamic ingress setups.

#### Terraform Provider

??? note "Terraform Kubernetes Provider"
    **[Access Resource](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs)** 🌟🌟🌟🌟 | Level: Beginner
    
    Official Kubernetes provider for Terraform, enabling declarative deployment and management of Kubernetes resources using HashiCorp Configuration Language (HCL).

### Package Management

#### Helm

??? note "Helm"
    **[Access Resource](https://github.com/helm/helm)** 🌟🌟🌟🌟🌟 | Level: Advanced
    
    Official Go implementation of the Helm client, acting as the package manager for Kubernetes. Helm manages complex application definitions through charts, providing repeatable deployments, in-place upgrades, and robust rollback capabilities.

### Templating Engine

#### Jinja

??? note "jinja 🌟"
    **[Access Resource](https://github.com/pallets/jinja)** 🌟🌟🌟🌟🌟 | Level: Advanced
    
    The official repository for Jinja, the ubiquitous Python-based templating engine. Jinja underpins all dynamic evaluation structures inside Ansible, enabling programmatic infrastructure assembly.

## Cloud Native

### Kubernetes Development

#### Go Client-Go

##### Generics

  - [itnext.io: Generically working with Kubernetes objects in Go](https://itnext.io/generically-working-with-kubernetes-resources-in-go-53bce678f887) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the use of Go 1.18+ generics to drastically reduce boilerplate when interacting with various Kubernetes API types. Live Grounding confirms that while standard client-go uses dynamic clients or interface{} for generic operations, integrating Go generics allows for cleaner, type-safe custom controllers. This article provides practical patterns for wrapping standard clients to streamline resource manipulation.
## Kubernetes Tools

### General Reference

  - [DZone: Defining Day-2 Operations](https://dzone.com/articles/defining-day-2-operations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==DZone: Defining Day-2 Operations== in the Kubernetes Tools ecosystem.
  - [alexander-goida.medium.com: Thoughts about breaking silos of software engineering' teams 🌟](https://alexander-goida.medium.com/thoughts-about-breaking-silos-of-software-engineering-teams-323d1f78ef68)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering alexander-goida.medium.com: Thoughts about breaking silos of software engineering' teams 🌟 in the Kubernetes Tools ecosystem.
  - [reddit.com: Promotion Driven Development](https://www.reddit.com/r/ExperiencedDevs/comments/pw6vuv/promotion_driven_development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering reddit.com: Promotion Driven Development in the Kubernetes Tools ecosystem.
  - [en.wikipedia.org: Kiss up kick down](https://en.wikipedia.org/wiki/Kiss_up_kick_down)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering en.wikipedia.org: Kiss up kick down in the Kubernetes Tools ecosystem.

---
💡 **Explore Related:** [Demos](./demos.md) | [Kubernetes](./kubernetes.md) | [Cloud Arch Diagrams](./cloud-arch-diagrams.md)

