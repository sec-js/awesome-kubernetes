---
description: "Curated, AI-ranked Databases resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Data & Advanced Analytics)."
---
# Databases on Kubernetes. Database DevOps

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/databases/).

!!! info "Architectural Context"
    Detailed reference for Databases on Kubernetes. Database DevOps in the context of Data & Advanced Analytics.

## Cloud Infrastructure

### FinOps

#### Cost Optimization

  - **(2023)** [treblle.com: How does Treblle scale on AWS without breaking the bank?](https://treblle.com/blog/how-does-treblle-scale-on-aws-without-breaking-the-bank) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights Treblle’s architectural strategy for processing billions of API requests on AWS affordably. Live Grounding details how modern SaaS platforms leverage spot instances, API gateway caching, serverless scale-to-zero databases, and intensive performance profiling to decouple traffic volume from infrastructure costs.
## Cloud-Native Design

### Architecture Patterns

  - **(2022)** [blog.yugabyte.com: Are Stored Procedures and Triggers Anti-Patterns in the Cloud Native World?](https://blog.yugabyte.com/are-stored-procedures-and-triggers-anti-patterns-in-the-cloud-native-world) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines stored procedures and database triggers in cloud-native microservice topologies. Warns against architectural coupling and operational performance bottlenecks, advocating for stateless application logic to preserve horizontal scalability.
## Data Analytics

### Real-time Analytics

#### Edge Computing

  - **(2021)** [thenewstack.io: Kubernetes-Run Analytics at the Edge: Postgres, Kafka, Debezium](https://thenewstack.io/kubernetes-run-analytics-at-the-edge-postgres-kafka-debezium) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced technical blueprint coordinating microservices for real-time edge analytics. Chains local PostgreSQL instances, Apache Kafka, and Debezium change data capture (CDC) pipelines in unified Kubernetes clusters.
## Data Operations

### Database CICD

  - **(2021)** [cloudbees.com: Introductory Handbook for Database Continuous Integration](https://www.cloudbees.com/blog/beginners-guide-to-continuous-integration-and-deployment) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical guide to continuous integration and delivery loops for relational databases. Synthesizes migration-based vs. declarative database state strategies, tooling integrations, rollback plans, and schema change automation.
## Data on Kubernetes

### DBaaS

#### Enterprise RedHat

  - **(2021)** [cloud.redhat.com: Simplifying Database Cloud Service Access](https://www.redhat.com/en/blog/simplifying-database-cloud-service-access)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details standard patterns for binding external managed cloud databases to Kubernetes workloads. Highlights the Service Binding Operator specification, simplifying secret delivery, and enforcing secure connection parameters.
#### Internal Mechanics

  - **(2021)** [percona.com: DBaaS on Kubernetes: Under the Hood 🌟](https://www.percona.com/blog/dbaas-on-kubernetes-under-the-hood) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive analysis of the architecture behind running custom, private Database-as-a-Service platforms inside a Kubernetes environment. Demonstrates automated provisioning, high availability clustering, and backup pipelines through Percona's open-source database operators.
### Disaster Recovery

#### Enterprise RedHat (1)

  - **(2021)** [cloud.redhat.com: OpenShift Commons Briefing: Database Disaster Recovery Made Easy with Annette Clewett (Red Hat) and Andrew L'Ecuyer (Crunchy Data)](https://www.redhat.com/en/blog/openshift-commons-briefing-database-disaster-recovery-made-easy-with-annette-clewett-red-hat-and-andrew-lecuyer-crunchy-data) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An expert briefing on constructing bulletproof disaster recovery pipelines for PostgreSQL databases hosted inside OpenShift. Showcases multi-region replication strategies, off-site storage configurations, and seamless failovers.
### Distributed Systems

#### ShardingSphere

  - **(2022)** [infoq.com: Create Your Distributed Database on Kubernetes with Existing Monolithic Databases](https://www.infoq.com/articles/kubernetes-databases-apache-sharding-sphere) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An implementation guide for modernizing monolithic databases into highly distributed, sharded databases using Apache ShardingSphere on Kubernetes. Outlines high-performance read-write splitting, data sharding strategies, and state orchestration.
### Performance Tuning

#### Autoscaling

  - **(2022)** [percona.com: Autoscaling Databases in Kubernetes for MongoDB, MySQL, and PostgreSQL](https://www.percona.com/blog/autoscaling-databases-in-kubernetes-for-mongodb-mysql-and-postgresql) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Outlines technical patterns for auto-scaling relational and document databases like MongoDB, MySQL, and PostgreSQL on Kubernetes. Examines vertical container resource updates, storage auto-expansion, and scaling read replicas in response to high traffic demand.
### Relational Databases

#### Operations

  - **(2021)** [sqlshack.com: SQL Database on Kubernetes: Considerations and Best Practices 🌟](https://www.sqlshack.com/sql-database-on-kubernetes-considerations-and-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides actionable guidance on running relational workloads inside container orchestration layers. Outlines patterns for configuring StateSet controllers, choosing fast storage classes, and applying anti-affinity rules to enforce cluster high availability.
#### PostgreSQL

  - **(2022)** [blog.crunchydata.com: Using Kubernetes? Chances Are You Need a Database 🌟](https://www.crunchydata.com/blog/using-kubernetes-chances-are-you-need-a-database)  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines why PostgreSQL is standardizing on Kubernetes. Explains how the Crunchy Data PostgreSQL Operator implements high availability, automated back-ups, pgBackRest integration, and localized failovers for microservice application stacks.
### Stateful Architecture

#### Operational Guide

  - **(2021)** [itnext.io: How to Run Databases in Kubernetes](https://itnext.io/stateful-workloads-in-kubernetes-e49b56a5959)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A granular blueprint on configuring stateful workloads inside Kubernetes clusters. Details the practical implementation of Headless Services, stable network identifiers, local persistent volumes, and graceful cluster shutdowns.
## Database Architecture

### DBaaS (1)

#### Market Trends

  - **(2021)** [thenewstack.io: Database-as-a-Service: A Key Technology for Agile Growth](https://thenewstack.io/database-as-a-service-a-key-technology-for-agile-growth)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates how the adoption of cloud-native DBaaS increases deployment velocity for modern, distributed engineering organizations by abstracting routine scaling and maintenance behind APIs.
### Database Interfaces

#### API Design

  - **(2022)** [thenewstack.io: How Radical API Design Changed the Way We Access Databases](https://thenewstack.io/how-radical-api-design-changed-the-way-we-access-databases)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores how modern schema-aware API clients, GraphQL adapters, and serverless proxy layers are replacing standard raw driver bindings, simplifying secure and high-performance database connection pooling.
### Microservices Patterns

#### Transactions

  - **(2020)** [hackernoon.com: Practical Transaction Handling in Microservice Architecture](https://hackernoon.com/practical-transaction-handling-in-microservice-architecture-5x1631ke) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides deep analysis of transactional boundaries inside distributed microservice systems. Explores the design of the Saga pattern (orchestrated/choreographed), transactional outboxes, and 2-phase commits for strong versus eventual consistency.
### Multi-tenancy

#### Schema Design

  - **(2020)** [vladmihalcea.com: A beginner’s guide to database multitenancy](https://vladmihalcea.com/database-multitenancy) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the three primary multi-tenant database models: database-per-tenant, schema-per-tenant, and shared-schema-shared-database. Critically evaluates trade-offs regarding data isolation, schema migrations, and database connection limits.
### Traffic Management

#### Load Balancing

  - **(2021)** [thenewstack.io: How Database Load Balancing Completes the 3-Tiered Architecture 🌟](https://thenewstack.io/database-load-balancing-and-the-delusion-of-3-tiered-architecture) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs the traditional 3-tier architecture to detail why decoupling query routing from application layers via dedicated database load balancers is essential. Examines how custom routing mitigates split-brain scenarios and ensures reliable active-passive replication failover.
## Distributed SQL

### APIs

  - **(2021)** [dev.to: REST Data Service on YugabyteDB / PostgreSQL](https://dev.to/yugabyte/rest-data-service-on-yugabytedb-postgresql-5f2h) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed walk-through demonstrating how to configure and deploy a high-throughput REST data microservice backed by YugabyteDB's PostgreSQL-compatible distributed SQL core. Bridges database replication and horizontally scalable API development patterns.
### CockroachDB

  - **(2025)** [Cockroach](https://www.cockroachlabs.com/docs/stable/kubernetes-overview) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official engineering design blueprint for executing CockroachDB on Kubernetes. Details multi-active master clustering, Raft consensus mechanics, anti-entropy processes, and seamless horizontal write scaling utilizing Kubernetes orchestration primitives.
## Infrastructure

### Container Orchestration

#### Data on Kubernetes (1)

  - **(2022)** [thenewstack.io: Data on Kubernetes: The Next Frontier](https://thenewstack.io/data-on-kubernetes-the-next-frontier) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Tracks the expansion of the 'Data on Kubernetes' (DoK) movement. Highlights how native operator progress and persistent storage plugins are enabling enterprise organizations to containerize databases, stream analytics, and run ML model pipelines directly on K8s clusters.
  - **(2022)** [cloud.google.com: To run or not to run a database on Kubernetes - What to consider](https://cloud.google.com/blog/products/databases/to-run-or-not-to-run-a-database-on-kubernetes-what-to-consider) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Google Cloud's decision matrix for running database structures on Kubernetes. Compares managed SaaS vs. native GKE container deployments, outlining networking, storage IOPS, recovery, and failover topologies.
  - **(2018)** [threadreaderapp.com:  Kelsey Hightower: "Kubernetes has made huge improvements in the ability to run stateful workloads including databases and message queues, but I still prefer not to run them on Kubernetes" 🌟](https://threadreaderapp.com/thread/963413508300812295.html) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kelsey Hightower's historical analysis on running stateful databases inside Kubernetes. While operator maturity has improved significantly, the core operational warning remains relevant: separating state from compute minimizes platform complexity and failure domain blast radius.
#### GitOps

  - **(2022)** [percona.com: MySQL on Kubernetes with GitOps 🌟](https://www.percona.com/blog/mysql-on-kubernetes-with-gitops) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Percona's technical case study on deploying MySQL clusters inside Kubernetes using GitOps pipelines. Connects ArgoCD or Flux workflows with declarative Percona Operators to automate database replication topologies.
#### Kubernetes Operators

  - **(2024)** [kubedb.com](https://kubedb.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical review of KubeDB, an operator platform for automating databases on Kubernetes. Highlights declarative management of clustering, scheduling backups, and schema updates across multiple database engines (PostgreSQL, MySQL, MongoDB).
#### MySQL Operators

  - **(2024)** [Moco](https://cybozu-go.github.io/moco) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduction to Cybozu's Moco, a highly resilient, modern Go-written MySQL operator for Kubernetes. Focuses on cluster setups, fast failover mechanics, and maintaining an extremely small operational footprint.
  - **(2021)** [tusacentral.com: MySQL on Kubernetes demystified](https://www.tusacentral.com/joomla/index.php/mysql-blogs/243-mysql-on-kubernetes-demystified) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demystifies MySQL container orchestration inside Kubernetes. Details local storage access, stateful set configuration, service discovery networks, and high-availability design constraints.
#### PostgreSQL HA

  - **(2023)** [devopscube.com: How to Deploy PostgreSQL Statefulset in Kubernetes With High Availability](https://devopscube.com/deploy-postgresql-statefulset) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comprehensive architectural guide to deploying a highly available PostgreSQL cluster on Kubernetes using standard StatefulSets. Covers headless services, persistent volume claims, replica configurations, and health probes.
#### PostgreSQL Operators

  - **(2023)** [blog.flant.com: Comparing Kubernetes operators for PostgreSQL](https://palark.com/blog/comparing-kubernetes-operators-for-postgresql) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive comparison of major Postgres operators for Kubernetes, including Crunchy Data, Zalando, and CloudNativePG. Evaluates failover metrics, backup reliability, upgrade safety, and overall complexity.
#### State Management

  - **(2023)** [xenonstack.com: Stateful and Stateless Applications Best Practices and Advantages](https://www.xenonstack.com/insights/stateful-and-stateless-applications) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational comparison of stateful vs. stateless application lifecycles. Discusses container orchestration challenges, dynamic volume provisioning, storage performance targets, and state management trends for scalable distributed networks.
### Enterprise Kubernetes

#### OpenShift Databases

  - **(2021)** [openshift.com: OpenShift, Databases and You: When to Put Containerized Database Workloads on OpenShift 🌟](https://www.redhat.com/en/blog/openshift-databases-and-you-when-to-put-containerized-database-workloads-on-openshift) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's structured criteria for running stateful production databases on OpenShift. Discusses storage tier performance, native high-availability architectures, and operator patterns to ensure robust containerized database operations.
### Infrastructure as Code

#### Terraform Database Ops

  - **(2022)** [cockroachlabs.com: Automated database operations with Terraform](https://www.cockroachlabs.com/blog/automate-database-ops-with-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates utilizing HashiCorp Terraform to automate CockroachDB configurations, database creation, user permissions, and deployment topologies. Standardizes declarative infrastructure-as-code patterns across production database deployments.
### PostgreSQL HA (1)

#### Kubernetes Operations

  - **(2022)** [How I've Set Up HA PostgreSQL on Kubernetes (powered by Patroni, a template for PostgreSQL HA)](https://disaev.me/p/how-i-have-set-up-ha-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hands-on implementation guide for deploying a high-availability Patroni-managed PostgreSQL cluster on Kubernetes. Configures persistent volumes, dynamic services, readiness probes, and etcd cluster coordination.
#### Orchestration

  - **(2026)** [==Patroni==](https://github.com/patroni/patroni) <span class='md-tag md-tag--info'>⭐ 8523</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e21c6e3e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 3 L 20 11 L 30 12 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-e21c6e3e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Industry-standard Python-driven template for high-availability PostgreSQL. Integrates with Distributed Consensus Stores (DCS) like etcd, Consul, or ZooKeeper to manage dynamic leader election, dynamic failover, and streaming replicas.
#### Zalando Stack

  - **(2026)** [==Zalando Postgres Operator==](https://github.com/zalando/postgres-operator) <span class='md-tag md-tag--info'>⭐ 5182</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-22392440" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 11 L 20 12 L 30 11 L 40 9 L 50 5" fill="none" stroke="url(#spark-grad-22392440)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Zalando's PostgreSQL Operator, which orchestrates highly available Spilo clusters on Kubernetes. Automates provisioning, scaling, master-failovers, offsite backups, and minor engine upgrades via declarative CRDs.
  - **(2025)** [==Spilo: HA PostgreSQL Clusters with Docker==](https://github.com/zalando/spilo) <span class='md-tag md-tag--info'>⭐ 1839</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2c312736" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 10 L 20 7 L 30 11 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-2c312736)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Spilo is Zalando's container image bundling PostgreSQL, Patroni, pgBackRest, and WAL-E/WAL-G. Built for mission-critical production reliability, it serves as the stable, standard database core for the Zalando Postgres Operator.
## Kubernetes Workloads

### CICD Pipelines

#### Database Migrations

  - **(2020)** [andrewlock.net: Running database migrations when deploying to Kubernetes 🌟](https://andrewlock.net/deploying-asp-net-core-applications-to-kubernetes-part-7-running-database-migrations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed deployment blueprint focusing on the execution of schema migrations within ASP.NET Core and relational databases inside Kubernetes. Critically compares using Kubernetes Jobs, Init Containers, and application bootstrap processes for migrations.
## Observability

### Distributed Storage

#### VictoriaMetrics

  - **(2024)** [VictoriaMetrics](https://victoriametrics.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official site of VictoriaMetrics, an extremely fast and cost-effective TSDB solution. Widely used as a drop-in replacement for Prometheus storage owing to high compression ratios and out-of-the-box cluster scalability.
## PostgreSQL (1)

### Alternative Paradigms

  - **(2022)** [blog.crunchydata.com: Devious SQL: Message Queuing Using Native PostgreSQL](https://www.crunchydata.com/blog/message-queuing-using-native-postgresql) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deconstructs patterns for building a robust message queue inside PostgreSQL. Leverages native SKIP LOCKED and SELECT FOR UPDATE syntax to process high-throughput transactional queues without external brokers.
### Application Architecture

  - **(2021)** [blog.crunchydata.com: Cut Out the Middle Tier: Generating JSON Directly from Postgres](https://www.crunchydata.com/blog/generating-json-directly-from-postgres) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates optimizing application architectures by generating JSON directly from PostgreSQL using built-in engine functions like row_to_json. Reduces serialization overhead in middleware services.
### Application Performance

  - **(2021)** [9 High-Performance Tips when using PostgreSQL with JPA and Hibernate](https://vladmihalcea.com/9-postgresql-high-performance-performance-tips) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A masterclass on optimizing PostgreSQL queries within JPA and Hibernate. Details batch inserts, query caching strategies, connection pool sizing, and avoiding N+1 select statement patterns.
### Database Architecture (1)

  - **(2021)** [percona.com: An Overview of Sharding in PostgreSQL and How it Relates to MongoDB’s](https://www.percona.com/blog/an-overview-of-sharding-in-postgresql-and-how-it-relates-to-mongodbs) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep architectural analysis contrasting PostgreSQL's declarative partitioning and foreign data wrapper sharding with MongoDB's native shard-key clustering, detailing query routing and execution tradeoffs.
## Relational Databases (1)

### Database Drivers

  - **(2020)** [thenewstack.io: Maria DB Gets Reactive with a Non-Blocking Connector for Java](https://thenewstack.io/maria-db-gets-reactive-with-a-non-blocking-connector-for-java) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores MariaDB's reactive Java driver. Details how non-blocking I/O operations and asynchronous connections improve database throughput in highly concurrent microservice runtimes.
## SQL

### ORM and Query Builders

#### Java Ecosystem

  - **(2026)** [blog.jooq.org](https://blog.jooq.org) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The premier engineering blog for the jOOQ framework. Explores advanced SQL query generation, type-safe persistence, optimizer bypasses, and JVM database integration paradigms.
## SQL Server

### DevOps

  - **(2022)** [devblogs.microsoft.com: DevOps for Azure SQL 🌟](https://devblogs.microsoft.com/azure-sql/devops-for-azure-sql) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical DevOps pipeline patterns for Azure SQL. Outlines dynamic deployment workflows using GitHub Actions and Azure DevOps to coordinate declarative state synchronizations matching app changes.
## Serverless Databases

### Resource Management

  - **(2023)** [thenewstack.io: How to Ensure Your Serverless Database Stays Serverless](https://thenewstack.io/how-to-ensure-your-serverless-database-stays-serverless) <span class='md-tag md-tag--warning'>[CONCEPTUAL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on preserving serverless paradigms at the database tier. Explores connection pooling, cold-start latency mitigation, dynamic compute scaling, and the integration of proxy layers to maintain seamless serverless workload support.
## Storage and Data

### Database Operators

#### Crunchy PostgreSQL

  - **(2023)** [Crunchy Data PostgreSQL Operator](https://nubenetes.com/crunchydata/) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Evaluates the Crunchy PostgreSQL Operator (PGO) which automates production-grade PostgreSQL deployments on Kubernetes. Features include automated high availability, pgBackRest-driven backup orchestration, connection pooling via pgBouncer, and deep monitoring metrics. A de facto standard solution for enterprises migrating critical relational engines into Kubernetes platforms.

---
💡 **Explore Related:** [Yaml](./yaml.md) | [Crunchydata](./crunchydata.md) | [NoSQL](./nosql.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

