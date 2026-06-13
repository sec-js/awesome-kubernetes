# Crunchy Data PostgreSQL Operator

!!! info "Architectural Context"
    Detailed reference for Crunchy Data PostgreSQL Operator in the context of Data & Advanced Analytics.

## Standard Reference

  - [Kubernetes.io: Operator pattern](https://kubernetes.io/docs/concepts/extend-kubernetes/operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [crunchydata.com](https://www.crunchydata.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/CrunchyData](https://github.com/CrunchyData)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/CrunchyData/postgres-operator](https://github.com/CrunchyData/postgres-operator) <span class='md-tag md-tag--info'>⭐ 4406</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>
  - [Documentation: Crunchy Data Container Suite 🌟](https://access.crunchydata.com/documentation/crunchy-postgres-containers/latest)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: Deploying PostgreSQL on Kubernetes](https://www.slideshare.net/vyruss000/deploying-postgresql-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [slideshare.net: Operating PostgreSQL at Scale with Kubernetes](https://www.slideshare.net/jkatz05/operating-postgresql-at-scale-with-kubernetes-137132067)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Youtube: Demo of Crunchy Data Postgres Operator v1.0.0 (2017)](https://www.youtube.com/watch?v=HX10WWTRiTY)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Youtube: Crunchy PostgreSQL Operator for Kubernetes 3.4 Overview (2018)](https://www.youtube.com/watch?v=gaXlrlz7GVc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Youtube: OpenShift Meetup Tokyo #05 - Operator and Operator Lifecycle Manager' on OpenShift (2019, openshift 4.1)](https://www.youtube.com/watch?v=X4vuktlK0Tg)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Scaling PostgreSQL with Kubernetes Operators 🌟](https://opensource.com/article/19/2/scaling-postgresql-kubernetes-operators)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [thenewstack.io: Advanced Kubernetes Namespace Management with the PostgreSQL' Operator 🌟](https://thenewstack.io/advanced-kubernetes-namespace-management-with-the-postgresql-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [postgresql.org: Crunchy PostgreSQL Operator 4.5: Enhanced Monitoring, Custom' Annotations, PostgreSQL 13 🌟](https://www.postgresql.org/about/news/crunchy-postgresql-operator-45-enhanced-monitoring-custom-annotations-postgresql-13-2086)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: OCB: High Availability PostgreSQL and more on OpenShift - Jonathan' Katz (Crunchy Data) 🌟](https://www.youtube.com/watch?v=9jbR9lZuSU0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Install and use Crunchy PostgreSQLfor OpenShift operator for simple' todo app on OpenShift 🌟](https://www.youtube.com/watch?v=9wuUXi6Qbis&ab_channel=MichaelBornholdtNielsen)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: PostgreSQL HA and Kubernetes](https://dzone.com/articles/postgresql-ha-and-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Crunchy Data Developer Portal](https://www.crunchydata.com/developers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [The PostgreSQL Operator Installer with kubectl](https://access.crunchydata.com/documentation/postgres-operator/4.3.0/installation/postgres-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ref1](https://docs.openshift.com/container-platform/4.1/authentication/using-service-accounts-in-applications.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ref1](https://docs.openshift.com/container-platform/3.6/admin_guide/manage_scc.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ref1](https://access.crunchydata.com/documentation/postgres-operator/latest/operatorcli/pgo-overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [crunchy-pgadmin4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/container-specifications/crunchy-pgadmin4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pgAdmin 4](https://access.crunchydata.com/documentation/crunchy-postgres-containers/4.3.0/examples/administration/pgadmin4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ref3](https://dzone.com/articles/understanding-openshift-security-context-constrain)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Data Infrastructure

### Database Backups

#### Disaster Recovery

  - **(2021)** [blog.crunchydata.com: pgBackRest Point-In-Time Recovery Using Crunchy PostgreSQL Operator](https://www.crunchydata.com/blog/pgbackrest-point-in-time-recovery-using-crunchy-postgresql-operator) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed playbook for executing continuous point-in-time recovery (PITR) with pgBackRest inside Kubernetes. Demonstrates configuring WAL archiving processes and utilizing operator CRDs to restore databases to a granular microsecond timestamp.
#### Storage Backends

  - **(2021)** [blog.crunchydata.com: Announcing Google Cloud Storage (GCS) Support for pgBackRest](https://www.crunchydata.com/blog/announcing-google-cloud-storage-gcs-support-for-pgbackrest)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces native Google Cloud Storage (GCS) driver support within pgBackRest integration. Explores the architectural advantage of streaming database backups directly to Google Cloud bucket infrastructures, skipping intermediate storage layers to perform high-efficiency Point-In-Time Recovery (PITR).
### PostgreSQL

#### Connection Pooling

  - **(2021)** [blog.crunchydata.com: Your Guide to Connection Management in Postgres 🌟](https://www.crunchydata.com/blog/your-guide-to-connection-management-in-postgres)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An in-depth guide on handling highly concurrent microservice application loads using PgBouncer. Compares transaction vs. session pooling mechanisms and defines cluster sizing guidelines required to protect underlying PostgreSQL memory structures from request overload.
#### Containerized Applications

  - **(2021)** [blog.crunchydata.com: Announcing Postgres Container Apps: Easy Deploy Postgres Apps](https://www.crunchydata.com/blog/announcing-postgres-container-apps-easy-deploy-postgres-apps)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Crunchy Container Apps, a design pattern to quickly run database-adjacent workflows inside lightweight container structures. Intended for development speed, it bundles testing, local databases, and migration utilities efficiently.
#### Database Replication

  - **(2021)** [blog.crunchydata.com: Active-Active PostgreSQL Federation on Kubernetes](https://www.crunchydata.com/blog/active-active-postgres-federation-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines active-active multi-master federation mechanisms on Kubernetes using logical replication. Addresses the inherent latency penalties, conflict resolution complexities, and split-brain risks that system architects must mitigate when building distributed relational topologies.
#### Database Upgrades

  - **(2021)** [blog.crunchydata.com: PostgreSQL 14 on Kubernetes (with examples!)](https://www.crunchydata.com/blog/postgresql-14-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walks through deploying and running PostgreSQL 14 workloads inside Kubernetes. Showcases updated query planning configurations, modern transactional scalability limits, and specific operational upgrades built into the Operator CRD.
#### Docker Swarm Deployment

  - **(2019)** [info.crunchydata.com: An Easy Recipe for Creating a PostgreSQL Cluster with Docker Swarm](https://www.crunchydata.com/blog/an-easy-recipe-for-creating-a-postgresql-cluster-with-docker-swarm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Outlines an automated recipe for deploying a highly available PostgreSQL cluster within a Docker Swarm orchestrator environment. While historically useful for simpler setups, live grounding shows modern production standardizations have aggressively shifted to declarative Kubernetes Operators due to robust control plane capabilities.
#### Performance Tuning

  - **(2020)** [blog.crunchydata.com: Query Optimization in Postgres with pg_stat_statements](https://www.crunchydata.com/blog/tentative-smarter-query-optimization-in-postgres-starts-with-pg_stat_statements)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide on configuring and parsing performance telemetry with the `pg_stat_statements` extension. Shows how to track query performance patterns, isolate slow statements, and resolve indexing shortfalls in Postgres instances running on containerized platforms.
### PostgreSQL on Kubernetes

#### GKE Deployments

  - **(2020)** [info.crunchydata.com: Deploying the PostgreSQL Operator on GKE](https://www.crunchydata.com/blog/install-postgres-operator-kubernetes-on-gke-ansible)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walks through deploying the Crunchy PostgreSQL Operator on Google Kubernetes Engine (GKE) leveraging Ansible automation. Demonstrates handling enterprise stateful requirements on managed Kubernetes, including GKE dynamic persistent volume provisioning and optimal storage class definitions.
#### Multi-Cluster

  - **(2021)** [blog.crunchydata.com: Multi-Kubernetes Cluster PostgreSQL Deployments](https://www.crunchydata.com/blog/multi-kubernetes-cluster-postgresql-deployments) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores building high-availability multi-cluster PostgreSQL topologies spanning distinct physical zones. Discusses network transit setup, Cross-Cluster backup syncs, and leveraging pgBackRest architectures to implement reliable regional disaster recovery frameworks.
#### Operator Releases

  - **(2021)** [blog.crunchydata.com: Crunchy Postgres Operator 4.6.0 🌟](https://www.crunchydata.com/blog/crunchy-postgres-operator-4.6.0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents the features of Crunchy Postgres Operator 4.6.0, highlighting upgrades to backup engines, custom sidecars, and integration monitoring. Live grounding notes that while 4.6.0 was a reliable milestone, users should prioritize modern 5.x releases featuring fully declarative control planes.
  - **(2021)** [blog.crunchydata.com: Next Generation Crunchy Postgres for Kubernetes 5.0 Released](https://www.crunchydata.com/news/next-generation-crunchy-postgres-for-kubernetes-released) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Crunchy Postgres Operator 5.0, a complete declarative redesign. By aligning with native Kubernetes API controllers and eliminating external CLI utilities like 'pgo', it significantly simplifies gitops compatibility and improves operational control over enterprise PG clusters.
## Databases

### Database Migration

#### Oracle to PostgreSQL

  - **(2021)** [info.crunchydata.com: Migrating from Oracle to PostgreSQL: Tips and Tricks](https://www.crunchydata.com/blog/migrating-from-oracle-to-postgresql-questions-and-considerations) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Addresses strategic planning, dialect disparities, and type-conversion pitfalls experienced by DBAs transitioning massive enterprise relational datasets from legacy Oracle instances to open-source PostgreSQL.
  - **(2021)** [info.crunchydata.com: Setup ora2pg for Oracle to Postgres Migration](https://www.crunchydata.com/blog/setup-ora2pg-for-oracle-to-postgres-migration) <span class='md-tag md-tag--warning'>[PERL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step setup guide for configuring ora2pg. This open-source migration tool extracts schemas, packages, triggers, and table definitions from Oracle database catalogs and rewrites them into clean, loadable PostgreSQL sql structures.
### Kubernetes Operators

#### OpenShift Deployments

  - **(2020)** [info.crunchydata.com: Getting Started with PostgreSQL Operator 4.3 in OpenShift](https://www.crunchydata.com/blog/getting-started-with-postgresql-operator-4.3-in-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identical to index 40. Outlines security profiles and integration configurations required to securely configure and run the v4.3 operator on OpenShift's container cluster fabric.
#### Postgres Operator v4

  - **(2020)** [info.crunchydata.com: Crunchy PostgreSQL for Kubernetes 4.3 Released](https://www.crunchydata.com/news/crunchy-postgresql-for-kuberenetes-4.3) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Release announcement for Crunchy PostgreSQL Operator v4.3, introducing pgBackRest multi-repository backing and enhanced security. Users should migrate to Operator v5+ to align with modern Kubernetes APIs.
  - **(2019)** [crunchydata blog: What's New in Crunchy PostgreSQL Operator 4.0](https://www.crunchydata.com/blog/crunchy-postgres-kubernetes-operator-4.0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Architectural announcement of Crunchy PostgreSQL Operator v4.0. Highlights performance gains, dynamic provisioning schemas, and initial scale-out capabilities. Users in 2026 should note that Crunchy Operator has evolved to v5+, making v4 patterns legacy.
#### Storage Engine Integration

  - **(2021)** [info.crunchydata.com: Using the PostgreSQL Operator with Rook Ceph Storage](https://www.crunchydata.com/blog/crunchy-postgresql-operator-with-rook-ceph-storage) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates configuring the Crunchy PostgreSQL Operator to dynamically claim storage resources managed by a Rook-orchestrated Ceph storage cluster. Harnesses block storage pools to achieve robust, distributed replication properties at the persistent volume layer.
### PostgreSQL (1)

#### Application Integration

  - **(2022)** [info.crunchydata.com: Composite Primary Keys, PostgreSQL and Django](https://www.crunchydata.com/blog/composite-primary-keys-postgresql-and-django) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Evaluates architectural challenges faced when integrating Django's ORM layer with legacy or complex multi-column composite primary key schemas designed on enterprise PostgreSQL tables.
#### Backup and Recovery

  - **(2022)** [info.crunchydata.com: Scheduled PostgreSQL Backups and Retention Policies with Kubernetes](https://www.crunchydata.com/blog/schedule-postgresql-backups-and-retention-with-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical deep-dive on managing database recovery points. Demonstrates automating pgBackRest-driven scheduled full and incremental backups targeting S3-compliant storage engines with custom retention periods.
  - **(2022)** [info.crunchydata.com: pgBackRest - Performing Backups on a Standby Cluster](https://www.crunchydata.com/blog/pgbackrest-performing-backups-on-a-standby-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Shows how to perform resource-intensive backup operations directly against standby clusters instead of primary nodes using pgBackRest. Eliminates overhead and maintains optimal performance levels on write-heavy primary database engines.
#### CLI and Tooling

  - **(2021)** [info.crunchydata.com: Quickly Document Your Postgres Database Using psql Meta-Commands](https://www.crunchydata.com/blog/d-meta) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Quick operational guide focusing on using psql meta-commands (like \d, \dt, and \di) to parse, discover, and document active database schemas, tables, and relationships via standard terminal interactions.
#### Data Consistency

  - **(2021)** [info.crunchydata.com: Guard Against Transaction Loss with PostgreSQL Synchronous Replication](https://www.crunchydata.com/blog/synchronous-replication-in-the-postgresql-operator-for-kubernetes-guarding-against-transactions-loss) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the trade-offs between write latency and zero-data-loss guarantees. Configures the Crunchy PostgreSQL Operator for synchronous replication topologies to protect transaction logs from host crashes.
#### Data Ingestion

  - **(2022)** [info.crunchydata.com: Fast CSV and JSON Ingestion in PostgreSQL with COPY](https://www.crunchydata.com/blog/fast-csv-and-json-ingestion-in-postgresql-with-copy) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights performance execution structures utilizing the PostgreSQL native `COPY` command to achieve optimal ingestion speeds for parsing bulk-formatted CSV and unstructured JSON data payloads.
#### Database Administration

  - **(2021)** [info.crunchydata.com: Deploy pgAdmin4 with PostgreSQL on Kubernetes](https://www.crunchydata.com/blog/deploy-pgadmin4-with-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical tutorial covering the setup and deployment of a web-based pgAdmin4 console side-by-side with running PostgreSQL StatefulSets on Kubernetes, ensuring secure local ingress routing.
#### Database Observability

  - **(2022)** [info.crunchydata.com: How to Setup PostgreSQL Monitoring in Kubernetes](https://www.crunchydata.com/blog/setup-postgresql-monitoring-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical orchestration walkthrough detailing Prometheus and Grafana instrumentation configurations optimized for monitoring multi-tenant Kubernetes PostgreSQL StatefulSet resources.
  - **(2022)** [info.crunchydata.com: Monitoring PostgreSQL clusters in kubernetes](https://www.crunchydata.com/blog/monitoring-postgresql-clusters-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines operational observability strategies for containerized PostgreSQL engines. Integrates Prometheus metric scraping with pg_exporter and custom dashboards to surface critical transaction rate, replication lag, and disk utilization graphs.
  - **(2022)** [info.crunchydata.com: PostgreSQL Monitoring for Application Developers: The DBA Fundamentals](https://www.crunchydata.com/blog/postgresql-monitoring-for-application-developers-dba-stats) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Essential monitoring playbook tailored for developers. Bridges abstract database layers with OS reality, helping analyze connection pool sizes, query performance bottlenecks, and active transactions using native catalog system tables.
  - **(2019)** [info.crunchydata.com: Introducing the Postgres Prometheus Adapter](https://www.crunchydata.com/blog/using-postgres-to-back-prometheus-for-your-postgresql-monitoring-1) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Overview of utilizing the timescale-based Postgres Prometheus adapter as a long-term data store backing Prometheus telemetry. While valuable, current architectures typically favor native OpenTelemetry or direct Cortex/Thanos integrations.
#### High Availability

  - **(2023)** [info.crunchydata.com: Deploying Active-Active PostgreSQL on Kubernetes](https://www.crunchydata.com/blog/active-active-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identical to index 27. Explains logical multi-node replication considerations, performance bounds, and conflict resolution schemas essential for cross-region, active-active PostgreSQL databases inside Kubernetes.
  - **(2023)** [info.crunchydata.com: Deploy High-Availability PostgreSQL Clusters on Kubernetes by Example](https://www.crunchydata.com/blog/deploy-high-availability-postgresql-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed blueprint utilizing Patroni-driven clustering to guarantee consensus, automatic failovers, and replica replication consistency within StatefulSet designs deployed inside Kubernetes.
#### Performance Tuning (1)

  - **(2023)** [info.crunchydata.com: Tuning Your Postgres Database for High Write Loads](https://www.crunchydata.com/blog/tuning-your-postgres-database-for-high-write-loads) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical manual on tuning PostgreSQL configuration flags (shared_buffers, max_wal_size, work_mem) to maximize write throughput performance on heavy transaction-processing clusters deployed within dynamic Kubernetes limits.
## Enterprise Platforms

### OpenShift Integration

#### PostgreSQL Operators

  - **(2019)** [Crunchy PostgreSQL and Openshift](https://www.redhat.com/en/blog/leveraging-the-crunchy-postgresql)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the operational integration of Crunchy PostgreSQL Operators within Red Hat OpenShift. Discusses automated storage scheduling, multi-tenancy constraints, and passing strict enterprise certification scans.
### OpenShift Security

#### Security Context Constraints

  - **(2019)** [ref1](https://www.redhat.com/en/blog/understanding-service-accounts-sccs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep dive into Security Context Constraints (SCC) and Service Accounts inside OpenShift clusters. Explains container security profiles, uid-range allocations, and custom SCC assignments required to safely run stateful engines like PostgreSQL.
## GitOps

### Declarative Infrastructure

#### PostgreSQL Automation

  - **(2021)** [info.crunchydata.com: Using GitOps to Self-Manage Postgres in Kubernetes 🌟](https://www.crunchydata.com/blog/gitops-postgres-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes managing database lifecycles inside Kubernetes using GitOps patterns with tools like Argo CD and Flux. This method enables declarative management of Crunchy Postgres Custom Resources (CRDs) to systematically coordinate scheme updates and database settings through version control.
### Kubernetes Packaging

#### Helm and Argo CD

  - **(2021)** [blog.crunchydata.com: Helm, GitOps and the Postgres Operator](https://www.crunchydata.com/blog/gitops-postgres-kubernetes-helm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details structural integration patterns combining Helm chart packaging with GitOps delivery cycles. Focuses on orchestrating Helm-wrapped Postgres Operator CRDs via Argo CD, offering a template-driven mechanism to enforce policy standards across fleet-wide deployments.
## Orchestration

### Kubernetes Bootstrap

#### Bare-Metal Deployments

  - **(2021)** [blog.crunchydata.com: Kubernetes + Postgres Cluster From Scratch on Rocky 8](https://www.crunchydata.com/blog/kube-cluster-from-scratch-on-rocky-8) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Duplicate publication detailing network engineering, CRI integration, SELinux enforcement, and kernel tuning modifications required on Rocky Linux 8 nodes hosting transactional Postgres instances.
### Kubernetes Scheduling

#### Stateful Pod Placement

  - **(2020)** [blog.crunchydata.com: Kubernetes Pod Tolerations and Postgres Deployment Strategies 🌟](https://www.crunchydata.com/blog/kubernetes-pod-tolerations-and-postgresql-deployment-strategies) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identical publication detailing the implementation of pod tolerations for database clusters. Explains how to separate mission-critical Postgres pods from general application microservices using node affinities to guarantee high IOPS disk structures and deterministic memory pools.
## Resources

### Developer Experience

#### Documentation Hub

  - **(2021)** [Announcing the Crunchy Data Developer Portal](https://www.crunchydata.com/blog/announcing-the-crunchy-data-developer-portal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Launches the Crunchy Developer Portal, offering curated documentation, interactive tutorials, and code samples. It focuses on accelerating developer adoption of advanced features like PostgreSQL JSONB schemas, GIS data modeling, and performance tuning.
## Security

### Transport Layer Security

#### Certificate Management

  - **(2021)** [blog.crunchydata.com: Using Cert Manager to Deploy TLS for Postgres on Kubernetes](https://www.crunchydata.com/blog/using-cert-manager-to-deploy-tls-for-postgres-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Covers automating TLS certificate provisioning and rotation on Kubernetes using CNCF cert-manager. Explains how to configure cert-manager Issuers to issue certificates directly consumed by Postgres Operator pods to maintain continuous secure database channels.
#### Database Encryption

  - **(2020)** [blog.crunchydata.com: Deploy PostgreSQL With TLS in Kubernetes](https://www.crunchydata.com/blog/set-up-tls-for-postgresql-in-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Establishes a security blueprint for setting up mutual TLS (mTLS) configurations on PostgreSQL within Kubernetes. Explains generation of trust stores, server certificates, and target secrets, emphasizing standard patterns to restrict client connections to verified TLS certificates.
## Storage

### Kubernetes Storage

#### Dynamic Volume Resizing

  - **(2021)** [blog.crunchydata.com: Can't Resize your Postgres Kubernetes Volume? No Problem!](https://www.crunchydata.com/blog/resize-postgres-kubernetes-volume-instance-sets) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores recovery strategies for cloud storage providers that do not support online volume expansion. Demonstrates dynamic cluster volume migration by scaling new stateful replica sets with larger PVC capacities and performing failovers via replication.

---
💡 **Explore Related:** [Databases](./databases.md) | [Yaml](./yaml.md) | [Message Queue](./message-queue.md)

