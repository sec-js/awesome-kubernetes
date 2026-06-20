---
description: "Top Docker resources for 2026, AI-ranked: Awesome Compose, jib and more — curated Cloud Native tools, guides and references."
---
# Docker

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/docker/).

!!! info "Architectural Context"
    Detailed reference for Docker in the context of The Container Stack.

## App Development

### CICD

#### GitHub Actions

  - **(2026)** [==**GitHub build-push-action**==](https://github.com/docker/build-push-action) <span class='md-tag md-tag--info'>⭐ 5304</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bdf56c78" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 8 L 20 7 L 30 6 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-bdf56c78)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The industry standard GitHub Action for building and pushing container images. Supports Docker Buildx, multi-platform builds, cache importing/exporting configurations, and native OCI-compliant registry deployments.
## Application Architecture

### Microservices

#### Java Ecosystem

  - **(2020)** [adictosaltrabajo.com: Cómo crear y desplegar microservicios con Spring Boot, Spring Cloud Netflix y Docker](https://adictosaltrabajo.com/2020/12/22/como-crear-y-desplegar-microservicios-con-spring-boot-spring-cloud-netflix-y-docker) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep-dive tutorial on building and orchestrating microservices in the Java ecosystem. Integrates Spring Boot applications with Spring Cloud Netflix (Eureka, Zuul) and packages them into containerized environments with custom Docker Compose manifests.
## Application Development

### Java

#### Image Building

  - **(2026)** [==jib==](https://github.com/GoogleContainerTools/jib) <span class='md-tag md-tag--info'>⭐ 14409</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b14e31cf" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 11 L 20 9 L 30 2 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-b14e31cf)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Jib is a fast, specialized build tool by Google that constructs optimized Docker and OCI images for Java applications without requiring a Docker daemon or Dockerfile. Integrating directly into Maven or Gradle builds, it divides Java applications into granular layers (dependencies, resources, classes) to speed up continuous iteration. It is an industry-standard practice for enterprise JVM application deployment pipelines.
### Node.js

#### Image Building (1)

  - **(2026)** [dev.to/pmbanugo: Goodbye Dockerfiles: Build Secure & Optimised Node.js Container Images with Cloud Native Buildpacks](https://dev.to/pmbanugo/goodbye-dockerfiles-build-secure-optimised-nodejs-container-images-with-cloud-native-buildpacks-489p) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on guide illustrating how to deploy secure, optimized Node.js container applications without writing custom Dockerfiles, utilizing Cloud Native Buildpacks. It demonstrates how buildpacks automatically handle package caching, optimize production dependencies, and strip non-essential files. This results in smaller, audit-ready Node images with minimum developer overhead.
### Python

#### Local Environments

  - **(2026)** [codesolid.com: How To Use Docker and Docker Compose With Python](https://codesolid.com/how-to-use-docker-with-python) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This tutorial outlines the process of containerizing Python-based workloads (Flask, Django, or FastAPI) and managing them with Docker Compose. It guides the reader through structuring multi-stage Dockerfiles to optimize image layers, implementing virtual environment packaging, and handling dependency caching. It serves as an architectural blueprint for packaging Python backends cleanly and consistently.
## CI-CD

### DevOps Pipelines

#### Container Delivery

  - **(2023)** [dev.to: Building a Robust CI/CD Pipeline with Docker: A Comprehensive Guide](https://dev.to/itsahsanmangal/building-a-robust-cicd-pipeline-with-docker-a-comprehensive-guide-4k8b) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architects high-performance integration pipelines utilizing localized image-building agents. Emphasizes step caching, secure build variable injection, and automated image lifecycle promotion directly to secure registries.
## Cloud Orchestration

### Multi-Cloud Deployments

#### Application Architecture (1)

  - **(2021)** [freecodecamp.org: Learn How to Deploy 12 Apps to AWS, Azure, & Google Cloud](https://www.freecodecamp.org/news/learn-how-to-deploy-12-apps-to-aws-azure-google-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An extensive multi-cloud deployment course demonstrating how to package and release applications across AWS, Azure, and Google Cloud container environments (ECS, Container Apps, and Cloud Run).
## Containers

### Architectural Patterns

#### Anti-patterns

  - **(2023)** [codefresh.io: Docker anti-patterns 🌟](https://octopus.com/blog/docker-anti-patterns) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identifies architectural antipatterns that degrade container system health, performance, and flexibility. Warns against embedding configuration states, mixing application processes, and handling secrets insecurely.
### Build Optimization

#### Java (1)

  - **(2023)** [piotrminkowski.com: Slim Docker Images for Java](https://piotrminkowski.com/2023/11/07/slim-docker-images-for-java) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical evaluation of JVM microservice configurations. Uses jlink and GraalVM native compilations to generate minimal container environments for Java workloads.
#### Kubernetes Deployment

  - **(2023)** [learnk8s.io: 3 simple tricks for smaller Docker images 🌟](https://learnkube.com/blog/smaller-docker-images) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents three highly concrete engineering actions to reduce footprint size. Addresses the use of alpine/distroless, pruning development environments, and optimizing layers.
  - **(2022)** [sequoia.makes.software: Reducing Docker Image Size (Particularly for Kubernetes Environments) 🌟](https://sequoia.makes.software/reducing-docker-image-size-particularly-for-kubernetes-environments) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines image sizing optimizations specifically within large-scale Kubernetes production networks. Highlights how smaller footprints accelerate pull cycles and deployment velocity.
#### Node.js (1)

  - **(2023)** [itsopensource.com: How to Reduce Node Docker Image Size by 10X](https://itsopensource.com/how-to-reduce-node-docker-image-size-by-ten-times) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates strategies to reduce Node.js runtime image sizes by up to 90%. Highlights multi-stage configurations, prune tools for dependencies, Alpine deployments, and build-time optimization.
#### Python (1)

  - **(2023)** [testdriven.io: Docker Best Practices for Python Developers](https://testdriven.io/blog/docker-best-practices) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details architectural recommendations for containerizing Python environments. Outlines wheel pre-compilation steps, proper usage of virtual environments in multi-stage execution, and secure user privilege levels.
#### Reference Implementation

  - **(2024)** [github.com/pabpereza/curated-dockerfiles-examples: Curated Dockerfiles examples](https://github.com/pabpereza/containers-best-practices) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly practical repository showing production-hardened Dockerfile recipes for standard enterprise frameworks. Emphasizes pipeline optimization, caching methods, and image size constraints.
#### Rust

  - **(2023)** [dev.to: Simplify Your Dockerfile wiyth Rust programming language| Kamesh Sampath](https://dev.to/kameshsampath/simplify-your-dockerfile-1j5k) <span class='md-tag md-tag--warning'>[RUST CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents Rust compilation patterns utilizing multi-stage Docker builds and Cargo Chef. Focuses on caching intermediate dependencies to drastically minimize development compiler times and deliver highly optimized target binaries.
#### Security and Hardening

  - **(2024)** [sysdig.com: Top 20 Dockerfile best practices 🌟](https://www.sysdig.com/learn-cloud-native/dockerfile-best-practices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An essential platform catalog of twenty fundamental guidelines to build highly secure, minimal container images. Emphasizes non-root process configuration, layer optimization, and safe handling of variables.
### Developer Tooling

#### Cloud Emulation

  - **(2024)** [==Floci - An AWS Local Emulator Alternative==](https://github.com/floci-io/floci) <span class='md-tag md-tag--info'>⭐ 14064</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-eeaf9b0a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 3 L 20 4 L 30 11 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-eeaf9b0a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An active and highly performant local alternative to localstack. Emulates AWS cloud service behavior locally using specialized lightweight container footprints.
### Diagnostics

#### Debugging Runtimes

  - **(2023)** [iximiuz.com: Docker: How To Debug Distroless And Slim Containers 🌟](https://iximiuz.com/en/posts/docker-debug-slim-containers) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces brilliant systems troubleshooting strategies for hardened distroless images containing no system shells. Details namespace sharing techniques, container attachment interfaces, and process-level inspection.
### Docker Basics

#### Workshops

  - **(2023)** [youtube: Docker 101 (Workshop) how an application can be run using Docker containers. First, you'll learn how to take an application all the way from source code to a running container. Docker-compose, networking, multi-stage and more 🌟](https://www.youtube.com/watch?v=0mxhS7H6bxM) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A cohesive workshop walking developers from local raw source files to complex multi-container runtime topologies. Demonstrates configuration directives for compose networks, volume persistent paths, and base dependency caching.
### Production Operations

#### Infrastructure

  - **(2023)** [dev.to: Top 8 Docker Best Practices for using Docker in Production 🌟](https://dev.to/techworld_with_nana/top-8-docker-best-practices-for-using-docker-in-production-1m39) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents eight engineering pillars for operating containers safely in dynamic environments. Features container read-only root filesystems, memory boundary controls, health check parameters, and logging architectures.
### Security and Hardening (1)

#### Node.js (2)

  - **(2023)** [clickittech.com: The Ultimate Docker Security Best Practices for Your Node.js Application](https://www.clickittech.com/devops/docker-security-best-practices) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical guide focused on hardening Node.js microservice containers. Details execution under non-root node users, trimming npm development modules, and managing runtime environment security.
#### Vulnerability Management

  - **(2024)** [snyk.io: 10 Docker Security Best Practices 🌟](https://snyk.io/blog/10-docker-image-security-best-practices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A vital guide on secure image design, highlighting automated vulnerability analysis tools, secure base selection frameworks, least-privilege principles, and structural dependency lifecycle policies.
## Infrastructure (1)

### Docker Compose

#### Reference Architectures

  - **(2026)** [==Awesome Compose 🌟==](https://github.com/docker/awesome-compose) <span class='md-tag md-tag--info'>⭐ 45540</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0f58c8e2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 11 L 20 10 L 30 13 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-0f58c8e2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Awesome Compose is an official, highly curated repository of declarative multi-container topologies using Docker Compose. It showcases optimal configuration patterns for databases, caching layers, application servers, and microservices (e.g., PostgreSQL, Redis, Elasticsearch, Go, Python, React). It represents a critical, high-impact reference architecture for platform engineers standardizing local development setups.
### Kubernetes

#### Container Management

  - **(2026)** [thenewstack.io: Deploy a Persistent Kubernetes Application with Portainer](https://thenewstack.io/deploy-a-persistent-kubernetes-application-with-portainer) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This step-by-step article illustrates how Portainer's web UI can be utilized to deploy a persistent application (e.g., WordPress with MySQL) onto a Kubernetes cluster. It demystifies the setup of Persistent Volume Claims (PVCs), service ingress, and network isolation, mapping these complex Kubernetes abstractions into accessible dashboard steps. It serves as an excellent onboarding tutorial for operations teams adapting to K8s paradigms.
### Local Environments (1)

#### Docker Compose (1)

  - **(2026)** [freecodecamp.org: a beginners guide to docker - how to create a client server side with docker compose](https://www.freecodecamp.org/news/a-beginners-guide-to-docker-how-to-create-a-client-server-side-with-docker-compose-12c8cf0ae0aa) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This practical tutorial outlines how to orchestrate a client-server application structure using Docker Compose. It guides developers through containerizing frontend assets and backend APIs separately, establishing a bridge network for internal communication, and handling persistent storage. The guide serves as a basic entry point for designing multi-container microservice patterns in development setups.
## Local Developer Environment

### Container Runtime Setup

#### Docker Compose (2)

  - **(2025)** [**DockSTARTer**](https://github.com/GhostWriters/DockSTARTer) <span class='md-tag md-tag--info'>⭐ 2560</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e14d560a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 9 L 20 8 L 30 2 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-e14d560a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A user-friendly CLI utility designed to simplify the configuration and installation of self-hosted server software via structured Docker Compose patterns. Serves as a solid entry point for containerization concepts in local server and edge hardware topologies.
## Security

### Container Security

#### Dockerfile optimization

  - **(2020)** [Broken by default: why you should avoid most Dockerfile example 🌟](https://pythonspeed.com/articles/dockerizing-python-is-hard) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Critically evaluates common Dockerfile patterns. Highlights failure vectors like poor caching strategies, bloated build images, and running containers as root. Offers concrete engineering improvements for Python.
#### RunAsUser

  - **(2020)** [americanexpress.io: **Do Not Run Dockerized Applications as Root** 🌟](https://americanexpress.io/do-not-run-dockerized-applications-as-root) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An essential security analysis explaining why running container workloads as root is highly vulnerable to privilege escalation. Highlights how OpenShift's default Security Context Constraints (SCCs) enforce rootless container profiles.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

