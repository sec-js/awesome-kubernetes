# AWS New Features

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-newfeatures/).

!!! info "Architectural Context"
    Detailed reference for AWS New Features in the context of Cloud Providers (Hyperscalers).

## Table of Contents

1. [Application Integration](#application-integration)
  - [Serverless Orchestration](#serverless-orchestration)
    - [Step Functions](#step-functions)
1. [Cloud Infrastructure](#cloud-infrastructure)
  - [AWS](#aws)
    - [Container Orchestration](#container-orchestration)
    - [Serverless](#serverless)
  - [Container Orchestration](#container-orchestration-1)
    - [ECS Deployments](#ecs-deployments)
    - [EKS Windows](#eks-windows)
    - [Storage Integration](#storage-integration)
  - [Messaging](#messaging)
    - [Event-Driven](#event-driven)
  - [Networking](#networking)
    - [Load Balancing](#load-balancing)
  - [Security and Service Mesh](#security-and-service-mesh)
    - [HashiCorp HCP](#hashicorp-hcp)
  - [Serverless](#serverless-1)
    - [Compute](#compute)
    - [Developer Tooling](#developer-tooling)
1. [Containers](#containers)
  - [Kubernetes](#kubernetes)
    - [EKS Console](#eks-console)
    - [EKS Networking](#eks-networking)
    - [EKS Security](#eks-security)
  - [Market Analysis](#market-analysis)
    - [ReInvent Announcements](#reinvent-announcements)
1. [Data and Analytics](#data-and-analytics)
  - [Data Streaming](#data-streaming)
    - [Kinesis](#kinesis)
1. [Database](#database)
  - [RDS Proxy](#rds-proxy)
    - [Networking](#networking-1)
1. [Observability](#observability)
  - [Grafana](#grafana)
    - [Managed Visualization](#managed-visualization)
  - [OpenTelemetry](#opentelemetry)
    - [Distributed Tracing](#distributed-tracing)
  - [Prometheus](#prometheus)
    - [Managed Container Monitoring](#managed-container-monitoring)

## Application Integration

### Serverless Orchestration

#### Step Functions

  - **(2021)** [==infoq.com: AWS Introduces a New Workflow Studio for AWS Step Functions==](https://www.infoq.com/news/2021/06/step-functions-workflow-studio) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A visual, low-code workflow designer that simplifies building distributed state machines on AWS. It allows developers to drag, drop, and configure states, mapping state transitions and payloads directly to downstream AWS services. This visual paradigm significantly accelerates development cycles for complex microservices orchestrations while generating ASL (Amazon States Language) behind the scenes.
  - **(2021)** [==Now — AWS Step Functions Supports 200 AWS Services To Enable Easier Workflow Automation==](https://aws.amazon.com/blogs/aws/now-aws-step-functions-supports-200-aws-services-to-enable-easier-workflow-automation) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Dramatically expands the capabilities of AWS Step Functions by offering direct SDK integration with over 200 AWS services and over 9,000 API actions. This architecture minimizes or completely eliminates custom 'glue' Lambda functions whose sole purpose was calling AWS APIs. It simplifies state machine engineering, reducing latency, maintenance costs, and execution failure risks.
  - **(2021)** [**xataka.com: Hasta AWS se pasa al low-code: Workflow Studio es su primera herramienta de desarrollo de bajo código**](https://www.xataka.com/pro/aws-se-pasa-al-low-code-workflow-studio-su-primera-herramienta-desarrollo-codigo) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Un análisis en español sobre Workflow Studio para AWS Step Functions, detallando cómo la interfaz visual democratiza el diseño de arquitecturas serverless de bajo código (low-code). Permite a desarrolladores y analistas diagramar flujos lógicos, interactuando con otros servicios de AWS de manera intuitiva y reduciendo la complejidad del código.
## Cloud Infrastructure

### AWS

#### Container Orchestration

  - **(2015)** [**EC2 Container Service Update – Container Registry, ECS CLI, AZ-Aware Scheduling, and More**](https://aws.amazon.com/blogs/aws/ec2-container-service-update-container-registry-ecs-cli-az-aware-scheduling-and-more) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Milestone feature updates outlining the inception of Amazon Elastic Container Registry (ECR), native ECS CLI utilities, and multi-AZ application container scheduler integrations.
#### Serverless

  - **(2015)** [==AWS Lambda Update – Python, VPC, Increased Function Duration, Scheduling, and More==](https://aws.amazon.com/blogs/aws/aws-lambda-update-python-vpc-increased-function-duration-scheduling-and-more) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Strategic release notes highlighting early serverless evolutions: introducing Python runtime environments, VPC integration paths, dynamic event scheduling, and longer execution timeout periods.
### Container Orchestration (1)

#### ECS Deployments

  - **(2022)** [Amazon ECS now integrates with Amazon CloudWatch alarms to improve safety for deployments](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-ecs-cloudwatch-alarms-safety-deployments) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon ECS integrated natively with CloudWatch alarms to implement automated deployment rollbacks. If custom indicators (like HTTP 5xx errors) cross alarm thresholds during a rolling update, ECS automatically rolls back the task definitions to the last known stable state.
#### EKS Windows

  - **(2022)** [Amazon EKS launches automated provisioning and lifecycle management for Windows containers](https://aws.amazon.com/about-aws/whats-new/2022/12/amazon-eks-automated-provisioning-lifecycle-management-windows-containers) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon EKS automated the deployment and lifecycle management of Windows container nodes. It simplifies AMI updates, security patching, and scaling operations for Windows-based workloads on Kubernetes, aligning them with traditional Linux container management patterns.
#### Storage Integration

  - **(2024)** [Amazon ECS and AWS Fargate now integrate with Amazon EBS](https://aws.amazon.com/about-aws/whats-new/2024/01/amazon-ecs-fargate-integrate-ebs) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon ECS and AWS Fargate introduced native integration with Amazon EBS volumes. This lets serverless container deployments mount high-performance block storage dynamically, accommodating data-intensive file-processing workloads.
### Messaging

#### Event-Driven

  - **(2022)** [Amazon SNS increases the default quota for subscription filter policies by 50x to 10,000 per account](https://aws.amazon.com/about-aws/whats-new/2022/11/amazon-sns-increases-default-quota-subscription-filter-policies-account) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Amazon SNS increased the default subscription filter policy limit 50-fold to 10,000 per account. This enhancement permits highly granular filtering configurations within event-driven architectures, eliminating the need to deploy complex dispatch microservices to parse message payloads.
### Networking

#### Load Balancing

  - **(2021)** [==Application Load Balancer now enables AWS PrivateLink and static IP addresses by direct integration with Network Load Balancer==](https://aws.amazon.com/about-aws/whats-new/2021/09/application-load-balancer-aws-privatelink-static-ip-addresses-network-load-balancer) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces direct, native integration between Application Load Balancers (ALB) and Network Load Balancers (NLB), enabling ALBs to leverage static IP addresses and register with AWS PrivateLink. This native bridge removes the complex AWS Lambda-based IP-sync workarounds. It allows organizations to expose Layer 7 HTTP/HTTPS routing routes securely over private, non-routable VPC endpoints.
### Security and Service Mesh

#### HashiCorp HCP

  - **(2021)** [**thenewstack.io: HashiCorp Adds Consul and Vault to Cloud Platform for AWS**](https://thenewstack.io/hashicorp-adds-consul-and-vault-to-cloud-platform-for-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Launches fully managed Consul and Vault offerings on the HashiCorp Cloud Platform (HCP) integrated with AWS. This allows engineering teams to leverage secure secret storage and high-performance service mesh patterns without operational cluster overhead. Architecturally, it integrates seamlessly into AWS VPC routing and transit gateway topologies.
### Serverless (1)

#### Compute

  - **(2022)** [AWS Lambda Now Supports Up to 10 GB Ephemeral Storage](https://aws.amazon.com/blogs/aws/aws-lambda-now-supports-up-to-10-gb-ephemeral-storage) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS Lambda's configuration options permit allocating up to 10 GB of ephemeral /tmp storage, up from the previous 512 MB limit. This architectural enhancement enables serverless executions to process larger datasets, run machine learning inference, and perform intensive ETL operations directly within memory-backed local storage, significantly expanding the viability of serverless data pipelines.
#### Developer Tooling

  - **(2023)** [AWS SAM CLI introduces ‘sam list’ command to inspect AWS SAM resources](https://aws.amazon.com/about-aws/whats-new/2023/02/aws-sam-cli-sam-list-command-inspect-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS SAM CLI introduced the 'sam list' command to improve local diagnostics for serverless stacks. This tool displays resource endpoints, IAM roles, and stack states directly within the terminal, streamlining deployment workflows.
## Containers

### Kubernetes

#### EKS Console

  - **(2021)** [**Visualize all your Kubernetes clusters in one place with Amazon EKS Connector, now generally available**](https://aws.amazon.com/about-aws/whats-new/2021/11/visualize-kubernetes-clusters-one-place-amazon-eks-connector-generally-available) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Enables registering and visualizing any Kubernetes cluster—on-premises, on EC2, or other cloud providers—directly inside the AWS EKS console. It acts as an outbound agent, linking remote clusters safely to AWS IAM and AWS Console views. It offers a single-pane-of-glass platform to observe multi-cloud and hybrid Kubernetes estates.
#### EKS Networking

  - **(2021)** [==Amazon VPC CNI plugin increases pods per node limits==](https://aws.amazon.com/about-aws/whats-new/2021/07/amazon-vpc-cni-plugin-increases-pods-per-node-limits) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces Prefix Delegation in the AWS VPC CNI, multiplying the number of pods allocatable per node. By assigning /28 IPv4 prefixes to network interfaces instead of single secondary IPs, small-to-medium EC2 instances can support significantly higher container densities. This architecture directly addresses the IP exhaustion problem in enterprise Kubernetes deployments on AWS.
#### EKS Security

  - **(2021)** [==Amazon EKS clusters now support user authentication with OIDC compatible identity providers==](https://aws.amazon.com/about-aws/whats-new/2021/02/amazon-eks-clusters-support-user-authentication-oidc-compatible-identity-providers) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Enables EKS clusters to utilize external OpenID Connect (OIDC) compatible identity providers for user authentication. This decouples Kubernetes RBAC from direct IAM identity mappings, allowing developers to leverage existing SSO solutions like Okta or Keycloak. It simplifies security governance by maintaining enterprise identity standards at the cluster API level.
### Market Analysis

#### ReInvent Announcements

  - **(2021)** [**forbes.com: AWS re:Invent - A Roundup Of Container Services Announcements**](https://www.forbes.com/sites/janakirammsv/2021/12/03/aws-reinventa-roundup-of-container-services-announcements) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Synthesizes containerization announcements from re:Invent 2021, highlighting Karpenter, EKS Anywhere, and ECS Anywhere expansion. This analysis emphasizes AWS's push to support hybrid and multi-cloud Kubernetes deployments. It details how Karpenter challenges standard Cluster Autoscaler architectures with direct, fast provisioning of right-sized EC2 instances.
## Data and Analytics

### Data Streaming

#### Kinesis

  - **(2021)** [==infoq.com: AWS Launches Amazon Kinesis Data Streams On-Demand==](https://www.infoq.com/news/2021/12/kinesis-data-streams-ondemand) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces a serverless, on-demand capacity mode for Kinesis Data Streams, automatically scaling write and read throughput to match unpredictable traffic patterns. This model eliminates the requirement for shard planning, capacity monitoring, and custom-scaling scripts. Architecturally, it makes streaming pipelines easier to operate while optimizing costs for variable workloads.
## Database

### RDS Proxy

#### Networking (1)

  - **(2021)** [**Amazon RDS Proxy can now be created in a shared Virtual Private Cloud (VPC)**](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-rds-proxy-created-shared-virtual-private-cloud-vpc) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Extends Amazon RDS Proxy capabilities to shared VPCs (Resource Access Manager environments), allowing centralized application environments to pool and multiplex database connections across multiple AWS accounts. By managing highly volatile database connection limits from serverless microservices, it enhances application performance and resilience. Architecturally, it decouples the database infrastructure layer from consumer VPC microservices.
## Observability

### Grafana

#### Managed Visualization

  - **(2021)** [**Amazon Managed Service for Grafana (AMG) preview updated with new capabilities**](https://aws.amazon.com/blogs/mt/amazon-managed-service-for-grafana-amg-preview-updated-with-new-capabilities) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Outlines preview enhancements to AMG, incorporating support for Grafana Enterprise upgrades, security posture controls, and direct data source connectivity (Prometheus, CloudWatch, OpenSearch). This update automates visualization scaling and secures connection configurations. It forms a central visualization plane across AWS-managed monitoring services.
### OpenTelemetry

#### Distributed Tracing

  - **(2021)** [==New for AWS Distro for OpenTelemetry – Tracing Support is Now Generally Available==](https://aws.amazon.com/blogs/aws/new-for-aws-distro-for-opentelemetry-tracing-support-is-now-generally-available) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Generally available, AWS-supported distribution of the CNCF OpenTelemetry standards, specifically optimized for application tracing. It simplifies collecting metadata and correlates application traces across containerized (EKS, ECS) and serverless (Lambda) stacks. It seamlessly forwards telemetry to AWS X-Ray, Amazon OpenSearch, and partner SaaS platforms, eliminating vendor lock-in.
### Prometheus

#### Managed Container Monitoring

  - **(2021)** [==siliconangle.com: Amazon debuts fully managed, Prometheus-based container monitoring service==](https://siliconangle.com/2021/09/29/amazon-debuts-fully-managed-prometheus-based-container-monitoring-service) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Launches a fully managed, Prometheus-compatible monitoring service designed to ingest, store, and query operational metrics from Kubernetes and ECS environments. Architecturally, it scales automatically to billions of metrics, leveraging Cortex technology for high-availability multi-zone persistence. It reduces the administrative overhead of managing large, DIY Prometheus TSDB clusters.
  - **(2021)** [==aws.amazon.com: Amazon Managed Service for Prometheus Is Now Generally Available with Alert Manager and Ruler==](https://aws.amazon.com/blogs/aws/amazon-managed-service-for-prometheus-is-now-generally-available-with-alert-manager-and-ruler) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Reaches General Availability, adding key enterprise capabilities such as Alert Manager and Ruler. Users can define native Prometheus alerting rules and route alerts to downstream incident response hubs like PagerDuty or AWS SNS. It reinforces the managed monitoring story by guaranteeing security, high availability, and out-of-the-box multi-region reliability.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Oraclecloud](./oraclecloud.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

