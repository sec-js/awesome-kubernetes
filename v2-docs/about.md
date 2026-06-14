# About Nubenetes

!!! info "Architectural Context"
    Detailed reference for About Nubenetes in the context of Architectural Foundations.

## The Nubenetes Engineering Manifest

!!! quote "The Positive Sum Game"
    ==*"Open Source is most successful when is played as a positive sum game" (Sarah Novotny)*==

### 🏛️ 1. The Genesis: Munich 2018
Nubenetes was forged in the internals of a massive Cloud Native transformation for a **major multinational car manufacturer** in Munich. Coordinating hundreds of microservices, thousands of developers, and millions of end-users taught us a fundamental truth: **Standardization, Automation, and GitOps are not "best practices"—they are survival requirements.**

### 🧠 2. Our Engineering Philosophy
We reject technical obfuscation as a competitive advantage. Solutions that are "the hard way" by design do not scale and create fragile, person-dependent silos. 

#### 2.1. Correctness by Design
We believe in doing DevOps correctly through the **GitOps pattern**. Automation without correctness is just faster failure. This architectural rigor ensures enterprise-grade stability at scale.

#### 2.2. The Scientific Method
We build bridges based on **evidence**, not politics or hype. If a solution cannot be empirically verified and automated, it is a liability. Engineers rely on evidence to solve problems.

#### 2.3. Anti-Bikeshining: Abstractions over Reinvention
We prioritize established frameworks and enterprise standards over ad-hoc, unmaintainable tooling. Reinventing the wheel is often a symptom of misaligned incentives in the IT sector.

### 📊 3. Comparative Maturity Framework

| Principle | Strategic Focus | Primary Toolset | Architectural Impact |
| :--- | :--- | :--- | :--- |
| **DevOps** | Automation & Frequency | CI/CD Pipelines | Operational Speed |
| **GitOps** | ==Correctness & Drift Control== | Git + Kubernetes | ==Enterprise Stability== |
| **SRE** | Reliability & Prevention | Observability | Scalable Quality |

### 🚀 4. The 2026 Vision: Agentic Intelligence
Nubenetes has evolved from a historical manual archive into an **Agentic Knowledge Graph**. 

#### 4.1. V1 Archive (Exhaustive)
Preserves historical context, the original curator's voice, and every technically valid link discovered since 2018. It serves as the foundational truth for the entire ecosystem.

#### 4.2. V2 Elite Portal (Distilled)
An O'Reilly-style technical library where 18k+ resources are filtered, ranked by impact, and enriched with AI-driven architectural summaries for high-speed reference.

> *"I am a big fan of the scientific method. Engineers do not build bridges from a right or left perspective... hello! I have a problem, can you help me? Engineers rely on evidence."* — **Mark Stevenson**

---

## Standard Reference

  - [DZone: Defining Day-2 Operations](https://dzone.com/articles/defining-day-2-operations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [alexander-goida.medium.com: Thoughts about breaking silos of software engineering' teams 🌟](https://alexander-goida.medium.com/thoughts-about-breaking-silos-of-software-engineering-teams-323d1f78ef68)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [devdriven.by: Promotion Driven Development](https://devdriven.by/promotion)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [reddit.com: Promotion Driven Development](https://www.reddit.com/r/ExperiencedDevs/comments/pw6vuv/promotion_driven_development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [en.wikipedia.org: Kiss up kick down](https://en.wikipedia.org/wiki/Kiss_up_kick_down)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Automation and Orchestration

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
## Infrastructure as Code

### Kubernetes

#### Terraform Boilerplates

  - **(2024)** [Terraform Kubernetes Boilerplates 🌟](https://nubenetes.com/terraform/) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A library of enterprise-stable Terraform templates configured specifically for modern Kubernetes environments (EKS, GKE, AKS). Includes pre-tested infrastructure specifications for VPC topologies, private nodes, and dynamic ingress setups.

---
💡 **Explore Related:** [Demos](./demos.md) | [Kubernetes](./kubernetes.md) | [Cheatsheets](./cheatsheets.md)

