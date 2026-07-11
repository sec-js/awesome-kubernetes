---
description: "Top Demos resources for 2026, AI-ranked: OpenShift AI Examples, knative-tutorial and more — curated Cloud Native tools, guides and references."
---
# DevOps Demos. Boilerplates/Samples, Tutorials and Screencasts

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/demos/).

!!! info "Architectural Context"
    Detailed reference for DevOps Demos. Boilerplates/Samples, Tutorials and Screencasts in the context of Architectural Foundations.

## Application Architecture

### Event-Driven

#### GraphQL

  - **(2021)** [hasura.io: A Simple, Realtime, Event Driven Architecture with QR Codes](https://hasura.io/blog/a-simple-real-time-event-driven-architecture-with-qr-codes) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates the construction of a real-time QR generation microservice using Hasura's instant GraphQL engine and PostgreSQL event triggers. Illustrates stateless serverless handlers reacting to database write mutations in real-time.
## Application Delivery

### Asynchronous Messaging

#### Red Hat Fuse

  - **(2021)** [developers.redhat.com: Message broker integration made simple with Red Hat Fuse](https://developers.redhat.com/blog/2021/01/08/message-broker-integration-made-simple-with-red-hat-fuse) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Explores enterprise application integration patterns (EIP) utilizing Red Hat Fuse. Translates message formats, routes real-time data pipelines, and interfaces legacy middleware brokers with modern cluster queues.
### CICD Pipelines

#### Tekton Pipelines

  - **(2020)** [Build a Go application using OpenShift Pipelines](https://developers.redhat.com/blog/2020/05/26/build-a-go-application-using-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML / GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers through compiling and deploying Go applications on OpenShift Pipelines using Tekton. Outlines how to write Tasks, configure Workspaces, and trigger image builds securely within non-privileged containers.
  - **(2020)** [Set up continuous integration for .NET Core with OpenShift Pipelines](https://developers.redhat.com/blog/2020/09/24/set-up-continuous-integration-for-net-core-with-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML / C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated implementation guide for configuring CI pipelines for .NET Core projects using OpenShift Pipelines. Explores automated build testing, Nuget dependency resolution, and secure image registration.
### Database Schema Management

#### Liquibase Integration

  - **(2021)** [piotrminkowski.com: Continuous Delivery on Kubernetes with Database using ArgoCD and Liquibase](https://piotrminkowski.com/2021/12/13/continuous-delivery-on-kubernetes-with-database-using-argocd-and-liquibase) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demystifies database migration management within a continuous deployment paradigm. Showcases how to coordinate Liquibase database schema updates alongside application container lifecycle updates using Argo CD hooks.
### Deployment Strategies

#### Canary Deployments

  - **(2020)** [openshift.com: Simple Canary Deployments using Kubernetes StatefulSets on OpenShift](https://www.redhat.com/en/blog/simple-canary-deployments-using-kubernetes-statefulsets-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates an architectural pattern for running canary deployments on OpenShift using StatefulSets. Discusses how deterministic network identities and storage bindings facilitate controlled, traffic-weighted application releases.
### Developer Platforms

#### App Deployment

  - **(2021)** [shipa.io: Deploying a real-world application on Kubernetes](https://shipa.io/a-real-world-application-deployment-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Walks through deploying a multi-tier production-grade application on Kubernetes using Shipa framework abstraction policies instead of raw, complex manifests. (Live Grounding: Demonstrates early architectural trends aiming to simplify the developer experience by decoupling container configurations from platform management).
#### Local Development

  - **(2021)** [shipa.io: Developing and deploying applications to Kubernetes locally with Shipa and Minikube](https://shipa.io/deploying-applications-on-kubernetes) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Showcases local application delivery pipelines combining Minikube with Shipa's developer-focused abstractions. Allows engineers to deploy code without writing verbose YAML. (Live Grounding: Important context for 2026 Developer Platforms. Shipa was acquired by Snyk in 2023, shifting its core value towards Snyk AppRisk for secure cloud development).
### GitOps

#### Microservices Showcase

  - **(2020)** [rromannissen/rhoar-microservices-demo: GitOps for Microservices with Red' Hat Runtimes demo](https://github.com/rromannissen/rhoar-microservices-demo) <span class='md-tag md-tag--warning'>[JAVA / YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A demonstration repository featuring GitOps patterns for microservices configured with Red Hat Runtimes. Illustrates safe promotion processes and environment configuration syncing using Argo CD.
### Java on Kubernetes

#### Eclipse JKube Tools

  - **(2021)** [Building and Deploying a Weather Web Application onto Kubernetes/Red Hat OpenShift using Eclipse JKube](https://itnext.io/building-and-deploying-a-weather-web-application-onto-kubernetes-red-hat-openshift-using-eclipse-62bf7c924be4) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores compiling and deploying Java-based web workloads to OpenShift clusters via Eclipse JKube. Demonstrates zero-configuration manifest generation and automated containerization workflows.
  - **(2021)** [youtube: Deploy your Java applications to the Cloud using Eclipse JKube (petclinic) 🌟](https://www.youtube.com/watch?v=vgIwRX4LXfU) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual demonstration deploying the classic Spring Petclinic Java web application using Eclipse JKube. Walks through target setups, Maven goals, and seamless image creation directly on Kubernetes.
### Load Balancing

#### High Availability

  - **(2021)** [dev.to: Build a highly available Node.js application using Docker, NGINX and AWS ELB](https://dev.to/sowmenappd/build-a-highly-available-node-js-application-using-docker-nginx-and-aws-elb-3cjp) <span class='md-tag md-tag--warning'>[JAVASCRIPT/SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed tutorial on architectural multi-tiering. Focuses on setting up a containerized Node.js application behind an NGINX reverse proxy, balanced globally by an AWS Elastic Load Balancer (ELB) for resilient target routing. (Live Grounding: Focuses on classic VM-to-container cloud architectures, forming a vital cognitive bridge before migrating entirely to Kubernetes Ingress/Gateway APIs).
## Application Development

### Cloud-Native Java

#### Advanced Microservices

  - **(2023)** [piomin/sample-spring-microservices-new: Microservices with Spring Cloud' Advanced Demo Project](https://github.com/piomin/sample-spring-microservices-new) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An updated showcase of modern, distributed architectures using the newest Spring Cloud dependencies. Features advanced setups including Spring Cloud Gateway, distributed tracing integrations, and resilient fault-tolerant design patterns.
#### Spring Boot Microservices

  - **(2022)** [piomin/sample-spring-microservices-kubernetes: Microservices with Spring' Boot and Spring Cloud on Kubernetes Demo Project - piotrminkowski.com 🌟](https://github.com/piomin/sample-spring-microservices-kubernetes) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active and highly referenceable demo project exhibiting the deployment of Spring Boot microservices inside a Kubernetes cluster. Utilizes Spring Cloud Kubernetes for discovery, ConfigMaps for configurations, and Ribbon/Feign client integrations for service-to-service communication.
### Containerization

#### Java Spring Boot

  - **(2021)** [javatechonline.com: How To Deploy Spring Boot Application In Docker?](https://javatechonline.com/deploy-spring-boot-docker-spring-boot) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory walkthrough detailing how to containerize Java-based enterprise workloads. Focuses on constructing optimized Dockerfiles, multi-stage builds to minimize image footprint, and utilizing spring-boot-maven-plugin or buildpacks to generate production-ready container layers.
### Java

#### Build Automation

  - **(2021)** [spring.io: YMNNALFT: Easy Docker Image Creation with the Spring Boot Maven Plugin and Buildpacks](https://spring.io/blog/2021/01/04/ymnnalft-easy-docker-image-creation-with-the-spring-boot-maven-plugin-and-buildpacks) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Spring technical guide illustrating optimized, multi-layer OCI container creation using the Spring Boot Maven Plugin. Deconstructs how Spring integrates Cloud Native Buildpacks directly, bypassing custom Dockerfiles to produce secure, cached, performance-optimized runtimes.
#### Local Development (1)

  - **(2020)** [piotrminkowski.com: Spring Boot on Kubernetes with Buildpacks and Skaffold 🌟](https://piotrminkowski.com/2020/12/18/spring-boot-on-kubernetes-with-buildpacks-and-skaffold) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — High-velocity development workflow blueprint leveraging Cloud Native Buildpacks and Skaffold to accelerate Java Spring Boot coding loops on Kubernetes. Minimizes manual Dockerfile maintenance and streamlines instantaneous hot-reloading code modifications into active development clusters.
#### Microservices Demo

  - **(2020)** [**redhat-actions/spring-petclinic**](https://github.com/redhat-actions/spring-petclinic) <span class='md-tag md-tag--info'>⭐ 4</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1ad3be1d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 10 L 20 11 L 30 2 L 40 11 L 50 12" fill="none" stroke="url(#spark-grad-1ad3be1d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Red Hat's enterprise fork of the classical Spring Petclinic microservice framework, tailored for deployment patterns on Red Hat OpenShift and vanilla Kubernetes. Showcases optimized Containerfile definitions and integrated automated CI/CD pipelines.
#### Project Bootstrapping

  - **(2026)** [Spring Initializr 🌟](https://start.spring.io) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The premier initialization dashboard for the Spring ecosystem. Incorporates direct dependency bindings to native Kubernetes microservices components, generating pre-configured templates with container-ready, cloud-native properties.
### Microservices Showcase (1)

#### Spring Boot

  - **(2021)** [MapIt](https://github.com/siamaksade/mapit-spring) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — MapIt is an interactive Spring Boot microservice designed to demonstrate cloud-native design principles on OpenShift. Showcases routing, Horizontal Pod Autoscaling (HPA), and config management using platform resources.
### NodeJS

#### Deployment Tooling

  - **(2021)** [developers.redhat.com: Deploying Node.js applications to Kubernetes with Nodeshift and Minikube](https://developers.redhat.com/blog/2021/03/09/deploying-node-js-applications-to-kubernetes-with-nodeshift-and-minikube) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat guide presenting Nodeshift to streamline NodeJS application deployment inside a local development environment running Minikube. Explores the automatic build, package, and deployment of Node workloads using built-in OpenShift-style S2I (Source-to-Image) concepts adapted for Kubernetes.
### Process Automation

#### RHPAM

  - **(2020)** [github.com/jbossdemocentral: Red Hat Process Automation Manager Mortgage' Demo](https://github.com/jbossdemocentral/rhpam7-mortgage-demo) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A complex workflow automation demo featuring Red Hat Process Automation Manager (RHPAM) orchestrating a mortgage application system. Represents a solid blueprint for integrating process engines with cloud-native containers.
### Reference Templates

#### OpenShift 4.8

  - **(2021)** [developers.redhat.com: New application samples in Red Hat OpenShift 4.8](https://developers.redhat.com/articles/2021/10/01/new-application-samples-red-hat-openshift-48) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces new application developer templates launched in OpenShift 4.8. Explains how developers can instantly import, test, and containerize various languages directly within the OpenShift developer GUI console.
### Serverless Java

#### Quarkus Integration

  - **(2020)** [Develop and test a Quarkus client on Red Hat CodeReady Containers with Red Hat Data Grid 8.0](https://developers.redhat.com/blog/2020/06/19/develop-and-test-a-quarkus-client-on-red-hat-codeready-containers-with-red-hat-data-grid-8-0) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers through testing a lightweight Quarkus application against Red Hat Data Grid (Infinispan) on Red Hat CodeReady Containers (now OpenShift Local). Emphasizes rapid developer iteration loops, memory minimization, and high-performance transactional caching.
#### gRPC Communication

  - **(2023)** [piotrminkowski.com: Introduction to gRPC with Quarkus](https://piotrminkowski.com/2023/09/15/introduction-to-grpc-with-quarkus) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the integration of low-latency gRPC services inside Quarkus. Demonstrates schema-first API creation via Protocol Buffers, building high-performance non-blocking streaming services, and optimizing binary communication interfaces for modern microservices.
### Tutorials

#### Developer Demos

  - **(2023)** [Red Hat Tutorials & Examples: github.com/redhat-developer-demos 🌟](https://github.com/redhat-developer-demos) <span class='md-tag md-tag--warning'>[JAVA / GO / NODE.JS CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main repository for Red Hat Developer developer demos. Offers a variety of quickstarts covering modern Java/Go runtimes, microservices integration, Kubernetes-native deployments, and pipeline automation designs.
## Application Modernization

### Integration Frameworks

#### OpenShift and Camel

  - **(2021)** [developers.redhat.com: Modernizing applications with Apache Camel, JavaScript, and Red Hat OpenShift](https://developers.redhat.com/articles/2021/07/26/modernizing-applications-apache-camel-javascript-and-red-hat-openshift) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Examines legacy integration strategies and modern microservices orchestration utilizing Apache Camel K (native integrations) coupled with Node.js/JavaScript on Red Hat OpenShift. Discusses enterprise integration patterns (EIPs) within modern container systems.
### Spring to Quarkus

#### Framework Migration

  - **(2020)** [aytartana.wordpress.com: Migrating SpringBoot PetClinic REST to Quarkus](https://aytartana.wordpress.com/2020/08/26/migrating-springboot-petclinic-rest-to-quarkus) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed migration journal porting the classic Spring Boot PetClinic REST API to Quarkus. Provides valuable benchmarking metrics comparing memory footprints, startup latencies, and implementation adjustments required for compilation to GraalVM native images.
## Architecture

### Microservices

#### Demo Systems

  - **(2021)** [hbollon/k8s-voting-app-aws](https://github.com/hbollon/k8s-voting-app-aws) <span class='md-tag md-tag--info'>⭐ 34</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-dbb89f44" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 9 L 20 13 L 30 9 L 40 11 L 50 7" fill="none" stroke="url(#spark-grad-dbb89f44)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference multi-tier microservice architecture demonstrating AWS integration. Contains a polyglot microservice arrangement with Redis caches, PostgreSQL transactional engines, and reactive frontend layers structured for EKS deployments.
## CI-CD

### Azure AKS

#### GitHub Actions

  - **(2021)** [trstringer.com: Deploy to AKS from GitHub Actions 🌟](https://trstringer.com/deploy-to-aks-from-github-actions) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A precise deployment guide detailing continuous integration and deployment to AKS from GitHub Actions. Explores how to leverage secure Azure Service Principals and Federated Credentials (OIDC) to safely authenticate and update container workloads.
### Java (1)

#### Automated Workflows

  - **(2020)** [CI/CD for Kubernetes through a Spring Boot example (Banzai Cloud CI/CD)](https://teletype.in/@sravancynixit/CcwqFANxY) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Continuous Integration and Deployment guide utilizing Banzai Cloud automation pipelines for Spring Boot applications. Illustrates container building, secure credential handling, configuration injects, and blue-green application promotion tactics on Kubernetes.
## CICD

### GitOps (1)

#### GitLab Agent

  - **(2022)** [about.gitlab.com: GitOps with GitLab: Connect with a Kubernetes cluster](https://about.gitlab.com/blog/gitops-with-gitlab-connecting-the-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step documentation detailing the setup of the GitLab Agent for Kubernetes. Provides secure pull-based GitOps workflows, ensuring real-time configuration sync and immediate cluster telemetry reporting to the GitLab enterprise console.
## CICD Infrastructure

### Build and Packaging

#### Custom Packager

  - **(2025)** [Jenkins Custom WAR Packager](https://github.com/jenkinsci/custom-war-packager) <span class='md-tag md-tag--info'>⭐ 87</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-eb9ca518" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 13 L 20 12 L 30 13 L 40 2 L 50 6" fill="none" stroke="url(#spark-grad-eb9ca518)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Duplicate citation verification for the Custom WAR Packager. Serves as the primary operational tool used to generate custom, pre-hardened enterprise Jenkins distributions tailored with pre-allocated configurations.
## CICD Pipelines (1)

### Automated Cloud Deployments

#### AWS ECS Deployments

  - **(2022)** [freecodecamp.org: How to Setup a CI/CD Pipeline with GitHub Actions and AWS](https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed tutorial constructing CI/CD deployment pipelines on AWS. Uses GitHub Actions to build Docker images, securely push them to AWS ECR, and update application definitions across AWS ECS and Fargate infrastructure safely.
## Cloud Native Architecture

### Microservices Migration

#### Case Study

  - **(2023)** [Salaboy/From Monolith to K8s](https://github.com/Salaboy/from-monolith-to-k8s) <span class='md-tag md-tag--info'>⭐ 354</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2ba9f9fc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 5 L 20 5 L 30 8 L 40 13 L 50 8" fill="none" stroke="url(#spark-grad-2ba9f9fc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive practical blueprint mapping out the refactoring of monolithic architectures to Kubernetes-native services. Demonstrates key modernization steps including structural separation of services, data partitioning, and ingress configuration. This project is highly referenceable as a hands-on pedagogical resource for architectural transitions.
## Cloud Native Infrastructure

### Enterprise Messaging

#### Kafka on Kubernetes

##### APIs and Gateways

  - **(2020)** [HTTP-based Kafka messaging with Red Hat AMQ Streams](https://developers.redhat.com/blog/2020/08/04/http-based-kafka-messaging-with-red-hat-amq-streams) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This guide covers the deployment and operational use of the Strimzi Kafka Bridge within Red Hat AMQ Streams. It exposes an HTTP-based REST API to Kafka, enabling lightweight web clients and non-native applications to produce and consume messages without importing complex Kafka client SDKs. Highlights include API request schemas, JSON payload configuration, and HTTP/Kafka translation semantics.
### Observability and Testing

#### Pod Mocking

  - **(2024)** [**stefanprodan/podinfo**](https://github.com/stefanprodan/podinfo) <span class='md-tag md-tag--info'>⭐ 5917</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-afb540d1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 7 L 20 6 L 30 7 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-afb540d1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A premium go-to microservice web application written in Go, specifically designed to showcase best practices in Kubernetes deployment, health checking, instrumentation (Prometheus/Jaeger), and progressive delivery validation (such as Flagger/Istio canary releases).
## Cloud Native Platforms

### Red Hat OpenShift

#### Local Development (2)

##### CodeReady Containers

  - **(2021)** [Red Hat CodeReady Containers (Minishift equivalent for OpenShift 4.2 or newer) - step-by-step demo guides](https://github.com/marcredhat/crcdemos) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight positions this project as a step-by-step demo guide for Red Hat CodeReady Containers (CRC), representing the modern equivalent of local Minishift. Live Grounding reveals CRC is an essential local development environment simulating multi-node OpenShift setups. The demos illustrate localized microservice deployment and validation before pushing to enterprise stages.
## Cloud Platform

### Microsoft Azure

#### Sample Architecture

  - **(2026)** [github.com/Azure-Samples 🌟](https://github.com/Azure-Samples) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Central directory of Azure engineering samples. Provides production-ready templates, deployment scripts, and reference implementations spanning Serverless, Azure Kubernetes Service, container orchestration, and multi-tenant systems.
## Cloud Providers

### Google GKE

#### Application Dev

  - **(2021)** [github.com/MatthewCYLau: TypeScript Node Express Google Kubernetes Engine' (GKE)](https://github.com/MatthewCYLau/node-express-typescript-k8-gke) <span class='md-tag md-tag--info'>⭐ 11</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-409059fc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 6 L 30 10 L 40 2 L 50 10" fill="none" stroke="url(#spark-grad-409059fc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical developer bootstrap repository containing configurations to build, package, and orchestrate a containerized TypeScript Node Express API application on Google Kubernetes Engine (GKE) under standard ingress architectures.
## Cloud-Native Application Development

### Go Development

#### Microservices (1)

  - **(2023)** [github.com/learning-cloud-native-go/myapp: Learning Cloud Native Go -' myapp 🌟](https://github.com/learning-cloud-native-go/myapp) <span class='md-tag md-tag--info'>⭐ 1093</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-5e282842" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 8 L 20 7 L 30 4 L 40 10 L 50 4" fill="none" stroke="url(#spark-grad-5e282842)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A reference Go application engineered specifically to demonstrate cloud-native design principles, featuring integrated telemetry endpoints, structured JSON logging, health probes (/healthz, /ready), and graceful termination handles. (Live Grounding: Serves as a textbook design blueprint for Golang microservices deployed within Kubernetes environments).
### Open Source Software

#### Reference Implementations

  - **(2021)** [todaywasawesome/oss-apps: OSS Applications](https://github.com/todaywasawesome/oss-apps) <span class='md-tag md-tag--warning'>[YAML/HELM CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A collection of production-ready, open-source application stack blueprints formatted for modern container and cloud platform environments. (Live Grounding: Serves as a reference baseline for application engineers evaluating functional cloud-native topologies).
## Cloud-Native Applications

### Java Microservices

#### Azure Container Apps

  - **(2025)** [docs.microsoft.com: Deploy Spring microservices to Azure](https://learn.microsoft.com/en-us/azure/container-apps) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural reference documentation illustrating Spring microservice deployment strategies on Azure Container Apps (ACA). Compares managed Spring Cloud components with raw container configurations.
#### Container Images

  - **(2021)** [ref 4](https://hub.docker.com/r/alwin2/petclinic-customers-service) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Docker container image representing the Customer Service sub-domain of the decomposed Spring Petclinic microservices suite. Designed for direct cluster deployments to test service-to-service communication.
#### Kubernetes Deployment

  - **(2024)** [==github.com/spring-petclinic/spring-petclinic-kubernetes 🌟==](https://github.com/spring-petclinic/spring-petclinic-cloud) <span class='md-tag md-tag--info'>⭐ 168</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-46abb034" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 10 L 20 9 L 30 3 L 40 12 L 50 2" fill="none" stroke="url(#spark-grad-46abb034)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A benchmark microservices architecture implementation demonstrating Spring Cloud and Spring Boot integration on Kubernetes. Demonstrates externalized configuration via Spring Cloud Config, service discovery, API gateway routing, and distributed tracing. Ideal reference for containerizing JVM monoliths.
#### Spring Cloud

  - **(2025)** [==Spring PetClinic Microservices==](https://github.com/spring-petclinic/spring-petclinic-microservices) <span class='md-tag md-tag--info'>⭐ 2136</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1e92787f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 3 L 20 9 L 30 4 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-1e92787f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The canonical reference implementation of the Spring PetClinic application decomposed into microservices. It leverages Spring Cloud Eureka, Spring Cloud Gateway, and Spring Cloud Config Server to showcase resilient distributed patterns.
  - **(2020)** [Distributed version of Spring Petclinic built with Spring Cloud 🌟](https://github.com/odedia/spring-petclinic-microservices) <span class='md-tag md-tag--info'>⭐ 2</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6acdeb4e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 6 L 20 5 L 30 13 L 40 3 L 50 9" fill="none" stroke="url(#spark-grad-6acdeb4e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A community-maintained fork of the distributed Spring PetClinic codebase focusing on alternative Spring Cloud configurations. Provides a lean reference for configuring multi-module Gradle/Maven setups for local microservice debugging.
## Cloud-Native Infrastructure

### Kubernetes Core

#### Declarative Templates

  - **(2024)** [Kubernetes Examples](https://github.com/ContainerSolutions/kubernetes-examples) <span class='md-tag md-tag--info'>⭐ 1421</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3b90864a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 4 L 20 13 L 30 10 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-3b90864a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly utilized, production-tested blueprint repository containing foundational Kubernetes manifests. It spans standard ingress rules, complex stateful configurations, and container startup patterns. (Live Grounding: An essential reference repository for platform engineers bootstrapping cloud topologies with validated standards).
### Learning Resources

#### Kubernetes Courses

  - **(2024)** [**wardviaene/kubernetes-course**](https://github.com/wardviaene/kubernetes-course) <span class='md-tag md-tag--info'>⭐ 1732</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-9d6612bb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 12 L 20 8 L 30 9 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-9d6612bb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML/GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Accompanying codebase for Ward Viaene's comprehensive Kubernetes course, demonstrating deployments, configurations, microservice communication patterns, and cloud migrations. (Live Grounding: Widely trusted community-backed repository illustrating production-grade YAML configurations).
## DevOps

### CICD Platforms

#### Jenkins

##### Docker Containerization

  - **(2018)** [github.com/arun-gupta/docker-jenkins-pipeline: Docker + Java + Jenkins Pipeline](https://github.com/arun-gupta/docker-jenkins-pipeline) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight structures this repository around running Docker-integrated Java application compilation inside Jenkins Pipelines. Live Grounding shows that mounting the Docker socket inside Jenkins agents remains a common albeit security-sensitive approach. It serves as a historical and practical reference for building containerized Java workloads using declarative pipelines.
##### Modular Pipeline Library

  - **(2021)** [youtube: Modular Pipeline Library: 4. Petclinic Pipeline 🌟](https://www.youtube.com/watch?v=GLtvxY1S3Aw) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights this video showcase mapping the Modular Pipeline Library (MPL) against a real-world Petclinic continuous integration execution flow. Live Grounding validates that illustrating modular configuration structures gives developers a tangible example of pipeline inheritance. This pattern minimizes repetitive pipeline coding efforts across diverse teams.
##### Spring Petclinic Pipeline

  - **(2020)** [deors/deors-demos-petclinic jenkinsfile](https://github.com/deors/deors-demos-petclinic/blob/master/Jenkinsfile) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details a functional Jenkinsfile built specifically to build and compile the Spring Petclinic application. Live Grounding illustrates how multi-stage Docker builds can be integrated cleanly within a declarative Jenkins template to produce production-ready container images. It is a highly practical execution reference.
### Cloud Native CICD

#### Jenkins X

##### AWS EKS Integration

  - **(2021)** [Modernize Your CI/CD Pipeline Using Jenkins X with Amazon EKS](https://aws.amazon.com/blogs/apn/modernize-your-ci-cd-pipeline-using-jenkins-x-with-amazon-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight shares an AWS APN blog focusing on modernizing pipelines using Jenkins X with Amazon EKS. Live Grounding clarifies that Jenkins X differs entirely from classic Jenkins, utilizing Tekton, GitOps, and Kubernetes-native configurations under the hood. It acts as an instructional benchmark for organizations moving toward declarative development environments.
### Continuous Delivery

#### Infrastructure Provisioning

##### Crossplane Spinnaker Integration

  - **(2021)** [amazon.com: Declarative provisioning of AWS resources with Spinnaker and Crossplane](https://aws.amazon.com/blogs/opensource/declarative-provisioning-of-aws-resources-with-spinnaker-and-crossplane) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight showcases the declarative provisioning of AWS infrastructure using Spinnaker unified with Crossplane. Live Grounding shows that combining Crossplane's Kubernetes Control Plane model with Spinnaker's application pipelines represents an advanced platform engineering paradigm. This enables application developers to spin up dependencies dynamically without custom script hooks.
#### Spinnaker Setup

##### Kubernetes Native Deployment

  - **(2019)** [hackernoon: Using Spinnaker with Kubernetes for CI/CD](https://hackernoon.com/using-spinnaker-with-kubernetes-for-cicd-52w3uo9) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines utilizing Spinnaker's cloud native engine as an external continuous delivery pipeline for Kubernetes applications. Live Grounding validates that separating build execution (CI) from application delivery (CD) using a dedicated tool like Spinnaker prevents pipeline scaling bottlenecks. This pattern decouples deployment safety from runner nodes.
### Kubernetes Integration

#### AWS EKS

##### Jenkins Pipelines

  - **(2021)** [youtube: How to set up AWS Kubernetes Jenkins pipeline](https://www.youtube.com/watch?v=zI7_8M2KtRI&ab_channel=MicroserviceFactory) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents this video guide as a roadmap to deploying and running Jenkins pipelines on AWS EKS Kubernetes clusters. Live Grounding highlights the use of IAM Roles for Service Accounts (IRSA) to dynamically authorize cloud resource creation directly from Jenkins pods. This pattern avoids insecure long-lived static AWS access credentials.
## DevOps and Platform Engineering

### Interview Preparation

#### Reference Guides

  - **(2026)** [==bregman-arie/devops-exercises 🌟==](https://github.com/bregman-arie/devops-exercises) <span class='md-tag md-tag--info'>⭐ 82758</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7d8c130e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 8 L 20 12 L 30 9 L 40 12 L 50 3" fill="none" stroke="url(#spark-grad-7d8c130e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON/YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A massive curated repository containing thousands of questions, answers, and hands-on exercises covering Linux, Jenkins, Docker, Kubernetes, Ansible, Terraform, AWS, and system design. (Live Grounding: With over 82k stars, it stands in 2026 as the preeminent resource for preparing systems engineers and validating platform architecture skills).
## DevSecOps and Automation

### End-to-End Pipelines

#### Multi-Version Deployments

  - **(2023)** [mrcloudbook.com: Automating Tetris Deployments: DevSecOps with ArgoCD, Terraform, and Jenkins for Two Game Versions](https://mrcloudbook.com/automating-tetris-deployments-devsecops-with-argocd-terraform-and-jenkins-for-two-game-versions) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents an end-to-end DevSecOps execution path deploying two independent versions of a Tetris application. Coordinates Terraform for EKS infrastructure creation, Jenkins for CI builds, security scanning, and Argo CD for final GitOps delivery.
### Jenkins-based CI-CD

#### AWS and Jenkins

  - **(2020)** [bitbucket.org: setting up a cicd pipeline with spring mvc and kubernetes on aws](https://www.atlassian.com/blog/bitbucket/setting-up-a-ci-cd-pipeline-with-spring-mvc-jenkins-and-kubernetes-on-aws) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines constructing a complete continuous integration pipeline using Bitbucket, Jenkins, and AWS EKS. Covers maven compilation, Docker Hub image pushes, and automated rolling deployments on target host nodes.
#### Jenkins Architecture

  - **(2020)** [piotrminkowski.com: Continuous Integration with Jenkins on Kubernetes 🌟](https://piotrminkowski.com/2020/11/10/continuous-integration-with-jenkins-on-kubernetes) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details executing dynamically provisioned Jenkins agent pods inside a target Kubernetes cluster. Explores mounting credentials, executing parallel pipeline workloads, and cleanup phases to optimize compute budgets.
## DevSecOps and IDEs

### Google Cloud Code

#### Developer Experience

  - **(2024)** [==github.com/GoogleCloudPlatform/cloud-code-samples 🌟==](https://github.com/GoogleCloudPlatform/cloud-code-samples) <span class='md-tag md-tag--info'>⭐ 437</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c0cf791a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 12 L 30 4 L 40 8 L 50 2" fill="none" stroke="url(#spark-grad-c0cf791a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curated templates and setup workflows targeting GCP's Cloud Code extension. Helps developers structure containerized services locally before auto-deploying to Google Kubernetes Engine (GKE).
### Quality Assurance

#### Azure Cloud Testing

  - **(2024)** [==github.com/microsoft: Contoso Traders - Cloud testing tools demo app==](https://github.com/microsoft/contosotraders-cloudtesting) <span class='md-tag md-tag--info'>⭐ 168</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e6404a69" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 3 L 20 11 L 30 12 L 40 13 L 50 4" fill="none" stroke="url(#spark-grad-e6404a69)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive, multi-platform microservices demonstration application showcasing Azure cloud testing solutions. Features Playwright end-to-end tests, load testing scenarios, and automated regression validations.
## Developer Experience (1)

### Inner Loop Development

#### Local Tooling

  - **(2023)** [==Azure/Draft 🌟==](https://github.com/Azure/draft) <span class='md-tag md-tag--info'>⭐ 642</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2026e583" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 6 L 20 4 L 30 12 L 40 8 L 50 8" fill="none" stroke="url(#spark-grad-2026e583)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Azure Draft simplifies early-stage developer onboarding onto Kubernetes. By scanning source code directories, it automatically generates containerization assets including Dockerfiles, Kubernetes manifests, Helm charts, and deployment workflows.
## Enterprise Architecture

### Business Process Management

#### RHPAM (1)

  - **(2020)** [gitlab.com: Red Hat Process Automation Manager - Signal Marketing Demo](https://gitlab.com/bpmworkshop/rhpam-signal-marketing-demo) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A demonstration application built on Red Hat Process Automation Manager (RHPAM) modeling signal marketing workflows. Integrates Complex Event Processing (CEP) engine features, showcasing declarative state orchestration within microservice platforms.
## Event-Driven Architectures

### Cloud-Native Java (1)

#### Kafka with Spring Boot

  - **(2021)** [itnext.io: Event-Driven Architectures with Kafka and Java Spring-Boot — Revision 1](https://itnext.io/event-driven-architectures-with-kafka-and-java-spring-boot-revision-1-c0d43d103ee7) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights patterns and practices for integrating Apache Kafka with Spring Boot. Covers key concepts including transaction management, handling poison pills via dead-letter-queues (DLQs), message serialization/deserialization, and reactive messaging semantics.
### Go and CQRS

#### gRPC Microservices

  - **(2021)** [dev.to: Go, Kafka and gRPC clean architecture CQRS microservices with Jaeger tracing](https://dev.to/aleksk1ng/go-kafka-and-grpc-clean-architecture-cqrs-microservices-with-jaeger-tracing-45bj) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Implements high-throughput event sourcing and CQRS patterns in Go using gRPC, Apache Kafka, and PostgreSQL. Demonstrates how clean architecture and domain-driven design structure scalable systems, while integrating Jaeger for end-to-end distributed transaction tracing.
### Observability and Diagnostics

#### Kafka at Scale

  - **(2022)** [codeopinion.com: Troubleshooting Kafka with 2000 Microservices](https://codeopinion.com/troubleshooting-kafka-with-2000-microservices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A heavy-duty post-mortem and diagnostics reference analyzing event-driven topologies operating thousands of microservices. Addresses cluster starvation, schema registration bottlenecks, consumer lag detection, and the architectural overhead of massive multi-tenancy.
### Realtime Streams

#### FastAPI and Ably

  - **(2022)** [ably.com: Building a realtime ticket booking solution with Kafka, FastAPI, and Ably](https://ably.com/blog/realtime-ticket-booking-solution-kafka-fastapi-ably) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses transactional concurrency in reservation systems using Apache Kafka as an event broker, FastAPI for API management, and Ably for realtime WebSocket client updates. Solves standard problems like race conditions and high-throughput inventory allocation.
### Serverless Java (1)

#### Quarkus with Kafka

  - **(2021)** [piomin/sample-quarkus-serverless-kafka](https://github.com/piomin/sample-quarkus-serverless-kafka) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A reference implementation of reactive serverless pipelines using Quarkus, Knative, and Apache Kafka. Illustrates sub-second cold starts, reactive stream processing (using SmallRye Reactive Messaging), and optimized containerization tailored for Kubernetes native eventing.
## GitOps (2)

### Continuous Deployment

#### Flux v2

  - **(2023)** [flux2-kustomize-helm-example 🌟](https://github.com/fluxcd/flux2-kustomize-helm-example) <span class='md-tag md-tag--info'>⭐ 1268</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-98dba493" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 9 L 20 6 L 30 13 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-98dba493)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The canonical Flux v2 reference architecture. Provides production-tested blueprints for structuring multi-environment repositories, configuring Kustomize hierarchies, packaging Helm releases, and enforcing namespace isolation patterns.
## GitOps and Declarative Git

### Developer Platforms (1)

#### GitHub Actions (1)

  - **(2021)** [shipa.io: GitOps in Kubernetes, the easy way–with GitHub Actions and Shipa](https://shipa.io/gitops) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explores combining the ease of GitHub Actions workflows with Shipa's application management plane to implement secure GitOps pipelines. (Live Grounding: Proves early efforts in platform engineering to bridge continuous integration directly into abstract application runtimes).
### GitOps Tools

#### Flux and Helm

  - **(2022)** [mytechramblings.com: A practical example of GitOps using Azure DevOps, Azure Container Registry, Helm, Flux and Kubernetes](https://www.mytechramblings.com/posts/gitops-with-azure-devops-helm-acr-flux-and-k8s) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Presents a comprehensive GitOps architectural blueprint combining Azure DevOps, Helm, and ACR under the control of Flux inside a Kubernetes cluster to manage automated continuous rollouts. (Live Grounding: Flux v2 continues to represent a core declarative deployment vehicle, serving as a pillar for automated continuous delivery).
## Infrastructure and Operations

### Observability and Service Mesh

#### OpenShift ServiceMesh

  - **(2021)** [Monitoring Services like an SRE in OpenShift ServiceMesh](https://www.redhat.com/en/blog/monitoring-services-like-an-sre-in-openshift-servicemesh) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Unpacks Site Reliability Engineering (SRE) monitoring patterns using OpenShift Service Mesh. Synthesizes Istio, Kiali, and Prometheus telemetry to isolate performance bottlenecks and measure Golden Signals.
## Infrastructure and Platform

### Autoscaling

#### Event-Driven Scaling

  - **(2021)** [tomd.xyz: Event-driven integration on Kubernetes with Camel & KEDA 🌟](https://tomd.xyz/kubernetes-event-driven-keda) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to run Apache Camel integration microservices on Kubernetes, leveraging KEDA to dynamically scale Camel routes based on incoming message rates. Synthesizes enterprise integration patterns (EIP) with modern cloud-native autoscaling.
## Infrastructure as Code

### Serverless Deployment

#### Terraform and AWS Lambda

  - **(2022)** [dev.to: Creating a Rest API with Infrastructure as Code (Terraform) & Serverless (Lambda + Python) - Part 2 CI/CD](https://dev.to/aws-builders/creating-a-rest-api-with-infrastructure-as-code-terraform-serverless-lambda-python-part-2-cicd-g8h) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a modern serverless deployment loop, coupling HashiCorp Terraform with AWS API Gateway and Lambda functions. Part 2 focuses on constructing automated GitHub Actions CI/CD deployment pipelines for infrastructure and application code layers.
## Infrastructure as Code and CI-CD

### Developer Platforms (2)

#### CI-CD Pipelines

  - **(2021)** [shipa.io: A Developer focused CI/CD pipeline for Kubernetes](https://shipa.io/a-developer-focused-ci-cd-pipeline-for-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines designing application-centric CI/CD pipelines that leverage developer platform layers to remove raw Kubernetes configuration friction. (Live Grounding: Highlights the evolving landscape of platform engineering where developers focus on code deliverables while security/infrastructure is handled declaratively by platforms).
## Java Cloud Native

### Spring Cloud (1)

#### Kubernetes Integration (1)

  - **(2026)** [==github: Spring Cloud Kubernetes 🌟==](https://github.com/spring-cloud/spring-cloud-kubernetes) <span class='md-tag md-tag--info'>⭐ 3534</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7e7215a0" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 11 L 20 12 L 30 9 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-7e7215a0)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized integration library that allows Spring Cloud applications to run transparently on Kubernetes. It maps Kubernetes ConfigMaps and Secrets to Spring's Environment, and translates discovery mechanisms to native Kubernetes endpoints. It bridges the gap between Cloud Native infrastructure patterns and Java application logic.
## Local Development (3)

### Red Hat OpenShift Local

#### Process Automation (1)

  - **(2020)** [schabell.org: CodeReady Containers - Building a Cloud-Native Human Resources Process](https://www.schabell.org/2020/10/codeready-containers-building-cloud-native-hr-process.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details local development of a cloud-native Human Resources workflow using CodeReady Containers. Explains process containerization concepts on single-node platforms, though modern flows favor OpenShift Local frameworks.
## Networking

### Security

#### Recipes

  - **(2021)** [==ahmetb/kubernetes-network-policy-recipes 🌟==](https://github.com/ahmetb/kubernetes-network-policy-recipes) <span class='md-tag md-tag--info'>⭐ 6144</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a2f52f76" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 11 L 20 2 L 30 4 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-a2f52f76)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier open-source repository for reusable NetworkPolicy templates. Provides validated configuration files to handle common cloud-native security patterns.
## Observability

### Microservices Telemetry

#### Grafana Stack

  - **(2022)** [grafana.com: How Istio, Tempo, and Loki speed up debugging for microservices](https://grafana.com/blog/how-istio-tempo-and-loki-speed-up-debugging-for-microservices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details how to configure the unified Grafana observability stack (Loki for logs, Tempo for traces, Istio for mesh networking) to accelerate troubleshooting in microservices. Focuses on setting up automatic correlation IDs to jump from logs to tracing traces instantly.
### OpenTelemetry

#### Reliability Engineering

  - **(2022)** [itnext.io: OpenTelemetry — Understanding SLI and SLO with OpenTelemetry Demo](https://itnext.io/opentelemetry-understanding-sli-and-slo-with-opentelemetry-demo-74c1d0b263b0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural deep-dive evaluating Service Level Indicators (SLIs) and Service Level Objectives (SLOs) within an active OpenTelemetry distributed microservices demo. Explores Prometheus alerts, collector architecture, and structured telemetry processing.
## Orchestration

### AKS

#### Masterclass

  - **(2023)** [**github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟**](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A highly comprehensive masterclass repository containing declarative HCL files and manifests to deploy AKS with Azure Disks, Azure Files, Application Gateway ingress, and active Azure AD integration.
### Kubernetes

#### EKS Training

  - **(2025)** [eksworkshop.com](https://eksworkshop.com/) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — The canonical AWS EKS workshop framework. Outlines standard cluster orchestration procedures, highlighting network configurations (AWS VPC CNI), identity management (IAM Roles for Service Accounts - IRSA), and modern storage drivers (EBS/EFS CSI).
## Platform Engineering

### GitOps and CI-CD

#### AWS and Argo CD

  - **(2023)** [mrcloudbook.com: GitOps: Deploying Tetris on EKS Using ArgoCD](https://mrcloudbook.com/gitops-deploying-tetris-on-eks-using-argocd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A simplified tutorial mapping out the migration from manual deployments to automated GitOps workflows on AWS EKS using Argo CD. Focuses on setting up repositories, IAM credentials, and declarative reconciliations.
#### Argo CD and OpenShift Pipelines

  - **(2021)** [piotrminkowski.com: Kubernetes CI/CD with Tekton and ArgoCD 🌟](https://piotrminkowski.com/2021/08/05/kubernetes-ci-cd-with-tekton-and-argocd) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides the reader through building a Kubernetes-native CI/CD pipeline using Tekton for compiling, testing, and containerizing Java applications, combined with Argo CD for declarative GitOps delivery.
  - **(2020)** [developers.redhat.com: From code to production with OpenShift Pipelines and Argo CD](https://developers.redhat.com/blog/2020/09/10/from-code-to-production-with-openshift-pipelines-and-argo-cd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the deployment pipeline workflow integrating OpenShift Pipelines (based on Tekton) with Argo CD for declarative GitOps continuous delivery. The architecture promotes safe transitions from code repositories to production clusters via containerized build stages and automated resource reconciliation.
#### Multi-Cluster GitOps

  - **(2020)** [developers.redhat.com: Introduction to Tekton and Argo CD for multicluster development](https://developers.redhat.com/blog/2020/09/03/introduction-to-tekton-and-argo-cd-for-multicluster-development) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the synergy between Tekton tasks and Argo CD to drive multi-cluster continuous delivery. Defines the boundaries where Tekton controls cloud-native container builds while Argo CD manages drift resolution across remote target clusters.
#### Serverless Workflows

  - **(2020)** [developers.redhat.com: Building modern CI/CD workflows for serverless applications with Red Hat OpenShift Pipelines and Argo CD, Part 1](https://developers.redhat.com/blog/2020/10/01/building-modern-ci-cd-workflows-for-serverless-applications-with-red-hat-openshift-pipelines-and-argo-cd-part-1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates building CI/CD patterns for Knative-based serverless workloads using OpenShift Pipelines and Argo CD. Focuses on minimizing operational overhead and optimizing cold starts by isolating the build execution phase from deployment management.
### GitOps and Deployment

#### Flux Ecosystem

  - **(2020)** [A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux 🌟](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early step-by-step tutorial outlining GitOps workflows with original Flux tools. Offers historical context but must be updated to Flux v2 and the modern GitOps Toolkit conventions.
### Machine Learning Operations

#### OpenShift AI

  - **(2023)** [==OpenShift AI Examples==](https://github.com/CastawayEGR/openshift-ai-examples) <span class='md-tag md-tag--info'>⭐ 25</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d70ac3e8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 5 L 20 12 L 30 9 L 40 2 L 50 6" fill="none" stroke="url(#spark-grad-d70ac3e8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community collection of machine learning workflows and notebooks deployed on Red Hat OpenShift AI. Details deployment pipelines for distributed training, model serving, and GPU resource slicing.
## Quality Assurance (1)

### API Testing Automation

#### Newman Integration

##### Jenkins Pipelines (1)

  - **(2020)** [LerryAlexander: Postman + Newman API Automated Tests running on a Jenkins' Pipeline 🌟](https://github.com/LerryAlexander/postman_jenkins_api_tests) <span class='md-tag md-tag--info'>⭐ 3</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-04f3535c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 10 L 20 11 L 30 3 L 40 4 L 50 11" fill="none" stroke="url(#spark-grad-04f3535c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on running automated Postman test suites through Newman CLI inside a Jenkins Pipeline. Live Grounding confirms this is a standard integration step for end-to-end REST API verification. By surfacing test execution failures in Jenkins console output, teams can safely block regression deployments.
## Reference Architectures

### Industry Verticals

#### Healthcare

  - **(2022)** [gitlab.com/redhatdemocentral: Healthcare](https://gitlab.com/redhatdemocentral/portfolio-architecture-examples/-/blob/main/healthcare.adoc) <span class='md-tag md-tag--warning'>[ASCIIDOC CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly specialized reference architecture covering the integration of healthcare workflows, real-time messaging, and patient record databases on OpenShift. Explains how to reconcile strict data compliance directives (HL7/FHIR) with highly-scalable container orchestrations.
## Security (1)

### Vulnerabilities

#### Hacking Labs

  - **(2024)** [**The Kubernetes Goat**](https://github.com/madhuakula/kubernetes-goat) <span class='md-tag md-tag--info'>⭐ 5674</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d3ec5f02" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 5 L 30 6 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-d3ec5f02)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The premier interactive security training platform containing an intentionally vulnerable Kubernetes cluster. Designed as an educational sandbox to demonstrate real-world cluster vulnerabilities, RBAC privilege escalations, metadata exposure, and container breakout exploits.
## Serverless and Knative

### Serverless Frameworks

#### Knative Serving

  - **(2021)** [dev.to: What is Knative Serving? A Friendly Guide](https://dev.to/wiggitywhitney/9-waa-w-what-is-knative-serving-a-friendly-guide-28f6) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A conceptual guide to Knative Serving. Demystifies auto-scaling down to zero, request routing, and revision management, explaining serverless application delivery on Kubernetes in simple terms.
  - **(2020)** [aymen-segni.com: Deploying Serverless Services on Kubernetes using Knative](https://aymen-segni.com/index.php/2020/07/22/deploying-your-serverless-services-on-kubernetes-using-knative) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed technical analysis of running microservices as serverless functions on Kubernetes using Knative. Explains configuration pathways for Knative CRDs, route mapping, and automated scaling parameters.
#### Knative Tutorial

  - **(2023)** [==knative-tutorial==](https://github.com/redhat-developer-demos/knative-tutorial) <span class='md-tag md-tag--info'>⭐ 291</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2a3955d3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 7 L 20 12 L 30 7 L 40 13 L 50 11" fill="none" stroke="url(#spark-grad-2a3955d3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA / YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive repository tutorial focused on Knative. Delivers detailed, practical instructions for implementing Knative Serving, traffic splitting, event brokers, and scale-to-zero configurations.
### Serverless Java (2)

#### Knative Service

  - **(2021)** [piotrminkowski.com: Serverless Java Functions on OpenShift](https://piotrminkowski.com/2021/11/30/serverless-java-functions-on-openshift) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on optimizing Java applications for serverless execution using Knative on OpenShift. Explores Spring Boot and Quarkus execution patterns, emphasizing scale-to-zero capabilities and JVM resource management.
## Service Mesh

### Consul

#### Local Development (4)

  - **(2021)** [learn.hashicorp.com: Consul Service Discovery and Mesh on Minikube 🌟](https://developer.hashicorp.com/consul/tutorials/get-started-kubernetes/kubernetes-gs-deploy?in=consul%2Fkubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical HashiCorp tutorial teaching how to bootstrap and configure Consul Service Mesh inside Minikube. Details transparent proxy routing, catalog synchronization rules, and enforcing secure service-to-service cryptographic identities.
### GitOps (3)

#### Progressive Delivery

  - **(2023)** [github.com/stefanprodan/gitops-istio: A GitOps recipe for Progressive Delivery' with Flux v2, Flagger and Istio 🌟](https://github.com/stefanprodan/gitops-istio) <span class='md-tag md-tag--info'>⭐ 668</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-685cc944" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 3 L 20 9 L 30 6 L 40 8 L 50 13" fill="none" stroke="url(#spark-grad-685cc944)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced progressive delivery architectural recipe integrating Flux v2, Flagger, and Istio. Automates metric-driven canary releases, utilizing real-time Prometheus statistics to roll back failing application revisions with minimal user impact.
## Software Development

### Microservices (2)

#### Reference Architecture

##### Spring Petclinic

  - **(2022)** [spring-petclinic.github.io](https://spring-petclinic.github.io) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the official Spring Petclinic documentation as the premier reference application for modern Java software architectures. Live Grounding confirms its role as a testing bed for showcasing complex microservice interactions, database bindings, and telemetry configuration patterns.
##### Spring Petclinic Red Hat

  - **(2020)** [github.com/redhat-developer-demos/spring-petclinic 🌟](https://github.com/redhat-developer-demos/spring-petclinic) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps out Red Hat's customized developer demo fork of the Spring Petclinic project. Live Grounding indicates this version is heavily optimized for OpenShift deployments, featuring native integration with OpenShift build configs and Kubernetes secrets. It is ideal for illustrating red-hat native cloud development workflows.

---
💡 **Explore Related:** [About](./about.md) | [Kubernetes](./kubernetes.md) | [Kubernetes Tools](./kubernetes-tools.md)

🔗 **See Also:** [Postman](./postman.md) | [Angular](./angular.md)

