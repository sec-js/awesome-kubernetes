# AWS Containers

!!! info "Architectural Context"
    Detailed reference for AWS Containers in the context of Cloud Providers (Hyperscalers).

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Get started with Amazon EC2 Container Registry (Amazon ECR)](http://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - [blog.couchbase.com: Getting Started with Docker for AWS and Scaling Nodes](http://blog.couchbase.com/2016/july/docker-for-aws-getting-started-scaling-nodes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.couchbase.com in the Kubernetes Tools ecosystem.
  - [neal-davis.medium.com: ECS vs EC2 vs Lambda](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering neal-davis.medium.com: ECS vs EC2 vs Lambda in the Kubernetes Tools ecosystem.
  - [medium: Creating CI/CD Pipeline for AWS ECS — Part I](https://medium.com/@harshvijaythakkar/creating-ci-cd-pipeline-for-aws-ecs-part-i-b2f61bb1522f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Creating CI/CD Pipeline for AWS ECS — Part I in the Kubernetes Tools ecosystem.
  - [faun.pub: Why We Moved From Lambda to ECS](https://faun.pub/why-we-moved-from-lambda-to-ecs-b84674f31869)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Why We Moved From Lambda to ECS in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Choosing the Right AWS Container Service: ECS vs. EKS](https://aws.plainenglish.io/choosing-the-right-aws-container-service-ecs-vs-eks-3b11dd078c99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Choosing the Right AWS Container Service: ECS vs. EKS in the Kubernetes Tools ecosystem.
  - [A Better Dev/Test Experience: Docker and AWS](https://medium.com/aws-activate-startup-blog/a-better-dev-test-experience-docker-and-aws-291da5ab1238)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering A Better Dev/Test Experience: Docker and AWS in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: How to Push a Docker Image to the AWS ECR](https://aws.plainenglish.io/how-to-push-an-image-to-aws-ecr-b2be848c2ef)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: How to Push a Docker Image to the AWS ECR in the Kubernetes Tools ecosystem.
## Cloud Infrastructure

### AWS

#### Container Compute

  - **(2024)** [Amazon ECS-optimized AMI](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference manual for the AWS-engineered Amazon Machine Image (AMI) preconfigured with the ECS agent, Docker runtime, and optimal container configurations. Utilizing this specialized OS image ensures maximum orchestration performance, reliable telemetry, and security compliance out of the box.
#### Container Registries

  - **(2024)** [Amazon EC2 Container Registry Documentation](http://aws.amazon.com/es/documentation/ecr) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official engineering reference for Amazon ECR, a fully managed OCI-compliant container registry. It covers critical security integrations, image scanning capabilities, cross-region replication configurations, and direct integration with Amazon ECS/EKS to facilitate safe, high-speed container pull actions.
  - **(2020)** [ecrcp](https://github.com/bit-cloner/ecrcp) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight utility designed to copy Docker images directly between different Amazon ECR registries without requiring local download-and-reupload bandwidth. Useful for cross-account deployments and regional migration tasks in complex enterprise AWS landing zones.
#### Continuous Deployment

  - **(2021)** [Automate rollbacks for Amazon ECS rolling deployments with CloudWatch alarms](https://aws.amazon.com/blogs/containers/automate-rollbacks-for-amazon-ecs-rolling-deployments-with-cloudwatch-alarms) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide outlining automated deployment rollback capabilities within ECS rolling deployments. It illustrates how CloudWatch alarms can monitor application health (e.g., HTTP 5xx rates) during active deployments and automatically trigger rollbacks to a previously stable revision to maintain high availability.
#### Legacy Tooling

  - **(2016)** [Using Docker Machine with AWS](http://blog.scottlowe.org/2016/03/22/using-docker-machine-with-aws) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Detailed technical blog post showing how to provision and manage remote Docker engines on AWS using the deprecated Docker Machine utility. While valuable for historical debugging and legacy architecture comprehension, live industry alignment dictates migrating to modern Cloud API alternatives (such as AWS CLI, Terraform, or Rancher).
  - **(2016)** [Docker Datacenter on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/es/about-aws/whats-new/2016/06/docker-datacenter-on-the-aws-cloud-quick-start-reference-deployment) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Quick Start guide detailing the automated orchestration of Docker Datacenter (now Mirantis Kubernetes Engine) on AWS. It serves as an architectural design reference from the pre-Kubernetes dominance era, describing multi-zone registry configurations, control planes, and Swarm-based container engines.
#### Security Practices

  - **(2025)** [**awslabs/amazon-ecr-credential-helper: Amazon ECR Docker Credential Helper**](https://github.com/awslabs/amazon-ecr-credential-helper) <span class='md-tag md-tag--info'>⭐ 2703</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A Docker credential helper that handles seamless, transparent IAM-based authentication for Amazon ECR. By removing the need to run periodic 'aws ecr get-login-password' cron jobs, it enhances runtime security by integrating directly with standard IAM Instance Profiles and local AWS config files.
  - **(2022)** [dev.to: Sharing secrets to ECS in an AWS multi-account architecture](https://dev.to/aws-builders/sharing-secrets-to-ecs-in-an-aws-multi-account-architecture-5h1i) <span class='md-tag md-tag--warning'>[TERRAFORM CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blueprint for cross-account secret management for Amazon ECS using AWS Secrets Manager and Systems Manager (SSM) Parameter Store. It provides security engineers with an architectural approach to maintain strict separation of concerns, principal-of-least-privilege IAM policies, and cross-account IAM role assumption.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Azure](./azure.md)

