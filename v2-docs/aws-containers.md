# AWS Containers

!!! info "Architectural Context"
    Detailed reference for AWS Containers in the context of Cloud Providers (Hyperscalers).

## Standard Reference

  - [Get started with Amazon EC2 Container Registry (Amazon ECR)](http://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.couchbase.com: Getting Started with Docker for AWS and Scaling Nodes](http://blog.couchbase.com/2016/july/docker-for-aws-getting-started-scaling-nodes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws-quickstart.github.io: Rancher on the AWS Cloud. Quick Start Reference' Deployment](https://aws-quickstart.github.io/quickstart-eks-rancher)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [neal-davis.medium.com: ECS vs EC2 vs Lambda](https://neal-davis.medium.com/ecs-vs-ec2-vs-lambda-36b8ca380dea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Creating CI/CD Pipeline for AWS ECS — Part I](https://medium.com/@harshvijaythakkar/creating-ci-cd-pipeline-for-aws-ecs-part-i-b2f61bb1522f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dev.to: Sharing secrets to ECS in an AWS multi-account architecture](https://dev.to/aws-builders/sharing-secrets-to-ecs-in-an-aws-multi-account-architecture-5h1i)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [faun.pub: Why We Moved From Lambda to ECS](https://faun.pub/why-we-moved-from-lambda-to-ecs-b84674f31869)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Automate rollbacks for Amazon ECS rolling deployments with CloudWatch alarms](https://aws.amazon.com/blogs/containers/automate-rollbacks-for-amazon-ecs-rolling-deployments-with-cloudwatch-alarms)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.plainenglish.io: Choosing the Right AWS Container Service: ECS vs. EKS](https://aws.plainenglish.io/choosing-the-right-aws-container-service-ecs-vs-eks-3b11dd078c99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [A Better Dev/Test Experience: Docker and AWS](https://medium.com/aws-activate-startup-blog/a-better-dev-test-experience-docker-and-aws-291da5ab1238)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Docker Datacenter on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/es/about-aws/whats-new/2016/06/docker-datacenter-on-the-aws-cloud-quick-start-reference-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ecrcp](https://github.com/bit-cloner/ecrcp)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aws.plainenglish.io: How to Push a Docker Image to the AWS ECR](https://aws.plainenglish.io/how-to-push-an-image-to-aws-ecr-b2be848c2ef)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [awslabs/amazon-ecr-credential-helper: Amazon ECR Docker Credential Helper](https://github.com/awslabs/amazon-ecr-credential-helper) <span class='md-tag md-tag--info'>⭐ 2704</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Providers

### AWS

#### Compute

  - **(2026)** [Amazon ECS-optimized AMI](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight / Live Grounding: Deep dive into the Amazon ECS-Optimized AMI. Details the pre-integrated container runtimes, AWS ECS Agent configurations, and kernel optimizations necessary for running resilient ECS clusters.
#### Container Registries

  - **(2026)** [Amazon EC2 Container Registry Documentation](http://aws.amazon.com/es/documentation/ecr)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight / Live Grounding: High-density guide on Amazon Elastic Container Registry (ECR). Focuses on IAM integration, secure image scanning, replication rules, and optimization strategies for secure high-velocity deployments.
#### Legacy Tooling

  - **(2016)** [Using Docker Machine with AWS](http://blog.scottlowe.org/2016/03/22/using-docker-machine-with-aws)  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight / Live Grounding: Historical guide for provisioning AWS EC2 instances with docker runtimes using Docker Machine. Note: Docker Machine has been officially deprecated; modern architectures prioritize IaC utilities.
## Public Cloud Platforms

### AWS (1)

#### Container Orchestration Comparison

  - [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep comparison analyzing container scaling mechanics and metrics between ECS (using ASGs) and EKS (using Cluster Autoscaler). The analysis explains scale-up and scale-down behaviors, node provisioning latencies, and resource utilization optimizations.
  - [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comparative evaluation analyzing resource isolation, infrastructure management, and compute overhead between EKS, ECS, and AWS Fargate. Highlights scheduling efficiency, control plane pricing, and cost-of-scale dynamics for enterprise systems.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Public Cloud Solutions](./public-cloud-solutions.md) | [Managed Kubernetes In Public Cloud](./managed-kubernetes-in-public-cloud.md)

