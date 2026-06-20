---
description: "Curated, AI-ranked Dotnet resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Developer Ecosystem)."
---
# Microsoft .NET

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/dotnet/).

!!! info "Architectural Context"
    Detailed reference for Microsoft .NET in the context of Developer Ecosystem.

## Application Development

### .NET Framework

#### Architectural Guides

  - **(2024)** [==docs.microsoft.com: .NET Microservices: Architecture for Containerized .NET Applications==](https://learn.microsoft.com/en-us/dotnet/architecture/microservices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The definitive architectural design guide for planning and building containerized .NET microservices. Focuses on Domain-Driven Design (DDD) principles, CQRS patterns, Outbox event delivery, and deployment best practices inside Docker environments.
#### Event-Driven Microservices

  - **(2022)** [==itnext.io: How to Build an Event-Driven ASP.NET Core Microservice Architecture==](https://itnext.io/how-to-build-an-event-driven-asp-net-core-microservice-architecture-e0ef2976f33f) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Explains how to construct an event-driven ASP.NET Core microservices network using message brokers like RabbitMQ or Apache Kafka. Integrates clean architecture practices, transactional Outbox patterns, and retry strategies to ensure reliable messaging.
#### Microservices Design

  - **(2021)** [**telerik.com: Your First Microservice in .NET 6**](https://www.telerik.com/blogs/your-first-microservice-dotnet-6) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A hands-on guide to building a microservice using ASP.NET Core 6 Minimal APIs. Demonstrates how to write lightweight, highly optimized web APIs with minimal boilerplate code, perfect for deployment within containerized clusters.
#### gRPC Communication

  - **(2021)** [**blog.jetbrains.com: Getting Started with ASP.NET Core and gRPC**](https://blog.jetbrains.com/dotnet/2021/07/19/getting-started-with-asp-net-core-and-grpc) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Presents a technical guide on configuring high-performance gRPC services using ASP.NET Core. Details protobuf schema creation, client generation, and HTTP/2 connection pooling to achieve ultra-low latency between microservices.
## Cloud Infrastructure and Orchestration

### Container Orchestration

#### Kubernetes

  - **(2021)** [dotnetcurry.com: Kubernetes for ASP.NET Core Developers – Introduction, Architecture, Hands-On](https://www.dotnetcurry.com/aspnet-core/kubernetes-for-developers) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An educational guide targeted at .NET architects migrating legacy backends to Kubernetes. Details fundamental infrastructure layers including Pods, ReplicaSets, Deployments, Services, and containerization pipelines using Docker.
## Software Architecture and .NET Development

### Application Diagnostics

#### Environment Validation

  - **(2021)** [jeremydmiller.com: Self Diagnosing Deployments with Oakton and Lamar](https://jeremydmiller.com/2021/10/12/self-diagnosing-deployments-with-oakton-and-lamar) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents a design paradigm combining Lamar's compilation-safe IoC container with Oakton's self-diagnostics capability. Outlines systems validation strategies that trigger build failures if container registrations or service setups fail.
#### IoC Containers

  - **(2025)** [Lamar](https://jasperfx.github.io/lamar) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced, high-performance IoC container and assembly scanning engine compatible with Microsoft's DI standards. Leverages Roslyn-powered dynamic code compilation to optimize dependency resolution pathways in microservices.
### Microservices

#### Resilience Patterns

  - **(2026)** [==App-vNext/Polly==](https://github.com/App-vNext/Polly) <span class='md-tag md-tag--info'>⭐ 14192</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a2a0e361" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 13 L 20 6 L 30 7 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-a2a0e361)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier resilient fault-handling library for the .NET ecosystem. Enables developers to configure sophisticated reliability policies including Retry, Circuit Breaker, Timeout, Bulkhead Isolation, and Fallback, acting as the bedrock for stable microservices.
  - **(2022)** [procodeguide.com: Build Resilient Microservices (Web API) using Polly in ASP.NET Core](https://procodeguide.com/programming/polly-in-aspnet-core) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides a hands-on architectural approach to integrating Polly policy frameworks inside ASP.NET Core Web APIs. Details proper HttpClientFactory patterns, fallback strategies, and configuring resilient endpoint routing.
### Web Frameworks

#### Microservices (1)

  - **(2024)** [Paradigm framework](https://www.paradigm.net.co) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source development platform designed to facilitate rapid, highly structured .NET microservice engineering. Standardizes dependency configurations, modular architectures, data mapping protocols, and enterprise repository patterns.

---
💡 **Explore Related:** [Postman](./postman.md) | [Angular](./angular.md) | [Embedded Servlet Containers](./embedded-servlet-containers.md)

🔗 **See Also:** [About](./about.md) | [Cloudflare](./cloudflare.md)

