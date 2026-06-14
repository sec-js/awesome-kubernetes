# AWS Architecture and Best Practices

!!! info "Architectural Context"
    Detailed reference for AWS Architecture and Best Practices in the context of Cloud Providers (Hyperscalers).

## Standard Reference

  - [The Truth About Downtime in the Cloud](http://cloud.netapp.com/blog/prepare-for-the-day-of-all-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [awstip.com: Increase Security and Efficiency with a 3-Tier Cloud Architecture](https://awstip.com/increase-security-and-efficiency-with-a-3-tier-cloud-architecture-bf5e835cd55a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [DZone: A Guide to Performance Challenges with AWS EC2: Part 1](https://blog.appdynamics.com/cloud/a-guide-to-performance-challenges-with-aws-ec2-part-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [foreseeti.com: How to become and stay AWS well architected in a smart way](https://foreseeti.com/how-to-become-and-stay-aws-well-architected-in-a-smart-way)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@buraktahtacioglu: AWS Well-Architected Framework — AWS Roadmap](https://medium.com/@buraktahtacioglu/aws-well-architected-framework-aws-roadmap-80aaa6ca7f53)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Infrastructure

### AWS

#### Best Practices

  - **(2014)** [AWS Tips I Wish I'd Known Before I Started (Feb 2014)](https://wblinks.com/notes/aws-tips-i-wish-id-known-before-i-started) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A collection of fundamental AWS operational constraints including early patterns in IAM, billing, and VPC configuration. Although dated, it outlines core architectural traps teams still solve using Control Tower.
#### Governance

  - **(2021)** [AWS Architecture Blog: Use templated answers to perform Well-Architected reviews at scale](https://aws.amazon.com/blogs/architecture/use-templated-answers-to-perform-well-architected-reviews-at-scale) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical review detailing templated governance answers to scale AWS Well-Architected reviews. Offers architects a mechanism to automate and standardise security compliance reviews across decentralized environments.
#### Legacy Systems

  - **(2022)** [cbui.dev: Every company has an "old" production AWS account](https://www.cbui.dev/every-company-has-an-old-production-aws-account) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Explores patterns for managing single legacy production accounts containing unmapped dependencies. Details modernization pathways using AWS Organizations and VPC peering strategies.
#### Security

  - **(2021)** [thenewstack.io: Avoid the 5 Most Common Amazon Web Services Misconfigurations in Build-Time](https://thenewstack.io/avoid-the-5-most-common-amazon-web-services-misconfigurations-in-build-time) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on build-time CloudFormation and Terraform configuration errors. Outlines practical strategies for shifting infrastructure security check operations left into standard CI/CD pipelines.
### FinOps

#### Cost Management

  - **(2015)** [AWS Cost Explorer Update – Access to EC2 Usage Data](https://aws.amazon.com/blogs/aws/aws-cost-explorer-update-access-to-ec2-usage-data) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes early programmatic access to granular EC2 metrics inside Cost Explorer. Provides foundational methodologies for early-stage cloud-native resource optimization and FinOps planning.
### FinOps and Cloud Optimization

#### Sustainability

  - **(2023)** [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An engineering guide to optimizing AWS compute architectures for sustainability. Explores Graviton migrations, automated container resizing, and target serverless setups to lower carbon emissions.
  - **(2023)** [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This second installment targets storage modernization. Details how to implement Amazon S3 Lifecycle configurations, S3 Intelligent-Tiering, and storage optimization practices.
### Infrastructure as Code

#### Compliance Auditing

  - **(2026)** [AWS Well-Architected IaC Analyzer](https://github.com/aws-samples/well-architected-iac-analyzer) <span class='md-tag md-tag--info'>⭐ 483</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An AWS-backed auditing analyzer designed to inspect CloudFormation and Terraform designs against the AWS Well-Architected standard. Evaluates infrastructure-as-code deployments for security vulnerabilities and reliability issues before runtime provisioning.
## Cloud Native

### AWS (1)

#### Governance (1)

##### AWS Organizations

  - **(2024)** [AWS Organizations: The Key to Managing Your Cloud Infrastructure Effectively](https://awsfundamentals.com/blog/aws-organizations-the-key-to-managing-your-cloud-infrastructure-effectively)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores core configuration benefits of AWS Organizations for multi-account governance. Highlights service control policies (SCPs), unified billing, and secure programmatic account instantiation using IaC.
## Cloud Platform

### AWS Infrastructure

#### Reference Architectures

  - **(2026)** [AWS Labs GitHub](https://github.com/awslabs) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — The central AWS Labs GitHub organization housing hundreds of active experimental projects, tooling integrations, and reference CDK blueprints. Live Grounding highlights this hub as a critical launchpad for emerging patterns in infrastructure-as-code and cloud automation. It provides platform engineering teams with robust, peer-reviewed building blocks for accelerated architecture design.
## Data Architecture

### Databases

#### Amazon Aurora

  - **(2015)** [InfoWorld Review – Amazon Aurora Rocks MySQL](https://aws.amazon.com/blogs/aws/infoworld-review-amazon-aurora-rocks-mysql) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical analysis validating Amazon Aurora's decoupled compute and storage architecture. In production contexts, it remains a de facto standard for high-throughput, low-latency relational engines.
## Enterprise Architecture

### Cloud Architecture Best Practices

#### API Design

  - **(2023)** [Architecture patterns for consuming private APIs cross-account](https://aws.amazon.com/pt/blogs/compute/architecture-patterns-for-consuming-private-apis-cross-account) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights architectural approaches for routing and consuming private APIs across different AWS accounts. Emphasizes security through AWS PrivateLink, Route 53, and Network Load Balancers.
#### AWS Well-Architected

  - **(2023)** [AWS Well Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official documentation framework outlining six fundamental cloud architectural pillars: operational excellence, security, reliability, performance, cost optimization, and sustainability.
  - **(2023)** [aws.amazon.com/well-architected-tool: AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Overview of AWS's native tool designed to assess cloud workloads. Integrates with the Well-Architected Framework to systematically audit infrastructure and highlight configuration risks.
  - **(2023)** [infoq.com: AWS Updates the Well-Architected Framework](https://www.infoq.com/news/2023/04/aws-well-architected-framework)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes key revisions to the AWS Well-Architected Framework. Reviews shifts in security baseline configurations, serverless deployment guidelines, and the sustainability assessment pillar.
#### Cloud Governance

  - **(2023)** [Strategies for consolidating AWS environments](https://aws.amazon.com/de/blogs/mt/strategies-for-consolidating-aws-environments) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details architectural strategies for consolidating multi-account AWS environments. Explores AWS Organizations setups, control tower governance, and billing unification across enterprise structures.
  - **(2023)** [Maintain visibility over the use of cloud architecture patterns](https://aws.amazon.com/blogs/architecture/maintain-visibility-over-the-use-of-cloud-architecture-patterns)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines frameworks and tools to track, map, and enforce specific cloud architecture patterns across decentralized developer teams, helping prevent systemic configuration drift.
#### Design Blueprints

  - **(2023)** [AWS application-architecture](http://www.conceptdraw.com/examples/application-architecture) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architecture drafting resource providing standard AWS application design templates, components, and layout blocks. Essential for mapping out multi-tier cloud services.
  - **(2023)** [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official blog portal showcasing cloud solutions, pattern guides, and engineering strategies written directly by AWS Systems Architects.
  - **(2023)** [AWS Official Blog](http://blogs.aws.amazon.com) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The master AWS news platform. Tracks every new feature rollout, managed service launch, operational update, and security announcement from AWS engineering groups.
#### Engineering Culture

  - **(2023)** [dev.to: How Well-Architected Enables Junior Engineers](https://dev.to/aws-builders/how-well-architected-enables-junior-engineers-24j)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines how the AWS Well-Architected Framework acts as an educational and operational safety net for junior engineers, establishing structured system design patterns across developer teams.
#### Multi-Region Architecture

  - **(2023)** [Creating a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of a multi-region deployment guide. Covers DNS failover routing with Route 53, cross-region VPC peering, compute distribution, and unified security controls across AWS regions.
  - **(2023)** [Creating a Multi-Region Application with AWS Services – Part 2, Data and Replication](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-2-data-and-replication) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part two focuses on database replication, global data consistency, storage syncing protocols, and handling split-brain scenarios in multi-region cloud infrastructures.
#### Production Case Studies

  - **(2023)** [This is My Architecture](https://aws.amazon.com/architecture/this-is-my-architecture)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS's premier video and article series showcasing production-grade architectural solutions. Focuses on design tradeoffs, performance strategies, and networking topologies of modern web applications.
### Cloud Governance (1)

#### Case Studies

  - **(2023)** [==github.com/ministryofjustice: Modernisation Platform - Architecture Decisions==](https://github.com/ministryofjustice/modernisation-platform/tree/main/architecture-decision-record) <span class='md-tag md-tag--info'>⭐ 724</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The public collection of Architecture Decision Records (ADRs) from the UK Ministry of Justice Modernisation Platform. This serves as a key reference for cloud governance, public sector IT standards, and clear decision documentation.
## Kubernetes and Platform Engineering

### Modernization Tools

#### Microservice Migration

  - **(2023)** [AWS App2Container: Migrate your Applications to Containers at Scale](https://aws.amazon.com/blogs/architecture/migrate-your-applications-to-containers-at-scale) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Introduces AWS App2Container, a tool that automates the migration of legacy .NET and Java web applications into containerized structures ready for deployment on Amazon ECS or EKS.
  - **(2023)** [Let’s Architect! Architecting microservices with containers](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-microservices-with-containers)  <span class='md-tag md-tag--info'>[LEGACY]</span> — A foundational guide for decoupling large legacy applications. Explores container hosting options on ECS and EKS, microservice discovery patterns, and inter-service security standards.
## Software Engineering

### Frontend Architecture

#### Design Patterns

  - **(2021)** [Clean Architecture on Frontend](https://bespoyasov.me/blog/clean-architecture-on-frontend) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Adapts Robert C. Martin's Clean Architecture principles to modern client-side frontend applications. Focuses on isolation of core business domains, UI frameworks, and data sources via explicit dependency inversion layers, simplifying testing and future framework transitions.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Azure](./azure.md)

