# Kubernetes Distributions & Installers Matrix Table

!!! info "Architectural Context"
    Detailed reference for Kubernetes Distributions & Installers Matrix Table in the context of Architectural Foundations.

## Standard Reference

  - [Linode Kubernetes Engine (LKE)](https://www.linode.com/products/kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [napo.io: Kubernetes The (real) Hard Way on AWS](https://napo.io/posts/kubernetes-the-real-hard-way-on-aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [**VMware Kubernetes Tanzu**](https://cloud.vmware.com/tanzu)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Pharos 🌟](https://k8spharos.dev)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Container Engines

### Lightweight Runtimes

#### Archived Projects

  - **(2021)** [K3C](https://github.com/rancher/k3c) <span class='md-tag md-tag--info'>⭐ 564</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight features K3C as a classic lightweight container engine. Live grounding in 2026 confirms that K3C is an archived repository, serving primarily as an intellectual precursor to container daemon simplification and modular containerd patterns.
## Edge and IoT

### Cluster Provisioning

#### SSH Bootstrapping

  - **(2026)** [****k3sup (said 'ketchup')****](https://github.com/alexellis/k3sup) <span class='md-tag md-tag--info'>⭐ 7383</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An utility by Alex Ellis using SSH to provision K3s directly from local machines. It sets up secure, direct API configurations, bridges cluster nodes instantly, and configures target servers for operational readiness.
## Edge Computing

### Operating Systems

#### Archived Projects (1)

  - **(2022)** [****k3OS****](https://github.com/rancher/k3os) <span class='md-tag md-tag--info'>⭐ 3490</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight highlights k3OS as a purpose-built operating system designed for K3s. Live engineering truth in 2026 confirms k3OS has been officially archived by Rancher. Platform engineers seeking an active declarative OS for container workloads have transitioned to alternatives like Talos Linux or MicroOS.
## Infrastructure

### Cluster Provisioning (1)

#### Bare Metal

  - **(2026)** [==poseidon/typhoon==](https://github.com/poseidon/typhoon) <span class='md-tag md-tag--info'>⭐ 2044</span> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Typhoon is a minimalist, secure, and performant bare-metal and multi-cloud Kubernetes distribution built entirely with Terraform. It bootstraps standard, upstream CNCF-compliant Kubernetes onto Flatcar Container Linux (and historically CoreOS), providing an excellent reference model for git-driven infrastructure without vendor lock-in.
### Kubernetes Distributions

#### Edge and IoT (1)

  - **(2023)** [==xiaods/k8e==](https://github.com/xiaods/k8e) <span class='md-tag md-tag--info'>⭐ 449</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A lightweight Kubernetes distribution (k8e, standing for "k8s easy") modeled after K3s but strictly adhering to standard upstream components. It is tailored for low-resource edge architectures, CI environments, and hobbyist networks requiring low memory profiles and simple setups.
## Local Development

### Kubernetes Environments

#### k3d

  - **(2025)** [==**k3d**==](https://github.com/k3d-io/k3d) <span class='md-tag md-tag--info'>⭐ 6458</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight features k3d as an indispensable utility for launching multi-node K3s clusters inside Docker containers. Live grounding in 2026 affirms k3d remains the leading choice for local multi-node Kubernetes orchestration, integration testing, and local CI/CD pipelines due to its rapid spin-up speeds and minimal resource footprint.
## Local Kubernetes Environments

### Containerized Clusters

#### KIND

  - **(2026)** [****kind****](https://github.com/kubernetes-sigs/kind) <span class='md-tag md-tag--info'>⭐ 15299</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kubernetes in Docker (kind) is an indispensable ecosystem framework utilizing Docker container nodes to model multi-node clusters. Widely favored for continuous integration (CI) workflows and high-speed local control plane validation.
### Single-Node Clusters

#### Minikube

  - **(2026)** [==Minikube==](https://github.com/kubernetes/minikube) <span class='md-tag md-tag--info'>⭐ 31871</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Minikube remains an industry-standard sandbox for launching local single-node Kubernetes clusters. Supports diverse VM drivers, bare-metal deployment modes, and native Docker-in-Docker execution environments tailored for application testing.
## Networking and Security

### Kubernetes Networking

#### Ingress and Traffic

  - **(2023)** [==Learnk8s: Comparison of Kubernetes Ingress Controllers 🌟🌟==](https://docs.google.com/spreadsheets/d/191WWNpjJ2za6-nbG4ZoUMXMpUK8KlCIosvQB0f-oq3k/edit#gid=907731238) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An expansive, community-maintained comparison spreadsheet detailing the feature matrices, protocol supports, dynamic reloading behaviors, and ecosystem integrations of various Ingress Controllers. Live Grounding highlights this dynamic reference as an essential resource for architects choosing ingress tools based on enterprise requirements.
## Platform Architecture

### Cloud Providers

#### Managed Kubernetes Comparison

  - **(2021)** [Learnk8s: Comparison of Kubernetes Managed Services 🌟](https://docs.google.com/spreadsheets/d/1RPpyDOLFmcgxMCpABDzrsBYWpPYCIBuvAoUQLwOGoQw/edit) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly granular, community-maintained matrix tracking managed Kubernetes services across both major and minor cloud vendors. It details network capabilities, autoscaler integration, upgrades, security profiles, and persistent volume support. It represents an essential industry benchmark used by platform architects designing global cluster patterns.
  - **(2020)** [atodorov.me: Comparing Kubernetes managed services across Digital Ocean, Scaleway, OVHCloud and Linode](https://atodorov.me/2020/06/14/comparing-kubernetes-managed-services-across-digital-ocean-scaleway-ovhcloud-and-linode) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares managed Kubernetes offerings from secondary cloud providers: DigitalOcean, Scaleway, OVHCloud, and Linode. It analyzes storage driver speeds, control plane SLA pricing, and API version support. This evaluation helps teams design multi-cloud setups and avoid the cost overhead associated with tier-1 hyperscalers.
## Provisioning

### Ansible

#### Enterprise Playbooks

  - **(2026)** [==**Kubespray**==](https://github.com/kubernetes-sigs/kubespray) <span class='md-tag md-tag--info'>⭐ 18556</span> <span class='md-tag md-tag--warning'>[PYTHON/ANSIBLE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The industry standard Ansible automation framework for deploying enterprise-ready, production-grade clusters. Combining Kubeadm with highly flexible, battle-tested playbooks, it handles network policy deployment (CNIs like Calico/Cilium), storage classes, node lifecycle operations, and multi-distribution OS configurations.
#### Roles

  - **(2026)** [==Ansible Role - Kubernetes (Jeff Geerling)==](https://github.com/geerlingguy/ansible-role-kubernetes) <span class='md-tag md-tag--info'>⭐ 626</span> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Jeff Geerling's highly popular, community-standard Ansible role designed to automate core system dependencies, swap disabling, package installations, and initial Kubeadm commands on Debian and RedHat distributions, simplifying playbooks deployment.
### Bootstrapping

#### Core Engine

  - **(2026)** [==Kubernetes Cluster with **Kubeadm**==](https://github.com/kubernetes/kubeadm) <span class='md-tag md-tag--info'>⭐ 3980</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The standard bootstrapping engine for establishing conformant clusters, maintained by Kubernetes SIG-Cluster-Lifecycle. It abstracts certificate generation, etcd cluster building, and node onboarding into simplified `kubeadm init` and `kubeadm join` commands. It serves as the foundation for higher-level platform controllers.
### Deployment Tools

#### AWS

  - **(2026)** [==GitHub: Kubernetes Cluster with Kops==](https://github.com/kubernetes/kops) <span class='md-tag md-tag--info'>⭐ 16625</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kubernetes Operations (kops) is a production-grade orchestration tool designed to configure, scale, and manage highly available clusters on public cloud environments. Its declarative structure manages cloud instances, security groups, route tables, and internal etcd scaling configurations directly, primarily focusing on AWS.
### GitOps

#### Legacy Tools

  - **(2026)** [==Weave Kubernetes System Control - wksctl==](https://github.com/weaveworks/wksctl) <span class='md-tag md-tag--info'>⭐ 389</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Weaveworks' Weave Kubernetes System Control (wksctl) was a GitOps-based tool for cluster creation, configuring infrastructure directly from a declared state stored in git. Curator Insight vs Live Grounding: Following Weaveworks' operational shutdown, this tool has been archived and is considered historical legacy.

---
💡 **Explore Related:** [Demos](./demos.md) | [Kubernetes](./kubernetes.md) | [Cheatsheets](./cheatsheets.md)

