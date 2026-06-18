# On-Premise Production Kubernetes Cluster Installers

!!! info "Architectural Context"
    Detailed reference for On-Premise Production Kubernetes Cluster Installers in the context of The Container Stack.

## Table of Contents

1. [Application Delivery](#application-delivery)
  - [Developer Platforms](#developer-platforms)
    - [VMware Tanzu](#vmware-tanzu)
1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Databases](#databases)
  - [Kubernetes Operators](#kubernetes-operators)
    - [VMware Tanzu](#vmware-tanzu-1)
1. [Delivery](#delivery)
  - [Air-Gapped Deployments](#air-gapped-deployments)
    - [Zero Trust](#zero-trust)
1. [Education](#education)
  - [Kubernetes](#kubernetes)
    - [Training](#training)
1. [Infrastructure](#infrastructure)
  - [AI and GPU Computing](#ai-and-gpu-computing)
    - [VMware Tanzu](#vmware-tanzu-2)
  - [Bare Metal](#bare-metal)
    - [Cluster API](#cluster-api)
  - [Cluster Management](#cluster-management)
    - [Cluster API](#cluster-api-1)
    - [Cluster API Providers](#cluster-api-providers)
    - [GitOps](#gitops)
  - [Cluster Provisioning](#cluster-provisioning)
    - [Bare Metal](#bare-metal-1)
    - [Legacy Tooling](#legacy-tooling)
  - [Container Runtimes](#container-runtimes)
    - [Sandboxing](#sandboxing)
  - [Kubernetes Distributions](#kubernetes-distributions)
    - [Custom Installers](#custom-installers)
    - [Edge and IoT](#edge-and-iot)
    - [Market Landscapes](#market-landscapes)
    - [Selection Criteria](#selection-criteria)
  - [Training and Enablement](#training-and-enablement)
    - [Educational Content](#educational-content)
    - [Interactive Labs](#interactive-labs)
  - [Virtualization](#virtualization)
    - [VMware Tanzu](#vmware-tanzu-3)
1. [Kubernetes](#kubernetes-1)
  - [Operations](#operations)
    - [Productivity](#productivity)
1. [Kubernetes Platforms](#kubernetes-platforms)
  - [Mirantis](#mirantis)
    - [Enterprise](#enterprise)
  - [Rancher](#rancher)
    - [Multi-Cluster](#multi-cluster)
  - [Red Hat OpenShift](#red-hat-openshift)
    - [Enterprise](#enterprise-1)
1. [Networking](#networking)
  - [CNI Plugins](#cni-plugins)
    - [Overlay Networks](#overlay-networks)
  - [Service Mesh](#service-mesh)
    - [VMware Tanzu](#vmware-tanzu-4)
1. [Observability](#observability)
  - [Dashboards](#dashboards)
    - [Developer Tooling](#developer-tooling)
1. [Provisioning](#provisioning)
  - [Ansible](#ansible)
    - [Advanced Infrastructure](#advanced-infrastructure)
    - [Development Environments](#development-environments)
    - [Enterprise Playbooks](#enterprise-playbooks)
    - [Guides](#guides)
    - [Media](#media)
    - [Roles](#roles)
    - [Virtualization](#virtualization-1)
  - [Bare Metal](#bare-metal-2)
    - [Comparison](#comparison)
    - [Scale Stories](#scale-stories)
    - [Strategy](#strategy)
  - [Bootstrapping](#bootstrapping)
    - [AWS](#aws)
    - [Azure](#azure)
    - [Container Runtimes](#container-runtimes-1)
    - [Core Engine](#core-engine)
    - [Guides](#guides-1)
    - [Learning](#learning)
    - [Ubuntu](#ubuntu)
    - [VirtualBox](#virtualbox)
  - [Declarative Infrastructure](#declarative-infrastructure)
    - [Articles](#articles)
    - [Core Engine](#core-engine-1)
  - [Deployment Tools](#deployment-tools)
    - [AWS](#aws-1)
    - [Comparison](#comparison-1)
    - [Security](#security)
  - [GitOps](#gitops-1)
    - [Legacy Tools](#legacy-tools)
  - [Infrastructure-as-Code](#infrastructure-as-code)
    - [Exoscale](#exoscale)
1. [Security](#security-1)
  - [Compliance](#compliance)
    - [Vulnerability Management](#vulnerability-management)
1. [Storage](#storage)
  - [Stateful Applications](#stateful-applications)
    - [Legacy Tooling](#legacy-tooling-1)

## Application Delivery

### Developer Platforms

#### VMware Tanzu

  - **(2022)** [zdnet.com: VMware brings Tanzu Application Platform into GA to ease Kubernetes adoption](https://www.zdnet.com/article/vmware-brings-tanzu-application-platform-into-ga-to-ease-kubernetes-adoption) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — News of VMware's general availability announcement of Tanzu Application Platform (TAP). TAP serves as an enterprise-grade PaaS (Platform-as-a-Service) overlay on Kubernetes, packaging cloud-native buildpacks, API portals, Cartographer supply chains, and security scanning tools to deliver a streamlined developer experience.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [wecloudpro.com: Deploy HA kubernetes cluster in AWS in less than 5 minutes](https://wecloudpro.com/2020/01/13/kube-autp-aws.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering wecloudpro.com in the Kubernetes Tools ecosystem.
  - [blog.kubecost.com: Kubernetes kOps: Step-By-Step Example & Alternatives](https://blog.kubecost.com/blog/kubernetes-kops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.kubecost.com: Kubernetes kOps: Step-By-Step Example & Alternatives in the Kubernetes Tools ecosystem.
  - [imsundeep8.medium.com: Deploy Production-grade Kubernetes Cluster using' kOps on Amazon Cloud (AWS)](https://imsundeep8.medium.com/deploy-production-grade-kubernetes-cluster-using-kops-on-amazon-cloud-aws-abc79f46aa32)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering imsundeep8.medium.com: Deploy Production-grade Kubernetes Cluster using' kOps on Amazon Cloud (AWS) in the Kubernetes Tools ecosystem.
  - [medium.com: **Demystifying High Availability in Kubernetes Using Kubeadm**](https://medium.com/velotio-perspectives/demystifying-high-availability-in-kubernetes-using-kubeadm-3d83ed8c458b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: **Demystifying High Availability in Kubernetes Using Kubeadm** in the Kubernetes Tools ecosystem.
  - [blog.tobias-huebner.org: Low-budget self-hosted Kubernetes 🌟](https://blog.tobias-huebner.org/low-budget-kubernetes-self-hosted-series)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.tobias-huebner.org: Low-budget self-hosted Kubernetes 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@ZiXianZeroX: Setting Up an On-premise Kubernetes Cluster from' Scratch](https://medium.com/@ZiXianZeroX/setting-up-an-on-premise-kubernetes-cluster-from-scratch-8e3a6b415387)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ZiXianZeroX: Setting Up an On-premise Kubernetes Cluster from' Scratch in the Kubernetes Tools ecosystem.
  - [faun.pub: Configuring HA Kubernetes cluster on bare metal servers with kubeadm.' 1/3](https://faun.pub/configuring-ha-kubernetes-cluster-on-bare-metal-servers-with-kubeadm-1-2-1e79f0f7857b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Configuring HA Kubernetes cluster on bare metal servers with kubeadm.' 1/3 in the Kubernetes Tools ecosystem.
  - [blog.learncodeonline.in: Kubernetes Cluster Deployment on CentOS Linux](https://blog.learncodeonline.in/kubernetes-cluster-deployment-on-centos-linux)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.learncodeonline.in: Kubernetes Cluster Deployment on CentOS Linux in the Kubernetes Tools ecosystem.
  - [medium.com/@benjaminacar.private: A Comprehensive Guide to Setup a New K8s' Cluster](https://medium.com/@benjaminacar.private/a-comprehensive-guide-to-setup-a-new-k8s-cluster-4b88e6f021bc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@benjaminacar.private: A Comprehensive Guide to Setup a New K8s' Cluster in the Kubernetes Tools ecosystem.
  - [itwonderlab.com: Kubernetes Cluster using Vagrant and Ansible with Containerd' (in 3 minutes) 🌟](https://www.itwonderlab.com/en/ansible-kubernetes-vagrant-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering itwonderlab.com: Kubernetes Cluster using Vagrant and Ansible with Containerd' (in 3 minutes) 🌟 in the Kubernetes Tools ecosystem.
  - [napo.io: Kubernetes The (real) Hard Way on AWS](https://napo.io/posts/kubernetes-the-real-hard-way-on-aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering napo.io: Kubernetes The (real) Hard Way on AWS in the Kubernetes Tools ecosystem.
  - [napo.io: Terraform Kubernetes Multi-Cloud (ACK, AKS, DOK, EKS, GKE, OKE)](https://napo.io/posts/terraform-kubernetes-multi-cloud-ack-aks-dok-eks-gke-oke)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering napo.io: Terraform Kubernetes Multi-Cloud (ACK, AKS, DOK, EKS, GKE, OKE) in the Kubernetes Tools ecosystem.
  - [medium: Upgrading Kubernetes The Hard Way](https://medium.com/nordcloud-engineering/upgrading-kubernetes-the-hard-way-ac533cfb4ff2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Upgrading Kubernetes The Hard Way in the Kubernetes Tools ecosystem.
  - [medium: Kubernetes the hard way on Docker](https://medium.com/@brightzheng100/kubernetes-the-hard-way-on-docker-f512bae734af)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Kubernetes the hard way on Docker in the Kubernetes Tools ecosystem.
  - [medium.com/@norlin.t: Kubernetes the hard (illumos) way](https://medium.com/@norlin.t/kubernetes-the-hard-illumos-way-c4b45a080bac)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@norlin.t: Kubernetes the hard (illumos) way in the Kubernetes Tools ecosystem.
  - [medium.com/@norlin.t: Kubernetes the hard (illumos) way, last part](https://medium.com/@norlin.t/kubernetes-the-hard-illumos-way-last-part-c68ca71bc2ce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@norlin.t: Kubernetes the hard (illumos) way, last part in the Kubernetes Tools ecosystem.
  - [medium: ClusterOps: 1-Line Commit to Upgrade Your Kubernetes Clusters 🌟](https://medium.com/swlh/clusterops-1-line-commit-to-upgrade-your-kubernetes-clusters-de3548124d04)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: ClusterOps: 1-Line Commit to Upgrade Your Kubernetes Clusters 🌟 in the Kubernetes Tools ecosystem.
  - [cncf.io webinar: Deploying Kubernetes to bare metal using cluster API](https://www.cncf.io/webinars/deploying-kubernetes-to-bare-metal-using-cluster-api)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io webinar: Deploying Kubernetes to bare metal using cluster API in the Kubernetes Tools ecosystem.
  - [cncf.io: Kubernetes Cluster API reaches production readiness with version' 1.0](https://www.cncf.io/blog/2021/10/06/kubernetes-cluster-api-reaches-production-readiness-with-version-1-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io: Kubernetes Cluster API reaches production readiness with version' 1.0 in the Kubernetes Tools ecosystem.
  - [cloudsavvyit.com: How to run your own kubernetes cluster with Microk8s](https://www.cloudsavvyit.com/13024/how-to-run-your-own-kubernetes-cluster-with-microk8s)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cloudsavvyit.com: How to run your own kubernetes cluster with Microk8s in the Kubernetes Tools ecosystem.
  - [kubedex.com: Kubernetes Operating Systems 🌟](https://kubedex.com/kubernetes-operating-systems)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kubedex.com: Kubernetes Operating Systems 🌟 in the Kubernetes Tools ecosystem.
  - [baeldung.com: Lightweight Kubernetes Distributions](https://www.baeldung.com/ops/kubernetes-lightweight-distributions)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering baeldung.com: Lightweight Kubernetes Distributions in the Kubernetes Tools ecosystem.
  - [**VMware Kubernetes Tanzu**](https://cloud.vmware.com/tanzu)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering **VMware Kubernetes Tanzu** in the Kubernetes Tools ecosystem.
  - [wecloudpro.com: VMware Tanzu Community Edition 🌟](https://www.wecloudpro.com/2021/11/13/Tanzu-Community-Edition.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering wecloudpro.com: VMware Tanzu Community Edition 🌟 in the Kubernetes Tools ecosystem.
  - [Pharos 🌟](https://k8spharos.dev)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Pharos 🌟 in the Kubernetes Tools ecosystem.
  - [medium: K0s Supports Kubernetes 1.22](https://medium.com/k0sproject/k0s-supports-kubernetes-1-22-a498e41bf5af)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: K0s Supports Kubernetes 1.22 in the Kubernetes Tools ecosystem.
  - [medium: k0s Ready for Production](https://medium.com/k0sproject/k0s-ready-for-production-20255c4b0791)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: k0s Ready for Production in the Kubernetes Tools ecosystem.
  - [medium: k0s Optimizes Start Time, Adds Cluster Level Backup/Restore and' More](https://medium.com/k0sproject/k0s-optimizes-start-time-adds-cluster-level-backup-restore-and-more-8ffef894a1ae)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: k0s Optimizes Start Time, Adds Cluster Level Backup/Restore and' More in the Kubernetes Tools ecosystem.
## Databases

### Kubernetes Operators

#### VMware Tanzu (1)

  - **(2020)** [tanzu.vmware.com: VMware Tanzu SQL: MySQL at Scale Made Easy for Kubernetes](https://blogs.vmware.com/tanzu/vmware-tanzu-sql-mysql-at-scale-kubernetes) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Tanzu SQL provides a robust, operator-driven solution for provisioning and operating MySQL databases within Kubernetes clusters. It automates common lifecycle events such as data replication, high availability clustering, automatic backups, and critical security patching.
## Delivery

### Air-Gapped Deployments

#### Zero Trust

  - **(2026)** [==defenseunicorns/zarf==](https://github.com/zarf-dev/zarf) <span class='md-tag md-tag--info'>⭐ 1925</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7f272ef8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 2 L 30 12 L 40 4 L 50 3" fill="none" stroke="url(#spark-grad-7f272ef8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A highly resilient developer tool designed by Defense Unicorns to package, deploy, and manage Kubernetes clusters and cloud-native applications in strictly air-gapped, offline, or secure zero-trust environments. Zarf bundles container registries, Helm charts, binary dependencies, and configurations into a single cryptographically signed archive file, completely removing internet reliance.
## Education

### Kubernetes

#### Training

  - **(2020)** [tanzu.vmware.com: Introducing KubeAcademy Pro: In-Depth Kubernetes Training, Totally Free](https://blogs.vmware.com/tanzu/introducing-kubeacademy-pro-in-depth-kubernetes-training-totally-free)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — KubeAcademy by VMware provides modular education resources and deep-dive technical courses targeting Kubernetes administrators and application developers. It focuses on practical application scaling, cluster security, debugging, and continuous integration concepts.
## Infrastructure

### AI and GPU Computing

#### VMware Tanzu (2)

  - **(2022)** [dev.to/saintdle: Deploying Nvidia GPU enabled Tanzu Kubernetes Clusters](https://dev.to/saintdle/deploying-nvidia-gpu-enabled-tanzu-kubernetes-clusters-40ma) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed engineering walkthrough detailing the enablement of Nvidia GPU acceleration within guest Tanzu Kubernetes Grid (TKG) clusters on vSphere. Covers vGPU profiles, driver configuration, and assigning hardware-accelerated nodes to support AI/ML and deep learning workloads.
### Bare Metal

#### Cluster API

  - **(2021)** [thenewstack.io: Provision Bare-Metal Kubernetes with the Cluster API](https://thenewstack.io/provision-bare-metal-kubernetes-with-the-cluster-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into utilizing Cluster API for declarative provisioning on physical hardware. The guide details how Cluster API Provider BYOH (Bring Your Own Host) and Metal3 bridge the gap between bare-metal lifecycle management and cloud-like declarative workflows, orchestrating native bare-metal nodes through Kubernetes CRDs.
### Cluster Management

#### Cluster API (1)

  - **(2021)** [==github.com: Cluster API Helm Chart==](https://github.com/kgamanji/cluster-api-helm-chart) <span class='md-tag md-tag--info'>⭐ 58</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b6a3faaa" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 7 L 20 10 L 30 10 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-b6a3faaa)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community-driven Helm chart designed to package and deploy Cluster API (CAPI) resources and operators inside a management cluster. While it simplified CAPI components deployment via traditional Helm CI/CD pipelines, current production standards in 2026 have shifted entirely to official declarative setups via clusterctl or native GitOps operators, rendering this chart obsolete.
  - **(2021)** [thenewstack.io: Cluster API Offers a Way to Manage Multiple Kubernetes Deployments](https://thenewstack.io/cluster-api-offers-a-way-to-manage-multiple-kubernetes-deployments)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory technical overview of the Kubernetes Cluster API (CAPI) subproject. The article clarifies how CAPI leverages the Kubernetes operator pattern to deliver declarative, API-driven cluster creation, configuration, and management across heterogeneous cloud providers, establishing a unified control plane for multi-cluster operations.
#### Cluster API Providers

  - **(2023)** [==weaveworks/cluster-api-provider-existinginfra==](https://github.com/weaveworks/cluster-api-provider-existinginfra) <span class='md-tag md-tag--info'>⭐ 45</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-14160f2c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 7 L 20 6 L 30 12 L 40 6 L 50 12" fill="none" stroke="url(#spark-grad-14160f2c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Formerly known as CAPE, this Cluster API provider enabled declarative cluster bootstrap over pre-existing SSH-accessible infrastructure (bare-metal or legacy virtual machines). Following the shutdown of Weaveworks in 2024, the project was officially archived, yet it continues to serve as an engineering reference for building custom SSH-driven infrastructure control loops.
#### GitOps

  - **(2021)** [weave.works: Manage Thousands of Clusters with GitOps and the Cluster API](https://www.weave.works/blog/manage-thousands-of-clusters-with-gitops-and-the-cluster-api) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural guide exploring the intersection of Cluster API (CAPI) and GitOps (specifically Flux) to manage fleet-scale Kubernetes deployments. It outlines the declaration of tenant clusters as custom resources (CRDs) in a management cluster, enabling automated multi-cluster life cycle control. Following Weaveworks' exit in 2024, this approach remains standard, but is now realized using CNCF Flux and native CAPI providers.
  - **(2021)** [piotrminkowski.com: Create and Manage Kubernetes Clusters with Cluster API and ArgoCD](https://piotrminkowski.com/2021/12/03/create-kubernetes-clusters-with-cluster-api-and-argocd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive technical guide showcasing the integration of Cluster API and ArgoCD to manage the infrastructure lifecycle through a GitOps model. The author demonstrates declarative target cluster definitions stored in Git, allowing ArgoCD to reconcile and trigger Cluster API operators on a management cluster for automated target cluster deployments.
### Cluster Provisioning

#### Bare Metal (1)

  - **(2026)** [==poseidon/typhoon==](https://github.com/poseidon/typhoon) <span class='md-tag md-tag--info'>⭐ 2044</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3a94433d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 11 L 20 7 L 30 11 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-3a94433d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Typhoon is a minimalist, secure, and performant bare-metal and multi-cloud Kubernetes distribution built entirely with Terraform. It bootstraps standard, upstream CNCF-compliant Kubernetes onto Flatcar Container Linux (and historically CoreOS), providing an excellent reference model for git-driven infrastructure without vendor lock-in.
#### Legacy Tooling

  - **(2021)** [==**k8s-tew**==](https://github.com/darxkies/k8s-tew) <span class='md-tag md-tag--info'>⭐ 311</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-79ea7d28" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 6 L 20 13 L 30 8 L 40 12 L 50 2" fill="none" stroke="url(#spark-grad-79ea7d28)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — "Kubernetes The Easy Way" (k8s-tew) was a shell wrapper and declarative configuration tool designed to bypass the complex manual configuration steps associated with bootstrapping clusters via kubeadm. With the mature advancement of declarative Cluster API patterns and standard distribution installers, this repository is now obsolete and serves only historical reference value.
### Container Runtimes

#### Sandboxing

  - **(2021)** [==Kata Containers on MicroK8s==](https://github.com/didier-durand/microk8s-kata-containers) <span class='md-tag md-tag--info'>⭐ 34</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ab473c19" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 12 L 20 6 L 30 12 L 40 11 L 50 2" fill="none" stroke="url(#spark-grad-ab473c19)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community repository providing integration instructions and configurations to run Kata Containers within a Canonical MicroK8s environment. This architecture allows security teams to deploy hardware-isolated, hypervisor-sandboxed container runtimes (using QEMU or Cloud Hypervisor) inside lightweight local clusters, resolving tenant isolation concerns in multi-tenant environments.
### Kubernetes Distributions

#### Custom Installers

  - **(2026)** [kurl.sh](https://kurl.sh) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An open-source online utility and framework designed to construct custom, production-ready, air-gapped Kubernetes distribution installers. Replicated/kurl aggregates chosen components (like CNIs, storage, and registries) into a single bash-driven installer script to facilitate simple downstream application deliveries.
#### Edge and IoT

  - **(2026)** [==K0s - Zero Friction Kubernetes==](https://github.com/k0sproject/k0s) <span class='md-tag md-tag--info'>⭐ 6239</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e23c48a1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 5 L 20 12 L 30 2 L 40 9 L 50 4" fill="none" stroke="url(#spark-grad-e23c48a1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official open-source repository for the k0s Kubernetes distribution. Features active enterprise-grade developer tracks, offering built-in advanced networking plugins (Calico CNI, Kube-router), support for virtualized control planes, and automated bootstrapping tools without external dependencies.
  - **(2023)** [==xiaods/k8e==](https://github.com/xiaods/k8e) <span class='md-tag md-tag--info'>⭐ 449</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-93a7dc4f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 5 L 20 9 L 30 10 L 40 13 L 50 2" fill="none" stroke="url(#spark-grad-93a7dc4f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A lightweight Kubernetes distribution (k8e, standing for "k8s easy") modeled after K3s but strictly adhering to standard upstream components. It is tailored for low-resource edge architectures, CI environments, and hobbyist networks requiring low memory profiles and simple setups.
  - **(2026)** [**Microk8s**](https://canonical.com/microk8s) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Canonical's lightweight, zero-ops Kubernetes distribution designed for developers, IoT devices, and edge computing. MicroK8s is packaged as a single snap package with automatic updates, high-availability clustering, and a modular architecture that supports one-click deployment of common add-ons like Istio, Knative, and GPU acceleration.
  - **(2026)** [k0s](https://k0sproject.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Mirantis' zero-friction, single-binary Kubernetes distribution. Designed to operate across any cloud, hybrid, or edge infrastructure, k0s packages all control plane and node dependencies in a single executable, drastically simplifying lifecycle maintenance, upgrading, and operational footprint.
  - **(2020)** [thenewstack.io: Deploy Microk8s and the Kubernetes Dashboard for K8s Development](https://thenewstack.io/deploy-microk8s-and-the-kubernetes-dashboard-for-k8s-development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical tutorial covering the setup of Canonical's MicroK8s on local environments coupled with the enablement of the official Kubernetes Web UI (Dashboard). The guide details how MicroK8s' single-command add-on framework simplifies cluster observability and bootstrapping for developers.
  - **(2020)** [thenewstack.io: Deploy a Kubernetes Cluster on Ubuntu Server with Microk8s](https://thenewstack.io/deploy-a-kubernetes-cluster-on-ubuntu-server-with-microk8s)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step guide outlining how to install, configure, and scale MicroK8s on an Ubuntu Server environment. It demonstrates the simplicity of setting up multi-node local clusters with high availability (dqlite-backed control planes) using snap commands.
  - **(2020)** [infoq.com: Mirantis Announces k0s, a New Kubernetes Distribution](https://www.infoq.com/news/2020/12/k0s-kubernetes-distribution)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A retrospective announcement of Mirantis' launch of k0s. Highlighted its zero-friction approach, multi-master architectural patterns with a decentralized control plane, and its capability to run isolated control planes separate from application workload nodes.
#### Market Landscapes

  - **(2022)** [infoworld.com: 6 Kubernetes distributions leading the container revolution](https://www.infoworld.com/article/2266054/6-kubernetes-distributions-leading-the-container-revolution.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comparative market overview focusing on major commercial Kubernetes platforms driving enterprise cloud-native architecture. Evaluates core features of Red Hat OpenShift, VMware Tanzu Grid, Rancher Kubernetes Engine (RKE), Mirantis Kubernetes Engine, Docker Enterprise, and Canonical Kubernetes, contrasting their operational models and target markets.
#### Selection Criteria

  - **(2021)** [acloudguru.com: Which Kubernetes distribution is right for you?](https://www.pluralsight.com/resources/blog/cloud/which-kubernetes-distribution-is-right-for-you)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical guide comparing various Kubernetes distributions (including EKS, GKE, AKS, OpenShift, Rancher, and lightweight distributions like K3s) based on business needs, deployment environments, operational overhead, and budget. It guides enterprise architects in matching target environments with appropriate vendor or vanilla offerings.
### Training and Enablement

#### Educational Content

  - **(2024)** [kube.academy/pro 🌟](https://kube.academy/pro)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A premier education and certification program developed by VMware Tanzu focusing on core Kubernetes principles, multi-cluster management, networking, and security. Curated for intermediate and advanced engineers, offering deep technical tracks and real-world architectures.
#### Interactive Labs

  - **(2026)** [VMware hands-on Labs 🌟](https://labs.hol.vmware.com/HOL)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly rated, free cloud-based interactive training platform provided by Broadcom/VMware. It allows platform engineers and administrators to gain hands-on operational experience with VMware Tanzu, vSphere with Kubernetes, NSX-T, and modern multicloud management tools without needing local hardware.
### Virtualization

#### VMware Tanzu (3)

  - **(2020)** [**VMware vSphere 7 with Kubernetes** - Project Pacific](https://www.vmware.com/products/cloud-infrastructure/vsphere) <span class='md-tag md-tag--warning'>[PROPRIETARY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A transformative enterprise initiative (Project Pacific) that embedded native Kubernetes capabilities directly into the ESXi hypervisor. vSphere with Tanzu enables virtualization administrators to manage VMs and native Tanzu Kubernetes Grid (TKG) guest clusters inside a single vSphere Client interface, converging IT operations.
  - **(2020)** [cormachogan.com: A first look at vSphere with Kubernetes in action](https://cormachogan.com/2020/04/01/a-first-look-at-vsphere-with-kubernetes-in-action)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on architectural exploration of the early vSphere with Kubernetes implementation. The post walks through supervisor cluster enablement, native vSphere Pods execution, storage class integration with VMware CNS (Cloud Native Storage), and basic network policies.
  - **(2020)** [cormachogan.com: Building a TKG Cluster in vSphere with Kubernetes](https://cormachogan.com/2020/04/07/building-a-tkg-guest-cluster-in-vsphere-with-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep technical guide demonstrating how to declare and bootstrap Tanzu Kubernetes Grid (TKG) workload clusters (guest clusters) inside a vSphere supervisor cluster. Explains the underlying declarative custom resource definition (CRD) configurations matching Cluster API mechanics.
## Kubernetes (1)

### Operations

#### Productivity

  - **(2021)** [Kubernetes productivity tips and tricks 🌟](https://www.theodo.com/en-fr/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practitioner's guide to enhancing CLI-based Kubernetes productivity. It explores advanced setups such as custom shell autocompletion, kubectx/kubens utilities, smart aliases, and log-tailing helpers designed to reduce cognitive overhead during real-time incident responses.
## Kubernetes Platforms

### Mirantis

#### Enterprise

  - **(2020)** [Mirantis Docker Enterprise 3.1+ with Kubernetes](https://www.mirantis.com/software/mirantis-kubernetes-engine) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Formerly Docker Enterprise, Mirantis Kubernetes Engine (MKE) provides enterprise-ready cluster deployment capabilities utilizing either Kubernetes or Swarm orchestrators. It features integrated identity management, safe private image registries, and granular role-based security tooling.
### Rancher

#### Multi-Cluster

  - **(2026)** [Rancher: Enterprise management for Kubernetes](https://nubenetes.com/rancher) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Rancher is a unified platform for managing multi-cluster, heterogeneous Kubernetes deployments across diverse cloud providers and bare metal hosts. It simplifies operational management by providing centralized authentication, unified RBAC access, structured audit logs, and simplified Helm catalog deployments.
### Red Hat OpenShift

#### Enterprise (1)

  - **(2026)** [Openshift Container Platform](https://nubenetes.com/openshift) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat OpenShift is a premier enterprise-grade hybrid cloud Kubernetes application platform. It adds out-of-the-box developer tooling, integrated security standards, cluster virtualization, internal registry configurations, and Operator-based life cycle management directly over raw Kubernetes.
## Networking

### CNI Plugins

#### Overlay Networks

  - **(2024)** [==github: Weave Net - Weaving Containers into Applications==](https://github.com/weaveworks/weave) <span class='md-tag md-tag--info'>⭐ 6612</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d5161111" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 12 L 30 7 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-d5161111)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Weave Net is a widely adopted container CNI plugin that creates an autonomous peer-to-peer overlay network with no external database requirements. The repository was archived by Weaveworks in 2024, prompting enterprise engineering teams to migrate to active, high-performance CNIs like Cilium (eBPF-driven) or Calico.
### Service Mesh

#### VMware Tanzu (4)

  - **(2020)** [blogs.vmware.com: VMware Tanzu Service Mesh, built on VMware NSX is Now Available!](https://blogs.vmware.com/networkvirtualization/2020/03/vmware-tanzu-service-mesh-built-on-vmware-nsx-is-now-available.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement of VMware Tanzu Service Mesh (TSM), an Istio-based commercial service mesh integrated with VMware NSX. TSM delivers end-to-end traffic management, zero-trust security policies, cross-cluster connectivity, and deep API observability across hybrid and multi-cloud Kubernetes deployments.
## Observability

### Dashboards

#### Developer Tooling

  - **(2023)** [==vmware-tanzu/octant==](https://github.com/vmware-archive/octant) <span class='md-tag md-tag--info'>⭐ 6247</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-748690fb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 2 L 20 2 L 30 13 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-748690fb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Octant was an open-source, extensible developer dashboard designed to visualize local and remote Kubernetes cluster states, resource dependencies, and logs. Project development was officially archived in 2023 as developers shifted to other open-source or commercial alternatives like Lens, OpenLens, and K9s.
## Provisioning

### Ansible

#### Advanced Infrastructure

  - **(2024)** [==krd==](https://github.com/electrocucaracha/krd) <span class='md-tag md-tag--info'>⭐ 40</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-591523b5" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 10 L 20 11 L 30 6 L 40 8 L 50 6" fill="none" stroke="url(#spark-grad-591523b5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL/ANSIBLE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The Kubernetes Reference Deployment (KRD) leverages Ansible playbooks and shell scripts to automate multi-node cluster provisioning with advanced network architectures, hardware acceleration (SR-IOV), nested VM hypervisors, and distributed storage engines.
#### Development Environments

  - **(2024)** [==github.com/bluxmit: Kubespray Workspace==](https://github.com/bluxmit/alnoda-workspaces) <span class='md-tag md-tag--info'>⭐ 1361</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-4121a536" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 4 L 20 5 L 30 6 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-4121a536)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[DOCKER/SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A containerized development sandbox and workspace designed to streamline the execution of Kubespray and Ansible playbooks, ensuring dependency insulation and tool consistency across local machine environments.
#### Enterprise Playbooks

  - **(2026)** [==**Kubespray**==](https://github.com/kubernetes-sigs/kubespray) <span class='md-tag md-tag--info'>⭐ 18556</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6edab0e1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 9 L 20 11 L 30 11 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-6edab0e1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON/ANSIBLE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry standard Ansible automation framework for deploying enterprise-ready, production-grade clusters. Combining Kubeadm with highly flexible, battle-tested playbooks, it handles network policy deployment (CNIs like Calico/Cilium), storage classes, node lifecycle operations, and multi-distribution OS configurations.
#### Guides

  - **(2021)** [adamtheautomator.com/kubespray: Conquer Kubernetes Clusters with Ansible Kubespray](https://adamtheautomator.com/kubespray)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical troubleshooting handbook detailing how to configure Ansible inventories, override default deployment parameters, and run Kubespray deployment playbooks successfully against physical or virtual hosts.
  - **(2020)** [redhat.com: An introduction to Kubespray](https://www.redhat.com/en/blog/kubespray-deploy-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory Red Hat guide summarizing how Kubespray leverages Ansible to abstract system-level provisioning tasks, allowing teams to declare cluster configurations and scaling strategies across mixed on-premises and multi-cloud environments.
#### Media

  - **(2020)** [youtube: OpenShift Commons En Vivo - KubeInit con Maria Bracho, Scott McCarty, and Carlos Camacho (Red Hat, Spanish) 🌟](https://www.youtube.com/watch?v=9_6H7Ahsdm4&ab_channel=OpenShift) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video presentation detailing the internal architecture of KubeInit. Red Hat engineers demonstrate dynamic provisioning of nested virtual environments to accelerate local sandbox deployments of enterprise OpenShift platforms.
#### Roles

  - **(2026)** [==Ansible Role - Kubernetes (Jeff Geerling)==](https://github.com/geerlingguy/ansible-role-kubernetes) <span class='md-tag md-tag--info'>⭐ 626</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ba0c4ff3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 12 L 20 7 L 30 3 L 40 9 L 50 11" fill="none" stroke="url(#spark-grad-ba0c4ff3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Jeff Geerling's highly popular, community-standard Ansible role designed to automate core system dependencies, swap disabling, package installations, and initial Kubeadm commands on Debian and RedHat distributions, simplifying playbooks deployment.
#### Virtualization (1)

  - **(2026)** [==Kubeinit 🌟==](https://github.com/kubeinit/kubeinit) <span class='md-tag md-tag--info'>⭐ 222</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-770e6936" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 3 L 20 4 L 30 9 L 40 4 L 50 9" fill="none" stroke="url(#spark-grad-770e6936)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON/ANSIBLE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight vs Live Grounding: Kubeinit was designed as an Ansible automation tool to deploy Kubernetes, OKD, or OpenShift on VMs using libvirt/KVM. Live telemetry shows this repository has moved to legacy status with zero recent commits, reflecting a shift toward Cluster API providers for virtualization.
### Bare Metal (2)

#### Comparison

  - **(2020)** [thenewstack.io: Kubernetes on Bare Metal vs. VMs: It’s Not Just Performance](https://thenewstack.io/kubernetes-on-bare-metal-vs-vms-its-not-just-performance)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comparative analysis dissecting the operational trade-offs of deploying Kubernetes directly on bare metal versus utilizing virtualized hypervisors. Outlines performance gains, networking simplicity, compute overhead, and isolation profiles that dictate platform selection.
#### Scale Stories

  - **(2020)** [linecorp.com: Building Large Kubernetes Clusters with **Caravan**](https://engineering.linecorp.com/en/blog/building-large-kubernetes-clusters) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An engineering blog post by Line Corporation detailing Caravan, their proprietary bare-metal bare-metal lifecycle orchestration tool. Covers bare-metal host discovery, automated OS deployments, and high-availability operations handling thousands of production nodes.
#### Strategy

  - **(2021)** [containerjournal.com: When Kubernetes-as-a-Service Doesn’t Cut It](https://cloudnativenow.com/features/when-kubernetes-as-a-service-doesnt-cut-it)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the operational and economic conditions where off-the-shelf Kubernetes-as-a-Service platforms fall short. Highlights constraints around custom hardware drivers, performance requirements, data sovereignty, and custom routing options that force organizations toward self-managed bare-metal solutions.
  - **(2020)** [containerjournal.com: Deploying Kubernetes on Bare Metal](https://cloudnativenow.com/features/deploying-kubernetes-on-bare-metal)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architecture-level examination of building out Kubernetes clusters directly on raw physical hardware. Explores the complexities of dynamic volume provisioning, API load balancing, manual host bootstrapping, and CNI integration compared to cloud environments.
### Bootstrapping

#### AWS

  - **(2022)** [==Kubernetes The Hard Way: AWS Edition==](https://github.com/prabhatsharma/kubernetes-the-hard-way-aws) <span class='md-tag md-tag--info'>⭐ 668</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6a9e6015" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 9 L 20 4 L 30 12 L 40 11 L 50 3" fill="none" stroke="url(#spark-grad-6a9e6015)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An educational repository porting 'Kubernetes the Hard Way' directly onto AWS infrastructure. Step-by-step documentation on manually creating VPCs, Security Groups, EC2 nodes, and manually compiling and executing cluster daemons.
#### Azure

  - **(2021)** [Kubernetes the Hard Way: Azure Edition](https://github.com/carlosonunez/kubernetes-the-hard-way-on-azure) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A localized adaptation of 'Kubernetes the Hard Way' targeting Azure cloud services. Focuses on manual creation of Virtual Networks (VNets), Network Security Groups (NSGs), Azure load balancers, and systemd service profiles to build a transparent control plane.
#### Container Runtimes (1)

  - **(2021)** [thenewstack.io: How to Deploy Kubernetes with Kubeadm and containerd](https://thenewstack.io/how-to-deploy-kubernetes-with-kubeadm-and-containerd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical deployment guide focusing on initializing Kubeadm-driven clusters using containerd as the underlying Container Runtime Interface (CRI) instead of Docker. Explains config setup, namespace settings, and systemd integration.
#### Core Engine

  - **(2026)** [==Kubernetes Cluster with **Kubeadm**==](https://github.com/kubernetes/kubeadm) <span class='md-tag md-tag--info'>⭐ 3981</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-119e1510" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 10 L 20 10 L 30 5 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-119e1510)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The standard bootstrapping engine for establishing conformant clusters, maintained by Kubernetes SIG-Cluster-Lifecycle. It abstracts certificate generation, etcd cluster building, and node onboarding into simplified `kubeadm init` and `kubeadm join` commands. It serves as the foundation for higher-level platform controllers.
#### Guides (1)

  - **(2021)** [mirantis.com: How to install Kubernetes with Kubeadm: A quick and dirty guide](https://www.mirantis.com/blog/how-install-kubernetes-kubeadm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Mirantis' architectural guide to installing Kubernetes utilizing Kubeadm. Outlines exact host configurations, networking kernel parameter modifications, and container runtime configs needed to establish a conformant control plane.
  - **(2018)** [Setting Up a Kubernetes Cluster on Ubuntu 18.04](https://loves.cloud/setting-up-a-kubernetes-cluster-on-ubuntu-18-04)  <span class='md-tag md-tag--info'>[LEGACY]</span> — An early tutorial detailing step-by-step master and worker initialization on legacy Ubuntu 18.04 using Kubeadm. Explains system preparation, Docker daemon runtime configuration, and initial CNI deployment steps.
#### Learning

  - **(2026)** [==**Kelsey Hightower: kubernetes the hard way**==](https://github.com/kelseyhightower/kubernetes-the-hard-way) <span class='md-tag md-tag--info'>⭐ 48654</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-94421552" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 4 L 20 7 L 30 6 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-94421552)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN/SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kelsey Hightower's legendary guide for bootstrapping highly available clusters manually without automated installers. It details SSL/TLS certificate generation, etcd cluster builds, and control plane daemon setup (kube-apiserver, kube-scheduler, etc.), representing the gold standard for understanding low-level Kubernetes engineering.
#### Ubuntu

  - **(2021)** [blog.radwell.codes: Provisioning Single-node Kubernetes Cluster using kubeadm on Ubuntu 20.04](https://blog.radwell.codes/2021/05/provisioning-single-node-kubernetes-cluster-using-kubeadm-on-ubuntu-20-04)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step workflow focused on configuring a single-node Kubernetes cluster on Ubuntu 20.04 using Kubeadm. Outlines how to untaint the control plane node to enable single-node scheduling for development and resource-constrained test beds.
#### VirtualBox

  - **(2020)** [kosyfrances.com: Using kubeadm to create a Kubernetes 1.20 cluster on VirtualBox with Ubuntu](https://kosyfrances.com/kubernetes-cluster)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step local sandboxing guide describing how to set up a multi-node Kubernetes 1.20 cluster on VirtualBox using Ubuntu and Kubeadm. Valuable for local learning, CNI testing, and running sandboxed environments.
### Declarative Infrastructure

#### Articles

  - **(2020)** [itnext.io: Multi-Cloud and Multi-Cluster Declarative Kubernetes Cluster Creation and Management with Cluster API (CAPI — v1alpha3)](https://itnext.io/multi-cloud-and-multi-cluster-declarative-kubernetes-cluster-creation-and-management-with-cluster-6df8efdc2a89) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — A deep-dive technical article illustrating the design patterns behind Cluster API (CAPI v1alpha3) for multi-cloud and bare-metal cluster deployments. It details how CAPI separates infrastructure provisioning from cluster bootstrapping via clean Custom Resource Definitions.
#### Core Engine (1)

  - **(2026)** [ClusterAPI](https://cluster-api.sigs.k8s.io) <span class='md-tag md-tag--warning'>[GO/MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The home page of Cluster API (CAPI), a Kubernetes SIG project that implements declarative API-driven cluster management. Utilizing custom controllers and CRDs, CAPI treats clusters, machines, and control planes as native Kubernetes resources, enabling unified multi-cloud infrastructure automation.
### Deployment Tools

#### AWS (1)

  - **(2026)** [==GitHub: Kubernetes Cluster with Kops==](https://github.com/kubernetes/kops) <span class='md-tag md-tag--info'>⭐ 16625</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3d0a913e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 7 L 20 8 L 30 10 L 40 12 L 50 4" fill="none" stroke="url(#spark-grad-3d0a913e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kubernetes Operations (kops) is a production-grade orchestration tool designed to configure, scale, and manage highly available clusters on public cloud environments. Its declarative structure manages cloud instances, security groups, route tables, and internal etcd scaling configurations directly, primarily focusing on AWS.
#### Comparison (1)

  - **(2020)** [A Comparative Analysis of Kubernetes Deployment Tools: Kubespray, kops, and conjure-up](https://www.altoros.com/blog/404-page-doesnt-exist)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight vs Live Grounding: Originally a comparative study contrasting Kubespray, Kops, and Conjure-up. Live check reveals the URL now returns a 404 error page. However, the historical significance of the comparison remains as a reference point for early multi-cloud orchestration methods.
#### Security

  - **(2020)** [blog.ivnilv.com: Rotating Kops Etcd Certificates](https://blog.ivnilv.com/posts/rotating-kops-etcd-certificates) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical troubleshooting guide mapping out the precise sequence required to rotate internal etcd client and peer certificates within a running, Kops-managed cluster. Addresses avoidance of control plane downtime and potential etcd split-brain scenarios during CA transitions.
### GitOps (1)

#### Legacy Tools

  - **(2026)** [==Weave Kubernetes System Control - wksctl==](https://github.com/weaveworks/wksctl) <span class='md-tag md-tag--info'>⭐ 389</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-edca5296" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 7 L 20 10 L 30 4 L 40 10 L 50 8" fill="none" stroke="url(#spark-grad-edca5296)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Weaveworks' Weave Kubernetes System Control (wksctl) was a GitOps-based tool for cluster creation, configuring infrastructure directly from a declared state stored in git. Curator Insight vs Live Grounding: Following Weaveworks' operational shutdown, this tool has been archived and is considered historical legacy.
### Infrastructure-as-Code

#### Exoscale

  - **(2020)** [Autoscalable Kubernetes cluster at Exoscale, using Packer and Terraform](https://github.com/PhilippeChepy/exoscale-kubernetes-crio) <span class='md-tag md-tag--info'>⭐ 2</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-cfa54f7d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 7 L 20 13 L 30 13 L 40 9 L 50 9" fill="none" stroke="url(#spark-grad-cfa54f7d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL/PACKER CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An IaC blueprint using Packer and Terraform to deploy an auto-scaling cluster on Exoscale with CRI-O. Curator Insight vs Live Grounding: The repository is now inactive, but serves as a historical example of orchestrating custom cloud pools with native container engines.
## Security (1)

### Compliance

#### Vulnerability Management

  - **(2022)** [==MicroK8s & Kubernetes security benchmark from CIS==](https://github.com/didier-durand/microk8s-kube-bench) <span class='md-tag md-tag--info'>⭐ 17</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-68087c20" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 2 L 20 7 L 30 3 L 40 5 L 50 2" fill="none" stroke="url(#spark-grad-68087c20)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source tool adapted from Aqua Security's kube-bench designed to validate Canonical MicroK8s clusters against the Center for Internet Security (CIS) Kubernetes Benchmark. It provides granular compliance auditing of control plane configurations, API security settings, and node compliance profiles directly inside lightweight development or edge clusters.
## Storage

### Stateful Applications

#### Legacy Tooling (1)

  - **(2019)** [Stateful Kubernetes-In-a-Box with Kontena Pharos](https://blog.purestorage.com/stateful-kubernetes-pure-service-orchestrator-kontena-pharos) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical blog post detailing stateful storage solutions in Kubernetes using Pure Service Orchestrator on Kontena Pharos, a lightweight enterprise distribution. With Kontena Pharos discontinued and Pure Storage workflows fully migrated to standard CSI plugins (like Portworx), this remains of historical interest only.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Openshift](./openshift.md) | [Serverless](./serverless.md)

