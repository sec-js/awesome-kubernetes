---
description: "Curated, AI-ranked AWS Databases resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Architectural Foundations)."
---
# AWS RDS Databases

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-databases/).

!!! info "Architectural Context"
    Detailed reference for AWS RDS Databases in the context of Architectural Foundations.

## Cloud Infrastructure

### AWS Databases

#### Amazon Aurora

  - [Introducing the Aurora Storage Engine](https://aws.amazon.com/blogs/database/introducing-the-aurora-storage-engine) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An architectural deep-dive into the specialized, log-structured distributed storage engine of Amazon Aurora. Details how it decouples computing from database storage, replicating blocks six ways across three availability zones.
#### Amazon RDS

  - **(2026)** [==Working with PostgreSQL, MySQL, and MariaDB Read Replicas - Amazon==](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Exhaustive official guide detailing the design, limits, and monitoring of read-replicas for open-source engines in AWS RDS. Covers cross-region replication strategies and promoting a replica to master during failovers.
  - **(2026)** [==Working with an Amazon RDS DB Instance in a VPC==](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The foundational AWS RDS VPC networking architecture reference. Analyzes subnet group designations, public versus private access configurations, and network isolation topologies for secure DB hosting.
### Databases

#### NoSQL

  - [Let’s Architect! Architecting with Amazon DynamoDB](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-with-amazon-dynamodb) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Curator Insight presents an architectural masterclass on schema design and partitioning in Amazon DynamoDB. Live Grounding verifies the recommendations cover single-table design, global secondary indexes (GSIs), and write-sharding strategies. It is an indispensable guide for engineers building highly scalable, low-latency microservices.
#### Serverless Architecture

  - [Amazon RDS Proxy – Now Generally Available](https://aws.amazon.com/es/blogs/aws/amazon-rds-proxy-now-generally-available) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight presents Amazon RDS Proxy as a managed solution to handle high database connection concurrency. Live Grounding validates that RDS Proxy multiplexes connections, bypassing the performance degradation caused by high serverless (AWS Lambda) spin-up events. A critical integration pattern for cloud-native microservices. [SPANISH CONTENT]
## Cloud Native

### Kubernetes Operators

#### Managed Databases

  - [itnext.io: Manage Redis on AWS from Kubernetes](https://itnext.io/manage-redis-on-aws-from-kubernetes-eeadba7eb889) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight describes how to manage AWS ElastiCache for Redis directly from Kubernetes. Live Grounding highlights using AWS Controllers for Kubernetes (ACK) or Crossplane to define managed Redis instances as custom resources (CRDs). This unifies stateful cloud infrastructure management within standard GitOps workflows.

---
💡 **Explore Related:** [Git](./git.md) | [Other Awesome Lists](./other-awesome-lists.md) | [AWS Tools Scripts](./aws-tools-scripts.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

