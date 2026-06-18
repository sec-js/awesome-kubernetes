# Liquibase

!!! info "Architectural Context"
    Detailed reference for Liquibase in the context of Hardened Infrastructure.

## Table of Contents

1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Native Infrastructure](#cloud-native-infrastructure)
  - [Kubernetes Deployment Patterns](#kubernetes-deployment-patterns)
    - [Database Deployment](#database-deployment)
1. [Continuous Delivery](#continuous-delivery)
  - [Database GitOps](#database-gitops)
    - [Liquibase](#liquibase-1)
1. [Data Architecture](#data-architecture)
  - [Database Migrations](#database-migrations)
    - [Tool Comparison](#tool-comparison)
1. [Database Architecture](#database-architecture)
  - [Cloud Native Databases](#cloud-native-databases)
    - [Vitess](#vitess)
  - [Database GitOps](#database-gitops-1)
    - [Schema Management](#schema-management)
  - [Database Migration](#database-migration)
    - [Schema Evolution](#schema-evolution)
1. [Infrastructure as Code](#infrastructure-as-code)
  - [Database Migration](#database-migration-1)
    - [CICD and Delivery](#cicd-and-delivery)

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Flyway](https://www.red-gate.com/products/flyway/community)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.red-gate.com in the Kubernetes Tools ecosystem.
  - [wikipedia](https://en.wikipedia.org/wiki/Evolutionary_database_design)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering wikipedia in the Kubernetes Tools ecosystem.
  - [dzone: Introduction to Liquibase and Managing Your Database Source Code](https://dzone.com/articles/introduction-to-liquibase-and-managing-your-databa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Introduction to Liquibase and Managing Your Database Source Code in the Kubernetes Tools ecosystem.
  - [dzone: Managing Your Database With Liquibase and Gradle](https://dzone.com/articles/managing-your-database-with-liquibase-and-gradle)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Managing Your Database With Liquibase and Gradle in the Kubernetes Tools ecosystem.
  - [dzone: Executing Liquibase: 3 Use Cases](https://dzone.com/articles/executing-liquibase-3-use-cases)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Executing Liquibase: 3 Use Cases in the Kubernetes Tools ecosystem.
  - [dzone: Build a Spring Boot App With Flyway and Postgres](https://dzone.com/articles/build-a-spring-boot-app-with-flyway-and-postgres)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Build a Spring Boot App With Flyway and Postgres in the Kubernetes Tools ecosystem.
  - [medium: Database version control — Liquibase versus Flyway](https://medium.com/@ruxijitianu/database-version-control-liquibase-versus-flyway-9872d43ee5a4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Database version control — Liquibase versus Flyway in the Kubernetes Tools ecosystem.
## Cloud Native Infrastructure

### Kubernetes Deployment Patterns

#### Database Deployment

  - **(2021)** [piotrminkowski.com: Blue-green deployment with a database on Kubernetes 🌟](https://piotrminkowski.com/2021/02/18/blue-green-deployment-with-a-database-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical blueprint demonstrating blue-green deployments on Kubernetes for applications bound to transactional databases. Explores state synchronization, schema compatibility, and traffic routing mechanisms to prevent transaction loss during rolling updates.
## Continuous Delivery

### Database GitOps

#### Liquibase (1)

  - **(2023)** [**percona: Database Schema Management Via Liquibase**](https://percona.community/blog) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Architectural guide for automating relational database migrations using Liquibase in CI/CD chains. Evaluates declarative XML/SQL changeset formats, execution tracking setups, and rollback configurations necessary to safely release database modifications alongside microservices.
## Data Architecture

### Database Migrations

#### Tool Comparison

  - **(2024)** [liquibase.org: Liquibase vs. Flyway](https://www.liquibase.com/liquibase-vs-flyway)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed evaluation of the architectural trade-offs between Liquibase and Flyway. This resource explores Liquibase's multi-database abstraction layers (XML, YAML, JSON) alongside Flyway's developer-focused, SQL-first approach, explaining their impact on continuous delivery pipelines and database schema version control.
## Database Architecture

### Cloud Native Databases

#### Vitess

  - **(2021)** [docs.planetscale.com: The PlanetScale workflow 🌟](https://planetscale.com/docs/vitess/best-practices) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documentation outlining the schema migration workflow in PlanetScale, powered by Vitess. Introduces non-blocking schema changes and deployment branches, enabling developers to modify production databases without locking tables or causing downtime.
### Database GitOps (1)

#### Schema Management

  - **(2021)** [==bytebase/bytebase==](https://github.com/bytebase/bytebase) <span class='md-tag md-tag--info'>⭐ 14143</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d71ad053" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 4 L 20 8 L 30 10 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-d71ad053)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Open-source, web-based database schema change and collaboration tool engineered for DevOps teams and DBAs. Features GitOps-driven workflow mechanics, automated visual SQL review, and centralized security compliance policies to govern multi-engine environments.
### Database Migration

#### Schema Evolution

  - **(2006)** [liquibase.org](https://www.liquibase.org) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Liquibase is an open-source, platform-independent database schema migration tool designed to track, version, and deploy schema modifications. Employing XML, YAML, JSON, or SQL formats, it integrates into enterprise CI/CD pipelines to ensure database schemas evolve safely and repeatably alongside application code.
## Infrastructure as Code

### Database Migration (1)

#### CICD and Delivery

  - **(2023)** [martinfowler.com](https://martinfowler.com/articles/evodb.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A seminal essay on evolutionary database architectures. Highlights methods for treating database schemas as declarative code, versioning migrations, and automating data migrations safely inside unified application delivery pipelines.

---
💡 **Explore Related:** [IaC](./iac.md) | [Terraform](./terraform.md) | [Oauth](./oauth.md)

