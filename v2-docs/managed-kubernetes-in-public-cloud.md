---
description: "Curated, AI-ranked Managed Kubernetes In Public Cloud resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Cloud Providers."
---
# Managed Kubernetes in Public Cloud

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/managed-kubernetes-in-public-cloud/).

!!! info "Architectural Context"
    Detailed reference for Managed Kubernetes in Public Cloud in the context of Cloud Providers (Hyperscalers).

## Alternative Cloud

### DigitalOcean Kubernetes DOKS

#### GitOps and Continuous Delivery

  - **(2022)** [digitalocean.com: Automating GitOps and Continuous Delivery With DigitalOcean Kubernetes (Terraform, Helm and Flux)](https://www.digitalocean.com/community/tech-talks/automating-gitops-and-continuous-delivery-with-digitalocean-kubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide on implementing declarative GitOps structures on DOKS using Flux CD, Terraform, and Helm charts. Provides a complete architectural template for managing infrastructure and application configurations declaration-first, reducing configuration drift in production.
### Linode Kubernetes Engine LKE

#### Autoscaling Core

  - **(2022)** [dev.to: Practical Introduction to Kubernetes Autoscaling Tools with Linode Kubernetes Engine 🌟](https://dev.to/rahulrai/practical-introduction-to-kubernetes-autoscaling-tools-with-linode-kubernetes-engine-2i7k) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to Kubernetes scaling tools (HPA, VPA, and Cluster Autoscaler) leveraging the Linode Kubernetes Engine (LKE). This guide demystifies metric validation loops and autoscaler behavior, providing a practical foundation for engineers implementing scaling outside major hyperscalers.
## Architecture and Design

### Microservices Design

#### Production AKS Deployment

  - **(2021)** [optisolbusiness.com: Implementing Microservices Architecture in AKS](https://www.optisolbusiness.com/insight/implementing-microservices-architecture-in-aks) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details blueprint designs for structural microservices running on AKS clusters. Reviews optimal container scaling, deployment strategies, and integration with container registries (ACR). Guides engineers on transforming multi-container apps into production-ready architectures.
### Serverless Migrations

#### Container Apps

  - **(2022)** [dev.to: Moving Azure Functions from AKS to Container Apps](https://dev.to/christle/moving-azure-functions-from-aks-to-container-apps-k60) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical migration post detailing the shift of Azure Functions from AKS (utilizing KEDA) into Azure Container Apps (ACA). Compares resource footprints, administration friction, and scale behaviors. Highly educational for choosing the correct serverless scale model.
## Architecture Blueprint

### Multi-Cloud and Azure

#### Infrastructure Design

  - **(2024)** [github.com/stephaneey/azure-and-k8s-architecture: Azure and K8s Architecture' 🌟](https://github.com/stephaneey/azure-and-k8s-architecture) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated open-source repository featuring detailed visual design maps and deployment blueprints for running enterprise-grade workloads on Azure and AKS. Demonstrates architectural patterns for network security zoning, private endpoints, DNS configuration, and highly isolated hub-and-spoke virtual networks.
## Cloud Infrastructure

### AWS

#### Container Orchestration

  - **(2023)** [cast.ai: AWS EKS vs. ECS vs. Fargate: Where to manage your Kubernetes?](https://cast.ai/blog/aws-eks-vs-ecs-vs-fargate-where-to-manage-your-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive comparing AWS ECS, EKS, and serverless container execution via AWS Fargate. Synthesizing live cloud architectural trends, it presents insights into financial management, operational simplicity, and dynamic resource scaling, mapping out the trade-offs of using managed VM pools versus completely serverless options.
  - **(2022)** [clickittech.com: Amazon ECS vs EKS : The Best Container Orchestration Platform](https://www.clickittech.com/cloud-services/amazon-ecs-vs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This comprehensive comparison highlights the operational differences, cost implications, and architecture layouts of Amazon ECS versus Amazon EKS. EKS targets standard Kubernetes-based deployments requiring high portability, while ECS is a highly optimized, opinionated AWS native orchestrator designed for seamless integration.
  - **(2021)** [cloudonaut.io: Scaling Container Clusters on AWS: ECS and EKS](https://cloudonaut.io/scaling-container-clusters-on-aws-ecs-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed comparative analysis of scaling strategies between Amazon ECS and EKS clusters. The article walks through key operational considerations, including EC2 Auto Scaling Groups, Karpenter, cluster autoscalers, and resource utilization dynamics, highlighting how choice of orchestration influences microservices scale limits.
### Amazon EKS

#### Deployments

  - **(2021)** [youtube/StackSimplify: Kubernetes Deployments on AWS EKS | Amazon Elastic Kubernetes Service | Amazon EKS 🌟](https://www.youtube.com/watch?v=vZK_W-fpft0&ab_channel=StackSimplify) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video-guided technical deep dive detailing how to launch and manage standard Kubernetes Deployments on AWS EKS. It covers declarative manifest configuration, pod scaling strategies, and external exposure of services through AWS integration.
#### Traffic Management

  - **(2022)** [Create a pipeline with canary deployments for Amazon EKS with AWS App Mesh 🌟](https://aws.amazon.com/blogs/containers/create-a-pipeline-with-canary-deployments-for-amazon-eks-with-aws-app-mesh) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive technical walkthrough on implementing canary deployment pipelines using Amazon EKS and AWS App Mesh. It details the integration of AWS CodePipeline and Envoy-based service meshes to orchestrate fine-grained traffic shifting, minimizing blast radiuses during software rollouts.
### Auto-scaling

#### Fargate

  - **(2021)** [aws.amazon.com: Autoscaling EKS on Fargate with custom metrics](https://aws.amazon.com/blogs/containers/autoscaling-eks-on-fargate-with-custom-metrics) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores scaling mechanisms for EKS pods deployed onto AWS Fargate using Prometheus-emitted custom metrics. Illustrates HPA structures that scale serverless compute workloads without maintaining EC2 scaling profiles.
#### Prometheus

  - **(2021)** [aws.amazon.com: Using Prometheus Adapter to autoscale applications running on Amazon EKS](https://aws.amazon.com/blogs/mt/automated-scaling-of-applications-running-on-eks-using-custom-metric-collected-by-amazon-prometheus-using-prometheus-adapter) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to configure the Prometheus Adapter to expose custom application metrics to the Kubernetes Horizontal Pod Autoscaler (HPA). The article outlines ingestion pipelines from Amazon Managed Service for Prometheus to enable dynamic workload scaling.
### Container Orchestration (1)

#### AKS Integration

  - **(2023)** [techcommunity.microsoft.com: How to install an AKS cluster with the Istio service mesh add-on via Bicep](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/how-to-install-an-aks-cluster-with-the-istio-service-mesh-add-on-via-bicep/3802069) <span class='md-tag md-tag--warning'>[BICEP CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the automated provisioning of Azure Kubernetes Service (AKS) coupled with the native Istio service mesh add-on using Bicep. This blueprint demonstrates declarative service mesh lifecycle management, reducing manual Helm or post-deployment orchestration overhead.
#### EKS Security

  - **(2023)** [Amazon EKS introduces EKS Pod Identity](https://aws.amazon.com/about-aws/whats-new/2023/11/amazon-eks-pod-identity) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — EKS Pod Identity simplifies the association of IAM roles with Kubernetes service accounts. This model bypasses the complexities of OIDC trust configurations, offering highly scalable, secure, and isolated credential structures for containers.
### Continuous Delivery

#### GitOps

  - **(2020)** [pages.awscloud.com: GitOps on AWS for High Performing Team Operations (eBook)](https://pages.awscloud.com/GLOBAL-partner-DL-DevOps-weaveworks-ebook-2020-learn.html) <span class='md-tag md-tag--warning'>[PDF CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An e-book co-authored by AWS and Weaveworks exploring the deployment of GitOps workflows on AWS. It presents architectural patterns for using declarative systems to synchronize desired states defined in Git with operational EKS environments.
#### Preview Environments

  - **(2022)** [thenewstack.io: How We Built Preview Environments on Kubernetes and AWS](https://thenewstack.io/how-we-built-preview-environments-on-kubernetes-and-aws) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural case study illustrating how to dynamically generate on-demand sandbox preview environments on AWS EKS. It outlines how custom controllers spin up ephemeral namespaces triggered by GitHub pull requests, improving QA workflows.
### Infrastructure as Code

#### Terraform

  - **(2021)** [youtube: CloudGeeks - Terraform Eks Kubernetes RDS Secrets Manager Eksctl Cloudformation ALB Controller (Redmine App)](https://www.youtube.com/watch?v=OFZYIr66Ku4&ab_channel=cloudgeeksinc) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive practical video guide displaying multi-tier app deployment. Integrates Terraform, EKS, RDS, AWS Secrets Manager, and AWS ALB Controller to assemble an enterprise-grade cloud footprint.
### Multi-Cluster Management

#### Case Study

  - **(2021)** [Onfido’s Journey to a Multi-Cluster Amazon EKS Architecture](https://aws.amazon.com/blogs/containers/onfidos-journey-to-a-multi-cluster-amazon-eks-architecture) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores Onfido's architectural transition from single-cluster configurations to a multi-region, multi-cluster Amazon EKS framework. Details scaling hurdles, network federation, load balancing, and configuration management at global enterprise scale.
### Networking

#### Ingress Controllers

  - **(2026)** [==github.com/kubernetes-sigs/aws-load-balancer-controller==](https://github.com/kubernetes-sigs/aws-load-balancer-controller) <span class='md-tag md-tag--info'>⭐ 4300</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d9499149" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 7 L 20 2 L 30 10 L 40 13 L 50 3" fill="none" stroke="url(#spark-grad-d9499149)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The core controller that manages AWS Elastic Load Balancers (ALB and NLB) on behalf of a Kubernetes cluster. Live Grounding verifies its continuous support for advanced features like target grouping by IP, ACM certificate integration, and shared ALBs. It acts as the primary ingress controller for modern AWS EKS network architectures.
  - **(2021)** [aws.amazon.com: Kubernetes Ingress with AWS ALB Ingress Controller](https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Covers the deployment and usage architecture of the AWS Application Load Balancer (ALB) Ingress Controller. It shows how the controller interprets Kubernetes Ingress resources to provision physical AWS ALB layers, routing external HTTP traffic directly to backend pods.
#### Scale Optimization

  - **(2022)** [engineering.salesforce.com: Optimizing EKS networking for scale](https://engineering.salesforce.com/optimizing-eks-networking-for-scale-1325706c8f6d) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical case study detailing Salesforce's optimizations of the AWS VPC CNI within high-density EKS clusters. It addresses IP address exhaustion, custom networking configurations, prefix delegation, and scaling metrics crucial for maintaining thousands of ephemeral microservices.
## Cloud Providers

### AWS EKS

#### GitOps and Automation

##### Infrastructure Provisioning

  - **(2023)** [aws.amazon.com: GitOps model for provisioning and bootstrapping Amazon EKS clusters using Crossplane and Argo CD](https://aws.amazon.com/blogs/containers/gitops-model-for-provisioning-and-bootstrapping-amazon-eks-clusters-using-crossplane-and-argo-cd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates an elegant architectural GitOps paradigm that unifies cloud infrastructure and software delivery. Integrates Crossplane for declarative AWS API provisioning with Argo CD for continuous application state synchronizations.
#### Hybrid Cloud

##### Service Mesh Integration

  - **(2022)** [solo.io: Connect Your Services Seamlessly with Amazon EKS Anywhere and Istio](https://www.solo.io/blog/amazon-eks-anywhere-and-solo-istio) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on extending enterprise network topologies and security controls to the hybrid-edge using Solo Gloo Mesh (Istio) over EKS Anywhere nodes. Streamlines cross-cloud security boundaries and load balancing profiles.
#### Networking (1)

##### Private Connectivity

  - **(2022)** [docs.aws.amazon.com: Access container applications privately on Amazon EKS using AWS PrivateLink and a Network Load Balancer](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-container-applications-privately-on-amazon-eks-using-aws-privatelink-and-a-network-load-balancer.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed architectural pattern showcasing secure, private consumption of containerized applications deployed on Amazon EKS. Leverages AWS PrivateLink integrated with a Network Load Balancer (NLB) to isolate traffic from the public internet entirely.
##### Service Mesh Latency

  - **(2023)** [aws.amazon.com: Addressing latency and data transfer costs on EKS using Istio](https://aws.amazon.com/blogs/containers/addressing-latency-and-data-transfer-costs-on-eks-using-istio) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural guide analyzing multi-AZ data transfer charges and service-to-service latency in EKS. Demonstrates how to design topology-aware routing strategies within an Istio Service Mesh to keep traffic localized and cost-effective.
### Azure Kubernetes Service AKS

#### API Gateway

  - **(2023)** [returngis.net: Exponer APIs en AKS a través de Azure API Management](https://www.returngis.net/2023/05/exponer-apis-en-aks-a-traves-de-azure-api-management) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a hands-on architectural walkthrough for exposing microservices deployed on AKS through Azure API Management (APIM). Focuses on securing internal endpoints via private virtual network injection, setting up private DNS zones, and orchestrating ingress paths with NGINX or AGIC. Essential reading for configuring robust API monetization and rate-limiting behaviors.
#### Ingress and Routing

  - **(2023)** [returngis.net: Desplegar AGIC en AKS utilizando workload identity](https://www.returngis.net/2023/05/desplegar-agic-en-aks-utilizando-workload-identity) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A deep dive into deploying the Azure Application Gateway Ingress Controller (AGIC) utilizing passwordless Azure AD Workload Identity instead of legacy pod-managed identity options. By using OpenID Connect (OIDC) federation, this design model mitigates key-rotation liabilities and secures the control plane path to application gateways. This configuration represents the de facto standard for zero-trust ingress security on Azure.
#### Multi-Tenancy

  - **(2024)** [learn.microsoft.com: Use Application Gateway Ingress Controller (AGIC) with a multitenant Azure Kubernetes Service](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/aks-agic/aks-agic) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This official reference architecture outlines deployment scenarios for using AGIC within multi-tenant AKS cluster designs. It synthesizes strategies for shared vs. dedicated Application Gateways, details path-based and host-based microservices routing, and outlines how to securely terminate TLS while enforcing Web Application Firewall (WAF) rule sets at the perimeter.
#### Security

  - **(2024)** [learn.microsoft.com: Deploy AKS and API Management with mTLS](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-mutual-certificates-for-clients) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation for implementing mutual TLS (mTLS) configurations between Azure API Management (APIM) and backend AKS services. Includes certificate exchange setups, ingress controller enforcement (such as NGINX), and identity validation processes. Necessary blueprinting for highly compliant systems such as open-banking and healthcare APIs.
  - **(2023)** [techcommunity.microsoft.com: Securing Windows workloads on Azure Kubernetes Service with Calico](https://techcommunity.microsoft.com/blog/containers/securing-windows-workloads-on-azure-kubernetes-service-with-calico/3815429) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This architectural guide details how to leverage Tigera Calico's CNI and policy engine to enforce advanced microsegmentation on Windows workloads within Azure Kubernetes Service (AKS). It addresses heterogeneous node pool configurations (Windows and Linux mixed architectures) and demonstrates how to apply consistent security policies across dual-OS workloads to meet strict enterprise isolation and compliance requirements.
### Google Kubernetes Engine GKE

#### Cost Optimization

  - **(2021)** [cloud.google.com: Announcing Spot Pods for GKE Autopilot—save on fault tolerant workloads](https://cloud.google.com/blog/products/containers-kubernetes/announcing-spot-pods-for-gke-autopilot) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Spot Pods for GKE Autopilot, enabling cost reductions of up to 60-80% for fault-tolerant, stateless workloads and background microservices. Examines how Autopilot schedules, preempts, and relocates workloads based on Google's excess compute capacity without operator intervention.
#### DNS Optimization

  - **(2024)** [Setting up NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed technical guide to configuring NodeLocal DNSCache on GKE clusters. By running a lightweight caching agent as a node-level DaemonSet, this pattern prevents connection track table exhaustion and significantly decreases DNS lookup latency for high-throughput microservices.
  - **(2024)** [Kubernetes Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-dns) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical documentation for implementing Cloud DNS for GKE. Illustrates how integrating managed GCP Cloud DNS with GKE clusters removes the CPU/Memory overhead of running in-cluster CoreDNS (kube-dns) instances. Essential for highly-scaled microservices architectures prone to DNS query bottlenecking.
#### Ingress and Routing (1)

  - **(2022)** [Using new traffic control features in External HTTP(S) load balancer](https://cloud.google.com/blog/products/networking/how-to-use-new-traffic-control-features-in-cloud-load-balancing) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details advanced traffic engineering patterns utilizing Google Cloud external HTTP(S) Load Balancing. Outlines how GKE architects can configure header-based request redirection, traffic mirroring, and weight-based canary routes directly at the external ingress tier to construct robust microservices patterns.
#### Multi-Cluster Architectures

  - **(2022)** [cloud.google.com: How to do multi-cluster Kubernetes in the real world—one GKE shop’s approach](https://cloud.google.com/blog/products/containers-kubernetes/multi-cluster-kubernetes-with-gke-at-geotab) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A real-world engineering case study from Geotab detailing their approach to multi-cluster GKE administration. Addresses cross-region latency issues, regional failover strategies, and global DNS configurations, demonstrating how to maintain highly available microservices environments at scale.
#### Multi-Cluster Networking

  - **(2021)** [cloud.google.com: Discover and invoke services across clusters with GKE multi-cluster services](https://cloud.google.com/blog/products/containers-kubernetes/introducing-gke-multi-cluster-services) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces GKE Multi-Cluster Services (MCS), allowing cross-cluster service discovery and load balancing using standard Kubernetes primitives. Enables seamless cross-cluster communication, simplifying geographic scaling, disaster recovery architectures, and multi-region microservice fabrics.
#### Performance Scaling

  - **(2021)** [acloudguru.com: GKE ludicrous speed! GKE Image Streaming speeds up container starts](https://www.pluralsight.com/resources/blog/cloud/gke-ludicrous-speed-gke-image-streaming-speeds-up-container-starts) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores GKE Image Streaming, a performance feature that speeds up container startups by lazy-loading image layers over the network. By starting pods before the entire image is downloaded, this architecture accelerates auto-scaling and quickens recovery times from node failures.
#### Security and IAM

  - **(2024)** [Fetches all Primitive and Predefined GCP IAM Roles](https://github.com/darkbitio/gcp-iam-role-permissions) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source security tool that parses and exports GCE IAM pre-defined and primitive role definitions. Helps platform security architects map precise least-privilege configurations when implementing Workload Identity bounds inside production GKE clusters.
### Microsoft AKS

#### Microservices Design (1)

##### Production Architecture

  - **(2023)** [docs.microsoft.com: Microservices architecture on Azure Kubernetes Service (AKS) 🌟](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-microservices/aks-microservices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural design guide detailing enterprise container patterns for deploying robust, scalable, and secure microservices architectures natively inside Azure Kubernetes Service.
## Container Platforms

### Enterprise Platforms

#### KubeSphere

  - **(2026)** [kubesphere.io](https://kubesphere.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — KubeSphere is a distributed, multi-tenant enterprise container platform built on top of Kubernetes. It provides an intuitive GUI dashboard for managing multi-cloud container orchestration, DevOps pipelines (Jenkins-based), service meshes (Istio), observability, and microservice governance. (Live Grounding: Actively developed in 2026, offering a complete, modular, cloud-agnostic platform alternative to OpenShift).
  - **(2020)** [itnext.io: KubeSphere: A New Pluggable Kubernetes Application Management Platform](https://itnext.io/kubesphere-a-new-pluggable-kubernetes-application-management-platform-bf078b9f3330) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the modular and pluggable architecture of KubeSphere, showing how enterprises can customize their deployments by enabling or disabling components like DevOps, Service Mesh, and Logging/Monitoring. Discusses native application lifecycle management integrations. (Live Grounding: Underlines KubeSphere's strategic market position as a flexible, lower-overhead alternative to Red Hat OpenShift).
## Delivery and CICD

### Application Packaging

#### Draft and Acorn

  - **(2023)** [medium.com/@pauldotyu: Effortlessly Deploy to AKS with Open Source Tools Draft and Acorn](https://medium.com/@pauldotyu/app-to-aks-with-draft-and-acorn-2d25f19649b7) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Focuses on simplifying development workflows on AKS using Draft and Acorn. Streamlines container generation and cluster deployments. Live grounding note: Acorn changed operations in early 2024, emphasizing legacy community-tool status.
### Continuous Deployment

#### Azure Pipelines

  - **(2023)** [azuredevopslabs.com: Deploying a multi-container application to Azure Kubernetes Services](https://azuredevopslabs.com/labs/vstsextend/kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An interactive, practical lab illustrating the step-by-step setup of continuous delivery pipelines targeting AKS using Azure DevOps. Covers container builds, ACR image pushes, and multi-stage YAML pipeline deployment structures.
## Developer Experience

### Inner Loop Development

#### Local Tooling

  - **(2023)** [==Azure/Draft 🌟==](https://github.com/Azure/draft) <span class='md-tag md-tag--info'>⭐ 642</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2026e583" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 6 L 20 4 L 30 12 L 40 8 L 50 8" fill="none" stroke="url(#spark-grad-2026e583)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Azure Draft simplifies early-stage developer onboarding onto Kubernetes. By scanning source code directories, it automatically generates containerization assets including Dockerfiles, Kubernetes manifests, Helm charts, and deployment workflows.
## Infrastructure

### Ingress and Routing (2)

#### Application Gateway AGIC

  - **(2022)** [returngis.net: Configurar más de un Application Gateway con AGIC para AKS](https://www.returngis.net/2022/05/configurar-mas-de-un-application-gateway-con-agic-para-aks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Written in Spanish, this technical guide explains how to control multiple Azure Application Gateways through a single AGIC controller inside AKS. Explains resource routing partitions between internal microservices and public endpoints.
  - **(2020)** [itnext.io: Kubernetes Ingress on Azure using the Application Gateway](https://itnext.io/kubernetes-ingress-on-azure-using-the-application-gateway-2779b647deb5) <span class='md-tag md-tag--warning'>[YAML/TERRAFORM CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes configuring the Application Gateway Ingress Controller (AGIC) to leverage Azure's Layer 7 load balancer inside AKS clusters. Outlines integrating native Web Application Firewall (WAF) services and avoiding extra routing hops. Promotes scalable network architectures for modern APIs.
#### Dynamic DNS

  - **(2022)** [dev.to/javiermarasco: HTTPs with Ingress controller, cert-manager and DuckDNS (in AKS/Kubernetes)](https://dev.to/javiermarasco/https-with-ingress-controller-cert-manager-and-duckdns-in-akskubernetes-2jd1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents a dynamic DNS development environment setup using cert-manager, NGINX ingress, and DuckDNS on AKS clusters. Helps development teams quickly wire secure, externally accessible TLS endpoints without needing official domain registrations.
#### ExternalDNS

  - **(2023)** [techcommunity.microsoft.com: Kubernetes External DNS for Azure DNS & AKS](https://techcommunity.microsoft.com/blog/coreinfrastructureandsecurityblog/kubernetes-external-dns-for-azure-dns--aks/3809393) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines configuring ExternalDNS inside an AKS cluster to dynamically sync Kubernetes Ingress resources with Azure DNS zones. Avoids manual DNS configuration, automating resource and IP updates on target domain records.
#### Hybrid Ingress Architecture

  - **(2021)** [returngis.net: Azure Application Gateway con WAF y wildcard + Nginx Controller para AKS](https://www.returngis.net/2021/11/azure-application-gateway-con-waf-y-wildcard-nginx-controller-para-aks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A Spanish-language architecture guide demonstrating a hybrid ingress design: placing an Azure Application Gateway (with WAF enabled) in front of an in-cluster NGINX ingress controller. Solves wildcard SSL setups and advanced ingress rules within AKS.
#### TLS Ingress Controller

  - **(2020)** [docs.microsoft.com: Create an HTTPS ingress controller on Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/previous-versions/azure/aks/ingress-tls) <span class='md-tag md-tag--warning'>[YAML/BASH CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A legacy Microsoft technical manual outlining the step-by-step deployment of an NGINX ingress controller with cert-manager on AKS. Curators highlight its historical value in configuring dynamic TLS certificates via Let's Encrypt. Live grounding shows this is marked as a legacy/previous version doc, as engineering teams in 2026 favor native Application Gateway Ingress Controller (AGIC) or native Istio integrations.
### Networking and CNI

#### Azure CNI Cilium

  - **(2022)** [isovalent.com: Announcing Azure CNI Powered by Cilium](https://isovalent.com/blog/post/azure-cni-cilium) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Isovalent's technical summary showcasing Azure CNI powered by Cilium integration. This architecture combines Azure's high-performance native routing fabrics with the advanced, secure eBPF-driven networking layer of Cilium. Represents the modern standard for fast AKS networking in 2026.
#### Calico eBPF

  - **(2021)** [thenewstack.io: Turbocharging AKS Networking with Calico eBPF](https://thenewstack.io/turbocharging-aks-networking-with-calico-ebpf) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the performance enhancements derived from running Calico's eBPF data plane over AKS cluster topologies. Discusses how bypassing traditional iptables routing overhead reduces connection latency and CPU usage. It remains a relevant comparative benchmark for high-performance networks.
#### WireGuard Encryption

  - **(2021)** [tigera.io: Calico WireGuard support with Azure CNI](https://www.tigera.io/blog/calico-wireguard-support-with-azure-cni) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines configuring Calico WireGuard encryption overlaying Azure CNI networks. Details setting up highly secure node-to-node transport layer encryption with minimal CPU overhead. Grounding points to this as an excellent alternative to heavy IPsec deployments.
### Provisioning and IaC

#### AWS CDK and Multicluster

  - **(2022)** [Using CDK to perform continuous deployments in multi-region Kubernetes environments](https://aws.amazon.com/blogs/containers/using-cdk-to-perform-continuous-deployments-in-multi-region-kubernetes-environments) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the use of AWS Cloud Development Kit (CDK) to model continuous delivery systems across multi-region Kubernetes deployments. Highly relevant for cloud engineers designing hybrid-cloud architectures that span AKS and EKS infrastructure.
## Networking (2)

### Multi-Cluster

#### DNS

  - **(2022)** [nginx.com: Automating Multi-Cluster DNS with NGINX Ingress Controller](https://www.f5.com/products/nginx) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical blueprint showcasing DNS synchronization and traffic routing automation across multi-cluster environments. Demonstrates leveraging NGINX Ingress for global load balancing and resilient geographical failovers.
## Observability

### Telemetry

#### Azure Monitoring

  - **(2022)** [grafana.com: Scrape Azure metrics and monitor AKS using Grafana Agent 🌟](https://grafana.com/blog/scrape-azure-metrics-and-monitor-aks-using-grafana-agent) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A telemetry extraction guide focused on deploying Grafana Agent inside AKS to scrape and forward metrics directly to Grafana Cloud. Avoids expensive, proprietary log-forwarding configurations and maintains unified telemetry visualization dashboards.
## Orchestration

### Azure Compute

#### AKS and ACI

  - **(2022)** [k21academy.com: Azure Kubernetes Service & Azure Container Instances For Beginners 🌟](https://k21academy.com/azure-cloud/azure-container-instances-and-kubernetes-service) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory training reference explaining Azure Kubernetes Service (AKS) and Azure Container Instances (ACI). Describes virtual node orchestration patterns to dynamically offload execution spikes from AKS onto ACI serverless compute.
### Azure Networking

#### AKS VNET Integration

  - **(2021)** [azurecloudai.blog: Deploy Azure Kubernetes Service (AKS) to a preexisting VNET](https://azurecloudai.blog/verify.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide outlining the architectural parameters needed to deploy Azure Kubernetes Service (AKS) within a custom, pre-existing Virtual Network (VNET). Addresses CIDR constraints, subnet delegation, and Azure CNI configurations.
### Kubernetes

#### Managed Kubernetes Comparison

  - **(2021)** [stackrox.com: EKS vs GKE vs AKS - Evaluating Kubernetes in the Cloud](https://www.stackrox.io/blog/eks-vs-gke-vs-aks-jan2021) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A multi-dimensional comparison of the three primary managed Kubernetes services: AWS EKS, Google GKE, and Azure AKS. Weighs crucial metrics including control plane management fees, SLA guarantees, automated master scaling, and IAM-to-K8s role bindings.
## Platform Engineering

### CICD and Delivery

#### Developer Experience (1)

  - **(2023)** [youtube: Day -25 | No Dockerfile, No K8s Manifests | Setup CI/CD in 5 minutes for any programming language](https://www.youtube.com/watch?v=io_yBU7vhIo) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates rapid deployment flows to Kubernetes bypassing standard manual Dockerfile and YAML manifest configurations. Showcases automated scaffolding utilities like Draft and Cloud Native Buildpacks. Targeted at reducing onboarding friction for software developers moving applications to production orchestrators.
#### GitHub Actions

  - **(2023)** [insights.project-a.com: Using GitHub Actions to deploy to Kubernetes in GKE 🌟](https://www.project-a.vc/perspectives) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical roadmap for setting up secure Continuous Delivery pipelines to GKE using GitHub Actions. Specifically covers passwordless identity validation utilizing GCP Workload Identity Federation (WIF) to eliminate long-lived GCP service account JSON keys. Walks through Docker builds, GCR/GAR pushes, and Helm deployments.
### Developer Experience (2)

#### Legacy Scaffolding

  - **(2022)** [blog.baeke.info: Trying out Draft 2 on AKS](https://baeke.info/2022/06/02/trying-out-draft-2-on-aks) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early evaluation testing out the Draft v2 workflow within AKS environments. Evaluates standard dev loops and notes architectural changes between initial Draft implementations and subsequent buildpack-driven tools. Modern architects should target standard buildpacks and OCI artifacts over older Draft versions.
## Research

### Architecture Analysis

#### Infrastructure Design (1)

  - **(2024)** [learnk8s.io: Kubernetes Research. Research documents on node instance types, managed services, ingress controllers, CNIs, etc.](https://learnkube.com/research) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An exceptional, data-driven research catalog evaluating critical Kubernetes deployment components. Compiles comparative benchmarks and analyses of CNI plugins (Cilium, Calico), cloud providers (EKS, GKE, AKS), virtual machine shapes, and Ingress Controller solutions, highlighting costs and latencies.
## Resilience

### Chaos Engineering

#### Cloud Architecture

  - **(2021)** [Chaos engineering on Amazon EKS using AWS Fault Injection Simulator](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical walkthrough demonstrating how to orchestrate chaos experiments on Amazon EKS using AWS Fault Injection Simulator (FIS). Highlights configuring managed cluster actions to trigger node terminations, API failures, and container termination within isolated namespaces.
## Security and Governance

### Access and Identity

#### Azure Key Vault

  - **(2022)** [dev.to: Access Secrets in AKV using Managed identities for AKS 🌟](https://dev.to/vivekanandrapaka/access-secrets-from-akv-using-managed-identities-for-aks-91p) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Shows how to retrieve and access secrets securely within AKS workloads using Managed Identities and Azure Key Vault CSI Provider. Avoids persisting plaintext credentials in cluster definitions, mounting secrets as secure volumes instead.
#### OAuth2 Proxy

  - **(2022)** [kristhecodingunicorn.com: Setting Up OAuth 2.0 Authentication for Applications in AKS With NGINX and OAuth2 Proxy](https://www.kristhecodingunicorn.com/post/aks-oauth2-proxy-with-nginx-ingress-controller) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides detailed YAML deployment specs for running OAuth2 Proxy alongside NGINX on AKS. Demonstrates configuring ingress annotations and token validation loops, creating a robust baseline for securing production routes.
### Microservices Security

#### Pod Security and Identities

  - **(2020)** [medium: Secure your Microservices on AKS — Part 1 🌟](https://itnext.io/running-your-microservices-securely-on-aks-417a110b2e76) <span class='md-tag md-tag--warning'>[TERRAFORM/YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth security architecture guide covering secure microservices deployment on AKS. Leverages Azure Active Directory (AAD) Pod Identity (and modern Workload Identity shifts) along with network security policies. Details methods to restrict pod-to-pod communications, configure secret vaults, and enforce security baselines at the runtime layer.

---
💡 **Explore Related:** [AWS](./aws.md) | [Azure](./azure.md) | [Edge Computing](./edge-computing.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

