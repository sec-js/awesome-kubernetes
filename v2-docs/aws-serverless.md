# AWS Serverless

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-serverless/).

!!! info "Architectural Context"
    Detailed reference for AWS Serverless in the context of Cloud Providers (Hyperscalers).

## Table of Contents

1. [API Management](#api-management)
  - [GraphQL and AppSync](#graphql-and-appsync)
    - [Security](#security)
1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Platforms](#cloud-platforms)
  - [Serverless Architecture](#serverless-architecture)
    - [AWS Lambda](#aws-lambda)
    - [Concepts](#concepts)
    - [Resources](#resources)
1. [Container Orchestration](#container-orchestration)
  - [AWS ECS and Fargate](#aws-ecs-and-fargate)
    - [Machine Learning Ops](#machine-learning-ops)
    - [Performance Optimization](#performance-optimization)
    - [Storage Architecture](#storage-architecture)
  - [Kubernetes and EKS](#kubernetes-and-eks)
    - [Serverless Containers](#serverless-containers)
1. [DevOps and CICD](#devops-and-cicd)
  - [Serverless Deployment](#serverless-deployment)
    - [AWS SAM](#aws-sam)
    - [AWS SAM Pipelines](#aws-sam-pipelines)
1. [Infrastructure](#infrastructure)
  - [Automation](#automation)
    - [AWS Lambda and EventBridge](#aws-lambda-and-eventbridge)
1. [Infrastructure as Code](#infrastructure-as-code)
  - [AWS CDK](#aws-cdk)
    - [Serverless IaC](#serverless-iac)
  - [AWS SAM](#aws-sam-1)
    - [Fundamentals](#fundamentals)
  - [Terraform](#terraform)
    - [Serverless Provisioning](#serverless-provisioning)
1. [Modernization](#modernization)
  - [Monolith Migration](#monolith-migration)
    - [.NET Core](#net-core)
1. [Observability and Monitoring](#observability-and-monitoring)
  - [CloudWatch](#cloudwatch)
    - [Alerting Systems](#alerting-systems)
1. [Security and Governance](#security-and-governance)
  - [IAM and Access Control](#iam-and-access-control)
    - [ABAC](#abac)
  - [Kubernetes Compliance](#kubernetes-compliance)
    - [Infrastructure Translation](#infrastructure-translation)
  - [Secret Management](#secret-management)
    - [Go Runtime](#go-runtime)
1. [Serverless Architecture](#serverless-architecture-1)
  - [API Gateway](#api-gateway)
    - [REST APIs](#rest-apis)
  - [AWS Lambda](#aws-lambda-1)
    - [Antipatterns](#antipatterns)
    - [Cold Starts](#cold-starts)
    - [Concurrency and Scaling](#concurrency-and-scaling)
    - [Configuration Management](#configuration-management)
    - [Fundamentals](#fundamentals-1)
    - [Hardware Platforms](#hardware-platforms)
    - [Java Runtimes](#java-runtimes)
    - [Performance Optimization](#performance-optimization-1)
  - [Caching](#caching)
    - [Data Management](#data-management)
  - [Databases](#databases)
    - [Selection Criteria](#selection-criteria)
  - [Event-Driven](#event-driven)
    - [Design Patterns](#design-patterns)
  - [Messaging and Integration](#messaging-and-integration)
    - [Webhooks](#webhooks)
  - [Orchestration](#orchestration)
    - [AWS Step Functions](#aws-step-functions)

## API Management

### GraphQL and AppSync

#### Security

  - **(2022)** [How to enforce user quota on AWS AppSync with Lambda Authorizer](https://aws.amazon.com/blogs/mobile/how-to-enforce-user-quota-on-aws-appsync-with-lambda-authorizer) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to design custom Lambda Authorizers for AWS AppSync (GraphQL) to implement rate-limiting, user tier quotas, and tenant-based isolation. Reduces compute strain by verifying credentials and quotas at the API edge.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Build a Python Microservice with Amazon Web Services Lambda & API Gateway](https://www.giantflyingsaucer.com/blog/?p=5730)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.giantflyingsaucer.com in the Kubernetes Tools ecosystem.
  - [blog.powerupcloud.com: AWS inventory details in CSV using lambda](https://blog.powerupcloud.com/2016/02/07/aws-inventory-details-in-csv-using-lambda)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.powerupcloud.com in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Lambda vs. Step Functions: The Battle of Cost and' Performance](https://betterprogramming.pub/lambda-vs-step-functions-the-battle-of-cost-and-performance-5f008045e2ab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==betterprogramming.pub: Lambda vs. Step Functions: The Battle of Cost and' Performance== in the Kubernetes Tools ecosystem.
  - [kothiyal-anuj.medium.com: Serverless Diary: The Ultimate Guide to **Caching' in the Cloud**](https://kothiyal-anuj.medium.com/serverless-diary-the-ultimate-guide-to-caching-in-the-cloud-249f6a06915f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kothiyal-anuj.medium.com: Serverless Diary: The Ultimate Guide to **Caching' in the Cloud** in the Kubernetes Tools ecosystem.
  - [npmjs.com: Lambda load test](https://www.npmjs.com/package/lambda-load-test)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering npmjs.com: Lambda load test in the Kubernetes Tools ecosystem.
  - [blog.usejournal.com: Building a Serverless Back-end with AWS](https://blog.usejournal.com/building-a-serverless-back-end-with-aws-5bb3642a3f4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.usejournal.com: Building a Serverless Back-end with AWS in the Kubernetes Tools ecosystem.
  - [medium: Going Serverless (on AWS)](https://medium.com/galvanize/going-serverless-on-aws-116a04a0defd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Going Serverless (on AWS) in the Kubernetes Tools ecosystem.
  - [liavyona09.medium.com: Spice up Your Kubernetes Environment with AWS Lambda](https://liavyona09.medium.com/spice-up-your-kubernetes-environment-with-aws-lambda-a07d81347607)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering liavyona09.medium.com: Spice up Your Kubernetes Environment with AWS Lambda in the Kubernetes Tools ecosystem.
  - [medium: Serverless enterprise-grade multi-tenancy using AWS | Tarek Becker](https://medium.com/@tarekbecker/serverless-enterprise-grade-multi-tenancy-using-aws-76ff5f4d0a23)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Serverless enterprise-grade multi-tenancy using AWS | Tarek Becker in the Kubernetes Tools ecosystem.
  - [medium.com/@andrewjr350: Misunderstanding of Serverless (AWS)](https://medium.com/@andrewjr350/misunderstanding-of-serverless-aws-835c7076ea4c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@andrewjr350: Misunderstanding of Serverless (AWS) in the Kubernetes Tools ecosystem.
  - [medium.com/aws-serverless-microservices-with-patterns-best: Cloud-Native' Microservices Evolves to AWS Serverless Event-driven Architectures](https://medium.com/aws-serverless-microservices-with-patterns-best/cloud-native-microservices-evolves-to-aws-serverless-event-driven-architectures-9a38c473f4f8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/aws-serverless-microservices-with-patterns-best: Cloud-Native' Microservices Evolves to AWS Serverless Event-driven Architectures== in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Exploring the Serverless Event-Driven Architecture](https://betterprogramming.pub/exploring-the-serverless-event-driven-architecture-8d6bda93e823)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Exploring the Serverless Event-Driven Architecture in the Kubernetes Tools ecosystem.
  - [medium.com/awesome-cloud: AWS — Difference between Serverless (Lambda) and' Containers (Kubernetes)](https://medium.com/awesome-cloud/aws-difference-between-serverless-lambda-and-containers-kubernetes-serverless-vs-containers-lambda-vs-k8s-a166931870a2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/awesome-cloud: AWS — Difference between Serverless (Lambda) and' Containers (Kubernetes) in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Let's design a serverless ETL pipeline with AWS services](https://aws.plainenglish.io/lets-design-a-serverless-etl-pipeline-with-aws-services-9ab88c95afd4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Let's design a serverless ETL pipeline with AWS services in the Kubernetes Tools ecosystem.
  - [faun.pub: Serverless With Spring Boot & AWS Lambda](https://faun.pub/serverless-with-spring-boot-aws-lambda-bc76c1de2b12)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Serverless With Spring Boot & AWS Lambda in the Kubernetes Tools ecosystem.
  - [medium.com/@dan.avila7: Prueba tus proyectos serverless de forma local con' serverless-offline](https://medium.com/@dan.avila7/prueba-tus-proyectos-serverless-de-forma-local-con-serverless-offline-2e555f2b5e9b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@dan.avila7: Prueba tus proyectos serverless de forma local con' serverless-offline in the Kubernetes Tools ecosystem.
  - [medium.com/lego-engineering: A Journey into Serverless and Handling Step' Function Failures](https://medium.com/lego-engineering/a-journey-into-serverless-and-handling-step-function-failures-dba51b4e8e99)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/lego-engineering: A Journey into Serverless and Handling Step' Function Failures in the Kubernetes Tools ecosystem.
  - [blog.devops.dev: Deploying Awesome App on AWS Serverless Services — Step-by-Step' Guide](https://blog.devops.dev/deploying-awesome-app-on-aws-serverless-services-step-by-step-guide-54bc89e4d236)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devops.dev: Deploying Awesome App on AWS Serverless Services — Step-by-Step' Guide in the Kubernetes Tools ecosystem.
  - [medium.com/@sassenthusiast: Serverless Simplified: Integrating Docker Containers' into AWS Lambda via serverless.yml](https://medium.com/@sassenthusiast/serverless-simplified-integrating-docker-containers-into-aws-lambda-via-serverless-yml-cdef9be1681e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@sassenthusiast: Serverless Simplified: Integrating Docker Containers' into AWS Lambda via serverless.yml in the Kubernetes Tools ecosystem.
  - [medium.com/@HirenDhaduk1: Best choice to run your containers: AWS FARGATE' or AWS LAMBDA or Both?](https://medium.com/@HirenDhaduk1/best-choice-to-run-your-containers-aws-fargate-or-aws-lambda-or-both-d9e14685a363)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@HirenDhaduk1: Best choice to run your containers: AWS FARGATE' or AWS LAMBDA or Both? in the Kubernetes Tools ecosystem.
  - [AWS SAM CLI Advanced Serverless Deployments](https://medium.com/@mertmengu/aws-sam-cli-advanced-serverless-deployments-07432fee87ab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering AWS SAM CLI Advanced Serverless Deployments in the Kubernetes Tools ecosystem.
## Cloud Platforms

### Serverless Architecture

#### AWS Lambda

  - **(2025)** [AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — The critical reference table mapping AWS Lambda system quotas. Outlines payload thresholds, execution timeouts, ephemeral storage configurations, and concurrency parameters necessary for scalable platform designs.
  - **(2024)** [you can use Python with AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The authoritative documentation for designing, packaging, and optimizing Python functions running inside AWS Lambda. Detail runtime limits, library dependencies, and context executions.
  - **(2023)** [Security Overview of AWS Lambda](https://d1.awsstatic.com/whitepapers/Overview-AWS-Lambda-Security.pdf) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The authoritative AWS security whitepaper detailing the multi-tenant isolation architectures of Firecracker microVMs. Explores IAM execution policies, VPC security group associations, and transport encryption controls.
  - **(2021)** [dashbird.io: Deploying AWS Lambda with Docker Containers: I Gave it a Try and Here’s My Review](https://dashbird.io/blog/deploying-aws-lambda-with-docker) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An engineering review of packaging and deploying AWS Lambda targets as OCI-compliant Docker containers. Analyzes cold-start impacts, image composition strategies, and orchestration workflow modifications.
  - **(2021)** [aws.amazon.com: Operating Lambda: Understanding event-driven architecture – Part 1](https://aws.amazon.com/blogs/compute/operating-lambda-understanding-event-driven-architecture-part-1) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational multi-part operational guide from AWS technical evangelists focusing on event-driven serverless architectures. Explores decoupled communication, idempotent execution, and event processing.
  - **(2021)** [aws.amazon.com: Optimizing Lambda functions packaged as container images](https://aws.amazon.com/es/blogs/compute/optimizing-lambda-functions-packaged-as-container-images) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Highly technical optimization guide for serverless containers. Focuses on cache warming, base image choices, and reducing multi-tier image footprints to minimize cold start latency.
  - **(2020)** [Using Amazon EFS for AWS Lambda in your serverless applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed implementation pattern describing how to mount Amazon Elastic File System (EFS) onto serverless Lambda functions. This unlocks local high-performance file sharing, and heavy workload storage operations.
  - **(2020)** [cloudonaut.io: Serverless Hybrid Cloud: Accessing an API Gateway via VPN or Direct Connect](https://cloudonaut.io/serverless-hybrid-cloud-accessing-an-api-gateway-via-vpn-or-direct-connect) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An engineering case study showcasing how to securely route public API Gateway requests into localized networks via VPN tunnels or Direct Connect links. Details complex hybrid serverless network setups.
  - **(2016)** [AWS Lambda, Echo, and the Future of Cloud Automation](https://www.logicworks.net/blog/2016/01/aws-lambda-echo-cloud-automation) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical analysis of voice automation and early event-driven serverless architectures using AWS Lambda alongside smart devices. Serves as a reference for evolutionary IoT and API integration models.
#### Concepts

  - **(2022)** [Serverless: The Future of Software Architecture?](https://acg-notice.pluralsight.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — An evolutionary study evaluating the long-term design patterns of serverless architectures. Compares legacy VM deployments with transient, stateless event handlers to optimize computational costs.
#### Resources

  - **(2025)** [Youtube channel: AWS Serverless](https://www.youtube.com/channel/UC_vJsnqdpuEoRseFmlkHMkA) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS's official developer video channel focusing on serverless systems design. Shares step-by-step engineering tutorials on EventBridge, Step Functions, and API Gateway optimization.
## Container Orchestration

### AWS ECS and Fargate

#### Machine Learning Ops

  - **(2020)** [Deploy Machine Learning Pipeline on AWS Fargate](https://www.kdnuggets.com/2020/07/deploy-machine-learning-pipeline-aws-fargate.html) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Describes deploying modular machine learning pipeline tasks onto AWS Fargate containers. Demonstrates cost savings from using serverless container architectures instead of maintaining idle GPU/CPU virtual machine clusters for inference engines.
#### Performance Optimization

  - **(2022)** [element7.io: A Hidden Gem: Two Ways to Improve AWS Fargate Container Launch Times](https://www.element7.io/2022/10/a-hidden-gem-two-ways-to-improve-aws-fargate-container-launch-times) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Uncovers performance mechanics to drastically reduce boot-up latency in AWS Fargate container instances. Examines optimizing image sizes using alpine/scratch structures and utilizing AWS's Seekable OCI (SOCI) lazy-loading framework.
#### Storage Architecture

  - **(2021)** [Amazon EFS with Amazon ECS and AWS Fargate – Part 1](https://aws.amazon.com/es/blogs/containers/developers-guide-to-using-amazon-efs-with-amazon-ecs-and-aws-fargate-part-1) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A detailed developer's guide showing how to mount elastic, multi-writer shared storage structures (Amazon EFS) onto transient AWS ECS containers running under AWS Fargate. Highly critical for migrating legacy workloads requiring stateful configurations.
### Kubernetes and EKS

#### Serverless Containers

  - **(2022)** [deloitte.com: Fargate con EKS](https://www.deloitte.com/es/es/services/consulting/blogs/todo-tecnologia/fargate-con-eks.html) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates using AWS Fargate with Amazon EKS to run serverless Kubernetes pods. Eliminates the overhead of configuring, patching, and scaling standard EC2 worker node pools, transferring structural management duties back to AWS.
## DevOps and CICD

### Serverless Deployment

#### AWS SAM

  - **(2021)** [Simplify CI/CD configuration for serverless applications and your favorite CI/CD system — Public Preview](https://aws.amazon.com/about-aws/whats-new/2021/07/simplify-ci-cd-configuration-serverless-applications-your-favorite-ci-cd-system-public-preview) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores AWS's expanded support for external CI/CD toolkits using SAM. It simplifies deployment templates, lowers barriers to multi-environment promotions, and enables secure AWS credential management using OpenID Connect (OIDC) with major git repository providers.
#### AWS SAM Pipelines

  - **(2021)** [Introducing AWS SAM Pipelines: Automatically generate deployment pipelines for serverless applications](https://aws.amazon.com/blogs/compute/introducing-aws-sam-pipelines-automatically-generate-deployment-pipelines-for-serverless-applications) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces AWS SAM Pipelines, a feature within the Serverless Application Model CLI that auto-generates multi-stage CI/CD pipelines. It supports integration with Jenkins, GitLab, GitHub Actions, and Bitbucket, standardizing infrastructure-as-code deployment procedures across corporate accounts.
## Infrastructure

### Automation

#### AWS Lambda and EventBridge

  - **(2024)** [How do I stop and start EC2 instances at regular intervals using AWS Lambda? (Video)](https://repost.aws/knowledge-center/start-stop-lambda-eventbridge)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An operational video walkthrough demonstrating serverless compute cost-reduction routines. Details how to coordinate AWS Lambda with EventBridge cron schedules to automate lifecycle actions for EC2 fleets.
## Infrastructure as Code

### AWS CDK

#### Serverless IaC

  - **(2022)** [dev.to: Go fast and reduce risk: using CDK to deploy your serverless applications on AWS](https://dev.to/aws-builders/go-fast-and-reduce-risk-using-cdk-to-deploy-your-serverless-applications-on-aws-2i3k) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the advantages of deploying AWS serverless architectures via the AWS Cloud Development Kit (CDK) over classic raw CloudFormation or SAM. Highlights object-oriented constructs, automated IAM policy generation, and multi-environment validation patterns.
### AWS SAM (1)

#### Fundamentals

  - **(2022)** [dev.to/aws-builders: Introduction to AWS SAM (Serverless Application Model)](https://dev.to/aws-builders/introduction-to-aws-sam-serverless-application-model-12oc) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to the AWS Serverless Application Model (SAM). Demonstrates how this declarative YAML framework extends CloudFormation, drastically simplifying the resource definition of REST APIs, databases, and scheduled execution scripts.
### Terraform

#### Serverless Provisioning

  - **(2023)** [terrateam.io: AWS Lambda Function with Terraform](https://terrateam.io/blog/aws-lambda-function-with-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to configure and deploy AWS Lambda functions natively using HashiCorp Terraform. Covers managing the function zip package, continuous IAM role updates, integration with API Gateway, and dealing with Terraform's state transitions.
## Modernization

### Monolith Migration

#### .NET Core

  - **(2022)** [Migrating a monolithic .NET REST API to AWS Lambda](https://aws.amazon.com/blogs/compute/migrating-a-monolithic-net-rest-api-to-aws-lambda) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Formulates a structured migration plan to convert a monolithic ASP.NET Core Web API into a serverless AWS Lambda execution environment. Evaluates the use of the Amazon.Lambda.AspNetCoreServer bridge, highlighting cold start profiling and memory management strategies.
## Observability and Monitoring

### CloudWatch

#### Alerting Systems

  - **(2021)** [tutorialsdojo.com: Real-time Monitoring of 5XX Errors using AWS Lambda, CloudWatch Logs and Slack](https://tutorialsdojo.com/real-time-monitoring-of-5xx-errors-using-aws-lambda-cloudwatch-logs-slack) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides an implementation guide for parsing AWS CloudWatch logs in real-time. Leverages subscription filters and Lambda to extract system-level 5XX errors, instantly routing rich-formatted exception payloads directly to Slack webhooks for rapid operational triage.
## Security and Governance

### IAM and Access Control

#### ABAC

  - **(2022)** [aws.amazon.com: Scaling AWS Lambda permissions with Attribute-Based Access Control (ABAC)](https://aws.amazon.com/blogs/compute/scaling-aws-lambda-permissions-with-attribute-based-access-control-abac) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Attribute-Based Access Control (ABAC) strategies to scale AWS Lambda permission management in complex enterprise accounts. Uses resource tags and IAM policies to authorize Lambda actions, avoiding the overhead of managing extensive role definitions.
### Kubernetes Compliance

#### Infrastructure Translation

  - **(2023)** [==github.com/awslabs/specctl==](https://github.com/awslabs/specctl) <span class='md-tag md-tag--info'>⭐ 258</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-652425c6" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 10 L 20 10 L 30 7 L 40 12 L 50 2" fill="none" stroke="url(#spark-grad-652425c6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized security tool developed by AWS Labs to parse, extract, and map standard Kubernetes manifest objects or ECS task definitions directly into AWS infrastructure controls. Analyzes security and network isolation requirements.
### Secret Management

#### Go Runtime

  - **(2022)** [==aidansteele/secretsctx==](https://github.com/aidansteele/secretsctx) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A Go-based runtime library designed to inject dynamic secrets from external storage layers directly into context-aware serverless pipelines. By managing runtime secret validation outside main configuration structures, it significantly reduces code complexity.
## Serverless Architecture (1)

### API Gateway

#### REST APIs

  - **(2022)** [freecodecamp.org: How to Setup a Basic Serverless REST API with AWS Lambda and API Gateway](https://www.freecodecamp.org/news/how-to-setup-a-basic-serverless-backend-with-aws-lambda-and-api-gateway) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A beginner-oriented walkthrough demonstrating the integration of Amazon API Gateway with AWS Lambda. Illustrates how to build an HTTP endpoint, configure CORS, parse incoming JSON request payloads, and return standardized JSON responses to a frontend client.
### AWS Lambda (1)

#### Antipatterns

  - **(2021)** [Issues to Avoid When Implementing Serverless Architecture with AWS Lambda](https://aws.amazon.com/blogs/architecture/mistakes-to-avoid-when-implementing-serverless-architecture-with-lambda) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identifies critical pitfalls in serverless system designs, including over-allocated memory tiers, synchronous Lambda chaining, and poor database connection reuse. Offers concrete architectural remediations like asynchronous message queuing and utilizing RDS Proxy for connection pooling.
#### Cold Starts

  - **(2022)** [aws.amazon.com: New – Accelerate Your Lambda Functions with Lambda SnapStart](https://aws.amazon.com/blogs/aws/new-accelerate-your-lambda-functions-with-lambda-snapstart) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces AWS Lambda SnapStart, an optimization technique that dramatically reduces startup latency for Java runtimes by capturing and caching memory/disk snapshots of initialized microcontainers. Sub-second cold starts are achieved with minimal code changes.
#### Concurrency and Scaling

  - **(2023)** [aws.amazon.com: Understanding AWS Lambda scaling and throughput](https://aws.amazon.com/blogs/compute/understanding-aws-lambda-scaling-and-throughput) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Breaks down AWS Lambda's concurrency allocation models, describing burst limits, provisioned concurrency, and account-wide throttling mechanisms. Essential for architects designing low-latency architectures under erratic user workloads.
#### Configuration Management

  - **(2021)** [Deploying AWS Lambda layers automatically across multiple Regions](https://aws.amazon.com/blogs/compute/deploying-aws-lambda-layers-automatically-across-multiple-regions) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an automation framework for replicating Lambda Layers across multiple geographical AWS regions. Ensures dependency consistency, reduces manual overhead in multi-region failover setups, and leverages CloudFormation and Step Functions for automated version control.
#### Fundamentals (1)

  - **(2021)** [infoworld.com: Serverless computing with AWS Lambda, Part 1](https://www.infoworld.com/article/2254500/serverless-computing-with-aws-lambda.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational guide introducing AWS Lambda's core event-driven architecture, compute-on-demand scaling models, and pricing structures. It discusses cold start implications, resource allocation limits, and the initial shift away from persistent virtual machine infrastructure towards highly transient microservices.
#### Hardware Platforms

  - **(2021)** [Achieve up to 34% better price/performance with AWS Lambda Functions powered by AWS Graviton2 processor](https://aws.amazon.com/about-aws/whats-new/2021/09/better-price-performance-aws-lambda-functions-aws-graviton2-processor) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents the architectural benefits of running Lambda functions on ARM64-based Graviton2 processors. Demonstrates how compiled runtimes (Go, Rust) and interpreted runtimes (Node.js, Python) achieve superior cost-efficiency and reduced execution durations compared to traditional x86 architecture.
#### Java Runtimes

  - **(2022)** [infoworld.com: AWS Lambda kickstarts Java functions](https://www.infoworld.com/article/2337529/aws-lambda-kickstarts-java-functions.html) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the architectural impacts of AWS Lambda SnapStart on Java microservices. Addresses how this feature shifts the paradigm for enterprise Java, making frameworks like Spring Boot and Quarkus viable alternatives for low-latency serverless operations.
#### Performance Optimization (1)

  - **(2022)** [dashbird.io: 4 Tips for AWS Lambda Optimization for Production](https://dashbird.io/blog/optimizing-aws-lambda-for-production) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on advanced optimization techniques for AWS Lambda in high-throughput environments. It covers cold start mitigation, memory provisioning tuning to balance cost and performance, connection pooling for databases, and leveraging structured execution logs for real-time observability.
### Caching

#### Data Management

  - **(2022)** [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates architectural strategies for distributed caching within serverless applications. It highlights the use of Amazon ElastiCache (Redis) and DynamoDB Accelerator (DAX) to alleviate performance bottlenecks, reduce database round-trips, and maintain low latency in ultra-elastic stateless execution environments.
### Databases

#### Selection Criteria

  - **(2023)** [theserverlessmindset.com: Choosing the Best Database for Your Serverless Project](https://www.theserverlessmindset.com/p/best-serverless-database) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a comprehensive comparison of serverless-friendly databases, covering DynamoDB, Aurora Serverless, Supabase, and PlanetScale. Focuses on scaling limits, execution connection limits, cold-start latency, and transactional suitability.
### Event-Driven

#### Design Patterns

  - **(2022)** [dev.to: Event driven architectures using AWS with example](https://dev.to/aws-builders/event-driven-architectures-using-aws-with-example-3d2d) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Breaks down standard Event-Driven Architecture (EDA) paradigms, demonstrating asynchronous patterns utilizing AWS EventBridge, SQS, and Lambda. Illustrates decoupling domains to achieve maximum system scalability and operational tolerance.
### Messaging and Integration

#### Webhooks

  - **(2022)** [dev.to: Manage webhooks at scale with AWS Serverless](https://dev.to/aws-builders/manage-webhooks-at-scale-with-aws-serverless-fof) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details a resilient cloud architecture designed to consume, validate, and process high-volume webhook traffic. Employs Amazon API Gateway to ingest requests, Amazon SQS to decouple workloads, and AWS Lambda to asynchronously process events, minimizing drop rates during traffic spikes.
### Orchestration

#### AWS Step Functions

  - **(2024)** [AWS Step Functions](https://aws.amazon.com/step-functions) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A managed serverless orchestration service that simplifies state machine design for multi-step microservices. It coordinates complex distributed workflows, manages execution state, handles built-in retries, and integrates natively with over 200 AWS services to prevent deep nesting of Lambda functions.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Azure](./azure.md)

