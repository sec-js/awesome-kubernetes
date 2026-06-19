# Container Runtimes/Managers, Base Images and Container Tools. Podman, Buildah and Skopeo

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/container-managers/).

!!! info "Architectural Context"
    Detailed reference for Container Runtimes/Managers, Base Images and Container Tools. Podman, Buildah and Skopeo in the context of The Container Stack.

## Table of Contents

1. [Application Development](#application-development)
  - [PHP](#php)
    - [Kubernetes Integration](#kubernetes-integration)
1. [Container Infrastructure](#container-infrastructure)
  - [Container Engines](#container-engines)
    - [Secret Management](#secret-management)
  - [Container Tooling](#container-tooling)
    - [Compose Comparison](#compose-comparison)
    - [Docker Compose Compatibility](#docker-compose-compatibility)
    - [Podman Compose](#podman-compose)
  - [Edge Orchestration](#edge-orchestration)
    - [Auto-Updates and Rollbacks](#auto-updates-and-rollbacks)
  - [Image Distribution](#image-distribution)
    - [Ecosystem Registries](#ecosystem-registries)
  - [Image Optimization](#image-optimization)
    - [Base Images](#base-images)
    - [Red Hat UBI](#red-hat-ubi)
  - [Image Synthesis](#image-synthesis)
    - [Builder Comparison](#builder-comparison)
    - [Language-Specific Builders](#language-specific-builders)
  - [Kubernetes Integration](#kubernetes-integration-1)
    - [Declarative Pods](#declarative-pods)
    - [Manifest Translation](#manifest-translation)
  - [Service Orchestration](#service-orchestration)
    - [Quadlet Integration](#quadlet-integration)
1. [Containerization](#containerization)
  - [Container Engines](#container-engines-1)
    - [Strategy and Standards](#strategy-and-standards)
  - [Runtimes](#runtimes)
    - [High-Level Engines](#high-level-engines)
    - [Kubernetes Integration](#kubernetes-integration-2)
1. [Microservices](#microservices)
  - [Mocking and Testing](#mocking-and-testing)
    - [Podman Compose Integration](#podman-compose-integration)

## Application Development

### PHP

#### Kubernetes Integration

  - **(2026)** [==sherifabdlnaby/kubephp==](https://github.com/sherifabdlnaby/kubephp) <span class='md-tag md-tag--info'>⭐ 456</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b979da19" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 4 L 20 11 L 30 7 L 40 5 L 50 4" fill="none" stroke="url(#spark-grad-b979da19)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PHP CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — KubePHP is a specialized repository detailing optimal configurations for deploying PHP applications (particularly PHP-FPM and Nginx sidecars) onto Kubernetes clusters. It addresses PHP-specific cloud-native challenges such as shared volume sessions, OPcache preloading, and graceful shutdown handling. It provides critical scaffolding and architectural advice for modernizing legacy PHP monoliths into production-grade, autoscaled microservices.
## Container Infrastructure

### Container Engines

#### Secret Management

  - **(2021)** [redhat.com: Exploring the new Podman secret command 🌟](https://www.redhat.com/en/blog/new-podman-secrets-command) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth look at the `podman secret` command subsystem, which manages sensitive credentials securely on the local host keyring rather than hardcoding them in images. This pattern brings Kubernetes-style secret mounting to systemd and standalone container workloads, preventing credentials leakage in microservice environments.
### Container Tooling

#### Compose Comparison

  - **(2021)** [crunchtools.com: Should I Use Docker Compose Or Podman Compose With Podman?](https://crunchtools.com/should-i-use-docker-compose-or-podman-compose-with-podman) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This architectural comparison contrasts the usage of Podman Compose with Docker Compose running on Podman's virtualized API socket. The synthesis recommends leveraging the Docker-compatible socket configuration in enterprise environments for high-fidelity compatibility with complex multi-container definitions.
#### Docker Compose Compatibility

  - **(2021)** [redhat.com: Using Podman and Docker Compose](https://www.redhat.com/en/blog/podman-docker-compose) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — This technical brief details the integration of Podman with Docker Compose via the virtualization of a Docker-compatible UNIX socket (`podman.sock`). By enabling this systemd-managed service, developers can execute legacy multi-container environments defined in Docker Compose files without modification, shifting the workload under Podman's daemonless, secure execution model.
  - **(2021)** [youtube: Podman 3 and Docker Compose - How Does the Dockerless Compose Work? 🌟](https://www.youtube.com/watch?v=15PFfjuxtvM&ab_channel=mkdev) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This video tutorial covers the REST API capabilities introduced in Podman 3 and its virtualized Docker-compatible socket. It provides step-by-step demonstrations running unmodified Docker Compose setups under Podman, illustrating the underlying socket mapping mechanics that enable seamless developer workflows.
  - **(2021)** [fedoramagazine.org: Use Docker Compose with Podman to Orchestrate Containers on Fedora Linux](https://fedoramagazine.org/use-docker-compose-with-podman-to-orchestrate-containers-on-fedora) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An implementation manual focused on configuring Docker Compose pipelines to run on Fedora Linux workstations utilizing Podman's unprivileged user sockets. It explains how to bypass typical daemon-related attack vectors while maintaining high-fidelity support for standard multi-service YAML specs.
#### Podman Compose

  - **(2021)** [fedoramagazine.org: Manage containers with Podman Compose](https://fedoramagazine.org/manage-containers-with-podman-compose) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This resource reviews the configuration of Podman Compose, a Python-based utility developed to interpret YAML schemas and execute local multi-container groupings. While it functions as a lightweight alternative, live grounding highlights that modern enterprise setups prefer native Docker Compose with `podman.sock` compatibility due to its deeper feature coverage.
### Edge Orchestration

#### Auto-Updates and Rollbacks

  - **(2021)** [redhat.com: How to use auto-updates and rollbacks in Podman](https://www.redhat.com/en/blog/podman-auto-updates-rollbacks) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Podman's automated container lifecycle features designed for distributed edge environments. By coordinating with registry tags and systemd health checks, Podman triggers zero-touch image updates and automatic rollback workflows if service validation tests fail.
### Image Distribution

#### Ecosystem Registries

  - **(2022)** [Red Hat Ecosystem Catalog](https://catalog.redhat.com/en/software/containers/explore)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The access portal to the Red Hat Ecosystem Catalog, providing a registry of verified, security-scanned container images. This resource is an enterprise-stable source for deploying secure database runtimes, middleware, and application frameworks on production clusters.
### Image Optimization

#### Base Images

  - **(2023)** [iximiuz.com: In Pursuit of Better Container Images: Alpine, Distroless, Apko, Chisel, DockerSlim, oh my!](https://iximiuz.com/en/posts/containers-making-images-better) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep technical comparison of minimalist base image architectures (apko, Distroless, Chisel, DockerSlim) and their role in shrinking microservice attack surfaces. This guide walks through the trade-offs between packaging minimum system packages and compiling entirely distroless, binary-only configurations.
#### Red Hat UBI

  - **(2021)** [ubi-micro: RHEL tiny images to build containers 🌟](https://github.com/fatherlinux/ubi-micro) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source repository dedicated to UBI-Micro, Red Hat's smallest, zero-dependency base image layer designed for extreme attack surface minimization. It contains only essential package databases and relies on host-side tools like Buildah to inject necessary microservice binaries.
  - **(2019)** [Introducing the Red Hat Universal Base Image 🌟](https://www.redhat.com/en/blog/introducing-red-hat-universal-base-image)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An overview introducing the Red Hat Universal Base Image (UBI), designed to provide enterprise RHEL security configurations without subscription constraints. UBI delivers a reliable foundation for packaging and distributing cloud-native microservices across multi-cloud environments.
### Image Synthesis

#### Builder Comparison

  - **(2020)** [itnext.io: Docker, Kaniko, Buildah](https://itnext.io/docker-kaniko-buildah-209abdde5f94) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares Docker, Kaniko, and Buildah for image compilation in modern CI/CD setups. It highlights Buildah's capability to compile OCI images without a daemon or complex kernel privileges, making it the premier choice for Kubernetes-native build steps.
#### Language-Specific Builders

  - **(2022)** [blog.kubesimplify.com: Getting started with ko: A fast container image builder for your Go applications](https://blog.kubesimplify.com/getting-started-with-ko-a-fast-container-image-builder-for-your-go-applications) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates `ko`, an open-source image synthesis compiler built to package Go applications without requiring Docker or a local daemon. By compiling and pushing binaries directly to registries, it simplifies Go-based microservice shipping with built-in Software Bill of Materials (SBOM) generation.
### Kubernetes Integration (1)

#### Declarative Pods

  - **(2021)** [redhat.com: Build Kubernetes pods with Podman play kube](https://www.redhat.com/en/blog/podman-play-kube-updates) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the `podman play kube` command, which allows Podman to parse and deploy standard Kubernetes YAML definitions locally. This capability allows engineers to test and validate multi-container Kubernetes pod networks in a lightweight, local environment without a running Kubernetes cluster.
#### Manifest Translation

  - **(2021)** [redhat.com: From Docker Compose to Kubernetes with Podman](https://www.redhat.com/en/blog/compose-kubernetes-podman) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This guide covers the migration workflow from local Docker Compose files to production-ready Kubernetes manifests using Podman's native capability `podman generate kube`. This mechanism allows engineering teams to export local container configurations directly into standardized Kubernetes Pod specifications, accelerating the orchestration of modern microservices.
### Service Orchestration

#### Quadlet Integration

  - **(2023)** [redhat.com/sysadmin/quadlet-podman](https://www.redhat.com/en/blog/quadlet-podman) <span class='md-tag md-tag--warning'>[INI CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth review of Quadlet, a tool built into Podman that integrates container management with systemd. Quadlet reads declarative configuration files to dynamically synthesize optimized systemd service definitions, resolving complex container network and dependency issues automatically.
## Containerization

### Container Engines (1)

#### Strategy and Standards

  - **(2019)** [Why Red Hat is investing in CRI-O and Podman](https://www.redhat.com/en/blog/why-red-hat-investing-cri-o-and-podman) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A strategic analysis detailing Red Hat's engineering shift from Docker to CRI-O and Podman. It explores the security advantages of rootless architectures, the reduction of single-point-of-failure daemons, and the architectural benefits of aligning runtimes strictly to Kubernetes-compatible CRI specifications.
### Runtimes

#### High-Level Engines

  - **(2017)** [containerd.io](https://containerd.io) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official home page and core design documentation for the containerd runtime engine. It details the modular runtime API architecture, gRPC interfaces, client-side abstractions, and storage drivers that enable major cloud providers and local workstations to run containers at massive scale.
#### Kubernetes Integration (2)

  - **(2024)** [Kubernetes.io: Container runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official Kubernetes documentation detailing installation and integration patterns for CRI-compliant container runtimes. It provides step-by-step production setup configurations for containerd and CRI-O, detailing necessary kernel parameters, socket configurations, and systemd driver alignments.
## Microservices

### Mocking and Testing

#### Podman Compose Integration

  - **(2021)** [developers.redhat.com: Using Podman Compose with Microcks: A cloud-native API mocking and testing tool](https://developers.redhat.com/blog/2021/04/22/using-podman-compose-with-microcks-a-cloud-native-api-mocking-and-testing-tool) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates executing Microcks, a cloud-native API mocking and testing tool, with Podman Compose in unprivileged host environments. This integration enables developers to simulate OpenAPI, gRPC, and AsyncAPI services locally without the overhead or security risks of managing a complex virtualized Docker daemon.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

