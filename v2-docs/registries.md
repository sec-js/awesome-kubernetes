# Registries

!!! info "Architectural Context"
    Detailed reference for Registries in the context of Engineering Pipeline.

## CI-CD Pipelines

### Jenkins Ecosystem

#### Artifact Integration

  - **(2026)** [Nexus Platform Plugin for Jenkins](https://help.sonatype.com/en/nexus-platform-plugin-for-jenkins.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official plugin guide for linking Jenkins automation controllers to Sonatype Nexus platforms. It explains the mechanics of publishing, staging, and verifying build artifacts dynamically.

</div></details>
#### Video Tutorials

  - **(2022)** [youtube: uploading artifacts from jenkins to nexus](https://www.youtube.com/watch?v=7NmGSnqLd58) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A hands-on video tutorial showing Maven-based Jenkins builds pushing compilation outputs and binary distributions into local Nexus environments.

</div></details>
  - **(2021)** [youtube: Jenkins Integration with Nexus](https://www.youtube.com/watch?v=qbO4MTESiJQ) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A video guide showing integration steps for building Jenkins jobs and storing artifacts into a target Sonatype Nexus server repository.

</div></details>
## Career Development

### Industry Trends

#### Market Analysis

  - **(2021)** [seekingalpha.com: JFrog Reminds Me Of MongoDB](https://seekingalpha.com/article/4427517-jfrog-reminds-me-of-mongodb) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A financial market study of JFrog's business model and growth strategy, drawing comparisons to MongoDB's database model and developer adoption lifecycle.

</div></details>
## Cloud Native Security and Artifact Management

### Container Registry

#### Deployment Guides

  - **(2020)** [goharbor.io: Deploy Harbor with the Quick Installation Script](https://goharbor.io/docs/2.0.0/install-config/quick-install-script) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official quick-start deployment guide describing the automated script installation pipeline for Harbor. It provides developers and sandbox operators with rapid local provisioning using Docker and Docker Compose.

</div></details>
#### Harbor

  - **(2026)** [==Harbor==](https://goharbor.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

CNCF-graduated enterprise-grade registry that secures cloud-native artifacts with role-based access control, vulnerability scanning, and cryptographic signing. It serves as a central hub for microservice images, offering high-throughput image replication and multi-tenant capabilities.

</div></details>
#### P2P Distribution

  - **(2021)** [**uber/kraken**](https://github.com/uber/kraken) <span class='md-tag md-tag--info'>⭐ 6691</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Uber's open-source peer-to-peer (P2P) Docker registry designed for ultra-high-throughput image distribution in massive clusters. Although highly optimized, it is largely archived in favor of CNCF Dragonfly.

</div></details>
## Enterprise Kubernetes

### Red Hat OpenShift

#### CI-CD Pipelines (1)

  - **(2020)** [openshift.com: Using JFrog's Artifactory and Red Hat OpenShift Together](https://www.redhat.com/en/blog/18333-2) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

An architectural guide detailing integrations between JFrog Artifactory and Red Hat OpenShift, showing how to coordinate secure, automated image promotion paths.

</div></details>
## Infrastructure Standards

### Artifact Registry

#### Best Practices

  - **(2021)** [The JFrog journey to kubernetes: best practices for taking your containers all the way to production](https://jfrog.com/whitepaper/the-jfrog-journey-to-kubernetes-best-practices-for-taking-your-containers-all-the-way-to-production) 🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A detailed whitepaper detailing strategies for transitioning binaries safely into Kubernetes environments, highlighting JFrog's best practices for container staging.

</div></details>
#### CLI Utilities

  - **(2026)** [nexus3-cli.readthedocs.io](https://nexus3-cli.readthedocs.io/en/latest) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Documentation site for Python-based command-line utilities built to interface with Nexus 3 APIs. It simplifies batch tasks and permissions reporting.

</div></details>
  - **(2021)** [GitHub: Nexus-CLI](https://github.com/mlabouardy/nexus-cli) <span class='md-tag md-tag--info'>⭐ 294</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A custom command-line interface helper for managing Nexus repository clusters, written in Go. The repository is unmaintained with no commit activity in over four years.

</div></details>
#### DevOps Guides

  - **(2022)** [Devopscube.com: Setup Nexus Kubernetes 🌟](https://devopscube.com/setup-nexus-kubernetes) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A highly practical step-by-step installation guide demonstrating how to provision Sonatype Nexus on a Kubernetes cluster. It covers configuration for Persistent Volumes, persistent claims, and ingress routing.

</div></details>
#### Enterprise Kubernetes (1)

  - **(2020)** [Sonatype Nexus Community: Nexus Kubernetes OpenShift 🌟](https://github.com/sonatype-nexus-community/nexus-kubernetes-openshift) <span class='md-tag md-tag--info'>⭐ 8</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A community-supported project featuring Helm charts and YAML manifests to deploy Sonatype Nexus in OpenShift and standard Kubernetes. Currently marked as legacy due to over four years of inactivity.

</div></details>
#### Enterprise Platforms

  - **(2026)** [**sonatype.com/nexus-repository-oss**](https://www.sonatype.com/products/sonatype-nexus-repository) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The main landing page for Sonatype Nexus Repository Manager, a universal artifact engine supporting major formats including npm, PyPI, Maven, and OCI containers. It plays a critical role in secure software supply chains.

</div></details>
  - **(2026)** [**Nexus Repository Manager (NXRM) 3 🌟**](https://help.sonatype.com/en/sonatype-nexus-repository.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official comprehensive documentation for Sonatype Nexus Repository Manager 3, providing deployment, backup, migration, and clustering guidelines for enterprise system administrators.

</div></details>
  - **(2022)** [jfrog.com: What Artifactory as your kubernetes docker registry means to you](https://jfrog.com/integrations/kubernetes-docker-registry) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

An exploration of JFrog Artifactory's role as a local Kubernetes Docker registry proxy, showing how it minimizes deployment latency and manages external registry rate limits.

</div></details>
  - **(2021)** [JFrog Artifactory: Your Kubernetes Registry](https://jfrog.com/blog/jfrog-artifactory-kubernetes-registry) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A deep technical article showing how JFrog Artifactory works as a high-density Kubernetes-integrated OCI registry with caching and security protections.

</div></details>
#### Industry Trends (1)

  - **(2021)** [jfrog.com: GitHub vs JFrog: Who Can do the Job for DevOps?](https://jfrog.com/blog/github-vs-jfrog-who-can-do-the-job-for-devops) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A detailed product comparison of GitHub Packages and JFrog Artifactory, contrasting binary registry performance limits, metadata depth, and enterprise scaling models.

</div></details>
#### Infrastructure as Code

  - **(2021)** [github.com/samrocketman/nexus3-config-as-code](https://github.com/samrocketman/nexus3-config-as-code) <span class='md-tag md-tag--info'>⭐ 62</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A declarative configuration-as-code utility for bootstrapping Nexus 3 configurations, utilizing Groovy scripting. Unmaintained for over four years and marked as legacy.

</div></details>
#### Legacy Resources

  - **(2018)** [github.com/cinhtau/sonatype-nexus-waffle](https://github.com/cinhtau/sonatype-nexus-waffle) <span class='md-tag md-tag--info'>⭐ 6</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

An archive project that integrates Nexus authentication with Active Directory. It is inactive and obsolete, retained purely for vintage reference purposes.

</div></details>
#### Open Source Initiatives

  - **(2026)** [Sonatype Nexus Community 🌟](https://github.com/sonatype-nexus-community) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The master community hub containing third-party integrations, developer plugins, and configuration scripts targeting the Sonatype Nexus software ecosystem.

</div></details>
### Container Registry (1)

#### Artifact Registry (1)

  - **(2026)** [Docker Registry](https://help.sonatype.com/en/docker-registry.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official administrator guidelines outlining how to host, proxy, and manage Docker container images securely within Sonatype Nexus Repository Manager.

</div></details>
  - **(2021)** [blog.sonatype.com: Using Nexus 3 as Your Repository – Part 3: Docker Images 🌟](https://www.sonatype.com/blog/using-sonatype-nexus-repository-3-part-3-docker-images) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The third segment in Sonatype's setup series, illustrating container hosting paradigms, private Docker registry configurations, and the setup of secure local proxy repositories.

</div></details>
#### Configuration Guides

  - **(2018)** [Configure Docker Service To Use Insecure Registry](https://github.com/Juniper/contrail-docker/wiki/Configure-docker-service-to-use-insecure-registry) <span class='md-tag md-tag--info'>⭐ 48</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A historic wiki page detailing Docker daemon changes needed to whitelist unencrypted private registries. It is classified as legacy due to lack of commits in more than four years.

</div></details>
  - **(2017)** [Running an insecure registry –insecure-registry](https://forums.docker.com/t/running-an-insecure-registry-insecure-registry/8159) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A classic Docker community forum discussion focusing on troubleshooting local TLS handshake issues when executing push operations to local registry endpoints.

</div></details>
#### Enterprise Platforms (1)

  - **(2026)** [JFrog Container Registry](https://jfrog.com/container-registry) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Enterprise landing page for JFrog's Container Registry, showing support for Helm, Docker, and OCI specifications with high-availability clustering and build-of-materials reporting.

</div></details>
#### Kubernetes Operators

  - **(2024)** [Quay Community Edition operator](https://github.com/quay/quay-operator) <span class='md-tag md-tag--info'>⭐ 143</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The official Kubernetes Operator for deploying and managing the life cycle of Project Quay registries. It automates storage setup, database migrations, and SSL termination within OpenShift and OKD clusters.

</div></details>
#### Legacy Resources (1)

  - **(2026)** [Test an insecure registry 🌟](https://docs.docker.com/retired) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Retired Docker documentation dealing with configurations of insecure, unencrypted private registries. Preserved for diagnosing vintage local developer configurations.

</div></details>
  - **(2026)** [guides.sonatype.com: secure docker registries](https://help.sonatype.com/en/404-page.html) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

An identical retired documentation path representing defunct guidelines on Nexus-based private container security. Preserved purely for historical configuration mapping.

</div></details>
#### Maintenance Scripts

  - **(2019)** [hackermoon.com: cleanup old docker images from nexus repository](https://hackernoon.com/cleanup-old-docker-images-from-nexus-repository-617b1004dad8) 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A guide on managing storage allocations in Nexus Repository Manager by automating the deletion of legacy Docker image tags. It outlines task scheduler configurations and artifact purging tasks.

</div></details>
#### Open Source Initiatives (1)

  - **(2026)** [**github.com/quay**](https://github.com/quay) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The master GitHub organization for Project Quay, housing the enterprise registry engine, the Clair vulnerability scanner, the setup operators, and auxiliary storage backend connectors.

</div></details>
#### Release Notes

  - **(2019)** [Quay 3.0 released in May 2019](https://www.redhat.com/en/blog/introducing-red-hat-quay-3-registry-your-linux-and-windows-containers) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official release documentation for Red Hat Quay 3.0. It highlights architectural additions including Windows Container support, a revamped UI, and improved multi-tenant namespace management.

</div></details>
## Infrastructure as Code and Automation

### Configuration Management

#### Ansible

  - **(2021)** [nicholasamorim/ansible-role-harbor](https://github.com/nicholasamorim/ansible-role-harbor) <span class='md-tag md-tag--info'>⭐ 26</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

An Ansible role dedicated to provisioning and configuring Harbor. Due to limited recent maintenance, it serves primarily as a reference architecture for legacy automation projects.

</div></details>
  - **(2019)** [mramanathan/ansible-harbor](https://github.com/mramanathan/ansible-harbor) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Legacy Ansible playbook for Harbor deployment orchestration. It lacks modern feature updates and is deprecated in favor of Kubernetes-native Helm-based deployments.

</div></details>
#### VMware

  - **(2020)** [galaxy.ansible.com/mkgin/vmware-harbor](https://galaxy.ansible.com/mkgin/vmware-harbor) 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Ansible Galaxy role designed to install Harbor registries on VMware-based virtual infrastructure. It remains a historical reference but has been surpassed by containerized approaches.

</div></details>
## Security

### Certificates

#### TLS Automation

  - **(2026)** [==cert-manager/cert-manager==](https://github.com/cert-manager/cert-manager) <span class='md-tag md-tag--info'>⭐ 13818</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Consolidated record of the cert-manager project, automating dynamic certificate lifecycles to guarantee encrypted transport paths between internal microservice runtimes.

</div></details>

***
💡 **Explore Related:** [Jenkins Alternatives](./jenkins-alternatives.md) | [Argo](./argo.md) | [Jenkins](./jenkins.md)

