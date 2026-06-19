# AWS Messaging Services

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-messaging/).

!!! info "Architectural Context"
    Detailed reference for AWS Messaging Services in the context of Cloud Providers (Hyperscalers).

## Table of Contents

1. [Application Integration](#application-integration)
  - [Messaging Services](#messaging-services)
    - [AWS Integration](#aws-integration)
1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Infrastructure](#cloud-infrastructure)
  - [AWS](#aws)
    - [Event-Driven Architecture](#event-driven-architecture)
    - [Messaging Services](#messaging-services-1)

## Application Integration

### Messaging Services

#### AWS Integration

  - **(2025)** [**Amazon SQS FAQs**](https://aws.amazon.com/sqs/faqs) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The official FAQ suite detailing Amazon SQS's scaling behavior, FIFO queue logic, dead-letter configurations, encryption capabilities, and pricing metrics.
  - **(2023)** [dev.to: Getting started with SNS and SQS](https://dev.to/aws-builders/getting-started-with-sns-and-sqs-3m4i) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a practical introduction to setting up AWS Simple Notification Service (SNS) and Simple Queue Service (SQS) patterns, outlining operational configurations for messaging-driven microservices.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Limits in Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-limits.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.aws.amazon.com in the Kubernetes Tools ecosystem.
  - [enlear.academy: How To Build a Scalable Email Notification Service Using' AWS](https://enlear.academy/how-to-build-a-scalable-email-service-using-aws-d404b347a7fb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering enlear.academy: How To Build a Scalable Email Notification Service Using' AWS in the Kubernetes Tools ecosystem.
  - [faun.pub: Implementing Event Driven Architecture With AWS EventBridge —' Event-Driven Messaging Pattern](https://faun.pub/implementing-event-driven-architecture-with-aws-eventbridge-event-driven-messaging-pattern-9d29262bfade)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Implementing Event Driven Architecture With AWS EventBridge —' Event-Driven Messaging Pattern in the Kubernetes Tools ecosystem.
## Cloud Infrastructure

### AWS

#### Event-Driven Architecture

  - **(2020)** [Building an event-driven application with Amazon EventBridge](https://aws.amazon.com/blogs/compute/building-an-event-driven-application-with-amazon-eventbridge) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This AWS architecture blog details how to design and build serverless event-driven applications using Amazon EventBridge. It highlights the platform's ability to act as a centralized serverless event bus that simplifies decoupled communication across distributed microservices by routing events using declarative rules. The pattern eliminates custom routing code, improving structural robustness.
#### Messaging Services (1)

  - **(2022)** [dev.to: When to SNS or SQS](https://dev.to/aws-builders/when-to-sns-or-sqs-2aji) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical comparison of Amazon Simple Notification Service (SNS) and Simple Queue Service (SQS) within event-driven architectures. It details SNS's pub-sub push mechanism versus SQS's pull-based queueing model, analyzing throughput characteristics and decoupling strategies. This guide clarifies architectural patterns for integrating microservices via point-to-point and fan-out message routing.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [AWS Pricing](./aws-pricing.md) | [AWS Spain](./aws-spain.md)

