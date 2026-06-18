# Argo Declarative GitOps for Kubernetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/argo/).

!!! info "Architectural Context"
    Detailed reference for Argo Declarative GitOps for Kubernetes in the context of Engineering Pipeline.

## Table of Contents

1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Native](#cloud-native)
  - [Orchestration](#orchestration)
    - [Argo Workflows](#argo-workflows)
      - [Reliability](#reliability)
      - [Security](#security)
      - [Templates](#templates)
1. [GitOps and CD](#gitops-and-cd)
  - [Argo Project Ecosystem](#argo-project-ecosystem)
  - [Argo Rollouts](#argo-rollouts)
    - [Blue-Green Deployment](#blue-green-deployment)
    - [Canary Deployment](#canary-deployment)
    - [Configuration Management](#configuration-management)
    - [Progressive Delivery](#progressive-delivery)
  - [Argo Workflows](#argo-workflows-1)
    - [Release News](#release-news)
  - [ArgoCD](#argocd)
    - [ApplicationSets](#applicationsets)
    - [Authentication and SSO](#authentication-and-sso)
      - [GitHub Integration](#github-integration)
    - [Best Practices](#best-practices)
    - [Bootstrap Automation](#bootstrap-automation)
      - [Autopilot](#autopilot)
    - [Concepts and Practices](#concepts-and-practices)
    - [Introduction](#introduction)
    - [Multi-Cluster](#multi-cluster)
      - [ApplicationSets](#applicationsets-1)
    - [Patterns](#patterns)
      - [App-of-Apps](#app-of-apps)
    - [Plugins and Extensions](#plugins-and-extensions)
    - [Synchronization Strategies](#synchronization-strategies)
    - [Tutorials](#tutorials)
    - [Workload Management](#workload-management)
      - [Demos](#demos)
  - [CICD Integration](#cicd-integration)
  - [Tool Comparison](#tool-comparison)
    - [ArgoCD vs FluxCD](#argocd-vs-fluxcd)
1. [Kubernetes GitOps and Packaging](#kubernetes-gitops-and-packaging)
  - [Argo Project Ecosystem](#argo-project-ecosystem-1)
    - [Event-Driven Automation](#event-driven-automation)
    - [GitOps Strategy](#gitops-strategy)
    - [UI Visualization](#ui-visualization)
    - [Video Guides](#video-guides)
1. [Platform Engineering](#platform-engineering)
  - [ArgoCD](#argocd-1)
    - [Internal Developer Platforms](#internal-developer-platforms)
    - [Security and Compliance](#security-and-compliance)
      - [RBAC](#rbac)
  - [GitOps](#gitops)
    - [AWS EKS](#aws-eks)
      - [Tekton](#tekton)
    - [ArgoCD](#argocd-2)
      - [Architecture Topologies](#architecture-topologies)
      - [Terraform Integration](#terraform-integration)
    - [Authentication and SSO](#authentication-and-sso-1)
      - [OpenShift](#openshift)
    - [GitHub Actions](#github-actions)
      - [AWS EKS](#aws-eks-1)
    - [Kubernetes Operators](#kubernetes-operators)
      - [CRD Lifecycle](#crd-lifecycle)
    - [Multi-Tenancy](#multi-tenancy)
      - [Security and Compliance](#security-and-compliance-1)
    - [Terraform Integration](#terraform-integration-1)
      - [Data Infrastructure](#data-infrastructure)
  - [Infrastructure as Code](#infrastructure-as-code)
    - [Modular Architecture](#modular-architecture)
    - [Terraform and AWS](#terraform-and-aws)
      - [EKS Modules](#eks-modules)
  - [Progressive Delivery](#progressive-delivery-1)
    - [DNS Routing](#dns-routing)
      - [Blue-Green Deployment](#blue-green-deployment-1)
  - [Secret Management](#secret-management)
    - [HashiCorp Vault](#hashicorp-vault)
      - [ArgoCD Plugins](#argocd-plugins)
    - [Sealed Secrets](#sealed-secrets)
      - [ArgoCD](#argocd-3)
1. [Security and Compliance](#security-and-compliance-2)
  - [Vulnerabilities and CVEs](#vulnerabilities-and-cves)
    - [ArgoCD Security](#argocd-security)
      - [Remediation](#remediation)

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [medium: Argo CD: A Tool for Kubernetes DevOps](https://medium.com/geekculture/argo-cd-a-tool-for-kubernetes-devops-c46f2881edfe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Argo CD: A Tool for Kubernetes DevOps in the Kubernetes Tools ecosystem.
  - [wecloudpro.com: Deploying Helm Charts with ArgoCD](https://www.wecloudpro.com/2021/11/28/Argocd-helm.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering wecloudpro.com: Deploying Helm Charts with ArgoCD in the Kubernetes Tools ecosystem.
  - [medium.com/gumgum-tech: Streamlining your Kubernetes adoption with Helmfile' / ArgoCD and GitOps](https://medium.com/gumgum-tech/streamlining-your-kubernetes-adoption-with-helmfile-argocd-and-gitops-211937e21e29)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/gumgum-tech: Streamlining your Kubernetes adoption with Helmfile' / ArgoCD and GitOps in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: Getting Started With ArgoCD on your Kubernetes' Cluster](https://levelup.gitconnected.com/getting-started-with-argocd-on-your-kubernetes-cluster-552ca5d8cf41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: Getting Started With ArgoCD on your Kubernetes' Cluster in the Kubernetes Tools ecosystem.
  - [igboie.medium.com: Kubernetes CI/CD with GitHub, GitHub Actions and Argo' CD](https://igboie.medium.com/kubernetes-ci-cd-with-github-github-actions-and-argo-cd-36b88b6bda64)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering igboie.medium.com: Kubernetes CI/CD with GitHub, GitHub Actions and Argo' CD in the Kubernetes Tools ecosystem.
  - [medium.com/containers-101: Using GitOps, Multiple Argo Instances, and Environments' with Argo CD at Scale](https://medium.com/containers-101/using-gitops-multiple-argo-instances-and-environments-with-argo-cd-at-scale-e6b19c86be36)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/containers-101: Using GitOps, Multiple Argo Instances, and Environments' with Argo CD at Scale in the Kubernetes Tools ecosystem.
  - [medium.com/@ScrumPokerPro: Cloud native architecture with Kubernetes and' ArgoCD](https://medium.com/@ScrumPokerPro/cloud-native-architecture-with-kubernetes-and-argocd-ebecda7784b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ScrumPokerPro: Cloud native architecture with Kubernetes and' ArgoCD in the Kubernetes Tools ecosystem.
  - [faun.pub: Deploying Argo CD and Sealed Secrets with Helm](https://faun.pub/deploying-argo-cd-and-sealed-secrets-with-helm-8de12f53051b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Deploying Argo CD and Sealed Secrets with Helm in the Kubernetes Tools ecosystem.
  - [amralaayassen.medium.com: How to create ArgoCD Applications Automatically' using ApplicationSet? “Automation of GitOps”](https://amralaayassen.medium.com/how-to-create-argocd-applications-automatically-using-applicationset-automation-of-the-gitops-59455eaf4f72)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering amralaayassen.medium.com: How to create ArgoCD Applications Automatically' using ApplicationSet? “Automation of GitOps” in the Kubernetes Tools ecosystem.
  - [blog.akuity.io: Unveil the Secret Ingredients of Continuous Delivery at' Enterprise Scale with Argo CD](https://blog.akuity.io/unveil-the-secret-ingredients-of-continuous-delivery-at-enterprise-scale-with-argo-cd-7c5b4057ee49)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.akuity.io: Unveil the Secret Ingredients of Continuous Delivery at' Enterprise Scale with Argo CD in the Kubernetes Tools ecosystem.
  - [prashant-48386.medium.com: Continuous Delivery for Kubernetes With Argo' CD](https://prashant-48386.medium.com/continuous-delivery-for-kubernetes-with-argo-cd-9d5f3b69f1db)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering prashant-48386.medium.com: Continuous Delivery for Kubernetes With Argo' CD in the Kubernetes Tools ecosystem.
  - [medium.com/@outlier.developer: Getting Started with ArgoCD for GitOps Kubernetes' Deployments](https://medium.com/@outlier.developer/getting-started-with-argocd-for-gitops-kubernetes-deployments-fafc2ad2af0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@outlier.developer: Getting Started with ArgoCD for GitOps Kubernetes' Deployments in the Kubernetes Tools ecosystem.
  - [medium.com/@hmquan08011996: Setup Microservices on Kubernetes — Automating' Kubernetes with ArgoCD](https://medium.com/@hmquan08011996/setup-microservices-on-kubernetes-automating-kubernetes-with-argocd-cb94622dac5b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@hmquan08011996: Setup Microservices on Kubernetes — Automating' Kubernetes with ArgoCD in the Kubernetes Tools ecosystem.
  - [kamsjec.medium.com: ArgoCD Setup on Kubernetes/OpenShift Cluster](https://kamsjec.medium.com/argocd-setup-on-kubernetes-openshift-cluster-f7340344c017)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kamsjec.medium.com: ArgoCD Setup on Kubernetes/OpenShift Cluster in the Kubernetes Tools ecosystem.
  - [medium.com/@versentfastforward: GitOps on Kubernetes with ArgoCD](https://medium.com/@versentfastforward/gitops-and-argocd-to-automate-kubernetes-deployments-640f3a086865)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@versentfastforward: GitOps on Kubernetes with ArgoCD in the Kubernetes Tools ecosystem.
  - [medium.com/@versentfastforward: One-click Bootstrap Deployment of ArgoCD](https://medium.com/@versentfastforward/one-click-bootstrap-deployment-of-argocd-e06f848aacc5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@versentfastforward: One-click Bootstrap Deployment of ArgoCD in the Kubernetes Tools ecosystem.
  - [medium.com/@versentfastforward: Structuring Your Repo for ArgoCD, Part 1](https://medium.com/@versentfastforward/structuring-your-repo-for-argocd-part-1-582817713b0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@versentfastforward: Structuring Your Repo for ArgoCD, Part 1 in the Kubernetes Tools ecosystem.
  - [faun.pub: Continuous Deployments of Kubernetes Applications using Argo CD' GitOps & Helm Charts](https://faun.pub/continuous-deployments-of-kubernetes-applications-using-argo-cd-gitops-helm-charts-9df917caa2e4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Continuous Deployments of Kubernetes Applications using Argo CD' GitOps & Helm Charts in the Kubernetes Tools ecosystem.
  - [jamalshahverdiev.medium.com: ArgoCD ApplicationSet with Applications, Image' Updater and Notification controller with SSO](https://jamalshahverdiev.medium.com/argocd-applicationset-with-applications-image-updater-and-notification-controller-with-sso-bba3182dad8a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering jamalshahverdiev.medium.com: ArgoCD ApplicationSet with Applications, Image' Updater and Notification controller with SSO in the Kubernetes Tools ecosystem.
  - [faun.pub: Hygiene of an ArgoCD-built automation at a scale](https://faun.pub/hygiene-of-argocd-built-automation-at-a-scale-cf63ee459510)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Hygiene of an ArgoCD-built automation at a scale in the Kubernetes Tools ecosystem.
  - [blog.devgenius.io: Argo CD Introduction](https://blog.devgenius.io/argo-cd-introduction-4b16f50b0d56)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devgenius.io: Argo CD Introduction in the Kubernetes Tools ecosystem.
  - [figments.medium.com: ArgoCD: The first step towards GitOps](https://figments.medium.com/argocd-the-first-step-towards-gitops-899732fbc33e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering figments.medium.com: ArgoCD: The first step towards GitOps in the Kubernetes Tools ecosystem.
  - [medium.com/@nsfabrice2009: How to install ArgoCD on k8s cluster](https://medium.com/@nsfabrice2009/how-to-install-argocd-on-k8s-cluster-ad9084c71f16)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@nsfabrice2009: How to install ArgoCD on k8s cluster in the Kubernetes Tools ecosystem.
  - [medium.com/containers-101: How to Install and Upgrade Argo CD](https://medium.com/containers-101/how-to-install-and-upgrade-argo-cd-a64f4635f97b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/containers-101: How to Install and Upgrade Argo CD in the Kubernetes Tools ecosystem.
  - [medium.com/containers-101: Argo CD Best Practices](https://medium.com/containers-101/best-practices-for-argo-cd-8253bcd31897)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/containers-101: Argo CD Best Practices in the Kubernetes Tools ecosystem.
  - [gokhan-karadas1992.medium.com: ArgoCD + Kubevela Integration](https://gokhan-karadas1992.medium.com/argocd-kubevela-integration-eb88dc0484e0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering gokhan-karadas1992.medium.com: ArgoCD + Kubevela Integration in the Kubernetes Tools ecosystem.
  - [blog.tanmaysarkar.tech: Beginners Guide to Argo CD](https://blog.tanmaysarkar.tech/beginners-guide-to-argo-cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==blog.tanmaysarkar.tech: Beginners Guide to Argo CD== in the Kubernetes Tools ecosystem.
  - [medium.com/devops-techable: GitOps with ArgoCD running in Kubernetes for' deployment processing](https://medium.com/devops-techable/gitops-with-argocd-running-in-kubernetes-for-deployment-processing-c5d21770ca97)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/devops-techable: GitOps with ArgoCD running in Kubernetes for' deployment processing in the Kubernetes Tools ecosystem.
  - [medium.com/@eduard.mihai.lemnaru: Auto-update helm chart version using ArgoCD](https://medium.com/@eduard.mihai.lemnaru/auto-update-helm-chart-version-using-argocd-4936933a2bac)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@eduard.mihai.lemnaru: Auto-update helm chart version using ArgoCD in the Kubernetes Tools ecosystem.
  - [53jk1.medium.com: ArgoCD: The Continuous Delivery Solution for Kubernetes](https://53jk1.medium.com/argocd-the-continuous-delivery-solution-for-kubernetes-ae5b008e76d1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering 53jk1.medium.com: ArgoCD: The Continuous Delivery Solution for Kubernetes in the Kubernetes Tools ecosystem.
  - [medium.com/@jon.mclean: ArgoCD: The GitOps Way](https://medium.com/@jon.mclean/argocd-the-gitops-way-90f7eb0d2606)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@jon.mclean: ArgoCD: The GitOps Way in the Kubernetes Tools ecosystem.
  - [medium.com/@devopsrockers: Blue-Green Deployment on EKS using Argocd with' Kubecost, Istio, External DNS, Grafana-Prometheus and More: “Build, Deploy a Resilient and Observability-Driven Application”](https://medium.com/@devopsrockers/blue-green-deployment-on-eks-using-argocd-with-kubecost-istio-external-dns-grafana-prometheus-d5d5508f0748)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@devopsrockers: Blue-Green Deployment on EKS using Argocd with' Kubecost, Istio, External DNS, Grafana-Prometheus and More: “Build, Deploy a Resilient and Observability-Driven Application” in the Kubernetes Tools ecosystem.
  - [medium.com/@samuelbagattin: Partial Helm values encryption using AWS KMS' with ArgoCD](https://medium.com/@samuelbagattin/partial-helm-values-encryption-using-aws-kms-with-argocd-aca1c0d36323)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@samuelbagattin: Partial Helm values encryption using AWS KMS' with ArgoCD in the Kubernetes Tools ecosystem.
  - [blog.devops.dev: GitOps at Scale](https://blog.devops.dev/gitops-at-scale-69639c9a3dd7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devops.dev: GitOps at Scale in the Kubernetes Tools ecosystem.
  - [medium.com/@jerome.decoster: Create temporary environment from Pull Request' with ArgoCD ApplicationSet](https://medium.com/@jerome.decoster/create-temporary-environment-from-pull-request-with-argocd-applicationset-1cef9803223a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@jerome.decoster: Create temporary environment from Pull Request' with ArgoCD ApplicationSet in the Kubernetes Tools ecosystem.
  - [medium.com/@geoffrey.muselli: ArgoCD: Multi-cluster Helm charts management' in mono-repo](https://medium.com/@geoffrey.muselli/argocd-multi-cluster-helm-charts-installation-in-mono-repo-0a406ff7c578)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@geoffrey.muselli: ArgoCD: Multi-cluster Helm charts management' in mono-repo in the Kubernetes Tools ecosystem.
  - [medium.com/otomi-platform: Helmfile and ArgoCD are better together](https://medium.com/otomi-platform/helmfile-and-argocd-better-together-f8d4587263ff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/otomi-platform: Helmfile and ArgoCD are better together in the Kubernetes Tools ecosystem.
  - [overcast.blog: GitOps with ArgoCD for Kubernetes](https://overcast.blog/gitops-with-argocd-for-kubernetes-tips-and-tricks-4b926ba75f88)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering overcast.blog: GitOps with ArgoCD for Kubernetes in the Kubernetes Tools ecosystem.
  - [medium.com/globant: Using multiple sources for a Helm Chart deployment in' ArgoCD](https://medium.com/globant/using-multiple-sources-for-a-helm-chart-deployment-in-argocd-cf3cd2d598fc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/globant: Using multiple sources for a Helm Chart deployment in' ArgoCD in the Kubernetes Tools ecosystem.
  - [faun.pub: ArgoCD Finalizer Shield: Protecting Your Production Clusters from' Unintended Deletion](https://faun.pub/argocd-finalizer-shield-protecting-your-clusters-from-unintended-deletion-c7929a82d983)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: ArgoCD Finalizer Shield: Protecting Your Production Clusters from' Unintended Deletion in the Kubernetes Tools ecosystem.
  - [overcast.blog: Kubernetes — ArgoCD — Gitlab Webhook Configuration](https://overcast.blog/kubernetes-argocd-gitlab-webhook-configuration-30bc5a75139e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering overcast.blog: Kubernetes — ArgoCD — Gitlab Webhook Configuration in the Kubernetes Tools ecosystem.
  - [dnastacio.medium.com: Six critical blindspots while securing Argo CD](https://dnastacio.medium.com/gitops-argocd-security-cbb6fb6378bb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dnastacio.medium.com: Six critical blindspots while securing Argo CD in the Kubernetes Tools ecosystem.
  - [jijujacob27.medium.com: Sharded applications on Kubernetes using Helm, ArgoCD,' and Argo-Rollouts](https://jijujacob27.medium.com/sharded-saas-applications-on-kubernetes-using-helm-argocd-and-argo-rollouts-a683c66f8646)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering jijujacob27.medium.com: Sharded applications on Kubernetes using Helm, ArgoCD,' and Argo-Rollouts in the Kubernetes Tools ecosystem.
  - [medium.com/@ej.sta.ana: Easy Blue-Green Deployment on Openshift Container' Platform using Argo Rollouts](https://medium.com/@ej.sta.ana/easy-blue-green-deployment-on-openshift-container-platform-using-argo-rollouts-4d514b3c5c0f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ej.sta.ana: Easy Blue-Green Deployment on Openshift Container' Platform using Argo Rollouts in the Kubernetes Tools ecosystem.
  - [medium.com/everything-full-stack: Deployment Strategies: Argo Rollouts](https://medium.com/everything-full-stack/deployment-strategies-argo-rollouts-1980fc0685e6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/everything-full-stack: Deployment Strategies: Argo Rollouts in the Kubernetes Tools ecosystem.
  - [faun.pub: Kubernetes Practice — Automating Blue/Green Deployment with Argo' Rollouts](https://faun.pub/kubernetes-practice-automating-blue-green-deployment-with-argo-rollouts-2279aa890c53)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Kubernetes Practice — Automating Blue/Green Deployment with Argo' Rollouts in the Kubernetes Tools ecosystem.
  - [faun.pub: How Helm Subcharts Make the Transition to Argo Rollouts a Breeze](https://faun.pub/how-helm-subcharts-make-the-transition-to-argo-rollouts-a-breeze-aaf160924dbf)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: How Helm Subcharts Make the Transition to Argo Rollouts a Breeze in the Kubernetes Tools ecosystem.
  - [medium.com/atlantbh: Implementing CI/CD pipeline using Argo Workflows and' Argo Events 🌟](https://medium.com/atlantbh/implementing-ci-cd-pipeline-using-argo-workflows-and-argo-events-6417dd157566)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/atlantbh: Implementing CI/CD pipeline using Argo Workflows and' Argo Events 🌟 in the Kubernetes Tools ecosystem.
## Cloud Native

### Orchestration

#### Argo Workflows

##### Reliability

  - **(2023)** [blog.argoproj.io: Architecting Workflows For Reliability](https://blog.argoproj.io/architecting-workflows-for-reliability-d33bd720c6cc) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines reliable architectural patterns for running large-scale Argo Workflows. Covers retry policies, rate-limiting configurations, and workflow controller adjustments necessary to safely sustain highly concurrent executions without experiencing system degradation.
##### Security

  - **(2023)** [blog.argoproj.io: Practical Argo Workflows Hardening 🌟](https://blog.argoproj.io/practical-argo-workflows-hardening-dd8429acc1ce) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical guide to security hardening for Argo Workflows deployments in enterprise environments. Focuses on minimizing RBAC permissions, configuring network policies, securing the workflow controller, and utilizing read-only file systems to mitigate risks of privilege escalation and container breakouts.
##### Templates

  - **(2023)** [dev.to: The three meanings of "template" in Argo Workflows](https://dev.to/crenshaw_dev/the-three-meanings-of-template-in-argo-workflows-2paf) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes the semantic differences and runtime boundaries between the three distinct definitions of 'template' in Argo Workflows. Distinguishes template definitions, invocations, and inline declarations within a workflow manifest, preventing common YAML structure misconfigurations in complex pipelines.
## GitOps and CD

### Argo Project Ecosystem

  - **(2021)** [**devops.com: The Argo Project: Making GitOps Practical**](https://devops.com/the-argo-project-making-gitops-practical) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Investigates the rapid industry adoption of the Argo ecosystem (Argo CD, Workflows, Rollouts, Events). Explains how the projects solve operational gaps in native Kubernetes, making declarative continuous delivery robust and enterprise-ready.
### Argo Rollouts

#### Blue-Green Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts : Blue-Green Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-blue-green-deployment) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through setting up a complete Blue-Green deployment workflow with Argo Rollouts. Outlines routing controls, active/preview service handoffs, and visual UI verification configurations.
#### Canary Deployment

  - **(2022)** [**infracloud.io: Progressive Delivery with Argo Rollouts: Canary Deployment**](https://www.infracloud.io/blogs/progressive-delivery-argo-rollouts-canary-deployment) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Offers a practical exploration of canary rollouts configured via Argo Rollouts. Focuses on setting step-based traffic splitting, managing dynamic service mesh weights (SMI, Linkerd, Istio), and defining automated rollbacks based on analysis metrics.
#### Configuration Management

  - **(2022)** [**codefresh.io: Progressive delivery for Kubernetes Config Maps using Argo Rollouts**](https://octopus.com/blog/progressive-delivery-for-kubernetes-config-maps-using-argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Solves the tricky challenge of managing and rolling out application configuration updates dynamically. Demonstrates how to trigger controlled, safe progressive delivery cycles for applications when only ConfigMaps or Secrets are modified.
#### Progressive Delivery

  - **(2023)** [==argoproj.github.io: Argo Rollouts - Kubernetes Progressive Delivery Controller==](https://argoproj.github.io/argo-rollouts) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduces the core concepts of Argo Rollouts, which replaces standard Kubernetes Deployment objects with custom Rollout resources. Enables automatic analysis, metrics integration (Prometheus, Datadog), and automated rollback strategies.
### Argo Workflows (1)

#### Release News

  - **(2022)** [**blog.argoproj.io: What’s new in Argo Workflows v3.3**](https://blog.argoproj.io/whats-new-in-argo-workflows-v3-3-dd051d2f1c7) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Highlights the key feature additions, execution optimizations, and performance enhancements introduced in Argo Workflows version 3.3. Discusses UI/UX developments, DAG scaling capabilities, and robust security upgrades.
### ArgoCD

#### ApplicationSets

  - **(2023)** [==argoproj-labs/applicationset: Argo CD ApplicationSet Controller==](https://github.com/argoproj/applicationset) <span class='md-tag md-tag--info'>⭐ 582</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-636d4826" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 13 L 20 13 L 30 10 L 40 3 L 50 9" fill="none" stroke="url(#spark-grad-636d4826)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The standard orchestrator extending Argo CD to support multi-cluster application distribution templates. Processes multi-source configurations, automates environment scaling, and drastically reduces the maintenance overhead of managing distinct Application manifests.
  - **(2024)** [**developers.redhat.com: Enhance Kubernetes deployment efficiency with Argo CD and ApplicationSet**](https://developers.redhat.com/articles/2024/06/06/enhance-kubernetes-deployment-efficiency-argo-cd-and-applicationset) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Deep technical review of optimization practices when deploying large-scale software footprints using ApplicationSets. Outlines how to maximize rendering efficiency, prevent performance bottlenecks, and design clean matrix-based generators.
#### Authentication and SSO

##### GitHub Integration

  - **(2021)** [cloud.redhat.com: How to Use ArgoCD Deployments with GitHub Tokens](https://www.redhat.com/en/blog/how-to-use-argocd-deployments-with-github-tokens) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explains how to securely integrate ArgoCD with private GitHub repositories using Personal Access Tokens (PATs) and fine-grained permissions. Addresses secure secret management inside Kubernetes to safeguard credentials used during the repository fetching phase.
#### Best Practices

  - **(2022)** [**datree.io: ArgoCD Best Practices You Should Know**](https://www.datree.io/resources/argocd-best-practices-you-should-know) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Expands on essential ArgoCD best practices, emphasizing the isolation of Git repositories for source code and Kubernetes manifests, configuring auto-prune, and defining declarative sync policies to maintain platform stability.
#### Bootstrap Automation

##### Autopilot

  - **(2023)** [==argoproj-labs/argocd-autopilot: Argo-CD Autopilot==](https://github.com/argoproj-labs/argocd-autopilot) <span class='md-tag md-tag--info'>⭐ 1121</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ef274bf2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 11 L 20 9 L 30 5 L 40 4 L 50 3" fill="none" stroke="url(#spark-grad-ef274bf2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An official Argo project opinionated tool designed to structure, install, and update Argo CD setups automatically. Uses a clean directory structure separating infrastructure from application manifests, enabling rapid multi-project bootstrap with version tracking and disaster recovery features.
#### Concepts and Practices

  - **(2022)** [**thenewstack.io: Applied GitOps with ArgoCD**](https://thenewstack.io/applied-gitops-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A comprehensive examination of GitOps workflows operationalized via ArgoCD. Highlights key practices such as declarative environment definition, pull-based synchronization, and automated drift detection to maintain cluster state parity.
  - **(2022)** [thenewstack.io: Why ArgoCD Is the Lifeline of GitOps](https://thenewstack.io/why-argo-cd-is-the-lifeline-of-gitops) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the architectural superiority of ArgoCD as a pull-based GitOps operator. Focuses on its continuous reconciliation loop, granular cluster state visualization, and out-of-the-box self-healing capabilities that minimize human intervention.
  - **(2021)** [blog.risingstack.com: Argo CD Kubernetes Tutorial](https://blog.risingstack.com/argo-cd-kubernetes-tutorial) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A structured starter guide covering ArgoCD installation, repository connection, and application deployment. Outlines core synchronization paradigms and provides a practical walkthrough of transitioning standard manifests to GitOps.
  - **(2021)** [blog.getambassador.io: GitOps in Kubernetes with ArgoCD](https://blog.getambassador.io/gitops-in-kubernetes-with-argocd-c6ea0e510741) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Describes the conceptual pillars of GitOps and details how ArgoCD implements them on Kubernetes. Explains key mechanisms such as out-of-sync alert signaling, dry-run synchronization, and visual drift visualization.
#### Introduction

  - **(2022)** [kubebyexample.com: Argo CD Overview 🌟](https://kubebyexample.com/learning-paths/argo-cd/argo-cd-overview) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational educational overview of the ArgoCD engine, architecture, and UI dashboard. Introduces the concepts of Target State versus Live State, and details the controller-to-API communication model.
#### Multi-Cluster

##### ApplicationSets (1)

  - **(2022)** [**openshift.com: Getting Started with ApplicationSets**](https://www.redhat.com/en/blog/getting-started-with-applicationsets) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Deep dive into the ArgoCD ApplicationSet controller, explaining how to model and automate multi-cluster and multi-tenant application deployments. Covers generators like List, Directory, and Git to scale configurations with minimal templating boilerplate.
  - **(2022)** [**piotrminkowski.com: Manage Multiple Kubernetes Clusters with ArgoCD 🌟**](https://piotrminkowski.com/2022/12/09/manage-multiple-kubernetes-clusters-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step architectural guide on configuring a centralized ArgoCD instance to manage resources across several remote Kubernetes clusters. Covers network endpoints, remote credentials provisioning, and configuration drift auditing.
#### Patterns

##### App-of-Apps

  - **(2021)** [**opensource.com: Automatically create multiple applications in Argo CD**](https://opensource.com/article/21/7/automating-argo-cd) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates how to leverage the 'App-of-Apps' pattern in ArgoCD to construct recursive, nested application structures. Enables engineers to automate the bootstrapping of complex multi-tier platforms from a single root configuration.
#### Plugins and Extensions

  - **(2023)** [**github.com/crumbhole/argocd-lovely-plugin: argocd-lovely-plugin**](https://github.com/crumbhole/argocd-lovely-plugin) <span class='md-tag md-tag--info'>⭐ 486</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-fc918a40" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 13 L 20 3 L 30 2 L 40 8 L 50 12" fill="none" stroke="url(#spark-grad-fc918a40)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — A flexible Custom Config Management Plugin (CMP) for Argo CD designed to combine Helm, Kustomize, and raw YAML. It solves the nested tooling dilemma by processing multiple template layers without requiring complex shell scripts, simplifying enterprise GitOps chains.
#### Synchronization Strategies

  - **(2022)** [**blog.argoproj.io: New sync and diff strategies in ArgoCD**](https://blog.argoproj.io/new-sync-and-diff-strategies-in-argocd-44195d3f8b8c) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Explores performance optimizations and enhanced reconciliation engines introduced in ArgoCD. Details advanced diff options, custom synchronization hooks, and resource tracking methods that streamline deployment workflows in large-scale environments.
#### Tutorials

  - **(2022)** [digitalocean.com: How to Deploy to Kubernetes using Argo CD and GitOps](https://www.digitalocean.com/community/tutorials/how-to-deploy-to-kubernetes-using-argo-cd-and-gitops) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical implementation guide showcasing the deployment of containerized workloads onto DigitalOcean Kubernetes (DOKS) using ArgoCD. Establishes a complete declarative delivery pipeline driven by version-controlled manifests.
#### Workload Management

##### Demos

  - **(2023)** [github.com/myspotontheweb/gitops-workloads-demo](https://github.com/myspotontheweb/gitops-workloads-demo) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive demo repository showcasing real-world GitOps workload configurations. Provides a structural blueprint for multi-tenant environments, detailing how to cleanly decouple cluster-wide infrastructure configurations from individual application manifests.
### CICD Integration

  - **(2023)** [dev.to: Extending GitOps: Effortless continuous integration and deployment on Kubernetes](https://dev.to/amplication/extending-gitops-effortless-continuous-integration-and-deployment-on-kubernetes-1oem) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores architectural models for bridging continuous integration (CI) platforms with GitOps-driven deployment mechanisms. Emphasizes clean decoupling where CI updates target config states while Kubernetes reconcile loops execute the rollout.
### Tool Comparison

#### ArgoCD vs FluxCD

  - **(2022)** [**thenewstack.io: GitOps on Kubernetes: Deciding Between Argo CD and Flux**](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Evaluates the architectural differences, strengths, and trade-offs of the two dominant GitOps controllers: ArgoCD and FluxCD. Compares ArgoCD's powerful web UI and multi-tenancy model against Flux's lightweight, decentralized, and Kubernetes-native approach.
## Kubernetes GitOps and Packaging

### Argo Project Ecosystem (1)

#### Event-Driven Automation

  - **(2026)** [argoproj.github.io: Argo Events - The Event-driven Workflow Automation Framework](https://argoproj.github.io/argo-events) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The standard event-driven orchestration engine for Kubernetes. Argo Events integrates with sources like webhooks, S3, or pub-sub, dynamically executing serverless triggers, custom scripts, and Argo Workflows with native scalability.
#### GitOps Strategy

  - **(2022)** [Why and when do you need Argo CD?](https://mkdev.me/posts/why-and-when-do-you-need-argo-cd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An executive guide explaining the core capabilities of GitOps and the necessity of declarative pull engines like Argo CD. It details drift management, configuration alignment, and security advantages compared to manual push deployments.
#### UI Visualization

  - **(2024)** [==feat(ui): Add AppSet to Application Resource Tree in Argo CD==](https://github.com/argoproj/argo-cd/pull/26601) <span class='md-tag md-tag--info'>⭐ 23128</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c23c8a66" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 2 L 20 9 L 30 13 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-c23c8a66)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Argo CD feature enhancement that maps ApplicationSets directly inside the dashboard UI tree. This view simplifies managing multi-tenant topologies and nested application definitions for platform operators.
#### Video Guides

  - **(2022)** [youtube: GitOps with Argo-CD & Kubernetes](https://www.youtube.com/watch?v=QrLwFEXvxbo&ab_channel=HoussemDellai) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory video guide showing how to configure and run continuous deployment pipelines using Argo CD and Kubernetes. It walks through initial repository setups, synchronization configurations, and basic troubleshooting procedures.
## Platform Engineering

### ArgoCD (1)

#### Internal Developer Platforms

  - **(2023)** [**itnext.io: Build a Lightweight Internal Developer Platform with Argo CD and Kubernetes Labels**](https://itnext.io/build-a-lightweight-internal-developer-platform-with-argo-cd-and-kubernetes-labels-4c0e52c6c0f4) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Demonstrates how to design a lightweight, self-service Internal Developer Platform (IDP) by leveraging Kubernetes metadata labels, admission webhooks, and ArgoCD's API to dynamically generate applications.
#### Security and Compliance

##### RBAC

  - **(2021)** [itnext.io: ArgoCD: users, access, and RBAC](https://itnext.io/argocd-users-access-and-rbac-ddf9f8b51bad) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details the configuration of user management, local accounts, and role-based access control (RBAC) in ArgoCD. Guides platform engineers through restricting access to specific applications, projects, or clusters using fine-grained policies.
### GitOps

#### AWS EKS

##### Tekton

  - **(2022)** [==aws.amazon.com: Cloud Native CI/CD with Tekton and ArgoCD on AWS==](https://aws.amazon.com/blogs/containers/cloud-native-ci-cd-with-tekton-and-argocd-on-aws) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Discusses designing an end-to-end, Kubernetes-native CI/CD pipeline on AWS EKS. Uses Tekton for building and containerizing microservices, seamlessly handing off the deployment phase to ArgoCD for pull-based application delivery.
#### ArgoCD (2)

##### Architecture Topologies

  - **(2022)** [==akuity.io: How many do you need? - Argo CD Architectures Explained==](https://akuity.io/blog/argo-cd-architectures-explained) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Evaluates different topology designs for ArgoCD deployments in large organizations. Details the trade-offs between a single centralized Hub-and-Spoke cluster controller versus multiple decentralized Argo instances scattered across target clusters.
##### Terraform Integration

  - **(2022)** [seraf.dev: ArgoCD Tutorial — (with Terraform)](https://seraf.dev/argocd-tutorial-with-terraform-af77ddea2e6e) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers on bootstrapping an entire ArgoCD installation, including repositories, projects, and application instances, declaratively via the official HashiCorp Terraform provider for ArgoCD.
#### Authentication and SSO (1)

##### OpenShift

  - **(2022)** [**openshift.com: OpenShift Authentication Integration with ArgoCD**](https://www.redhat.com/en/blog/openshift-authentication-integration-with-argocd) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the integration of OpenShift's native OAuth server with ArgoCD. Explains how to map OpenShift user groups to ArgoCD RBAC roles, establishing a secure, unified single sign-on (SSO) experience for enterprise platforms.
#### GitHub Actions

##### AWS EKS (1)

  - **(2023)** [**dev.to/devsatasurion: Deploying Applications with GitHub Actions and ArgoCD to EKS: Best Practices and Techniques**](https://dev.to/devsatasurion/deploying-applications-with-github-actions-and-argocd-to-eks-best-practices-and-techniques-4epc) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed configuration recipe detailing how to orchestrate deployments to AWS EKS using GitHub Actions as the CI pipeline and ArgoCD as the GitOps agent. Includes IAM role assumptions, token handling, and multi-environment promotions.
#### Kubernetes Operators

##### CRD Lifecycle

  - **(2023)** [**piotrminkowski.com: Manage Kubernetes Operators with ArgoCD**](https://piotrminkowski.com/2023/05/05/manage-kubernetes-operators-with-argocd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Addresses challenges and patterns for deploying Kubernetes Operators (e.g., Prometheus Operator, Cert-Manager) via ArgoCD. Analyzes solutions for Custom Resource Definition (CRD) lifecycle management during upgrades and synchronization.
#### Multi-Tenancy

##### Security and Compliance (1)

  - **(2021)** [==blog.argoproj.io: Best Practices for Multi-tenancy in Argo CD==](https://blog.argoproj.io/best-practices-for-multi-tenancy-in-argo-cd-273e25a047b0) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Outlines critical architectural patterns for implementing multi-tenancy in ArgoCD. Covers AppProjects boundaries, target namespace isolation, network policies, and cluster-wide RBAC to ensure secure sharing of GitOps infrastructure.
#### Terraform Integration (1)

##### Data Infrastructure

  - **(2022)** [**piotrminkowski.com: Manage Kubernetes Cluster with Terraform and Argo CD. Create Kakfa Cluster using GitOps 🌟**](https://piotrminkowski.com/2022/06/28/manage-kubernetes-cluster-with-terraform-and-argo-cd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical demonstration of deploying and managing a Kafka cluster on Kubernetes using a hybrid Terraform and ArgoCD approach. Discusses how to configure infrastructure dependencies with Terraform and declare workload states inside GitOps.
### Infrastructure as Code

#### Modular Architecture

  - **(2022)** [dev.to: Towards a Modular DevOps Stack](https://dev.to/camptocamp-ops/towards-a-modular-devops-stack-257c) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Proposes a blueprint for building modular, maintainable DevOps platforms. Focuses on orchestrating infrastructure provisioners, secret engines, and GitOps engines under unified declarative frameworks to minimize vendor lock-in.
#### Terraform and AWS

##### EKS Modules

  - **(2023)** [**AWS EKS Argo CD Terraform Component**](https://github.com/cloudposse-terraform-components/aws-eks-argocd) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Enterprise-ready Terraform submodule designed to deploy, configure, and bootstrap Argo CD onto an existing AWS EKS cluster. Standardizes complex security configurations, integrates with IAM Roles for Service Accounts (IRSA), and provisions preconfigured Helm releases.
### Progressive Delivery (1)

#### DNS Routing

##### Blue-Green Deployment (1)

  - **(2022)** [**infracloud.io: How to Setup Blue Green Deployments with DNS Routing 🌟**](https://www.infracloud.io/blogs/blue-green-deployments-dns-routing) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Examines advanced architectural design patterns using DNS-based routing to switch traffic for Blue-Green deployments. Discusses how to coordinate external load balancers and global DNS systems during the migration window.
### Secret Management

#### HashiCorp Vault

##### ArgoCD Plugins

  - **(2023)** [==argoproj-labs/argocd-vault-plugin==](https://github.com/argoproj-labs/argocd-vault-plugin) <span class='md-tag md-tag--info'>⭐ 967</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6067d302" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 13 L 20 7 L 30 10 L 40 2 L 50 9" fill="none" stroke="url(#spark-grad-6067d302)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An indispensable Argo CD plugin built to inject secrets dynamically from HashiCorp Vault, AWS Secrets Manager, or GCP Secret Manager. Replaces custom templating hacks by decrypting and injecting secret values directly into workloads at synchronization time, ensuring zero plaintext secrets enter the Git repository.
  - **(2022)** [github.com/crumbhole/argocd-vault-replacer](https://github.com/crumbhole/argocd-vault-replacer) <span class='md-tag md-tag--info'>⭐ 109</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-287cb1bb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 2 L 20 11 L 30 5 L 40 2 L 50 13" fill="none" stroke="url(#spark-grad-287cb1bb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized replacement utility designed to pull secrets from HashiCorp Vault during the Argo CD rendering phase. Acts as a lightweight precursor/alternative to full plugin integrations, enabling targeted placeholder substitutions within native Kubernetes manifest streams.
#### Sealed Secrets

##### ArgoCD (3)

  - **(2021)** [**dev.to: Argo CD and Sealed Secrets is a perfect match**](https://dev.to/timtsoitt/argo-cd-and-sealed-secrets-is-a-perfect-match-1dbf) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Illustrates the architecture of deploying Bitnami Sealed Secrets alongside ArgoCD. Solves the core GitOps paradox by allowing users to safely commit encrypted secrets to Git, which are then decrypted inside the cluster by the controller.
## Security and Compliance (2)

### Vulnerabilities and CVEs

#### ArgoCD Security

##### Remediation

  - **(2022)** [**infoworld.com: How to protect your Kubernetes infrastructure from the Argo CD vulnerability**](https://www.infoworld.com/article/2334525/how-to-protect-your-kubernetes-infrastructure-from-the-argo-cd-vulnerability.html) 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Provides concrete mitigation, scanning, and patching guidelines in the wake of CVE-2022-24348. Demonstrates strategies for minimizing risks in ArgoCD, including least-privilege service account configurations and network boundaries.
  - **(2022)** [**armosec.io: CVE 2022-24348 – Argo CD High Severity Vulnerability and its impact on Kubernetes**](https://www.armosec.io/blog/cve-2022-24348-argo-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Highly detailed technical breakdown of CVE-2022-24348, analyzing how Helm/Kustomize relative path resolution was bypassed. Outlines step-by-step remediation plans and security control recommendations to protect clusters.
  - **(2022)** [threatpost.com: Argo CD Security Bug Opens Kubernetes Cloud Apps to Attackers](https://threatpost.com/argo-cd-security-bug-kubernetes-cloud-apps/178239) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — News coverage of a severe vulnerability affecting ArgoCD. Explains how the path traversal flaw (CVE-2022-24348) allowed malicious manifests to pull sensitive secrets and files from the GitOps control plane cluster.
  - **(2022)** [thehackernews.com: New Argo CD Bug Could Let Hackers Steal Secret Info from Kubernetes Apps](https://thehackernews.com/2022/02/new-argo-cd-bug-could-let-hackers-steal.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how security researchers identified a critical path-traversal bug (CVE-2022-24348) within the ArgoCD repository-reconciliation component. Evaluates the potential risk exposure of configuration data and key material.
  - **(2022)** [securityaffairs.co: Argo CD flaw could allow stealing sensitive data from Kubernetes Apps](https://securityaffairs.com/127708/hacking/kubernetes-argo-cd-flaw.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the threat landscape exposed by vulnerability CVE-2022-24348 in multi-tenant environments. Emphasizes why prompt patching of GitOps controllers is critical when handling multi-tenant repositories on shared control planes.

---
💡 **Explore Related:** [Jenkins](./jenkins.md) | [Openshift Pipelines](./openshift-pipelines.md) | [Flux](./flux.md)

