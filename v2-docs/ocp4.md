# OCP 4

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ocp4/).

!!! info "Architectural Context"
    Detailed reference for OCP 4 in the context of The Container Stack.

## App Migration

### Application Modernization

#### Quarkus

  - **(2020)** [developers.redhat.com: Spring Boot to Quarkus migrations and more in Red Hat’s migration toolkit for applications 5.1.0](https://developers.redhat.com/blog/2020/12/08/spring-boot-to-quarkus-migrations-and-more-in-red-hats-migration-toolkit-for-applications-5-1-0)  <span class='md-tag md-tag--critical'>[LEGACY]</span> — An exploration of Red Hat's Migration Toolkit for Applications 5.1.0, focusing on automating the migration path from legacy Spring Boot dependencies to lightweight, Kubernetes-native Quarkus microservices to reduce resource overhead.
## Artifact Management

### Container Registries

#### Red Hat Quay

  - **(2022)** [OpenShift Registry & Quay](https://nubenetes.com/registries/) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comprehensive analysis of Red Hat Quay and the integrated OpenShift Container Registry. Details secure image storage, vulnerability scanning with Clair, and geo-replication capabilities. It highlights Quay's enterprise-grade multi-tenancy and RBAC controls, which ensure secure artifact promotion within high-performance microservices pipelines.
## Cloud Native Application

### Serverless

#### OpenShift Serverless

  - **(2020)** [Serverless applications made faster and simpler with **OpenShift Serverless GA**](https://developers.redhat.com/blog/2020/04/30/serverless-applications-made-faster-and-simpler-with-openshift-serverless-ga)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introducing OpenShift Serverless GA, this resource outlines the packaging of Knative into an enterprise-supported product. It details the integration of OpenShift's default routing layer, integration with service mesh (Istio), and developer console enhancements that provide visual revision graphs, simple traffic-splitting controls, and event-source creation.
  - **(2020)** [youtube](https://www.youtube.com/watch?v=6NM6sqXIsoA)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical walk-through of OpenShift Serverless features. The session demonstrates creating a Node.js microservice, deploying it via git-import, scaling down to absolute zero instances to conserve resources, and automatically scaling up instances to handle sudden HTTP request surges.
## Cloud Native Infrastructure

### Service Mesh

#### OpenShift

  - **(2022)** [==github.com: Maistra Istio==](https://github.com/maistra/istio) <span class='md-tag md-tag--info'>⭐ 94</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-13d7f9b5" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 2 L 20 2 L 30 10 L 40 4 L 50 4" fill="none" stroke="url(#spark-grad-13d7f9b5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official GitHub repository for Maistra's modified Istio control plane code. Optimized for multi-tenancy support, advanced security policies, and tight integration within OpenShift environments.
## Cluster Management

### Scheduling and Node Assignment

#### Dynamic Balancing

  - **(2026)** [==Descheduler for Kubernetes 🌟==](https://github.com/kubernetes-sigs/descheduler) <span class='md-tag md-tag--info'>⭐ 5441</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-05b97c78" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 13 L 20 11 L 30 8 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-05b97c78)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A highly critical Kubernetes SIG project that addresses scheduling drift by continuously examining running pods against modified constraints, evicting pods that violate affinities, taints, topology spreads, or resource capacities.
## Compute and Runtime

### Serverless (1)

#### Knative Tutorials

  - **(2023)** [redhat-developer-demos.github.io/knative-tutorial](https://redhat-developer-demos.github.io/knative-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A self-paced developer tutorial for master-level Knative techniques. It covers Knative Serving configurations, custom scaling thresholds, and routing strategies.
## Containerization

### Runtimes

#### Kubernetes Integration

  - **(2017)** [cri-o.io](https://cri-o.io) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official home of CRI-O, an optimized Container Runtime Interface (CRI) designed specifically and exclusively for Kubernetes. CRI-O avoids overhead by supporting only OCI-compliant runtimes, removing unnecessary client CLI abstractions to deliver minimum-footprint workload execution.
## Developer Experience

### Cloud IDEs

#### Dev Spaces

  - **(2020)** [developers.redhat.com: How to install CodeReady Workspaces in a restricted OpenShift 4 environment](https://developers.redhat.com/blog/2020/06/12/how-to-install-codeready-workspaces-in-a-restricted-openshift-4-environment) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This architectural guide details installing Red Hat CodeReady Workspaces (now OpenShift Dev Spaces) within highly restricted, air-gapped environments. Utilizing an internal container registry and offline operator configurations, it provides an in-browser development IDE based on Eclipse Che. The configuration ensures that code never leaves the secure boundaries of the company's internal network.
## Development

### Kubernetes Operators

#### API Design

  - **(2020)** [developers.redhat.com: Operator pattern: REST API for Kubernetes and Red Hat OpenShift 🌟](https://developers.redhat.com/blog/2020/01/22/operator-pattern-rest-api-for-kubernetes-and-red-hat-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This architectural design guide details exposing REST APIs on top of Kubernetes operators. It abstracts custom resource complexity into standard endpoints, simplifying third-party service integration.
## Enterprise Kubernetes

### Database Orchestration

#### Operator Integrations

  - **(2021)** [**blog.byte.builders: Manage MongoDB in Openshift Using KubeDB**](https://appscode.com/blog/post/openshift-mongodb) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Demonstrates how to run and manage MongoDB instances on OpenShift using the KubeDB Operator. Covers scaling clusters, orchestrating schema updates, configuring persistent disk claims, and executing point-in-time recoveries.
### Developer Experience (1)

#### Platform Onboarding

  - **(2020)** [**developers.redhat.com: OpenShift for Kubernetes developers: Getting started 🌟**](https://developers.redhat.com/blog/2020/08/14/openshift-for-kubernetes-developers-getting-started) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A transitional developer guide comparing native Kubernetes design abstractions with OpenShift-specific resource types. Explains how components like Routes, BuildConfigs, and DeploymentConfigs interact to streamline application deployment.
  - **(2021)** [cloud.redhat.com: Getting Started in OpenShift 🌟](https://www.redhat.com/en/blog/getting-started-in-openshift) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory platform guide for engineers beginning their transition to OpenShift. Covers simple code deployments, route generation strategies, environment parameter definitions, and container lifecycle actions.
  - **(2020)** [developers.redhat.com - Best practices: Using health checks in the OpenShift 4.5 web console 🌟](https://developers.redhat.com/blog/2020/07/20/best-practices-using-health-checks-in-the-openshift-4-5-web-console) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details operational best practices for defining and verifying container liveness, readiness, and startup health probes directly inside the OpenShift 4.5 web console.
### Hardware Architectures

#### Cloud Provider Integration

  - **(2021)** [**openshift.com: OpenShift on ARM Developer Preview Now Available for AWS**](https://www.redhat.com/en/blog/openshift-on-arm-developer-preview-now-available-for-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Profiles the technical preview of running OpenShift on AWS ARM64 (Graviton) environments. Explains performance metrics, lower operational energy signatures, and compilation steps required for ARM-based microservices.
#### Platform Strategy

  - **(2021)** [venturebeat.com: Red Hat gives an ARM up to OpenShift Kubernetes operations](https://venturebeat.com/data-infrastructure/red-hat-gives-an-arm-up-to-openshift-kubernetes-operations) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of Red Hat's native ARM support expansion. Focuses on the economic and operational benefits of deploying multi-tenant microservices to alternative hardware architectures under uniform automation templates.
### Network Engineering

#### Cloud Provider Integration (1)

  - **(2021)** [**openshift.com: How to Offer Service Running on OpenShift on AWS to Other AWS VPCs, Privately 🌟**](https://www.redhat.com/en/blog/how-to-offer-service-running-on-openshift-on-aws-to-other-aws-vpcs-privately) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Technical blueprint detailing how to expose application endpoints hosted on ROSA (Red Hat OpenShift on AWS) to external AWS VPCs utilizing AWS PrivateLink. Prevents traffic exposure to the public internet by configuring Network Load Balancers (NLBs).
### Performance Tuning

#### High Density Node Architectures

  - **(2020)** [==blog.openshift.com: OpenShift Scale: Running 500 Pods Per Node 🌟==](https://www.redhat.com/en/blog/500_pods_per_node) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Explains the systems engineering and kernel adjustments needed to execute up to 500 pods per cluster node on OpenShift. Focuses on tuning the CRI-O container runtime, garbage collection frequency, CPU scheduler configurations, and CIDR allocation limits.
### Platform Migrations

#### Cluster Upgrades

  - **(2021)** [==redhat-cop.github.io: Best practices for migrating from OpenShift Container Platform 3 to 4 🌟==](https://redhat-cop.github.io/openshift-migration-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An authoritative technical manual for migrating live enterprise applications from OpenShift 3 to OpenShift 4. Covers using the Migration Toolkit for Containers (MTC) to handle data volumes.
### Release Diagnostics

#### Serverless and CICD

  - **(2021)** [**thenewstack.io: Red Hat OpenShift 4.8 Adds Serverless Functions, Pipelines-As-Code**](https://thenewstack.io/red-hat-openshift-4-8-adds-serverless-functions-pipelines-as-code) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Details key features in OpenShift 4.8, focusing on serverless deployments built on Knative, pipelines-as-code models integrated with Tekton, and the orchestration of sandboxed runtimes for increased host security.
### Workload Modernization

#### Windows Container Support

  - **(2021)** [**developers.redhat.com: Containerize .NET for Red Hat OpenShift: Use a Windows VM like a container**](https://developers.redhat.com/blog/2021/04/29/containerize-net-for-red-hat-openshift-use-a-windows-vm-like-a-container) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Explains how to execute legacy .NET applications alongside Linux containers on OpenShift. Details the usage of the Windows Machine Config Operator (WMCO) to run and manage Windows Server VMs directly inside OpenShift.
## Extensibility and APIs

### Microservices

#### Operator Integrations (1)

  - **(2020)** [Deploy and bind enterprise-grade microservices with Kubernetes Operators](https://developers.redhat.com/blog/2020/05/18/deploy-and-bind-enterprise-grade-microservices-with-kubernetes-operators) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A developer guide explaining how to bind microservices dynamically to relational stores and caching layers using automated operators.
## Infrastructure

### Container Registry

#### Self-Hosted

  - **(2019)** [==GitHub Quay (OSS)==](https://github.com/quay/quay) <span class='md-tag md-tag--info'>⭐ 2785</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d2af50cc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 5 L 20 7 L 30 2 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-d2af50cc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Project Quay is the open-source upstream version of Red Hat Quay, providing a highly scalable container registry designed for cloud-native infrastructure. It features multi-tenancy, geo-replication, advanced security pruning, and Clair integration to secure the software delivery pipeline.
### Data Protection

#### Kubernetes Backup Operators

  - **(2026)** [==github.com/vmware-tanzu/velero==](https://github.com/velero-io/velero) <span class='md-tag md-tag--info'>⭐ 10062</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1fef8e38" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 10 L 20 7 L 30 12 L 40 5 L 50 4" fill="none" stroke="url(#spark-grad-1fef8e38)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Velero is the standard open-source utility for safely backing up and restoring entire Kubernetes cluster structures and persistent volumes. Deeply integrates with both raw cloud APIs and file-level utilities like Kopia and Restic.
### Kubernetes Distributions

#### Enterprise Distributions

  - **(2026)** [OKD](https://okd.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The community-backed, open-source upstream counterpart to Red Hat OpenShift. OKD integrates Kubernetes with core Linux container tools (like Fedora CoreOS) to offer a complete self-managing, multi-tenant container platform designed for declarative applications, CI/CD, and simplified enterprise operations.
## Networking and Security

### Cluster Networking

#### VPC Peering

  - **(2021)** [openshift.com: Using VPC Peering to Connect an OpenShift Service on an AWS (ROSA) Cluster to an Amazon RDS MySQL Database in a Different VPC](https://www.redhat.com/en/blog/using-vpc-peering-to-connect-an-openshift-service-on-an-aws-rosa-cluster-to-an-amazon-rds-mysql-database-in-a-different-vpc) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides step-by-step instructions for establishing low-latency VPC peering connections between an active ROSA container network and an external Amazon RDS MySQL database cluster.
### Traffic Routing

#### Ingress Controllers

  - **(2026)** [Ingress Controller](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official Kubernetes documentation explaining Ingress. It teaches engineers how to manage HTTP routing, SSL termination, and hostnames at the cluster edge.
## Security

### Container Registry (1)

#### Project Quay

  - **(2026)** [projectquay.io](https://www.projectquay.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The project homepage for Project Quay. Quay is an open-source, highly scalable, and secure container registry engine. The platform provides granular access controls, robot accounts, and support for multi-arch OCI registry specifications, serving as the upstream codebase for Red Hat Quay.
## Service Mesh (1)

### Red Hat OpenShift

#### Enterprise Platforms

  - **(2020)** [blog.openshift.com: Red Hat OpenShift Service Mesh is now available: What you should know 🌟](https://www.redhat.com/en/blog/red-hat-openshift-service-mesh-is-now-available-what-you-should-know)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement detailing the GA availability of Red Hat OpenShift Service Mesh. Explains the integrated packaging of Istio, Envoy, and Jaeger under OpenShift's strict security paradigms.

---
💡 **Explore Related:** [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

