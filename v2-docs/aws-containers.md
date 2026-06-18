# AWS Containers

!!! info "Architectural Context"
    Detailed reference for AWS Containers in the context of Cloud Providers (Hyperscalers).

## Table of Contents

1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Infrastructure](#cloud-infrastructure)
  - [AWS](#aws)
    - [Container Compute](#container-compute)
    - [Container Orchestration](#container-orchestration)
    - [Container Registries](#container-registries)
    - [Continuous Deployment](#continuous-deployment)
    - [Legacy Tooling](#legacy-tooling)
    - [Security Practices](#security-practices)
1. [Cloud Native](#cloud-native)
  - [Kubernetes](#kubernetes)
    - [Rancher Management](#rancher-management)

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Get started with Amazon EC2 Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - [blog.couchbase.com: Getting Started with Docker for AWS and Scaling Nodes](https://blog.couchbase.com/2016/july/docker-for-aws-getting-started-scaling-nodes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.couchbase.com in the Kubernetes Tools ecosystem.
  - [medium: Creating CI/CD Pipeline for AWS ECS — Part I](https://medium.com/@harshvijaythakkar/creating-ci-cd-pipeline-for-aws-ecs-part-i-b2f61bb1522f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Creating CI/CD Pipeline for AWS ECS — Part I in the Kubernetes Tools ecosystem.
  - [neal-davis.medium.com: ECS vs EC2 vs Lambda](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering neal-davis.medium.com: ECS vs EC2 vs Lambda in the Kubernetes Tools ecosystem.
  - [faun.pub: Why We Moved From Lambda to ECS](https://faun.pub/why-we-moved-from-lambda-to-ecs-b84674f31869)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Why We Moved From Lambda to ECS in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Choosing the Right AWS Container Service: ECS vs. EKS](https://aws.plainenglish.io/choosing-the-right-aws-container-service-ecs-vs-eks-3b11dd078c99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Choosing the Right AWS Container Service: ECS vs. EKS in the Kubernetes Tools ecosystem.
  - [A Better Dev/Test Experience: Docker and AWS](https://medium.com/aws-activate-startup-blog/a-better-dev-test-experience-docker-and-aws-291da5ab1238)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering A Better Dev/Test Experience: Docker and AWS in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: How to Push a Docker Image to the AWS ECR](https://aws.plainenglish.io/how-to-push-an-image-to-aws-ecr-b2be848c2ef)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: How to Push a Docker Image to the AWS ECR in the Kubernetes Tools ecosystem.
## Cloud Infrastructure

### AWS

#### Container Compute

  - **(2024)** [Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference manual for the AWS-engineered Amazon Machine Image (AMI) preconfigured with the ECS agent, Docker runtime, and optimal container configurations. Utilizing this specialized OS image ensures maximum orchestration performance, reliable telemetry, and security compliance out of the box.
#### Container Orchestration

  - **(2023)** [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive comparing AWS ECS, EKS, and serverless container execution via AWS Fargate. Synthesizing live cloud architectural trends, it presents insights into financial management, operational simplicity, and dynamic resource scaling, mapping out the trade-offs of using managed VM pools versus completely serverless options.
  - **(2022)** [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform](https://www.clickittech.com/cloud-services/amazon-ecs-vs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This comprehensive comparison highlights the operational differences, cost implications, and architecture layouts of Amazon ECS versus Amazon EKS. EKS targets standard Kubernetes-based deployments requiring high portability, while ECS is a highly optimized, opinionated AWS native orchestrator designed for seamless integration.
  - **(2021)** [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed comparative analysis of scaling strategies between Amazon ECS and EKS clusters. The article walks through key operational considerations, including EC2 Auto Scaling Groups, Karpenter, cluster autoscalers, and resource utilization dynamics, highlighting how choice of orchestration influences microservices scale limits.
#### Container Registries

  - **(2024)** [Amazon EC2 Container Registry Documentation](https://aws.amazon.com/es/documentation/ecr) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official engineering reference for Amazon ECR, a fully managed OCI-compliant container registry. It covers critical security integrations, image scanning capabilities, cross-region replication configurations, and direct integration with Amazon ECS/EKS to facilitate safe, high-speed container pull actions.
  - **(2020)** [ecrcp](https://github.com/bit-cloner/ecrcp) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight utility designed to copy Docker images directly between different Amazon ECR registries without requiring local download-and-reupload bandwidth. Useful for cross-account deployments and regional migration tasks in complex enterprise AWS landing zones.
#### Continuous Deployment

  - **(2021)** [Automate rollbacks for Amazon ECS rolling deployments with CloudWatch alarms](https://aws.amazon.com/blogs/containers/automate-rollbacks-for-amazon-ecs-rolling-deployments-with-cloudwatch-alarms) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide outlining automated deployment rollback capabilities within ECS rolling deployments. It illustrates how CloudWatch alarms can monitor application health (e.g., HTTP 5xx rates) during active deployments and automatically trigger rollbacks to a previously stable revision to maintain high availability.
#### Legacy Tooling

  - **(2016)** [Using Docker Machine with AWS](https://blog.scottlowe.org/2016/03/22/using-docker-machine-with-aws) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Detailed technical blog post showing how to provision and manage remote Docker engines on AWS using the deprecated Docker Machine utility. While valuable for historical debugging and legacy architecture comprehension, live industry alignment dictates migrating to modern Cloud API alternatives (such as AWS CLI, Terraform, or Rancher).
  - **(2016)** [Docker Datacenter on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/es/about-aws/whats-new/2016/06/docker-datacenter-on-the-aws-cloud-quick-start-reference-deployment) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Quick Start guide detailing the automated orchestration of Docker Datacenter (now Mirantis Kubernetes Engine) on AWS. It serves as an architectural design reference from the pre-Kubernetes dominance era, describing multi-zone registry configurations, control planes, and Swarm-based container engines.
#### Security Practices

  - **(2025)** [**awslabs/amazon-ecr-credential-helper: Amazon ECR Docker Credential Helper**](https://github.com/awslabs/amazon-ecr-credential-helper) <span class='md-tag md-tag--info'>⭐ 2703</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8a9b764e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 10 L 20 2 L 30 7 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-8a9b764e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A Docker credential helper that handles seamless, transparent IAM-based authentication for Amazon ECR. By removing the need to run periodic 'aws ecr get-login-password' cron jobs, it enhances runtime security by integrating directly with standard IAM Instance Profiles and local AWS config files.
  - **(2022)** [dev.to: Sharing secrets to ECS in an AWS multi-account architecture](https://dev.to/aws-builders/sharing-secrets-to-ecs-in-an-aws-multi-account-architecture-5h1i) <span class='md-tag md-tag--warning'>[TERRAFORM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blueprint for cross-account secret management for Amazon ECS using AWS Secrets Manager and Systems Manager (SSM) Parameter Store. It provides security engineers with an architectural approach to maintain strict separation of concerns, principal-of-least-privilege IAM policies, and cross-account IAM role assumption.
## Cloud Native

### Kubernetes

#### Rancher Management

  - **(2022)** [aws-quickstart.github.io: Rancher on the AWS Cloud. Quick Start Reference Deployment](https://aws-quickstart.github.io/quickstart-eks-rancher) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS Quick Start reference guide for standing up Rancher on AWS. This architecture installs Rancher on an Amazon EKS cluster, giving enterprise operations teams a unified interface to govern multiple downstream clusters, enforce unified RBAC models, and manage complex multi-tenant environments.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [AWS Pricing](./aws-pricing.md) | [AWS Spain](./aws-spain.md)

