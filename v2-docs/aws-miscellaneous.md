# AWS Miscellaneous

!!! info "Architectural Context"
    Detailed reference for AWS Miscellaneous in the context of Cloud Providers (Hyperscalers).

## Application Development

### Container Orchestration

#### App Runner

  - **(2026)** [AWS App Runner 🌟](https://aws.amazon.com/apprunner) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines AWS App Runner as a fully managed container service for rapid web application and API deployment. Live Grounding confirms its position in 2026 as a premier choice for developers wanting to bypass Kubernetes complexity, offering automated load balancing, scaling, and TLS termination directly from source code or ECR.
  - **(2022)** [Architecting for resiliency on AWS App Runner](https://aws.amazon.com/blogs/containers/architecting-for-resiliency-on-aws-app-runner) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on engineering multi-region, high-availability, and fault-tolerant topologies with App Runner. Live Grounding shows that resilient patterns rely on Route 53 routing, pilot light databases, and robust custom health checks to sustain production-grade service availability.
  - **(2021)** [dev.to: AWS App Runner : How to deploy containerized applications using App Runner](https://dev.to/aws-builders/aws-app-runner-how-to-deploy-containerized-applications-using-app-runner-1f7c) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight details the operational steps for configuring and running Dockerized workloads on AWS App Runner. Live Grounding verifies this as a classic, high-value guide for transitioning traditional VMs to serverless containers without having to manage raw ECS or EKS orchestration.
### Frontend and Mobile

#### AWS Amplify

  - **(2026)** [docs.amplify.aws: Set up Amplify Auth](https://docs.amplify.aws/javascript/build-a-backend/auth/set-up-auth) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight provides a guided reference for setting up secure Cognito authentication in JS applications via Amplify. Live Grounding validates this as the standard security integration method for frontend architectures, offering seamless token management, MFA, and federated identity providers out of the box.
  - **(2022)** [blog.logrocket.com: AWS Amplify and React Native: A tutorial](https://blog.logrocket.com/aws-amplify-react-native-tutorial-examples) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight steps through the integration of AWS Amplify into React Native projects for seamless mobile backend generation. Live Grounding confirms this setup remains a highly efficient workflow, though development teams in 2026 now focus heavily on Amplify Gen 2, which utilizes TypeScript-first code-first DX.
  - **(2021)** [dev.to: 10 New AWS Amplify Features to Check Out](https://dev.to/aws/10-new-aws-amplify-features-to-check-out-4291) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight catalogues critical feature updates in AWS Amplify to accelerate full-stack delivery. Live Grounding shows that while these specific features laid the foundation, modern Amplify ecosystems have converged around Next.js SSR support and CDK-based extensibility.
### Microservices

#### E-commerce Reference

  - **(2021)** [Architecting a Highly Available Serverless, Microservices-Based Ecommerce Site](https://aws.amazon.com/blogs/architecture/architecting-a-highly-available-serverless-microservices-based-ecommerce-site) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details the design of a highly available, multi-region e-commerce platform using EventBridge, Cognito, Lambda, and DynamoDB. Live Grounding shows this architecture represents the gold standard for serverless distributed microservices, emphasizing event-driven decoupling and global data consistency.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [bbvanexttechnologies.com: Cómo definir infraestructura como código en AWS' con CDK](https://www.bbvanexttechnologies.com/como-definir-infraestructura-como-codigo-en-aws-con-cdk)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering bbvanexttechnologies.com: Cómo definir infraestructura como código en AWS' con CDK in the Kubernetes Tools ecosystem.
  - [medium.com/contino-engineering: We’ve begun to move towards the AWS CDK' and here’s why](https://medium.com/contino-engineering/weve-begun-to-move-towards-the-aws-cdk-and-here-s-why-69c8fad688b3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/contino-engineering: We’ve begun to move towards the AWS CDK' and here’s why in the Kubernetes Tools ecosystem.
  - [medium.com/simform-engineering: Infrastructure as Code and CI/CD in Practice' with AWS CDK](https://medium.com/simform-engineering/infrastructure-as-code-and-ci-cd-in-practice-with-aws-cdk-bd0685b361f8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/simform-engineering: Infrastructure as Code and CI/CD in Practice' with AWS CDK in the Kubernetes Tools ecosystem.
  - [faun.pub: Using AWS Session Manager For Port Forwarding To Remote Hosts](https://faun.pub/using-aws-session-manager-for-port-forwarding-to-remote-hosts-8168589ba579)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Using AWS Session Manager For Port Forwarding To Remote Hosts in the Kubernetes Tools ecosystem.
  - [medium.com/@mike_tyson_cloud: AWS Landing Zone: Mastering the Architecture' — Best Practices and Design Secrets](https://medium.com/@mike_tyson_cloud/aws-landing-zone-mastering-the-architecture-best-practices-and-design-secrets-a37746f72962)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@mike_tyson_cloud: AWS Landing Zone: Mastering the Architecture' — Best Practices and Design Secrets in the Kubernetes Tools ecosystem.
## Cloud Infrastructure

### AWS

#### Application Deployment

  - **(2016)** [Creating and Deploying PHP Applications on AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_PHP_eb.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step developer guide for compiling, structuring, and launching robust PHP packages on AWS Beanstalk. Documents configuring system environment files and customized runtime settings.
#### Application Platform Updates

  - **(2016)** [AWS Elastic Beanstalk Supports ASP.NET Core and Multi-App .NET Support](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-asp-net-core-and-multi-app-net-support) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the 2016 platform expansion adding native support for ASP.NET Core applications and multi-app configuration models in Elastic Beanstalk Windows instances.
#### Cloud Migration

  - **(2016)** [AWS Application Discovery Service](https://docs.aws.amazon.com/application-discovery/latest/userguide/what-is-appdiscovery.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — AWS service that inventories and parses physical and virtual systems inside legacy on-premises environments. Maps active server dependencies and gathers CPU, RAM, and network utilization profiles to plan cloud migrations.
  - **(2016)** [AWS Application Discovery Service Update – Agentless Discovery for VMware](https://aws.amazon.com/blogs/aws/aws-application-discovery-service-update-agentless-discovery-for-vmware) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS announcement showing how Application Discovery Service interfaces directly with VMware vCenter environments. Avoids OS agent dependencies to quickly construct VM topology maps.
#### Configuration Management

  - **(2016)** [youtube: AWS OpsWorks Overview and Demo](https://www.youtube.com/watch?v=cj_LoG6C2xk&list=PLR3sVanzLpJN6BiYS20K4BMPpiDGifbZy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual and technical walkthrough demonstrating configuration layers, application deployments, and runtime lifecycle hooks executed via AWS OpsWorks stack engines.
  - **(2013)** [AWS OpsWorks](https://aws.amazon.com) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A managed configuration management platform utilizing Chef or Puppet layers. *2026 Engineering Reality*: Now classified as legacy, with standard DevOps workflows adopting AWS Systems Manager (SSM) and Terraform for infrastructure automation.
#### Hybrid Cloud

  - **(2017)** [VMware Cloud on AWS](https://aws.amazon.com/es/vmware) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official architectural landing page for VMware Cloud on AWS. Outlines SDDC framework deployments on bare-metal infrastructure, enabling disaster recovery, capacity bursting, and seamless VM migrations.
#### Infrastructure APIs

  - **(2021)** [AWS Cloud Control API](https://aws.amazon.com/cloudcontrolapi) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed programmatic standard for the Cloud Control API. Unifies CRUDL interactions across hundreds of AWS resource classes and third-party integration schemas, facilitating custom provisioning engine designs.
  - **(2021)** [AWS Cloud Control API, a Uniform API to Access AWS & Third-Party Services](https://aws.amazon.com/blogs/aws/announcing-aws-cloud-control-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official blog introduction announcing the Cloud Control API. Discusses how standardization simplifies life for infrastructure-as-code creators (e.g., Terraform, Pulumi) by delivering instant support for new cloud capabilities.
#### Infrastructure Operations

  - **(2016)** [blog.rackspace.com: Patch and AMI Management for Windows on AWS](https://blog.rackspace.com/patch-and-ami-management-for-windows-on-aws)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Engineering blog clarifying patch administration, automated AMI construction, and system compliance practices for running legacy or enterprise Windows Server nodes on AWS.
#### Load Balancing

  - **(2016)** [AWS Elastic Beanstalk Supports Application Load Balancer](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-application-load-balancer) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Product release documentation outlining integration of Application Load Balancers (ALBs) with Elastic Beanstalk. Unlocks path-based routing, target group pooling, and secure WebSocket connections.
  - **(2016)** [Configuring an Application Load Balancer](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-applicationloadbalancer.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Operational guide detailing how to declare, scale, and tune target parameters and routing policies on Application Load Balancers inside active Elastic Beanstalk projects.
#### PaaS Architecture

  - **(2016)** [Deploying a High-Availability PHP Application with an External Amazon RDS Database to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/php-ha-tutorial.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS deployment blueprint detailing how to structure a multi-availability zone PHP application using Beanstalk. Integrates an external multi-AZ Amazon RDS configuration to build failover resilience.
#### PaaS Platform

  - **(2011)** [AWS Elastic Beanstalk Documentation](https://aws.amazon.com/documentation/elastic-beanstalk) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference architecture and deployment guide for AWS Elastic Beanstalk. Simplifies cloud application lifecycle management by handling capacity provisioning, balancing, scaling, and platform patching.
#### Web Servers

  - **(2016)** [AWS Elastic Beanstalk Supports Nginx Proxy Server with Tomcat](https://aws.amazon.com/about-aws/whats-new/2016/08/aws-elastic-beanstalk-supports-nginx-proxy-server-with-tomcat) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Feature documentation announcing native Nginx reverse proxy configurations sitting in front of Apache Tomcat platforms in Beanstalk. Optimizes delivery of static assets and client routing.
### Ecosystem

#### AWS Partners

  - **(2026)** [AWS Partner Network](https://aws.amazon.com/partners) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the portal for finding verified APN Technology and Consulting partners. Live Grounding shows AWS Partner Network remains the core commercial engine for AWS, facilitating ISV integrations, validated architectures, and professional service engagements globally.
#### Case Studies

  - **(2025)** [AWS Partner Network (APN) blog](https://aws.amazon.com/blogs/apn) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on architecture walkthroughs, such as deploying high-availability services on AWS using Spotinst (now Spot by NetApp) and configuring Active Directory SSO. Live Grounding validates these blog posts as critical operational blueprints for multi-tenant integrations and cost-optimization strategies in enterprise environments.
### FinOps and Sustainability

#### Green Ops

  - **(2022)** [aws.amazon.com: Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces architectural paradigms for building carbon-efficient data ingestion pipelines and S3 data lakes on AWS. Live Grounding emphasizes that GreenOps and carbon tracing are major metrics in 2026, where design patterns like intelligent tiering, optimal compression (Parquet), and ARM64-based Graviton instances directly reduce environmental footprint.
### High Performance Computing

#### Life Sciences

  - **(2020)** [aws.amazon.com: Creating a digital map of COVID-19 virus for discovery of new treatment compounds](https://aws.amazon.com/blogs/hpc/creating-a-digital-map-of-covid-19-virus-for-discovery-of-new-treatment-compounds) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight captures the orchestration of highly parallelized, massive HPC grids on AWS to model viral interactions. Live Grounding confirms that AWS's modern HPC offerings (ParallelCluster, Batch, and FSx for Lustre) remain pivotal for global health research, processing exabytes of genomic data in record time.
### IoT and Edge

#### AWS IoT Core

  - **(2026)** [What Is AWS IoT?](https://docs.aws.amazon.com/iot/latest/developerguide/what-is-aws-iot.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps AWS IoT as the entry point for connecting physical devices to AWS cloud services. Live Grounding confirms it has evolved into a robust suite of services (Core, Greengrass, Device Defender) handling billions of messages daily. It provides secure, bi-directional communication with MQTT/HTTPS and acts as the foundational layer for enterprise IoT data ingestion.
### Migration

#### AWS MGN

  - **(2026)** [AWS Cloud Endure Migration](https://aws.amazon.com/application-migration-service) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps the evolution of CloudEndure into AWS Application Migration Service (AWS MGN). Live Grounding confirms AWS MGN is the primary enterprise engine for lift-and-shift migrations, maintaining block-level replication of physical, virtual, or cloud-based servers directly to AWS target instances.
### Operations

#### Service Quotas

  - **(2026)** [AWS API: get-service-quota](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/get-service-quota.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight describes the AWS CLI reference for auditing specific service limits. Live Grounding highlights its mandatory use in modern GitOps and IaC (Terraform/Pulumi) pipelines to preemptively validate account thresholds before executing large-scale resource provisioning.
  - **(2025)** [How can I troubleshoot errors using the AWS CLI to manage my service quota requests?](https://repost.aws/es/knowledge-center/troubleshoot-service-quotas-cli-commands) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight targets the diagnostics and troubleshooting workflows for managing AWS service quotas programmatically. Live Grounding points to this as a vital operational playbook for SRE teams, helping avoid throttling and deployment blocks during dynamic scaling by automating quota requests via CLI and API.
### Virtual Private Servers

#### AWS Lightsail

  - **(2026)** [AWS LightSail](https://aws.amazon.com/lightsail) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents AWS Lightsail as a simplified, cost-predictable virtual private server (VPS) alternative to raw EC2. Live Grounding confirms Lightsail is widely used in 2026 for small-scale projects, staging environments, and rapid WP deployments, offering pre-configured blueprints and straightforward billing.
## Cloud Native Infrastructure

### Service Mesh

#### AWS (1)

  - **(2022)** [aws.amazon.com/app-mesh](https://aws.amazon.com/app-mesh) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Live Grounding Synthesis: Built on Envoy as AWS's managed service mesh, AWS App Mesh was deprecated in late 2024 and fully sunsetted. Platform teams are urged to transition to Amazon ECS Service Connect or Amazon VPC Lattice.
## Edge and IoT

### AWS (2)

#### IoT Platforms

  - **(2015)** [aws.amazon.com/en/iot](https://aws.amazon.com/iot) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical documentation for AWS IoT Core, a high-throughput managed broker designed to securely route and map billions of device telemetry streams into cloud databases and analysis applications.
## Infrastructure as Code

### AWS CDK

#### Core Platform

  - **(2026)** [CDK](https://aws.amazon.com/cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the AWS Cloud Development Kit (CDK) for defining cloud infrastructure using familiar programming languages. Live Grounding confirms AWS CDK v2 is the undisputed standard for modern AWS programmatic provisioning, drastically reducing CloudFormation boilerplate via high-level, reusable constructs.
#### EKS and Kubernetes

  - **(2021)** [itnext.io: AWS CDK for EKS — Handling Helm Charts](https://itnext.io/aws-cdk-for-eks-handling-helm-charts-aa002afedde4) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight provides architectural guidelines on embedding Helm releases directly inside CDK-managed Amazon EKS clusters. Live Grounding validates this approach for combining platform-level AWS IaC with Kubernetes-native package management, streamlining cluster provisioning pipelines.
#### Migration Tools

  - **(2023)** [Announcing CDK Migrate: A single command to migrate to the AWS CDK](https://aws.amazon.com/blogs/devops/announcing-cdk-migrate-a-single-command-to-migrate-to-the-aws-cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight details the native CDK CLI capability to ingest deployed CloudFormation stacks or raw resources and output fully functional CDK code. Live Grounding demonstrates its extreme usefulness in technical debt remediation, shifting old legacy infrastructure into managed, programmatically modeled code bases.
#### Serverless Applications

  - **(2023)** [freecodecamp.org: AWS CDK v2 Tutorial – How to Create a Three-Tier Serverless Application](https://www.freecodecamp.org/news/aws-cdk-v2-three-tier-serverless-application) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight is a comprehensive, hands-on tutorial for constructing API Gateway, Lambda, and DynamoDB stacks via CDK v2. Live Grounding proves this three-tier serverless pattern remains the gold standard blueprint for robust, scalable web services in AWS.
### Alternative IaC

#### SST

  - **(2024)** [sst.dev: Moving away from CDK: CDK doesn’t create the infrastructure you define](https://sst.dev/blog/moving-away-from-cdk) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight captures the SST team's pivotal decision to transition from AWS CDK to Pulumi/Terraform engines (SST Ion) due to performance bottlenecks and CloudFormation limits. Live Grounding in 2026 highlights this article as a milestone in the serverless community, validating the growing adoption of highly optimized, engine-agnostic IaC tools.
## Networking and Security

### Identity and Access

#### Secrets Management

  - **(2022)** [dev.to: Automatic API Key rotation for Amazon Managed Grafana](https://dev.to/aws-heroes/automatic-api-key-rotation-for-amazon-managed-grafana-2h68) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight details the step-by-step automation of rotating Grafana API keys using AWS Lambda and Secrets Manager. Live Grounding validates this as a vital security standard, preventing persistent credential leaks and enforcing compliance policies across enterprise monitoring setups.
### Remote Access

#### AWS Systems Manager

  - **(2022)** [aws.amazon.com: AWS Systems Manager announces support for port forwarding to remote hosts using Session Manager](https://aws.amazon.com/about-aws/whats-new/2022/05/aws-systems-manager-support-port-forwarding-remote-hosts-using-session-manager) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight announces native SSM port-forwarding tunnels directly to database endpoints or remote hosts inside private subnets. Live Grounding confirms this is a standard operational practice in 2026, eliminating the security risks, costs, and management overhead of maintaining traditional jump box/bastion host VMs.
### Service Mesh (1)

#### Multi-Account

  - **(2021)** [amazon.com: Leveraging App Mesh with Amazon EKS in a Multi-Account environment](https://aws.amazon.com/blogs/containers/leveraging-app-mesh-with-amazon-eks-in-a-multi-account-environment) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents patterns for orchestrating cross-account microservice communication using AWS App Mesh and Amazon EKS. Live Grounding highlights that while the multi-account networking concepts remain structurally valid, the reliance on App Mesh is obsolete; modern architectures deploy VPC Lattice or cross-cluster Istio meshes.
## Organizational Culture

### Migration Journeys

#### Trainline

  - **(2016)** [Trainline.com dumps Oracle and Microsoft, gulps AWS Kool-Aid](https://www.theregister.co.uk/2016/07/13/trainline_dumps_oracle_microsoft_goes_full_aws_cto_interview) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight records Trainline's radical migration from legacy on-prem Oracle and Microsoft SQL/Windows monoliths to AWS. Live Grounding notes this historical case study illustrates the industry's massive mid-2010s migration pattern, proving that legacy modernization directly unlocks operational agility and cloud scalability.
  - **(2016)** [London DevOps - Trainline, A DevOps Journey - Chris Turvil](https://www.youtube.com/watch?v=IUvUmqu1MBQ) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight tracks the cultural and technical journey of Trainline’s DevOps transition during their full AWS migration. Live Grounding points to this talk as a textbook cultural reference, showing that microservices and infrastructure modernization fail without a parallel shift in organizational communication and delivery practices.
## Serverless

### Voice User Interfaces

#### Alexa Skills

  - **(2017)** [New Alexa Skills Kit Template: Build a Trivia Skill in under an Hour](https://developer.amazon.com) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Step-by-step developer tutorial detailing integration patterns between the Alexa Skills Kit and AWS Lambda serverless functions. Marked legacy as current conversational AI models have largely replaced basic programmatic trivia setups in production.
## Testing and Chaos

### Chaos Engineering

#### AWS FIS

  - **(2020)** [techcrunch.com: AWS introduces new Chaos Engineering as a Service offering](https://techcrunch.com/2020/12/15/aws-introduces-new-chaos-engineering-as-a-service-offering) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight documents the launch of AWS Fault Injection Simulator (FIS) to facilitate managed chaos engineering. Live Grounding demonstrates that FIS has transitioned from a new offering to a deeply integrated resilience tool in 2026, standardizing controlled failure injection across EC2, EKS, and RDS clusters.
### Debugging

#### AWS Troubleshooting

  - **(2021)** [thenewstack.io: Remote Debugging in AWS: The Missing Link in Your Debugging Toolset](https://thenewstack.io/remote-debugging-in-aws-the-missing-link-in-your-debugging-toolset) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight exposes methodologies for live-debugging cloud-hosted microservices without causing disruption. Live Grounding tracks the evolution of these techniques into sophisticated cloud-native debugging proxies and observability integrations (like OpenTelemetry and Telepresence), bridging local IDEs with remote VPC resources.
### Local Emulation

#### AWS Emulation

  - **(2026)** [==github.com/localstack/localstack==](https://github.com/localstack/localstack) <span class='md-tag md-tag--info'>⭐ 65044</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight identifies the open-source repository for LocalStack, the premier AWS cloud emulator. Live Grounding underscores its unparalleled adoption (>65k stars), showing it as a foundational dependency for developer productivity, enabling local execution of Lambdas, S3, DynamoDB, and CloudFormation stacks.
  - **(2026)** [localstack.cloud](https://www.localstack.cloud) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the enterprise cloud platform offering advanced local emulation of AWS services. Live Grounding reinforces that LocalStack has become the industry standard for offline AWS cloud development, supporting complex services like IAM, EKS, and RDS, which radically reduces cloud spend and speeds up inner-loop iteration cycles.
#### EC2 Metadata

  - **(2025)** [Amazon EC2 Metadata Mock](https://github.com/aws/amazon-ec2-metadata-mock) <span class='md-tag md-tag--info'>⭐ 291</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents this tool as a local mock for the Amazon EC2 Instance Metadata Service (IMDSv1/v2). Live Grounding confirms its high utility in local testing pipelines and CI/CD environments, allowing developers to simulate instance roles, security credentials, and spot interruption notices without provisioning real cloud resources.
#### Gitpod Integration

  - **(2021)** [github.com/omenking/localstack-gitpod-template: LocalStack Gitpod Template](https://github.com/omenking/localstack-gitpod-template) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces a Gitpod configuration template for bootstrapping LocalStack development environments instantly in the browser. Live Grounding highlights this as an efficient template for cloud-native training, though production teams in 2026 typically leverage official Dev Container or LocalStack-supported cloud environments.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Azure](./azure.md)

