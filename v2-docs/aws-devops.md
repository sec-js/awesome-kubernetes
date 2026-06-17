# AWS DevOps. AWS CodePipeline

!!! info "Architectural Context"
    Detailed reference for AWS DevOps. AWS CodePipeline in the context of Cloud Providers (Hyperscalers).

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [AWS CodeDeploy: Deploying from a Development Account to a Production Account](https://aws.amazon.com/blogs/devops/aws-codedeploy-deploying-from-a-development-account-to-a-production-account)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.amazon.com in the Kubernetes Tools ecosystem.
## CI-CD

### Cloud-Native Delivery

#### AWS

  - **(2019)** [blazemeter.com: Three Ways DevOps Benefit from AWS CodePipeline](https://www.blazemeter.com/blog/devops-best-practices-testing) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight emphasizes the DevOps efficiency gains using AWS-native pipelines. Live Grounding demonstrates how the platform automates continuous integration, integrates performance testing tools like BlazeMeter, and reduces manual deployment risk. It serves as a practical blueprint for cloud-native delivery.
## Cloud Infrastructure

### AWS Ecosystem

#### Cloud Services

  - **(2026)** [AWS DevOps 🌟](https://aws.amazon.com/devops) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS’s primary DevOps portal, presenting their native continuous delivery and infrastructure management stack, including CodePipeline, CodeBuild, and CloudFormation. While curator listings highlight frictionless integration with EC2 and ECS, live architectural patterns in 2026 showcase teams frequently combining AWS-native compute with cloud-agnostic deployment runtimes to avoid platform lock-in.
## Cloud Providers

### AWS (1)

#### Infrastructure-as-Code

  - **(2018)** [aws.amazon.com: AWS Quick Start (OpenShift 3.11 on AWS)](https://aws.amazon.com/solutions) <span class='md-tag md-tag--warning'>[CLOUDFORMATION CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Legacy AWS CloudFormation deployment template for automating OpenShift 3.11 cluster topologies. Serves as an architectural reference for VPC subnet divisions and multi-AZ load-balancer routing in early cloud-native systems.
## Cloud-Native Provisioning

### CICD Integration

#### AWS CodeDeploy

  - **(2022)** [adamtheautomator.com: Getting Started with AWS CodeDeploy](https://adamtheautomator.com/aws-codedeploy) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walkthrough outlining primary configuration steps, appspec.yml lifecycle hook schemas, and target group integrations inside the AWS CodeDeploy ecosystem.
#### AWS CodePipeline

  - **(2026)** [AWS Partner Network - CodePipeline Integrations](https://aws.amazon.com/es/codepipeline/product-integrations) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical integration matrix detailing partner-supported build, testing, and security scanning extensions available for AWS CodePipeline deployment pipelines.
  - **(2022)** [aws.amazon.com: AWS CodePipeline adds support for Branch-based development and Monorepos](https://aws.amazon.com/blogs/devops/aws-codepipeline-adds-support-for-branch-based-development-and-monorepos)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Release analysis highlighting newly added monorepo and branch-specific triggers within AWS CodePipeline, optimizing continuous delivery workflows and reducing build execution times.
#### AWS DevOps

  - **(2026)** [AWS DevOps Blog](https://aws.amazon.com/blogs/devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The authoritative AWS blog containing continuous architectural blueprints, release notes, and real-world implementation case studies for optimizing deployment patterns on Amazon Web Services.
  - **(2026)** [Continuous Deployment with AWS](https://aws.amazon.com/blogs/devops/tag/continuous-deployment)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curated collection of continuous deployment strategies optimized for AWS runtimes. Explains canary releases, blue/green cluster migrations, and automated rollbacks on ECS and EKS.
#### CDK Pipelines

  - **(2021)** [aws.amazon.com: Multi-branch pipeline management and infrastructure deployment using AWS CDK Pipelines](https://aws.amazon.com/blogs/devops/multi-branch-pipeline-management-and-infrastructure-deployment-using-aws-cdk-pipelines) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Advanced engineering tutorial detailing how to set up dynamic, multi-branch environments using AWS CDK Pipelines, enabling code-driven promotion of cloud architectures.
#### Comparisons

  - **(2021)** [k21academy.com: AWS DevOps Vs. Azure DevOps](https://k21academy.com/aws-cloud/aws-devops-vs-azure-devops/?utm_source=linkedin&utm_medium=referral&utm_campaign=awsdevops17_dec20_aws_cloud_computing_for_interested_parties__users)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comparative structural analysis pitting the AWS DevOps suite against Microsoft Azure DevOps, evaluating build pricing, third-party integrations, and native Kubernetes support configurations.
#### Jenkins Integration

  - **(2021)** [Setting Up the Jenkins Plugin for AWS CodeDeploy](https://aws.amazon.com/blogs/devops/setting-up-the-jenkins-plugin-for-aws-codedeploy) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Step-by-step setup guide for configuring the AWS CodeDeploy Jenkins plugin, allowing legacy, on-prem Jenkins orchestrations to deploy code artifacts directly to AWS cloud groups.
### Observability

#### AWS DevOps Guru

  - **(2021)** [infoq.com: AWS Launches Amazon DevOps Guru](https://www.infoq.com/news/2021/01/aws-devops-guru)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical product announcement introducing Amazon DevOps Guru, an ML-driven operations assistant that parses CloudWatch metrics and traces to proactively alert operators to system anomalies.
## Multi-Cluster and Edge

### Cluster Federation

#### Admiralty

  - **(2026)** [admiralty.io](https://admiralty.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official platform of Admiralty, an advanced multi-cluster proxy scheduler designed to programmatically dispatch workloads across physical, virtual, or serverless Kubernetes namespaces.
#### Serverless Integration

  - **(2021)** [thenewstack.io: Making Kubernetes Serverless and Global with AWS Fargate on EKS and Admiralty](https://thenewstack.io/making-kubernetes-serverless-and-global-with-aws-fargate-on-eks-and-admiralty) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigative analysis showcasing how Admiralty can coordinate with AWS Fargate serverless containers in an EKS environment to deploy globally distributed applications with low operational overhead.
  - **(2021)** [admiralty.io: Multi-Region AWS Fargate on EKS](https://admiralty.io/docs/tutorials/fargate) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Granular implementation tutorial for deploying Admiralty proxy schedulers to configure cross-cluster communication channels that target serverless AWS Fargate environments in multi-region setups.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [AWS Backup](./aws-backup.md) | [AWS Containers](./aws-containers.md)

