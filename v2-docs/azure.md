---
description: "Top Azure resources for 2026, AI-ranked: Bicep, Microsoft - DICOM Service and more — curated Cloud Native tools, guides and references."
---
# Microsoft Azure

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/azure/).

!!! info "Architectural Context"
    Detailed reference for Microsoft Azure in the context of Cloud Providers (Hyperscalers).

## API Design

### Standards

#### REST API

  - **(2026)** [==Microsoft REST API Guidelines 🌟🌟🌟==](https://github.com/microsoft/api-guidelines/blob/vNext/Guidelines.md) <span class='md-tag md-tag--info'>⭐ 23289</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4a0bb68b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 11 L 20 2 L 30 3 L 40 9 L 50 5" fill="none" stroke="url(#spark-grad-4a0bb68b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The comprehensive standards document establishing design specifications for REST APIs across Microsoft platforms. It defines explicit protocols for HTTP methods, error handling, versioning, pagination, and JSON schemas. This serves as a highly robust benchmark for software engineers designing public-facing and microservices-based API endpoints.
## Architecture

### Container Orchestration

#### AKS Mission Critical

  - **(2025)** [learn.microsoft.com: Mission-critical baseline architecture on Azure](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-intro) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference architecture blueprint for deploying highly reliable, multi-region containerized workloads on Azure Kubernetes Service (AKS). Integrates active-active clustering, zero-downtime routing architectures, and strict self-healing protocols.
### Well-Architected Framework

#### Mission-Critical Workloads

  - **(2025)** [learn.microsoft.com: Mission-critical workloads](https://learn.microsoft.com/en-us/azure/well-architected/mission-critical/mission-critical-overview) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Well-Architected guidance focusing on baseline patterns for mission-critical enterprise workloads. Outlines structural patterns for failure-domain isolation, operational health modeling, and continuous validation methodologies.
## Architecture and Microservices

### Infrastructure as Code

#### API Management

  - **(2024)** [==github.com/Azure/apiops 🌟==](https://github.com/Azure/apiops) <span class='md-tag md-tag--info'>⭐ 440</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4e188128" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 8 L 20 4 L 30 6 L 40 11 L 50 10" fill="none" stroke="url(#spark-grad-4e188128)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Azure APIOps repository implementing GitOps principles for Azure API Management (APIM). Enables organizations to automate the extraction, publishing, configuration control, and deployment of complex API configurations across development, staging, and production networks.
#### Application Delivery

  - **(2022)** [nubesgen.com](https://nubesgen.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official workspace for NubesGen, a community-driven GitOps bootstrapping engine. It streamlines developer onboarding by dynamically outputting tailored, best-practice Terraform or Bicep templates for hosting Java, Node.js, and .NET applications on Azure. This eliminates manual configuration of networking and identity components.
  - **(2022)** [infoq.com: NubesGen Brings Git Push to Azure Infrastructure](https://www.infoq.com/news/2022/03/nubesgen-azure-infrastructure)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analysis of the technical value proposition of NubesGen. Evaluates how developers can utilize Git-driven configurations to automatically provision secure Azure environments. This shift-left mechanism reduces platform engineering bottlenecks by providing automated, developer-accessible IaC pipelines aligned with security baselines.
### Migration Guides

#### Java Ecosystem

  - **(2023)** [learn.microsoft.com: Migrate Java applications to Azure 🌟🌟🌟](https://learn.microsoft.com/en-us/azure/developer/java/migration/migration-overview) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Microsoft’s official migration matrix for containerizing and deploying Java workloads on Azure. Evaluates migration paths for Tomcat, JBoss EAP, WebLogic, and Spring Boot to hosting targets such as Azure App Service, Azure Container Apps, and AKS. Includes assessments for dependency management and database connection pooling.
### Observability

#### Application Insights

  - **(2023)** [returngis.net: Monitorizar aplicación Java con Spring Boot con Azure Application Insights](https://www.returngis.net/2023/04/monitorizar-aplicacion-java-con-spring-boot-con-azure-application-insights) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Spanish-language technical implementation guide for monitoring Java Spring Boot applications using the Azure Application Insights auto-instrumentation JVM agent. Details trace correlation, distributed tracing patterns, resource metrics capture, and structured log ingestion with zero code modifications.
### Spring Cloud

#### Design Patterns

  - **(2021)** [devblogs.microsoft.com: Deploy Spring Boot applications by leveraging enterprise best practices – Azure Spring Cloud Reference Architecture](https://devblogs.microsoft.com/java/deploy-spring-boot-applications-by-leveraging-enterprise-best-practices) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive reference architecture for deploying enterprise Spring Boot workloads on Azure Spring Cloud (rebranded as Azure Spring Apps). Incorporates security benchmarks including hub-and-spoke virtual network isolation, private endpoints, and centralized configuration profiles. Curated best practices align Java microservice design patterns with enterprise cloud governance.
## CICD Pipelines

### DevOps Platforms

#### DevTest Labs

  - **(2025)** [learn.microsoft.com: DevTest and DevOps for microservice solutions](https://learn.microsoft.com/en-us/azure/devtest-labs) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official framework documentation detailing the integration of Azure DevTest Labs with modern DevOps pipelines. Focuses on setting up elastic testing environments and managing resource consumption patterns.
## Cloud Application Platforms

### Azure App Service

#### App Service Configuration

  - **(2026)** [==learn.microsoft.com: Environment variables and app settings in Azure App Service==](https://learn.microsoft.com/en-us/azure/app-service/reference-app-settings) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official reference detailing how App Settings and Connection Strings map directly to environment variables at container execution time. It covers critical security aspects, including referencing Key Vault secrets natively to prevent plaintext credential leaks in code. This configuration framework forms the architectural baseline for deploying portable, 12-factor cloud-native applications.
#### App Service Diagnostics

  - **(2025)** [**Azure App Service Auto-Heal: Capturing Relevant Data During Performance Issues**](https://techcommunity.microsoft.com/blog/appsonazureblog/azure-app-service-auto-heal-capturing-relevant-data-during-performance-issues/4390351) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A technical breakdown of the Azure App Service Auto-Heal capability, showing how to trigger automated mitigation actions during performance regressions. It explains how to collect diagnostic artifacts, such as thread dumps, memory dumps, and profiler traces, right before an instance restarts. This proactive debugging practice prevents transient microservice failures from escalating into major outages.
  - **(2024)** [azure.github.io/AppService: General availability of Diagnostics tools for App Service on Linux Node.js apps](https://azure.github.io/AppService/2024/01/05/Diagnose-Tools-for-NodeJs-Linux-apps.html) <span class='md-tag md-tag--warning'>[NODE.JS CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement and documentation highlighting advanced diagnostic tools built specifically for Node.js workloads running on Linux-based Azure App Services. It explains the integration of CPU profiling, memory allocation tracking, and automated core dump collection. These tools enable real-time analysis of single-threaded event loop blockages and memory leaks directly from the Azure portal.
#### Custom Containers

  - **(2026)** [==learn.microsoft.com: Configure a custom container for Azure App Service==](https://learn.microsoft.com/en-us/azure/app-service/configure-custom-container) <span class='md-tag md-tag--warning'>[DOCKER CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Technical reference for deploying custom Docker and OCI-compliant containers to Azure App Service (Web App for Containers). It covers crucial configurations, such as persistent storage mounts, multi-container deployments via Compose, and custom startup commands. Utilizing custom containers allows engineering teams to standardized packaging across local environments, AKS, and App Service.
#### Java Runtime Configurations

  - **(2026)** [**learn.microsoft.com: Configure a Java app for Azure App Service**](https://learn.microsoft.com/en-us/azure/app-service/configure-language-java-deploy-run) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Comprehensive documentation detailing JVM optimization, logging integration, and web container (Tomcat/JBoss) tuning within Azure App Service. It guides engineers through profiling settings, customizing JAR/WAR deployments, and configuring APM agent connections. This resource is essential for running enterprise-grade Java microservices with high throughput and low cold-start latency.
### Serverless Computing

#### Azure Functions Core

  - **(2026)** [==learn.microsoft.com: AZ-204: Implement Azure Functions 🌟==](https://learn.microsoft.com/en-us/training/paths/implement-azure-functions) <span class='md-tag md-tag--warning'>[C# / PYTHON / JS CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Microsoft training curriculum for implementing serverless workflows and event-driven computing via Azure Functions. It covers bindings and triggers, Durable Functions for stateful execution, execution context, and performance profiling. This path forms the core educational foundation for building reliable, event-driven microservices on the Azure platform.
## Cloud Architecture

### PaaS

#### App Service

  - **(2025)** [learn.microsoft.com: Azure Well-Architected Framework perspective on Azure App Service (Web Apps)](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/app-service-web-apps) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A target guide mapping WAF architecture principles to Web Apps on Azure App Service. It focuses on implementing zero-trust network configurations, managed identities, multi-region failovers, and auto-scaling rules. This resource equips platform engineers to deploy enterprise-grade PaaS runtimes with rigorous service-level objectives (SLOs).
## Cloud DevOps

### CI-CD Pipelines

#### YAML Templating and Reusability

  - **(2024)** [**github.com/JFolberth/TheYAMLPipelineOne 🌟**](https://github.com/JFolberth/TheYAMLPipelineOne) <span class='md-tag md-tag--info'>⭐ 221</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d516cd2e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 10 L 20 5 L 30 13 L 40 3 L 50 11" fill="none" stroke="url(#spark-grad-d516cd2e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[POWERSHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An open-source pipeline framework showcasing advanced DRY (Don't Repeat Yourself) YAML patterns for Azure DevOps. In 2026, this template system represents best-in-class orchestration, enabling developers to scale microservice builds without duplicating pipelines or configuration code.
### Container Orchestration (1)

#### GitOps

##### ArgoCD and Secrets

  - **(2023)** [**linkedin.com: Complete CI/CD Solution for mS on AKS using Azure DevOps, ArgoCD and External Kubernetes Secretes 🌟**](https://www.linkedin.com/pulse/complete-cicd-solution-ms-aks-using-azure-devops-argocd-singh) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Presents an architectural case study combining Azure DevOps for container build and ACR registration with ArgoCD for GitOps-driven deployment onto AKS. It highlights how to secure workloads using AKS Workload Identity and External Secrets Operator (ESO). Live 2026 validation confirms this hybrid pattern is the gold standard for high-density enterprise microservice applications.
#### Kubernetes CD

##### AKS Deployment

  - **(2022)** [medium.com/geekculture: Continuous Deployment with Azure DevOps Pipelines and Kubernetes](https://medium.com/geekculture/continuous-deployment-with-azure-devops-pipelines-and-kubernetes-12fe1c70b343) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates continuous deployment to Kubernetes clusters using Azure Pipelines, utilizing Helm charts and manifest-rendering tasks. In 2026, while direct-push deployments using Kubernetes tasks remain in use, enterprise architectures prefer pull-based GitOps tools (like ArgoCD or Flux) to prevent exposing cluster credentials to external runner systems.
### Infrastructure as Code (1)

#### End-to-End Lab Guides

  - **(2022)** [==thomast1906/DevOps-The-Hard-Way-Azure 🌟==](https://github.com/thomast1906/DevOps-The-Hard-Way-Azure) <span class='md-tag md-tag--info'>⭐ 582</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-37f99e5e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 5 L 20 3 L 30 4 L 40 11 L 50 6" fill="none" stroke="url(#spark-grad-37f99e5e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A hands-on, end-to-end sandbox guide mapping out 'The Hard Way' of deploying infrastructure and applications on Azure. This project details virtual network design, VM provisioning, AKS deployments, and pipeline-driven application releases. 2026 live grounding validates this repository as a premier community benchmark for building custom, highly-secure lab environments.
## Cloud Infrastructure

### Container Orchestration (2)

#### AKS Fleet Manager

  - **(2024)** [github.com/azure/fleet](https://github.com/azure/fleet) <span class='md-tag md-tag--info'>⭐ 224</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ff36d64d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 12 L 20 6 L 30 6 L 40 8 L 50 2" fill="none" stroke="url(#spark-grad-ff36d64d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Azure Kubernetes Service (AKS) Fleet Manager, designed for multi-cluster fleet-wide management. Coordinates application rollouts, implements global ingress configurations, and automates orchestrator upgrades across distributed topologies.
### Container Storage

#### Cloud Native Storage

  - **(2023)** [techcommunity.microsoft.com: Azure Container Storage in Public Preview](https://techcommunity.microsoft.com/blog/azurestorageblog/azure-container-storage-in-public-preview/3819246) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spotlights the public preview release of Azure Container Storage (now GA), a service offering volume management natively optimized for Kubernetes clusters. Minimizes container I/O overhead on stateful workloads.
### Monitoring and Observability

#### Multi-Tenant Observability

  - **(2024)** [**techcommunity.microsoft.com: How To Monitor Your Multi-Tenant Solution on Azure With Azure Monitor**](https://techcommunity.microsoft.com/blog/azureobservabilityblog/how-to-monitor-your-multi-tenant-solution-on-azure-with-azure-monitor/4042140) <span class='md-tag md-tag--warning'>[KQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed architectural analysis on isolating and correlating performance metrics and logs in a multi-tenant SaaS application on Azure. It highlights techniques like resource tagging, contextual workspace routing, and building tenant-specific dashboards via Azure Workbook and KQL. Perfect for engineering leads building robust performance isolation and billing models for SaaS workloads.
### Networking and Edge Routing

#### App Service Networking

  - **(2021)** [returngis.net: Acceder a un App Service con Private Endpoint desde otra Vnet](https://www.returngis.net/2021/08/acceder-a-un-app-service-con-private-endpoint-desde-otra-vnet) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An in-depth networking guide in Spanish detailing cross-VNet connectivity to an Azure App Service isolated behind a Private Endpoint. It explains how to configure Azure Private DNS zones, virtual network links, and routing rules to securely traverse VNet boundaries without public exposure. This pattern is fundamental for implementing zero-trust egress and ingress in enterprise cloud landing zones.
#### Application Gateway V2

  - **(2023)** [nathannellans.com: Azure Application Gateway - Part 1 🌟](https://www.nathannellans.com/post/azure-application-gateway-part-1) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — A multi-part guide focused on configuring and architecting the traditional Azure Application Gateway (v2). It covers the basics of listener configurations, routing rules, SSL/TLS termination, and Web Application Firewall (WAF) integration. This guide remains highly useful for understanding legacy reverse-proxy architectures before transitioning to modernized container gateway models.
#### Load Balancing Options

  - **(2024)** [acethecloud.com: Which is better Azure App Gateway or Nginx configured on Azure VMs](https://acethecloud.com/blog/azure-application-gateway-and-nginx-on-vm) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed comparison between leveraging a fully managed service (Azure Application Gateway) and hosting customized Nginx reverse proxies on virtual machines. It weighs factors such as administrative overhead, feature sets, security compliance, auto-scaling capabilities, and overall total cost of ownership (TCO). This serves as a vital tool for technical leads choosing a production-grade ingress layer.
### Serverless Containers

#### Azure Container Apps

  - **(2021)** [techcommunity.microsoft.com: Introducing Azure Container Apps: a serverless container service for running modern apps at scale](https://techcommunity.microsoft.com/blog/appsonazureblog/introducing-azure-container-apps-a-serverless-container-service-for-running-mode/2867265) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Azure Container Apps (ACA), a serverless platform built on Kubernetes, KEDA, Dapr, and Envoy. Streamlines microservices execution by removing underlying virtual host infrastructure complexity.
#### Container Governance

  - **(2023)** [techcommunity.microsoft.com: Azure Policy for Azure Container Apps? Yes, please](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/azure-policy-for-azure-container-apps-yes-please/3775200) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes implementation patterns for enforcing Azure Policy definitions on Azure Container Apps. Discusses baseline configurations to block unencrypted ingress, force private network endpoints, and mandate tag structures.
## Cloud Native and Kubernetes

### GitOps and Continuous Delivery

#### ArgoCD integration

  - **(2025)** [**Announcing Private Preview: ArgoCD through Microsoft GitOps**](https://techcommunity.microsoft.com/blog/azurearcblog/announcing-private-preview-argocd-through-microsoft-gitops/4399747) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An announcement regarding native ArgoCD integration managed directly through Azure Arc-enabled Kubernetes and Microsoft GitOps. This development bridges the gap between AKS native extensions and industry-standard GitOps tools, offering declarative cluster state management at scale. It significantly reduces operational overhead by hosting and maintaining control plane elements as a first-class Azure service.
#### DevOps Standardization

  - **(2021)** [techcommunity.microsoft.com: Standardize DevOps practices across hybrid and multicloud environments](https://techcommunity.microsoft.com/blog/itopstalkblog/standardize-devops-practices-across-hybrid-and-multicloud-environments/2795010) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A strategic discussion on leveraging Azure Arc-enabled Kubernetes to enforce standardized CI/CD pipelines and compliance rules across disparate infrastructure. It focuses on using GitOps (via Flux/ArgoCD) and Azure Policy to maintain consistent cluster configurations globally. This operational pattern eliminates configuration drift and reduces administrative friction across hybrid environments.
### Hybrid and Multicloud Solutions

#### App Services on Arc

  - **(2021)** [thomasmaurer.ch: Run cloud-native apps on Azure PaaS anywhere](https://www.thomasmaurer.ch/2021/06/run-cloud-native-apps-on-azure-paas-anywhere) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Exploring the deployment of Azure PaaS services—such as App Service, Functions, and Logic Apps—directly onto Azure Arc-enabled Kubernetes clusters. It showcases how enterprise teams can run standard cloud-managed offerings in on-premises data centers or other public clouds. This strategy combines public cloud developer experience with strict on-premises data sovereignty requirements.
  - **(2021)** [youtube: How to run an App Service Web App on Azure Arc-enabled Kubernetes - Part 2 | Azure Tips and Tricks](https://www.youtube.com/watch?v=53-Y_aI0KpE&ab_channel=MicrosoftAzure) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical video guide demonstrating the deployment and operation of Azure App Service workloads on custom Kubernetes clusters via Azure Arc. It walks through the resource provisioning pipeline, exposing the application endpoint, and validating state replication. This visual guide is optimal for platform engineers bridging traditional PaaS applications with cloud-native Kubernetes infrastructure.
#### Azure Arc Architecture

  - **(2025)** [**architecture diagrams and slides**](https://github.com/microsoft/azure_arc) <span class='md-tag md-tag--info'>⭐ 806</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-06a9b07f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 2 L 30 13 L 40 4 L 50 13" fill="none" stroke="url(#spark-grad-06a9b07f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN/IMAGES CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Official architectural blueprints and presentation slides detailing the inner workings of Azure Arc control planes and resource providers. This repository visually demonstrates how Arc bridges the control plane to edge environments and external cloud providers. It is an indispensable asset for enterprise architects designing unified management policies and hybrid cluster deployments.
#### Azure Arc Jumpstart

  - **(2026)** [==azurearcjumpstart.io==](https://jumpstart.azure.com) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The comprehensive Azure Arc Jumpstart portal, providing automated, hands-on sandbox scenarios for Arc-enabled infrastructure. It facilitates instant provisioning of hybrid Kubernetes, servers, and data services across multi-cloud environments like AWS and GCP. This portal remains the primary industry reference for testing real-world deployment patterns and complex integration topologies.
### Monitoring and Observability (1)

#### Managed Prometheus

  - **(2023)** [==techcommunity.microsoft.com: Introducing Azure Monitor managed service for Prometheus 🌟==](https://techcommunity.microsoft.com/blog/azureobservabilityblog/introducing-azure-monitor-managed-service-for-prometheus/3600185) <span class='md-tag md-tag--warning'>[PROMQL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Announcement of the native, fully managed Prometheus monitoring service integrated into Azure Monitor. This managed engine allows teams to leverage standard PromQL queries, alerting rules, and Grafana dashboarding without the maintenance complexity of scaling self-hosted Prometheus instances. This service has become the primary standard for collecting metrics from AKS and cloud-native workloads.
#### Network Observability

  - **(2024)** [**techcommunity.microsoft.com: Advanced Network Observability for your Azure Kubernetes Service clusters through Azure Monitor**](https://techcommunity.microsoft.com/blog/azureobservabilityblog/advanced-network-observability-for-your-azure-kubernetes-service-clusters-throug/4176736) <span class='md-tag md-tag--warning'>[KQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Unveiling advanced network observability features for AKS clusters, utilizing eBPF to capture kernel-level network telemetry. It provides deep visibility into pod-to-pod and egress traffic flow, packet drops, DNS resolution latencies, and TCP connection stats. This low-overhead monitoring is essential for debugging transient network issues inside microservices environments.
### Networking and Edge Routing (1)

#### Gateway API

  - **(2025)** [**Application Gateway for Containers: Istio Integration**](https://blog.cloudtrooper.net/2025/11/21/application-gateway-for-containers-istio-integration) <span class='md-tag md-tag--warning'>[GO / YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An advanced architectural post demonstrating how Azure Application Gateway for Containers (AGC) integrates with Istio Service Mesh via Kubernetes Gateway API. It details how edge traffic routing seamlessly hands off to internal mesh proxy sidecars while preserving end-to-end mTLS and header-based routing. This integration is critical for high-security microservices topologies demanding zero-trust communication.
## Cloud Native Platforms

### Azure

#### High Availability Architectures

  - **(2026)** [==github.com/azure/mission-critical-online: Welcome to Azure Mission-Critical' Online Reference Implementation==](https://github.com/azure/mission-critical-online) <span class='md-tag md-tag--info'>⭐ 401</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-07d045cb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 8 L 20 10 L 30 8 L 40 8 L 50 5" fill="none" stroke="url(#spark-grad-07d045cb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[BICEP CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An industry-grade reference template demonstrating design strategies for mission-critical cloud applications on Azure. Implements active-active patterns, automated failover, and zero-downtime updates.
## Cloud Platform

### Architecture Patterns

#### Cloud-Native

  - **(2022)** [==github.com/PacktPublishing/The-Azure-Cloud-Native-Architecture-Mapbook==](https://github.com/PacktPublishing/The-Azure-Cloud-Native-Architecture-Mapbook) <span class='md-tag md-tag--info'>⭐ 344</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e6b6f391" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 4 L 20 8 L 30 10 L 40 3 L 50 8" fill="none" stroke="url(#spark-grad-e6b6f391)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Architectural repository covering modern cloud design topologies, zero-trust cloud network security, infrastructure redundancy, microservice distribution, and cost models mapping.
### Microsoft Azure (1)

#### Sample Architecture

  - **(2026)** [github.com/Azure-Samples 🌟](https://github.com/Azure-Samples) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Central directory of Azure engineering samples. Provides production-ready templates, deployment scripts, and reference implementations spanning Serverless, Azure Kubernetes Service, container orchestration, and multi-tenant systems.
## Community

### Blogs

#### .NET Development

  - **(2024)** [dotnetcurry.com](https://www.dotnetcurry.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An educational resource offering deep dives into .NET enterprise application architectures, modern C# programming paradigms, and Azure integration. The platform supports developers migrating desktop architectures to modern, serverless, and container-based environments.
#### Cloud-Native Architecture

  - **(2025)** [azurebrains.com: Azurebrains](https://blog.azurebrains.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blog and community resource highlighting cloud-native application patterns, Kubernetes orchestration, and serverless compute frameworks. Offers targeted code reviews and reference architectures to simplify distributed cloud integrations.
## Compute and Containers

### Kubernetes

#### AKS Engine

  - **(2021)** [thenewstack.io: Azure Kubernetes Service Replaces Docker with containerd](https://thenewstack.io/azure-kubernetes-service-replaces-docker-with-containerd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical deep dive into the deprecation of Docker-shim in Azure Kubernetes Service (AKS) in favor of the containerd container runtime. This architectural shift eliminates runtime abstraction layers, drastically reducing node CPU and memory footprint overhead. Real-world implementation details confirm improved container launch latencies and optimal alignment with CNCF runtime specifications.
## Container Orchestration (3)

### Operating Systems

#### Azure Linux

  - **(2023)** [theregister.com: Microsoft has made Azure Linux generally available. Repeat, Azure Linux](https://www.theregister.com/software/2023/05/26/microsofts-azure-linux-distro-is-now-generally-available/568359) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on the GA release of Azure Linux, Microsoft's proprietary container host OS designed for AKS (CBL-Mariner). Optimized for minimal resource usage, fast boot times, and hardened security profiles. Azure Linux provides platform architects with a highly resilient host platform for secure Kubernetes worker nodes.
## DevOps

### CI-CD Pipelines (1)

#### Build Templates

  - **(2025)** [==microsoft/azure-pipelines-yaml: maven.yml==](https://github.com/microsoft/azure-pipelines-yaml/blob/master/templates/maven.yml) <span class='md-tag md-tag--info'>⭐ 1287</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-47539571" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 8 L 20 2 L 30 3 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-47539571)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Standardized Maven build template for Azure Pipelines. Configures secure package dependency restoration, execution of JUnit/TestNG tests, build caching parameters, and target JAR/WAR compilation workflows.
## Developer Experience

### CI-CD Runners

#### Ephemeral Containers

  - **(2024)** [nedinthecloud.com: Using azure container instances for an azure dev ops self hosted agent](https://nedinthecloud.com/2024/04/15/using-azure-container-instances-for-an-azure-devops-self-hosted-agent) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walks through establishing ephemeral, self-hosted Azure DevOps agent runners running within Azure Container Instances (ACI). Simplifies pipeline scaling and minimizes runner maintainability overhead.
## Governance and Management

### Enterprise Governance

#### Kubernetes Compliance

  - **(2021)** [techcommunity.microsoft.com: Azure Policy for Kubernetes releases support for custom policy](https://techcommunity.microsoft.com/blog/azuregovernanceandmanagementblog/azure-policy-for-kubernetes-releases-support-for-custom-policy/2699466) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical deep dive into Azure Policy integration with AKS, highlighting the support for custom policy definitions via OPA Gatekeeper. Enables platform engineers to build and enforce hyper-customized constraints on pods, network namespaces, and registry origins inside Kubernetes clusters.
## Healthcare IT

### Medical Imaging

#### Azure Healthcare APIs

  - **(2025)** [Microsoft - DICOM Service](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom) <span class='md-tag md-tag--warning'>[C# CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Azure's managed DICOMweb-compliant API designed for scalable medical imaging storage, access, and ingestion. Includes architectural links to OSS DICOM and FHIR server implementations for robust healthcare interoperability.
## Identity and Access

### Cloud Security

#### Workload Identity

##### Managed Identities

  - **(2024)** [==codewithme.cloud: Why aren’t you using Managed Identities?!==](https://codewithme.cloud/posts/2024/02/why-arent-you-using-secretless-authentication) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Advocates for the total elimination of secrets from application codebases by implementing Managed Identities. In 2026, secretless authentication using Managed Identities is the standard approach for cloud-native workloads, significantly reducing the risk of security leaks.
  - **(2023)** [**itnext.io: Secure Azure Cosmos DB access by using Azure Managed Identities**](https://itnext.io/secure-azure-cosmos-db-access-by-using-azure-managed-identities-55f9fdf48fda) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Details how to configure secretless authentication for Azure Cosmos DB databases using System-Assigned and User-Assigned Managed Identities. In 2026, avoiding static connection strings by utilizing native Entra ID RBAC data planes is the standard pattern for securing cloud-native microservice applications.
  - **(2024)** [linkedin.com/pulse: No Credentials, No Problem - using Azure Managed Identity](https://www.linkedin.com/pulse/credentials-problem-using-azure-managed-identity-dimitar-iliev--wzzaf) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a practical guide on setting up passwordless connections within Azure resources. Modern 2026 environments see this methodology as essential for zero-trust architectures, ensuring credentials never exist on disks or within environment variables.
## Identity and Access (1)

### Managed Identities (1)

#### Secretless Architectures

##### Graph API

  - **(2022)** [blog.yannickreekmans.be: Secretless applications: add permissions to a Managed Identity](https://blog.yannickreekmans.be/secretless-applications-add-permissions-to-a-managed-identity) <span class='md-tag md-tag--warning'>[POWERSHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Instructs engineers on configuring credential-free infrastructure inside Azure. Demystifies direct graph permissions injection on active user or system Managed Identities to avoid hardcoded credentials.
## Infrastructure

### Networking

#### Ingress

##### Azure Application Gateway

  - **(2025)** [==Application Gateway for Containers with AKS Overlay Networking and VNet Flow Logs==](https://blog.cloudtrooper.net/2025/04/02/application-gateway-for-containers-a-not-so-gentle-intro-4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A deep-dive technical investigation of Azure's next-generation Application Gateway for Containers (AGC) running atop AKS Overlay Networking. Details the setup, logging mechanics, and network telemetry capture.
  - **(2025)** [**Introduction to Azure Application Gateway for Containers (AGC)**](https://blog.cloudtrooper.net/2025/02/28/application-gateway-for-containers-a-not-so-gentle-intro-1) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — An introductory architecture guide covering the capabilities of Azure's modern Application Gateway for Containers (AGC). Illustrates how it integrates natively via Gateway API parameters to deliver low-latency application routing.
## Infrastructure Automation

### Infrastructure as Code (2)

#### Azure Bicep

##### Declarative Deployments

  - **(2026)** [==Bicep==](https://github.com/Azure/bicep) <span class='md-tag md-tag--info'>⭐ 3605</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-11af08d9" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 8 L 20 9 L 30 2 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-11af08d9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[BICEP CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier declarative DSL for provisioning Azure resources. Bicep simplifies the authoring experience over raw JSON ARM templates, featuring modular design structures and native validation checks.
### Shell Customization

#### Oh-My-Posh

##### Kubernetes Integration

  - **(2021)** [blog.guybarrette.com: Powershell prompt: How to display your current Kubernetes context using Oh-My-Posh 3 🌟](https://www.linkedin.com/newsletters/6962087231775772672) <span class='md-tag md-tag--warning'>[POWERSHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walkthrough on utilizing Oh-My-Posh engine configurations in PowerShell Core prompts to output current active Kubernetes clusters and contexts. Improves administrator visual feedback loops to prevent accidental namespace deployments.
## Microservices

### .NET Microservices

#### Project Tye

  - **(2020)** [techcommunity.microsoft.com: Building a path to success for microservices and .NET Core - Project Tye + GitHub Actions](https://techcommunity.microsoft.com/blog/appsonazureblog/building-a-path-to-success-for-microservices-and-net-core---project-tye--github-/1502270) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — Explores local microservice discovery and container orchestration using Microsoft's experimental Project Tye alongside GitHub Actions. While Project Tye is legacy, it represents a core structural stage in .NET microservices evolution.
## Network and Delivery

### API Management (1)

#### Monetization Models

  - **(2023)** [jmfloreszazo.com: Monetizar un API, con Azure API Management](https://jmfloreszazo.com/monetizar-un-api-con-azure-api-management) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spanish guide explaining the deployment of API monetization policies using Azure API Management (APIM). Focuses on quota restrictions, rate-limiting, subscription keys, and stripe integrations.
#### Workspace Migration

  - **(2024)** [github.com/Azure-Samples/api-management-workspaces-migration: Azure API' Management workspaces migration tool](https://github.com/Azure-Samples/api-management-workspaces-migration) <span class='md-tag md-tag--info'>⭐ 2</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-9048c619" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 7 L 20 5 L 30 8 L 40 8 L 50 4" fill="none" stroke="url(#spark-grad-9048c619)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official migration tool sample designed to transition traditional single-tenant Azure API Management APIs into modern, decentralized workspaces. Helps partition governance duties and resource isolation.
### Global Routing

#### DNS Traffic Management

  - **(2024)** [Azure Traffic Manager](https://learn.microsoft.com/en-us/azure/traffic-manager) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation for Azure Traffic Manager, a DNS-based traffic load balancer. Highlights performance-based routing, geographic routing configurations, and seamless service failover strategies for global-scale cloud architectures.
## Operating Systems (1)

### Azure Linux (1)

#### Kernel Curation

  - **(2026)** [==github.com/microsoft/CBL-Mariner==](https://github.com/microsoft/azurelinux) <span class='md-tag md-tag--info'>⭐ 4994</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-eaed73d2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 10 L 20 10 L 30 11 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-eaed73d2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official repository for Azure Linux (formerly CBL-Mariner), a lightweight, container-optimized OS designed for minimal footprint and maximum security inside AKS. Strips away non-essential packages to shrink attack surfaces and secure running microservices.
## Quality Assurance

### Performance Testing

#### Azure Load Testing

  - **(2025)** [==github.com/Azure-Samples/azure-load-testing-samples 🌟==](https://github.com/Azure-Samples/azure-load-testing-samples) <span class='md-tag md-tag--info'>⭐ 27</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b2d0558d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 6 L 20 3 L 30 4 L 40 11 L 50 13" fill="none" stroke="url(#spark-grad-b2d0558d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official Microsoft repository containing sample configurations and automation scripts for Azure Load Testing. Promotes direct integration of high-scale performance testing pipelines within existing Git workflows.
## Security and Identity

### API Security

#### Runtime Threat Protection

  - **(2023)** [techcommunity.microsoft.com: Microsoft Announces General Availability of Defender for APIs](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/microsoft-announces-general-availability-of-defender-for-apis/3981488) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spotlights the GA release of Microsoft Defender for APIs. Integrates directly with Azure API Management to inspect API security posture, analyze traffic patterns for anomalies, and defend backend microservices from complex runtime vectors.
### Vulnerability Research

#### Container Escape

  - **(2021)** [unit42.paloaltonetworks.com: Finding Azurescape – Cross-Account Container Takeover in Azure Container Instances](https://unit42.paloaltonetworks.com/azure-container-instances) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical autopsy of 'Azurescape', a cross-account vulnerability discovered in Azure Container Instances (ACI). Analyzes multitenancy container host escapes and explains subsequent platform-level security mitigations.

---
💡 **Explore Related:** [AWS](./aws.md) | [Managed Kubernetes In Public Cloud](./managed-kubernetes-in-public-cloud.md) | [Edge Computing](./edge-computing.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

