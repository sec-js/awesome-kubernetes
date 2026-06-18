# DevOps Demos. Boilerplates/Samples, Tutorials and Screencasts

!!! info "Architectural Context"
    Detailed reference for DevOps Demos. Boilerplates/Samples, Tutorials and Screencasts in the context of Architectural Foundations.

## Table of Contents

1. [AI and Data Engineering](#ai-and-data-engineering)
  - [Azure Container Apps](#azure-container-apps)
    - [Terraform and OpenAI](#terraform-and-openai)
1. [Application Architecture](#application-architecture)
  - [Event-Driven](#event-driven)
    - [GraphQL](#graphql)
1. [Application Delivery](#application-delivery)
  - [Asynchronous Messaging](#asynchronous-messaging)
    - [Red Hat Fuse](#red-hat-fuse)
  - [CICD Pipelines](#cicd-pipelines)
    - [Multi-Cluster Deployments](#multi-cluster-deployments)
    - [Tekton Pipelines](#tekton-pipelines)
    - [Tekton Tasks](#tekton-tasks)
    - [Tekton Templates](#tekton-templates)
    - [Workshops](#workshops)
  - [Containerization](#containerization)
    - [Docker](#docker)
    - [Self-Hosted Apps](#self-hosted-apps)
  - [Database Schema Management](#database-schema-management)
    - [Liquibase Integration](#liquibase-integration)
  - [Deployment Strategies](#deployment-strategies)
    - [Canary Deployments](#canary-deployments)
  - [Developer Platforms](#developer-platforms)
    - [App Deployment](#app-deployment)
    - [Local Development](#local-development)
  - [Enterprise Modernization](#enterprise-modernization)
    - [Migration Toolkit](#migration-toolkit)
    - [Multi-Cluster Strategy](#multi-cluster-strategy)
  - [GitOps](#gitops)
    - [Microservices Showcase](#microservices-showcase)
    - [Multi-Cluster Deployments](#multi-cluster-deployments-1)
    - [Multi-Tenancy](#multi-tenancy)
    - [kam CLI](#kam-cli)
  - [Java on Kubernetes](#java-on-kubernetes)
    - [Eclipse JKube Tools](#eclipse-jkube-tools)
  - [Load Balancing](#load-balancing)
    - [High Availability](#high-availability)
1. [Application Development](#application-development)
  - [Base Images](#base-images)
    - [Buildah](#buildah)
    - [Universal Base Image](#universal-base-image)
  - [Cloud-Native Java](#cloud-native-java)
    - [Advanced Microservices](#advanced-microservices)
    - [Spring Boot Microservices](#spring-boot-microservices)
  - [Containerization](#containerization-1)
    - [Java Spring Boot](#java-spring-boot)
  - [Developer Tools](#developer-tools)
    - [Alternative Tooling](#alternative-tooling)
  - [Enterprise Java Platforms](#enterprise-java-platforms)
    - [JBoss Foundations](#jboss-foundations)
  - [Java](#java)
    - [Build Automation](#build-automation)
    - [Local Development](#local-development-1)
    - [Microservices Demo](#microservices-demo)
    - [Project Bootstrapping](#project-bootstrapping)
  - [Microservices Showcase](#microservices-showcase-1)
    - [Spring Boot](#spring-boot)
  - [NodeJS](#nodejs)
    - [Deployment Tooling](#deployment-tooling)
  - [Process Automation](#process-automation)
    - [RHPAM](#rhpam)
  - [Python](#python)
    - [Django](#django)
    - [Scalability](#scalability)
  - [Reference Templates](#reference-templates)
    - [OpenShift 4.8](#openshift-48)
  - [Runtimes and CMS](#runtimes-and-cms)
    - [Strapi CMS](#strapi-cms)
  - [Serverless Java](#serverless-java)
    - [Quarkus Integration](#quarkus-integration)
    - [gRPC Communication](#grpc-communication)
  - [Tutorials](#tutorials)
    - [Developer Demos](#developer-demos)
1. [Application Migration](#application-migration)
  - [Containerization Tools](#containerization-tools)
    - [Move2Kube](#move2kube)
1. [Application Modernization](#application-modernization)
  - [Integration Frameworks](#integration-frameworks)
    - [OpenShift and Camel](#openshift-and-camel)
  - [Spring to Quarkus](#spring-to-quarkus)
    - [Framework Migration](#framework-migration)
1. [Architecture](#architecture)
  - [Microservices](#microservices)
    - [Demo Systems](#demo-systems)
    - [Design Patterns](#design-patterns)
1. [Artificial Intelligence and LLMs](#artificial-intelligence-and-llms)
  - [Prompt Engineering](#prompt-engineering)
    - [Developer Productivity](#developer-productivity)
1. [CI-CD](#ci-cd)
  - [Azure](#azure)
    - [GitHub Actions](#github-actions)
  - [Azure AKS](#azure-aks)
    - [GitHub Actions](#github-actions-1)
  - [Infrastructure](#infrastructure)
    - [Rancher](#rancher)
  - [Java](#java-1)
    - [Automated Workflows](#automated-workflows)
  - [Platform-as-a-Service](#platform-as-a-service)
    - [OpenShift](#openshift)
1. [CICD](#cicd)
  - [GitLab CI](#gitlab-ci)
    - [Pipeline Design](#pipeline-design)
  - [GitOps](#gitops-1)
    - [GitLab Agent](#gitlab-agent)
  - [Jenkins](#jenkins)
    - [Jenkins Pipeline Training](#jenkins-pipeline-training)
    - [Parallel Pipelines](#parallel-pipelines)
    - [SDKMAN](#sdkman)
      - [Docker Integration](#docker-integration)
1. [CICD and DevOps](#cicd-and-devops)
  - [Enterprise Jenkins](#enterprise-jenkins)
    - [OpenShift Integration](#openshift-integration)
1. [CICD Infrastructure](#cicd-infrastructure)
  - [Build and Packaging](#build-and-packaging)
    - [Custom Packager](#custom-packager)
  - [Configuration as Code](#configuration-as-code)
    - [Job Generation](#job-generation)
  - [Plugin Management](#plugin-management)
    - [CLI Tooling](#cli-tooling)
1. [CICD Pipeline](#cicd-pipeline)
  - [Automation Ecosystems](#automation-ecosystems)
    - [Jenkins and Nexus](#jenkins-and-nexus)
1. [CICD Pipeline Architecture](#cicd-pipeline-architecture)
  - [Pipeline Testing](#pipeline-testing)
    - [Local Execution](#local-execution)
    - [Unit Testing](#unit-testing)
1. [CICD Pipelines](#cicd-pipelines-1)
  - [Automated Cloud Deployments](#automated-cloud-deployments)
    - [AWS ECS Deployments](#aws-ecs-deployments)
    - [Kubernetes CD Pipelines](#kubernetes-cd-pipelines)
  - [Automated Image Builds](#automated-image-builds)
    - [Image Builder Workflows](#image-builder-workflows)
  - [Automated Testing](#automated-testing)
    - [Ephemeral K3s Cluster](#ephemeral-k3s-cluster)
    - [Pytest and GitHub Actions](#pytest-and-github-actions)
  - [Azure DevOps Solutions](#azure-devops-solutions)
    - [GitHub Actions Integration](#github-actions-integration)
  - [Data Engineering](#data-engineering)
    - [Automated Data Pipelines](#automated-data-pipelines)
  - [Multi-Cluster GitOps](#multi-cluster-gitops)
    - [ArgoCD Orchestrations](#argocd-orchestrations)
  - [Security and Compliance](#security-and-compliance)
    - [DevSecOps Integration](#devsecops-integration)
    - [GitHub Actions Security](#github-actions-security)
1. [Cloud IoT](#cloud-iot)
  - [Digital Twins](#digital-twins)
    - [API Management](#api-management)
1. [Cloud Learning](#cloud-learning)
  - [Curriculum](#curriculum)
    - [Cloud Engineering](#cloud-engineering)
1. [Cloud Native](#cloud-native)
  - [Security](#security)
    - [Policy Enforcement](#policy-enforcement)
1. [Cloud Native Architecture](#cloud-native-architecture)
  - [Kubernetes](#kubernetes)
    - [Fundamentals](#fundamentals)
  - [Microservices Migration](#microservices-migration)
    - [Case Study](#case-study)
1. [Cloud Native Infrastructure](#cloud-native-infrastructure)
  - [Enterprise Messaging](#enterprise-messaging)
    - [Kafka on Kubernetes](#kafka-on-kubernetes)
      - [APIs and Gateways](#apis-and-gateways)
  - [Observability and Testing](#observability-and-testing)
    - [Pod Mocking](#pod-mocking)
1. [Cloud Native Platforms](#cloud-native-platforms)
  - [Red Hat OpenShift](#red-hat-openshift)
    - [Automation Grading](#automation-grading)
      - [Academic Homework](#academic-homework)
    - [Jenkins Pipelines](#jenkins-pipelines)
      - [Deployment Automation](#deployment-automation)
      - [Lab Environments](#lab-environments)
    - [Local Development](#local-development-2)
      - [CodeReady Containers](#codeready-containers)
1. [Cloud Platform](#cloud-platform)
  - [Microsoft Azure](#microsoft-azure)
    - [Sample Architecture](#sample-architecture)
1. [Cloud Providers](#cloud-providers)
  - [AWS](#aws)
    - [Workshops](#workshops-1)
  - [AWS EKS](#aws-eks)
    - [Foundational](#foundational)
    - [GitOps Tooling](#gitops-tooling)
    - [Masterclass](#masterclass)
    - [Provisioning](#provisioning)
  - [Google GKE](#google-gke)
    - [Application Dev](#application-dev)
    - [Provisioning](#provisioning-1)
1. [Cloud Security](#cloud-security)
  - [Identity and Access Management](#identity-and-access-management)
    - [OIDC Providers](#oidc-providers)
1. [Cloud-Native Application Development](#cloud-native-application-development)
  - [Go Development](#go-development)
    - [Microservices](#microservices-1)
  - [Open Source Software](#open-source-software)
    - [Reference Implementations](#reference-implementations)
1. [Cloud-Native Applications](#cloud-native-applications)
  - [Java Microservices](#java-microservices)
    - [Azure Container Apps](#azure-container-apps-1)
    - [Container Images](#container-images)
    - [Kubernetes Deployment](#kubernetes-deployment)
    - [Spring Cloud](#spring-cloud)
1. [Cloud-Native Infrastructure](#cloud-native-infrastructure)
  - [Kubernetes Core](#kubernetes-core)
    - [Cluster Access Security](#cluster-access-security)
    - [Container Deployments](#container-deployments)
    - [Declarative Templates](#declarative-templates)
    - [Storage Operations](#storage-operations)
    - [Workload Management](#workload-management)
  - [Learning Resources](#learning-resources)
    - [Containerization Workshops](#containerization-workshops)
    - [IaC](#iac)
    - [Kubernetes Courses](#kubernetes-courses)
    - [Kubernetes Playgrounds](#kubernetes-playgrounds)
    - [Kubernetes Workshops](#kubernetes-workshops)
1. [Cloud-Native Java](#cloud-native-java-1)
  - [Runtimes](#runtimes)
    - [JBoss EAP](#jboss-eap)
      - [MicroProfile](#microprofile)
1. [Container Orchestration](#container-orchestration)
  - [Kubernetes](#kubernetes-1)
    - [Application Migration](#application-migration-1)
    - [Java Deployment Guides](#java-deployment-guides)
1. [Containerization](#containerization-2)
  - [AWS ECS](#aws-ecs)
    - [JFrog Artifactory](#jfrog-artifactory)
  - [Docker](#docker-1)
    - [Prebuilt Images](#prebuilt-images)
  - [NGINX](#nginx)
    - [React Production](#react-production)
1. [Core Orchestration](#core-orchestration)
  - [Workloads](#workloads)
    - [Examples](#examples)
    - [Foundational](#foundational-1)
1. [Data Engineering](#data-engineering-1)
  - [Azure Data Factory](#azure-data-factory)
    - [CICD Pipelines](#cicd-pipelines-2)
  - [Event Streaming](#event-streaming)
    - [Change Data Capture](#change-data-capture)
1. [Data Science](#data-science)
  - [Tooling](#tooling)
    - [Data Wrangling](#data-wrangling)
1. [Data Storage](#data-storage)
  - [Databases](#databases)
    - [Operators](#operators)
1. [Database and Storage](#database-and-storage)
  - [Stateful Workloads](#stateful-workloads)
    - [PostgreSQL](#postgresql)
1. [DevOps](#devops)
  - [CICD](#cicd-1)
    - [GitHub Actions](#github-actions-2)
  - [CICD Platforms](#cicd-platforms)
    - [Jenkins](#jenkins-1)
      - [Azure DevOps Integration](#azure-devops-integration)
      - [Docker Containerization](#docker-containerization)
      - [GitHub Integration](#github-integration)
      - [Modular Pipeline Library](#modular-pipeline-library)
      - [Multibranch Pipelines](#multibranch-pipelines)
      - [Spring Petclinic Pipeline](#spring-petclinic-pipeline)
  - [Cloud Native CICD](#cloud-native-cicd)
    - [GitLab Integration](#gitlab-integration)
      - [Kubernetes Native Setup](#kubernetes-native-setup)
    - [Jenkins X](#jenkins-x)
      - [AWS EKS Integration](#aws-eks-integration)
  - [Continuous Delivery](#continuous-delivery)
    - [Infrastructure Provisioning](#infrastructure-provisioning)
      - [Crossplane Spinnaker Integration](#crossplane-spinnaker-integration)
    - [Spinnaker Setup](#spinnaker-setup)
      - [Kubernetes Deployment Models](#kubernetes-deployment-models)
      - [Kubernetes Native Deployment](#kubernetes-native-deployment)
      - [Orchestration Concepts](#orchestration-concepts)
      - [Orchestration Engines](#orchestration-engines)
  - [Environment Management](#environment-management)
    - [SDKMAN](#sdkman-1)
  - [Infrastructure as Code](#infrastructure-as-code)
    - [Jenkins Configuration as Code](#jenkins-configuration-as-code)
      - [Docker Hook Scripts](#docker-hook-scripts)
      - [Kubernetes Native Setup](#kubernetes-native-setup-1)
    - [Jenkins JobDSL](#jenkins-jobdsl)
      - [Freestyle Migration](#freestyle-migration)
  - [Kubernetes Integration](#kubernetes-integration)
    - [AWS EKS](#aws-eks-1)
      - [Jenkins Pipelines](#jenkins-pipelines-1)
  - [Observability](#observability)
    - [Metrics Collection](#metrics-collection)
      - [Grafana InfluxDB Integration](#grafana-influxdb-integration)
  - [Pipeline Execution Engine](#pipeline-execution-engine)
    - [Groovy CPS](#groovy-cps)
      - [Continuation Passing Style](#continuation-passing-style)
1. [DevOps and CICD](#devops-and-cicd)
  - [AWS EKS](#aws-eks-2)
    - [CodePipeline](#codepipeline)
  - [AWS Infrastructure](#aws-infrastructure)
    - [DevOps Guides](#devops-guides)
  - [Azure DevOps](#azure-devops)
    - [Build Automation](#build-automation-1)
    - [Infrastructure Governance](#infrastructure-governance)
    - [Onboarding Engine](#onboarding-engine)
    - [YAML Pipelines](#yaml-pipelines)
  - [Continuous Delivery](#continuous-delivery-1)
    - [Docker Images](#docker-images)
  - [Jenkins](#jenkins-2)
    - [Kubernetes Agents](#kubernetes-agents)
    - [Pipeline-as-Code](#pipeline-as-code)
1. [DevOps and Platform Engineering](#devops-and-platform-engineering)
  - [Infrastructure Automation](#infrastructure-automation)
    - [Academic Materials](#academic-materials)
  - [Interview Preparation](#interview-preparation)
    - [Reference Guides](#reference-guides)
  - [Learning Resources](#learning-resources-1)
    - [Methodologies](#methodologies)
  - [Project Blueprints](#project-blueprints)
    - [Infrastructure Showcase](#infrastructure-showcase)
1. [DevOps Philosophy](#devops-philosophy)
  - [Software Engineering](#software-engineering)
    - [No Code Movement](#no-code-movement)
1. [DevSecOps and Automation](#devsecops-and-automation)
  - [End-to-End Pipelines](#end-to-end-pipelines)
    - [Multi-Version Deployments](#multi-version-deployments)
  - [Jenkins-based CI-CD](#jenkins-based-ci-cd)
    - [AWS and Jenkins](#aws-and-jenkins)
    - [Jenkins Architecture](#jenkins-architecture)
    - [Jenkins Basics](#jenkins-basics)
    - [Jenkins Shared Libraries](#jenkins-shared-libraries)
    - [Mobile Workflows](#mobile-workflows)
1. [DevSecOps and IDEs](#devsecops-and-ides)
  - [Eclipse Che](#eclipse-che)
    - [Cloud IDE Templates](#cloud-ide-templates)
  - [Google Cloud Code](#google-cloud-code)
    - [Developer Experience](#developer-experience)
    - [Enterprise Templates](#enterprise-templates)
  - [Quality Assurance](#quality-assurance)
    - [Azure Cloud Testing](#azure-cloud-testing)
1. [Developer Experience](#developer-experience-1)
  - [Inner Loop Development](#inner-loop-development)
    - [Local Tooling](#local-tooling)
1. [Developer Tools](#developer-tools-1)
  - [Quarkus CLI](#quarkus-cli)
    - [Local Development](#local-development-3)
1. [Education](#education)
  - [Certification](#certification)
    - [CKAD](#ckad)
1. [Enterprise Architecture](#enterprise-architecture)
  - [Business Process Management](#business-process-management)
    - [RHPAM](#rhpam-1)
1. [Enterprise Integration](#enterprise-integration)
  - [SAP Cloud Integration](#sap-cloud-integration)
    - [Azure Blob Storage](#azure-blob-storage)
1. [Event-Driven Architectures](#event-driven-architectures)
  - [Cloud-Native Java](#cloud-native-java-2)
    - [Kafka with Spring Boot](#kafka-with-spring-boot)
  - [Go and CQRS](#go-and-cqrs)
    - [gRPC Microservices](#grpc-microservices)
  - [Observability and Diagnostics](#observability-and-diagnostics)
    - [Kafka at Scale](#kafka-at-scale)
  - [Realtime Streams](#realtime-streams)
    - [FastAPI and Ably](#fastapi-and-ably)
  - [Serverless Java](#serverless-java-1)
    - [Quarkus with Kafka](#quarkus-with-kafka)
1. [Extensibility](#extensibility)
  - [Admission Controllers](#admission-controllers)
    - [JVM Configurations](#jvm-configurations)
  - [Event-Driven](#event-driven-1)
    - [Webhooks](#webhooks)
1. [GitOps](#gitops-2)
  - [Continuous Deployment](#continuous-deployment)
    - [Flux v2](#flux-v2)
  - [OpenShift](#openshift-1)
    - [Enterprise Dev](#enterprise-dev)
1. [GitOps and Declarative Git](#gitops-and-declarative-git)
  - [Developer Platforms](#developer-platforms-1)
    - [GitHub Actions](#github-actions-3)
  - [Enterprise GitOps](#enterprise-gitops)
    - [Anthos](#anthos)
  - [GitOps Tools](#gitops-tools)
    - [Flux and Helm](#flux-and-helm)
1. [Governance and Security](#governance-and-security)
  - [Platform Comparisons](#platform-comparisons)
    - [OpenShift vs Kubernetes](#openshift-vs-kubernetes)
  - [Policy Enforcement](#policy-enforcement-1)
    - [OPA Gatekeeper](#opa-gatekeeper)
1. [Hybrid Cloud Platforms](#hybrid-cloud-platforms)
  - [Anthos](#anthos-1)
    - [Multi-Cluster Mesh](#multi-cluster-mesh)
  - [OpenShift](#openshift-2)
    - [Developer Workspaces](#developer-workspaces)
1. [Hybrid Cloud Solutions](#hybrid-cloud-solutions)
  - [Multi-Cloud Architectures](#multi-cloud-architectures)
    - [Anthos with EKS](#anthos-with-eks)
  - [Multi-Cluster GitOps](#multi-cluster-gitops-1)
    - [Anthos Config Management](#anthos-config-management)
1. [Infrastructure](#infrastructure-1)
  - [Artifact Management](#artifact-management)
    - [Nexus3 Deployment](#nexus3-deployment)
      - [Kubernetes Helm Setup](#kubernetes-helm-setup)
  - [Edge Computing](#edge-computing)
    - [Minimalist Clusters](#minimalist-clusters)
  - [Production Hardening](#production-hardening)
    - [Examples](#examples-1)
  - [Provisioning](#provisioning-2)
    - [High Availability](#high-availability-1)
  - [Stateful Applications](#stateful-applications)
    - [Mail Services](#mail-services)
1. [Infrastructure and DevOps](#infrastructure-and-devops)
  - [CI-CD Concepts](#ci-cd-concepts)
    - [Jenkins Tutorials](#jenkins-tutorials)
  - [Shared Libraries](#shared-libraries)
    - [Production Blueprints](#production-blueprints)
1. [Infrastructure and Operations](#infrastructure-and-operations)
  - [Cost Optimization and Metering](#cost-optimization-and-metering)
    - [Metering Operator](#metering-operator)
  - [Enterprise Cluster Management](#enterprise-cluster-management)
    - [OKD Community Platform](#okd-community-platform)
    - [Red Hat ACM](#red-hat-acm)
  - [Ingress and Routing](#ingress-and-routing)
    - [Argo CD Deployment](#argo-cd-deployment)
  - [Observability and Service Mesh](#observability-and-service-mesh)
    - [Grafana and ACM](#grafana-and-acm)
    - [OpenShift ServiceMesh](#openshift-servicemesh)
1. [Infrastructure and Platform](#infrastructure-and-platform)
  - [Autoscaling](#autoscaling)
    - [Event-Driven Scaling](#event-driven-scaling)
1. [Infrastructure as Code](#infrastructure-as-code-1)
  - [AI-Assisted IaC](#ai-assisted-iac)
    - [AKS and ACR Deployments](#aks-and-acr-deployments)
  - [Kubernetes Management](#kubernetes-management)
    - [Infrastructure Blueprints](#infrastructure-blueprints)
  - [OpenShift Virtualization](#openshift-virtualization)
    - [GitOps VMs](#gitops-vms)
  - [Serverless Deployment](#serverless-deployment)
    - [Terraform and AWS Lambda](#terraform-and-aws-lambda)
  - [Terraform](#terraform)
    - [AWS Networking](#aws-networking)
    - [Azure Security](#azure-security)
    - [GCP Provisioning](#gcp-provisioning)
  - [Terraform Ecosystem](#terraform-ecosystem)
    - [AWS Compute Provisioning](#aws-compute-provisioning)
    - [AWS RDS Databases](#aws-rds-databases)
    - [AWS S3 Storage](#aws-s3-storage)
    - [Advanced HCL Loopings](#advanced-hcl-loopings)
    - [Azure Deployments](#azure-deployments)
    - [Beginner Blueprints](#beginner-blueprints)
    - [EKS and IAM Security](#eks-and-iam-security)
    - [Fundamental Syntaxes](#fundamental-syntaxes)
    - [Kubernetes Provider](#kubernetes-provider)
    - [Learning Platforms](#learning-platforms)
1. [Infrastructure as Code and CI-CD](#infrastructure-as-code-and-ci-cd)
  - [Configuration Management](#configuration-management)
    - [Ansible](#ansible)
    - [Ansible Galaxy](#ansible-galaxy)
    - [Ansible Inventory](#ansible-inventory)
    - [Ansible Tower](#ansible-tower)
    - [Ansible Workshops](#ansible-workshops)
  - [Developer Platforms](#developer-platforms-2)
    - [CI-CD Pipelines](#ci-cd-pipelines)
  - [GitOps and Declarative Git](#gitops-and-declarative-git-1)
    - [Ansible and Helm](#ansible-and-helm)
1. [Java Cloud Native](#java-cloud-native)
  - [Spring Cloud](#spring-cloud-1)
    - [Kubernetes Integration](#kubernetes-integration-1)
1. [Kubernetes Tools](#kubernetes-tools)
  - [General Reference](#general-reference)
1. [Local Development](#local-development-4)
  - [Legacy Cluster Tools](#legacy-cluster-tools)
    - [Minishift](#minishift)
  - [Red Hat OpenShift Local](#red-hat-openshift-local)
    - [Installation](#installation)
    - [Process Automation](#process-automation-1)
1. [Networking](#networking)
  - [Ingress](#ingress)
    - [Nginx](#nginx)
  - [Multicluster](#multicluster)
    - [eBPF](#ebpf)
  - [Security](#security-1)
    - [Recipes](#recipes)
  - [eBPF](#ebpf-1)
    - [Calico](#calico)
1. [Observability](#observability-1)
  - [Microservices Telemetry](#microservices-telemetry)
    - [Grafana Stack](#grafana-stack)
  - [Monitoring](#monitoring)
    - [Message Brokers](#message-brokers)
  - [OpenTelemetry](#opentelemetry)
    - [Governance](#governance)
    - [Reliability Engineering](#reliability-engineering)
  - [Troubleshooting](#troubleshooting)
    - [Azure AKS](#azure-aks-1)
    - [Google GKE](#google-gke-1)
1. [Observability and Testing](#observability-and-testing-1)
  - [Metrics Monitoring](#metrics-monitoring)
    - [TPG Monitoring Stack](#tpg-monitoring-stack)
1. [Orchestration](#orchestration)
  - [AKS](#aks)
    - [Masterclass](#masterclass-1)
  - [Kubernetes](#kubernetes-2)
    - [EKS Training](#eks-training)
  - [Kubernetes Security](#kubernetes-security)
    - [RKE Best Practices](#rke-best-practices)
1. [Platform Architecture](#platform-architecture)
  - [CICD](#cicd-2)
    - [Legacy Jenkins](#legacy-jenkins)
1. [Platform Deployment](#platform-deployment)
  - [Quality Assurance](#quality-assurance-1)
    - [Static Code Analysis](#static-code-analysis)
1. [Platform Engineering](#platform-engineering)
  - [Architectural Insights](#architectural-insights)
    - [Ecosystem Tools](#ecosystem-tools)
    - [Red Hat Ecosystem](#red-hat-ecosystem)
  - [CICD Platforms](#cicd-platforms-1)
    - [Azure DevOps](#azure-devops-1)
  - [Custom Controller Patterns](#custom-controller-patterns)
    - [Kubernetes Operators](#kubernetes-operators)
  - [Enterprise Kubernetes](#enterprise-kubernetes)
    - [OpenShift](#openshift-3)
  - [GitOps and CI-CD](#gitops-and-ci-cd)
    - [AWS and Argo CD](#aws-and-argo-cd)
    - [Argo ApplicationSets](#argo-applicationsets)
    - [Argo CD and OpenShift Pipelines](#argo-cd-and-openshift-pipelines)
    - [Argo CD Basics](#argo-cd-basics)
    - [Argo CD Plugins](#argo-cd-plugins)
    - [Configuration Rollouts](#configuration-rollouts)
    - [GitLab Integration](#gitlab-integration-1)
    - [Multi-Cluster GitOps](#multi-cluster-gitops-2)
    - [Serverless Workflows](#serverless-workflows)
    - [Tool Assessment](#tool-assessment)
  - [GitOps and Deployment](#gitops-and-deployment)
    - [Flux Ecosystem](#flux-ecosystem)
  - [Machine Learning Operations](#machine-learning-operations)
    - [OpenShift AI](#openshift-ai)
1. [Provisioning](#provisioning-3)
  - [Bootstrapping](#bootstrapping)
    - [Bare Metal](#bare-metal)
1. [Public Cloud Providers](#public-cloud-providers)
  - [AWS](#aws-1)
    - [Amplify Development](#amplify-development)
    - [Asset Management](#asset-management)
    - [Best Practices](#best-practices)
    - [DevOps Demos](#devops-demos)
    - [Operational Excellence](#operational-excellence)
    - [Resource Tagging](#resource-tagging)
    - [Security and WAF](#security-and-waf)
    - [Training Archives](#training-archives)
  - [GCP](#gcp)
    - [Enterprise Platform](#enterprise-platform)
1. [Quality Assurance](#quality-assurance-2)
  - [API Testing Automation](#api-testing-automation)
    - [Newman Integration](#newman-integration)
      - [Jenkins Pipelines](#jenkins-pipelines-2)
1. [Reference Architectures](#reference-architectures)
  - [Artifact Registries](#artifact-registries)
    - [Docker Images](#docker-images-1)
  - [Enterprise Demos](#enterprise-demos)
    - [Community Repositories](#community-repositories)
    - [Red Hat Demo Central](#red-hat-demo-central)
  - [Industry Verticals](#industry-verticals)
    - [Healthcare](#healthcare)
  - [Interactive Learning](#interactive-learning)
    - [OpenShift Labs](#openshift-labs)
1. [Resource Portal](#resource-portal)
  - [Video Tutorials](#video-tutorials)
    - [Cloud PoC](#cloud-poc)
1. [Security](#security-2)
  - [Admission Control](#admission-control)
    - [Go Development](#go-development-1)
  - [Vulnerabilities](#vulnerabilities)
    - [Hacking Labs](#hacking-labs)
1. [Security and Compliance](#security-and-compliance-1)
  - [Cloud Security Assessments](#cloud-security-assessments)
    - [AWS IAM Exploits](#aws-iam-exploits)
1. [Security and Governance](#security-and-governance)
  - [Identity and Access](#identity-and-access)
    - [OpenShift GitOps](#openshift-gitops)
  - [Platform Security](#platform-security)
    - [GitOps Security](#gitops-security)
    - [Resource Integrity](#resource-integrity)
  - [Secret Management](#secret-management)
    - [Argo CD Plugins](#argo-cd-plugins-1)
1. [Serverless and Knative](#serverless-and-knative)
  - [Serverless Frameworks](#serverless-frameworks)
    - [Knative Serving](#knative-serving)
    - [Knative Tutorial](#knative-tutorial)
  - [Serverless Java](#serverless-java-2)
    - [Knative Service](#knative-service)
1. [Serverless Architectures](#serverless-architectures)
  - [AWS Lambda](#aws-lambda)
    - [Java Performance](#java-performance)
  - [AWS Serverless](#aws-serverless)
    - [Cloud-Native Demo](#cloud-native-demo)
  - [Knative](#knative)
    - [Spring Boot](#spring-boot-1)
1. [Service Mesh](#service-mesh)
  - [Consul](#consul)
    - [Ingress Gateways](#ingress-gateways)
    - [Local Development](#local-development-5)
  - [GitOps](#gitops-3)
    - [Progressive Delivery](#progressive-delivery)
  - [Istio](#istio)
    - [Hands-On](#hands-on)
1. [Software Development](#software-development)
  - [Microservices](#microservices-2)
    - [Reference Architecture](#reference-architecture)
      - [Spring Petclinic](#spring-petclinic)
      - [Spring Petclinic Red Hat](#spring-petclinic-red-hat)

## AI and Data Engineering

### Azure Container Apps

#### Terraform and OpenAI

  - **(2023)** [techcommunity.microsoft.com: Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit Chat App in Container Apps using Terraform | Paolo Salvatori](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/create-an-azure-openai-langchain-chromadb-and-chainlit-chat-app-in-container-app/3885602) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly relevant modern architecture integrating OpenAI services, vector stores (ChromaDB), and custom LangChain agents. Built entirely on Azure Container Apps with deployment orchestrations fully managed by Terraform templates.
## Application Architecture

### Event-Driven

#### GraphQL

  - **(2021)** [hasura.io: A Simple, Realtime, Event Driven Architecture with QR Codes](https://hasura.io/blog/a-simple-real-time-event-driven-architecture-with-qr-codes) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates the construction of a real-time QR generation microservice using Hasura's instant GraphQL engine and PostgreSQL event triggers. Illustrates stateless serverless handlers reacting to database write mutations in real-time.
## Application Delivery

### Asynchronous Messaging

#### Red Hat Fuse

  - **(2021)** [developers.redhat.com: Message broker integration made simple with Red Hat Fuse](https://developers.redhat.com/blog/2021/01/08/message-broker-integration-made-simple-with-red-hat-fuse) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Explores enterprise application integration patterns (EIP) utilizing Red Hat Fuse. Translates message formats, routes real-time data pipelines, and interfaces legacy middleware brokers with modern cluster queues.
### CICD Pipelines

#### Multi-Cluster Deployments

  - **(2020)** [alesnosek.com: CI/CD Pipeline Spanning Multiple OpenShift Clusters (jenkins & tekton)](https://alesnosek.com/blog/2020/06/30/ci-slash-cd-pipeline-spanning-multiple-openshift-clusters) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the architecture of CI/CD pipelines running across multiple isolated OpenShift environments. Contrasts Jenkins and Tekton setups, proposing patterns for safe environment transition and credential management.
#### Tekton Pipelines

  - **(2021)** [developers.redhat.com: Getting started with Tekton and Pipelines](https://developers.redhat.com/blog/2021/01/13/getting-started-with-tekton-and-pipelines) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A step-by-step developer guide on constructing custom Tekton pipelines. Guides engineers through defining Tasks, Pipelines, and trigger templates to translate software releases into managed Kubernetes resources.
  - **(2020)** [Build a Go application using OpenShift Pipelines](https://developers.redhat.com/blog/2020/05/26/build-a-go-application-using-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML / GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers through compiling and deploying Go applications on OpenShift Pipelines using Tekton. Outlines how to write Tasks, configure Workspaces, and trigger image builds securely within non-privileged containers.
  - **(2020)** [Set up continuous integration for .NET Core with OpenShift Pipelines](https://developers.redhat.com/blog/2020/09/24/set-up-continuous-integration-for-net-core-with-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML / C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated implementation guide for configuring CI pipelines for .NET Core projects using OpenShift Pipelines. Explores automated build testing, Nuget dependency resolution, and secure image registration.
  - **(2020)** [openshift.com: Guide to OpenShift Pipelines Part 1 - Introducing OpenShift Pipelines](https://www.redhat.com/en/blog/guide-to-openshift-pipelines-part-1-introducing-openshift-pipelines) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory deep-dive on OpenShift Pipelines. Explains how Tekton native Custom Resource Definitions (CRDs) abstract execution steps directly into the Kubernetes engine, removing the need for external tooling engines.
#### Tekton Tasks

  - **(2023)** [==OpenShift Pipelines Catalog==](https://github.com/openshift/pipelines-catalog) <span class='md-tag md-tag--info'>⭐ 52</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-33e948f8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 13 L 20 7 L 30 3 L 40 9 L 50 13" fill="none" stroke="url(#spark-grad-33e948f8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The central repository containing reusable Tekton Tasks and Pipelines optimized for OpenShift. Provides pre-built blocks for standard development patterns, including Git integration, Maven compilations, and SonarQube analyses.
#### Tekton Templates

  - **(2020)** [kailashyogeshwar.medium.com: How we implemented Reusable CI/CD Pipeline using Git and Tekton](https://kailashyogeshwar.medium.com/how-we-implemented-reusable-ci-cd-pipeline-using-git-and-tekton-503bed91975b) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on building highly reusable CI/CD pipelines on Git and Tekton. Demonstrates decoupling generic build parameters from execution manifests, allowing development teams to share pipelines easily across projects.
#### Workshops

  - **(2021)** [systemcraftsman/lab-tekton-pipelines: OpenShift Pipelines workshop](https://github.com/systemcraftsman/lab-tekton-pipelines) <span class='md-tag md-tag--info'>⭐ 1</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d1c341c6" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 2 L 20 10 L 30 8 L 40 10 L 50 7" fill="none" stroke="url(#spark-grad-d1c341c6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured hands-on workshop focused on OpenShift Pipelines (Tekton). Teaches engineers how to write tasks, manage resources, and deploy production-level continuous integration workflows.
### Containerization

#### Docker

  - **(2021)** [linuxtechlab.com: How to create a Dockerfile with some dockerfile examples](https://linuxtechlab.com/learn-create-dockerfile-example) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical walkthrough demonstrating how to construct secure, optimized, and multi-staged Dockerfiles. Discusses layer caching optimizations, base-image selection (e.g., Alpine vs. Debian), and security isolation options. (Live Grounding: Standard foundational knowledge that remains critical for building minimal, vulnerable-free runtime containers).
#### Self-Hosted Apps

  - **(2024)** [Mautic](https://github.com/mautic/docker-mautic) <span class='md-tag md-tag--warning'>[DOCKERFILE/SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Official Docker container setups for deploying Mautic, an open-source marketing automation platform, covering multi-container composition, persistent volumes, and database link configurations. (Live Grounding: A great example of migrating legacy monolithic PHP/MySQL stacks into structured OCI container configurations).
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
### Enterprise Modernization

#### Migration Toolkit

  - **(2020)** [Migration Toolkit for Applications: Getting Started](https://developers.redhat.com/products/mta/getting-started) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Guides teams in utilizing Red Hat’s Migration Toolkit for Applications (MTA) to analyze legacy Java frameworks for cloud compatibility. Identifies proprietary dependencies and reports on modernization pathways.
  - **(2020)** [Migration Toolkit for Applications Demo - June 2020](https://www.youtube.com/watch?v=mRCz6Jl0Ds8&feature=youtu.be)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video walkthrough showcasing the analysis, automated code scanning, and structural reporting metrics generated by the Migration Toolkit for Applications to expedite migration tasks.
#### Multi-Cluster Strategy

  - **(2021)** [openshift.com: Applications Here, Applications There! - Part 3 - Application Migration](https://www.redhat.com/en/blog/applications-here-applications-there-part-3-application-migration) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates strategies for migrating active application states and resource structures between hybrid and multi-cloud OpenShift clusters without losing critical metadata or transaction continuity.
### GitOps

#### Microservices Showcase

  - **(2020)** [rromannissen/rhoar-microservices-demo: GitOps for Microservices with Red' Hat Runtimes demo](https://github.com/rromannissen/rhoar-microservices-demo) <span class='md-tag md-tag--warning'>[JAVA / YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A demonstration repository featuring GitOps patterns for microservices configured with Red Hat Runtimes. Illustrates safe promotion processes and environment configuration syncing using Argo CD.
#### Multi-Cluster Deployments (1)

  - **(2020)** [openshift.com: GitOps Using Red Hat OpenShift Pipelines (Tekton) and Red Hat Advanced Cluster Management](https://www.redhat.com/en/blog/gitops-using-red-hat-openshift-pipelines-tekton-and-red-hat-advanced-cluster-management) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines unified continuous delivery architecture matching OpenShift Pipelines (Tekton) with Advanced Cluster Management (ACM). Explains how to integrate CI workflows with multi-cluster governance rules.
  - **(2020)** [openshift.com: GitOps Using Red Hat OpenShift Pipelines (Tekton) and Red Hat Advanced Cluster Management to Deploy on Multiple Clusters 🌟](https://www.redhat.com/en/blog/gitops-using-red-hat-openshift-pipelines-tekton-and-red-hat-advanced-cluster-management-to-deploy-on-multiple-clusters) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive architectural guide for deploying multi-cluster applications using OpenShift Pipelines (Tekton) and Advanced Cluster Management (ACM). Provides deep configuration plans to coordinate releases across hybrid environments.
#### Multi-Tenancy

  - **(2023)** [==cloud-native-toolkit/multi-tenancy-gitops 🌟==](https://github.com/cloud-native-toolkit/multi-tenancy-gitops) <span class='md-tag md-tag--info'>⭐ 120</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-beb6cc32" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 12 L 20 9 L 30 5 L 40 6 L 50 7" fill="none" stroke="url(#spark-grad-beb6cc32)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML / SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A production-grade toolkit mapping GitOps and Argo CD architectures onto multi-tenant Kubernetes clusters. Outlines secure separation patterns, namespace isolations, and policy sync mechanisms for scaling environments.
#### kam CLI

  - **(2021)** [developers.redhat.com: Bootstrap GitOps with Red Hat OpenShift Pipelines and kam CLI](https://developers.redhat.com/articles/2021/07/21/bootstrap-gitops-red-hat-openshift-pipelines-and-kam-cli) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates how to bootstrap secure GitOps setups on OpenShift using the GitOps Application Manager (kam) CLI. Standardizes repository structures to align application delivery pipelines with GitOps models.
### Java on Kubernetes

#### Eclipse JKube Tools

  - **(2021)** [Building and Deploying a Weather Web Application onto Kubernetes/Red Hat OpenShift using Eclipse JKube](https://itnext.io/building-and-deploying-a-weather-web-application-onto-kubernetes-red-hat-openshift-using-eclipse-62bf7c924be4) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores compiling and deploying Java-based web workloads to OpenShift clusters via Eclipse JKube. Demonstrates zero-configuration manifest generation and automated containerization workflows.
  - **(2021)** [youtube: Deploy your Java applications to the Cloud using Eclipse JKube (petclinic) 🌟](https://www.youtube.com/watch?v=vgIwRX4LXfU) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual demonstration deploying the classic Spring Petclinic Java web application using Eclipse JKube. Walks through target setups, Maven goals, and seamless image creation directly on Kubernetes.
### Load Balancing

#### High Availability

  - **(2021)** [dev.to: Build a highly available Node.js application using Docker, NGINX and AWS ELB](https://dev.to/sowmenappd/build-a-highly-available-node-js-application-using-docker-nginx-and-aws-elb-3cjp) <span class='md-tag md-tag--warning'>[JAVASCRIPT/SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed tutorial on architectural multi-tiering. Focuses on setting up a containerized Node.js application behind an NGINX reverse proxy, balanced globally by an AWS Elastic Load Balancer (ELB) for resilient target routing. (Live Grounding: Focuses on classic VM-to-container cloud architectures, forming a vital cognitive bridge before migrating entirely to Kubernetes Ingress/Gateway APIs).
## Application Development

### Base Images

#### Buildah

  - **(2021)** [developers.redhat.com: Build and store universal application images on OpenShift (with Buildah)](https://developers.redhat.com/articles/2021/11/18/build-and-store-universal-application-images-openshift) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive on compiling security-focused container images using Buildah on OpenShift. Highlights how Buildah bypasses Docker daemon requirements, maintaining tight compliance bounds and minimizing vulnerabilities in CI/CD environments.
#### Universal Base Image

  - **(2021)** [developers.redhat.com: Build lean Java containers with the new Red Hat Universal Base Images OpenJDK runtime images 🌟](https://developers.redhat.com/articles/2021/05/24/build-lean-java-containers-new-red-hat-universal-base-images-openjdk-runtime) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes how to compile slim Java runtime layers using Red Hat Universal Base Images (UBI) OpenJDK templates. Emphasizes security compliance, footprint reduction, and performance optimizations for enterprise microservice platforms.
### Cloud-Native Java

#### Advanced Microservices

  - **(2023)** [piomin/sample-spring-microservices-new: Microservices with Spring Cloud' Advanced Demo Project](https://github.com/piomin/sample-spring-microservices-new) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An updated showcase of modern, distributed architectures using the newest Spring Cloud dependencies. Features advanced setups including Spring Cloud Gateway, distributed tracing integrations, and resilient fault-tolerant design patterns.
#### Spring Boot Microservices

  - **(2022)** [piomin/sample-spring-microservices-kubernetes: Microservices with Spring' Boot and Spring Cloud on Kubernetes Demo Project - piotrminkowski.com 🌟](https://github.com/piomin/sample-spring-microservices-kubernetes) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active and highly referenceable demo project exhibiting the deployment of Spring Boot microservices inside a Kubernetes cluster. Utilizes Spring Cloud Kubernetes for discovery, ConfigMaps for configurations, and Ribbon/Feign client integrations for service-to-service communication.
### Containerization (1)

#### Java Spring Boot

  - **(2021)** [javatechonline.com: How To Deploy Spring Boot Application In Docker?](https://javatechonline.com/deploy-spring-boot-docker-spring-boot) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory walkthrough detailing how to containerize Java-based enterprise workloads. Focuses on constructing optimized Dockerfiles, multi-stage builds to minimize image footprint, and utilizing spring-boot-maven-plugin or buildpacks to generate production-ready container layers.
### Developer Tools

#### Alternative Tooling

  - **(2021)** [youtube: No YAML! Kubernetes done the easy way | DevNation Tech Talk](https://www.youtube.com/watch?v=jBDmX85IjLM&ab_channel=RedHatDeveloper) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A DevNation Tech Talk analyzing methods to abstract, simplify, or completely bypass manual YAML creation on Kubernetes. Reviews developer-friendly frameworks that translate code-based configurations directly into running containers.
### Enterprise Java Platforms

#### JBoss Foundations

  - **(2021)** [redhat.com: Getting started with JBoss](https://www.redhat.com/en/blog/getting-started-jboss) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical and architectural overview of JBoss, designed for enterprise Java architects. Explains how JBoss evolved from a heavyweight application server to modular setups optimized for modern virtual machines and enterprise containers.
### Java

#### Build Automation

  - **(2021)** [spring.io: YMNNALFT: Easy Docker Image Creation with the Spring Boot Maven Plugin and Buildpacks](https://spring.io/blog/2021/01/04/ymnnalft-easy-docker-image-creation-with-the-spring-boot-maven-plugin-and-buildpacks) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Spring technical guide illustrating optimized, multi-layer OCI container creation using the Spring Boot Maven Plugin. Deconstructs how Spring integrates Cloud Native Buildpacks directly, bypassing custom Dockerfiles to produce secure, cached, performance-optimized runtimes.
#### Local Development (1)

  - **(2020)** [piotrminkowski.com: Spring Boot on Kubernetes with Buildpacks and Skaffold 🌟](https://piotrminkowski.com/2020/12/18/spring-boot-on-kubernetes-with-buildpacks-and-skaffold) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — High-velocity development workflow blueprint leveraging Cloud Native Buildpacks and Skaffold to accelerate Java Spring Boot coding loops on Kubernetes. Minimizes manual Dockerfile maintenance and streamlines instantaneous hot-reloading code modifications into active development clusters.
#### Microservices Demo

  - **(2020)** [**redhat-actions/spring-petclinic**](https://github.com/redhat-actions/spring-petclinic) <span class='md-tag md-tag--info'>⭐ 4</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1ad3be1d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 10 L 20 11 L 30 2 L 40 11 L 50 12" fill="none" stroke="url(#spark-grad-1ad3be1d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Red Hat's enterprise fork of the classical Spring Petclinic microservice framework, tailored for deployment patterns on Red Hat OpenShift and vanilla Kubernetes. Showcases optimized Containerfile definitions and integrated automated CI/CD pipelines.
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
### Python

#### Django

  - **(2020)** [dev.to: Django on K8s (Part 0: Introduction)](https://dev.to/mkalioby/django-apps-on-kubernetes-2edo) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory guide addressing Django application architectures tailored specifically for Containerization. Explains initial configurations, environment separation, Dockerfile design practices, and the integration of database migration steps into standard container start routines.
#### Scalability

  - **(2021)** [digitalocean.com: How To Deploy a Scalable and Secure Django Application with Kubernetes](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-scalable-and-secure-django-application-with-kubernetes) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A definitive deployment manual demonstrating how to host, scale, and secure Python Django applications using Kubernetes. Explores decoupling static assets to object storage, wrapping backend gunicorn runtimes, orchestrating connection-pooled PostgreSQL services, and utilizing Secrets for environmental configuration safety.
### Reference Templates

#### OpenShift 4.8

  - **(2021)** [developers.redhat.com: New application samples in Red Hat OpenShift 4.8](https://developers.redhat.com/articles/2021/10/01/new-application-samples-red-hat-openshift-48) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces new application developer templates launched in OpenShift 4.8. Explains how developers can instantly import, test, and containerize various languages directly within the OpenShift developer GUI console.
### Runtimes and CMS

#### Strapi CMS

  - **(2021)** [developers.redhat.com: Containerize and deploy Strapi CMS applications on Kubernetes and Red Hat OpenShift](https://developers.redhat.com/blog/2021/04/09/containerize-and-deploy-strapi-applications-on-kubernetes-and-red-hat-openshift) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on containerizing and deploying Strapi CMS onto OpenShift. Addresses key development procedures, including environment variable injection, database routing, and mounting persistent directories for media assets.
### Serverless Java

#### Quarkus Integration

  - **(2020)** [Develop and test a Quarkus client on Red Hat CodeReady Containers with Red Hat Data Grid 8.0](https://developers.redhat.com/blog/2020/06/19/develop-and-test-a-quarkus-client-on-red-hat-codeready-containers-with-red-hat-data-grid-8-0) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers through testing a lightweight Quarkus application against Red Hat Data Grid (Infinispan) on Red Hat CodeReady Containers (now OpenShift Local). Emphasizes rapid developer iteration loops, memory minimization, and high-performance transactional caching.
#### gRPC Communication

  - **(2023)** [piotrminkowski.com: Introduction to gRPC with Quarkus](https://piotrminkowski.com/2023/09/15/introduction-to-grpc-with-quarkus) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the integration of low-latency gRPC services inside Quarkus. Demonstrates schema-first API creation via Protocol Buffers, building high-performance non-blocking streaming services, and optimizing binary communication interfaces for modern microservices.
### Tutorials

#### Developer Demos

  - **(2023)** [Red Hat Tutorials & Examples: github.com/redhat-developer-demos 🌟](https://github.com/redhat-developer-demos) <span class='md-tag md-tag--warning'>[JAVA / GO / NODE.JS CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main repository for Red Hat Developer developer demos. Offers a variety of quickstarts covering modern Java/Go runtimes, microservices integration, Kubernetes-native deployments, and pipeline automation designs.
## Application Migration

### Containerization Tools

#### Move2Kube

  - **(2023)** [Move2Kube](https://move2kube.konveyor.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on Move2Kube, a command-line utility within the Konveyor toolset designed to automate migration pathways. It analyzes configuration files from source environments (such as Docker Compose or Cloud Foundry) and auto-generates platform-ready Kubernetes manifests, Helm charts, and custom Tekton pipelines.
## Application Modernization

### Integration Frameworks

#### OpenShift and Camel

  - **(2021)** [developers.redhat.com: Modernizing applications with Apache Camel, JavaScript, and Red Hat OpenShift](https://developers.redhat.com/articles/2021/07/26/modernizing-applications-apache-camel-javascript-and-red-hat-openshift) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Examines legacy integration strategies and modern microservices orchestration utilizing Apache Camel K (native integrations) coupled with Node.js/JavaScript on Red Hat OpenShift. Discusses enterprise integration patterns (EIPs) within modern container systems.
### Spring to Quarkus

#### Framework Migration

  - **(2020)** [aytartana.wordpress.com: Migrating SpringBoot PetClinic REST to Quarkus](https://aytartana.wordpress.com/2020/08/26/migrating-springboot-petclinic-rest-to-quarkus) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed migration journal porting the classic Spring Boot PetClinic REST API to Quarkus. Provides valuable benchmarking metrics comparing memory footprints, startup latencies, and implementation adjustments required for compilation to GraalVM native images.
## Architecture

### Microservices

#### Demo Systems

  - **(2021)** [hbollon/k8s-voting-app-aws](https://github.com/hbollon/k8s-voting-app-aws) <span class='md-tag md-tag--info'>⭐ 34</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-dbb89f44" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 9 L 20 13 L 30 9 L 40 11 L 50 7" fill="none" stroke="url(#spark-grad-dbb89f44)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference multi-tier microservice architecture demonstrating AWS integration. Contains a polyglot microservice arrangement with Redis caches, PostgreSQL transactional engines, and reactive frontend layers structured for EKS deployments.
#### Design Patterns

  - **(2021)** [itnext.io: Journey Of A Microservice Application In The Kubernetes World](https://itnext.io/journey-of-a-microservice-application-in-the-kubernetes-world-bdfe795532ef) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive architectural case study outlining the functional lifecycle journey of a microservice application cluster inside Kubernetes. Details cross-cutting concerns including distributed service discovery, secret distribution, configurations management, ingress controllers, and decentralized persistent data handling.
## Artificial Intelligence and LLMs

### Prompt Engineering

#### Developer Productivity

  - **(2024)** [**Awesome NotebookLM Slide Prompts**](https://github.com/serenakeyitan/awesome-notebookLM-prompts) <span class='md-tag md-tag--info'>⭐ 3761</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1f241f0c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 13 L 20 2 L 30 2 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-1f241f0c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A master curation of system-level prompt templates specifically optimized for Google NotebookLM. It accelerates complex source material ingestions, contextual extractions, and structured summarizing processes for technical architects. (Live Grounding: Highlights the 2026 intersection of AI workflow orchestration and engineering documentation maintenance).
## CI-CD

### Azure

#### GitHub Actions

  - **(2020)** [youtube: Deploy Docker image to Kubernetes Cluster | CI-CD for Azure Kubernetes Service | Mohamed Radwan - DevOps](https://www.youtube.com/watch?v=4DUhc0MjdUc&feature=youtu.be&ab_channel=MohamedRadwan-DevOps) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video guide demonstrating a comprehensive CI/CD pipeline targeting Azure Kubernetes Service (AKS). Illustrates direct code integration, automatic container build pipelines inside GitHub Actions, security scanning, container registration inside ACR, and deployment using native Kubernetes manifests.
### Azure AKS

#### GitHub Actions (1)

  - **(2021)** [trstringer.com: Deploy to AKS from GitHub Actions 🌟](https://trstringer.com/deploy-to-aks-from-github-actions) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A precise deployment guide detailing continuous integration and deployment to AKS from GitHub Actions. Explores how to leverage secure Azure Service Principals and Federated Credentials (OIDC) to safely authenticate and update container workloads.
### Infrastructure

#### Rancher

  - **(2020)** [Deploy a Rancher Cluster with GitLab CI and Terraform](https://www.suse.com/c/rancher_blog/deploy-a-rancher-cluster-with-gitlab-ci-and-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step automation blueprint demonstrating how to provision and orchestrate Rancher multi-cluster control planes. Harnesses Terraform to scale target virtual machines and GitLab CI to deploy and maintain management-plane state configurations.
### Java (1)

#### Automated Workflows

  - **(2020)** [CI/CD for Kubernetes through a Spring Boot example (Banzai Cloud CI/CD)](https://teletype.in/@sravancynixit/CcwqFANxY) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Continuous Integration and Deployment guide utilizing Banzai Cloud automation pipelines for Spring Boot applications. Illustrates container building, secure credential handling, configuration injects, and blue-green application promotion tactics on Kubernetes.
### Platform-as-a-Service

#### OpenShift

  - **(2018)** [stackoverflow: How to define BuildConfig object with Jenkins and openshift](https://stackoverflow.com/questions/52337851/how-to-define-buildconfig-object-with-jenkins-and-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight addresses automated OpenShift build pipelines. Live Grounding details the precise YAML and Jenkins pipeline syntax needed to safely trigger BuildConfig objects from external CI nodes. It remains highly relevant for legacy Jenkins-to-OpenShift integrations.
## CICD

### GitLab CI

#### Pipeline Design

  - **(2022)** [about.gitlab.com: The basics of CI: How to run jobs sequentially, in parallel, or out of order](https://about.gitlab.com/blog/basics-of-gitlab-ci-updated) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical guide focused on configuring GitLab CI for advanced pipelines. Outlines steps to transition from basic sequential stages to highly optimized workflows utilizing Direct Acyclic Graphs (DAGs) and dynamic parallel task configurations.
### GitOps (1)

#### GitLab Agent

  - **(2022)** [about.gitlab.com: GitOps with GitLab: Connect with a Kubernetes cluster](https://about.gitlab.com/blog/gitops-with-gitlab-connecting-the-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step documentation detailing the setup of the GitLab Agent for Kubernetes. Provides secure pull-based GitOps workflows, ensuring real-time configuration sync and immediate cluster telemetry reporting to the GitLab enterprise console.
### Jenkins

#### Jenkins Pipeline Training

  - **(2020)** [experfy.com e-learning: Effective Jenkins - Continuous Delivery and Continuous Integration](https://training.experfy.com/courses/effective-jenkins-continuous-delivery-and-continuous-integration) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A training curriculum on writing robust continuous integration and continuous deployment scripts in Jenkins using declarative Groovy DSL syntax. Regarded as legacy compared to contemporary container-native declarative engine configurations.
#### Parallel Pipelines

  - **(2021)** [Using Jenkins Pipeline parallel stages to build Maven project with different JDKs](https://e.printstacktrace.blog/using-jenkins-pipeline-parallel-stages-to-build-maven-project-with-different-jdks) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A technical guide illustrating how to build a Maven project against multiple JDKs simultaneously using Jenkins parallel stages. Live Grounding highlights its architectural utility for modern engineering, ensuring system backward-compatibility and multi-runtime reliability during pipeline validation.
#### SDKMAN

##### Docker Integration

  - **(2021)** [**Using SDKMAN! as a docker image for Jenkins Pipeline - a step by step guide 🌟**](https://e.printstacktrace.blog/using-sdkman-as-a-docker-image-for-jenkins-pipeline-a-step-by-step-guide) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — This tutorial explains how to use SDKMAN! inside a Docker container within a Jenkins Declarative Pipeline to build Java projects using different compiler versions. Live Grounding highlights its architectural value, eliminating the need to maintain distinct runner VMs or complex custom Dockerfiles for each target JDK configuration.
## CICD and DevOps

### Enterprise Jenkins

#### OpenShift Integration

  - **(2020)** [developers.redhat.com: An easier way to create custom Jenkins containers in OpenShift 4 🌟](https://developers.redhat.com/blog/2020/06/04/an-easier-way-to-create-custom-jenkins-containers) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical deep-dive for enterprise platform engineers building custom, secure Jenkins master images for OpenShift 4. Outlines Red Hat universal base images (UBI) optimization and policy-compliant plugin packaging.
  - **(2020)** [OpenShift Pipelines with Jenkins Blue Ocean 🌟](https://www.redhat.com/en/blog/openshift-pipelines-jenkins-blue-ocean) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guide on utilizing Jenkins Blue Ocean inside Red Hat OpenShift to build visual representations of continuous integration pipelines. Integrates OpenShift buildconfigs with user-friendly visualization panels.
  - **(2020)** [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Public demonstration repository providing configured manifests for launching Jenkins Blue Ocean on OpenShift clusters. Acts as a blueprint for visualizing pipeline stages in Red Hat environments.
## CICD Infrastructure

### Build and Packaging

#### Custom Packager

  - **(2025)** [Jenkins Custom WAR Packager](https://github.com/jenkinsci/custom-war-packager) <span class='md-tag md-tag--info'>⭐ 87</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-eb9ca518" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 13 L 20 12 L 30 13 L 40 2 L 50 6" fill="none" stroke="url(#spark-grad-eb9ca518)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Duplicate citation verification for the Custom WAR Packager. Serves as the primary operational tool used to generate custom, pre-hardened enterprise Jenkins distributions tailored with pre-allocated configurations.
### Configuration as Code

#### Job Generation

  - **(2025)** [**How to create initial "seed" job**](https://github.com/jenkinsci/configuration-as-code-plugin) <span class='md-tag md-tag--info'>⭐ 2790</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f76bee31" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 11 L 20 7 L 30 10 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-f76bee31)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — An operational setup manual detailing how to bootstrap a primary seed job inside configuration-as-code files. This enables the controller to dynamically generate all subsequent projects automatically on initial server launch.
### Plugin Management

#### CLI Tooling

  - **(2025)** [Plugin Installation Manager Tool](https://github.com/jenkinsci/plugin-installation-manager-tool) <span class='md-tag md-tag--info'>⭐ 460</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-88782202" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 9 L 20 8 L 30 4 L 40 3 L 50 11" fill="none" stroke="url(#spark-grad-88782202)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A vital dependency management utility designed to download and package plugin bundles offline before launching controllers. Eradicates run-time dependency resolution issues inside restricted, isolated air-gapped container networks.
## CICD Pipeline

### Automation Ecosystems

#### Jenkins and Nexus

  - **(2019)** [Continuous Delivery with Sonatype Nexus, Jenkins and the Cloudogu Ecosystem](https://platform.cloudogu.com/en/blog/cd-with-nexus-jenkins-ces) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates a full CD pipeline design combining Jenkins automation pipelines, Sonatype Nexus artifact caching, and the Cloudogu developer platform ecosystem. It discusses how to decouple build outputs, secure package verification, and trigger orchestrations. It demonstrates how standardizing on artifact-centric builds minimizes drift in multi-environment configurations.
## CICD Pipeline Architecture

### Pipeline Testing

#### Local Execution

  - **(2025)** [Jenkinsfile Runner Test Framework](https://github.com/jenkinsci/jenkinsfile-runner-test-framework) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A dedicated integration test harness designed to systematically validate pipeline structures using localized Jenkinsfile Runner micro-runtimes. Ensures robust sanity checking without deploying configurations to dynamic server nodes.
#### Unit Testing

  - **(2025)** [**Jenkins Pipeline Unit testing framework**](https://github.com/jenkinsci/JenkinsPipelineUnit) <span class='md-tag md-tag--info'>⭐ 1585</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0d0aad12" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 8 L 20 7 L 30 10 L 40 8 L 50 5" fill="none" stroke="url(#spark-grad-0d0aad12)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The standard community pipeline testing toolkit. Simplifies verifying multi-step pipeline syntax, credential queries, and shared libraries within local mock environments, accelerating delivery validation times.
## CICD Pipelines (1)

### Automated Cloud Deployments

#### AWS ECS Deployments

  - **(2022)** [freecodecamp.org: How to Setup a CI/CD Pipeline with GitHub Actions and AWS](https://www.freecodecamp.org/news/how-to-setup-a-ci-cd-pipeline-with-github-actions-and-aws) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A detailed tutorial constructing CI/CD deployment pipelines on AWS. Uses GitHub Actions to build Docker images, securely push them to AWS ECR, and update application definitions across AWS ECS and Fargate infrastructure safely.
#### Kubernetes CD Pipelines

  - **(2023)** [nicwortel.nl: Continuous deployment to Kubernetes with GitHub Actions](https://nth-root.nl/en/guides/automate-kubernetes-deployments-with-github-actions) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A clear operational guide showcasing custom deployments to external Kubernetes clusters using GitHub Actions. Explains secure credential management, configuring kubectl contexts, and deploying applications with zero-downtime rolling updates.
### Automated Image Builds

#### Image Builder Workflows

  - **(2021)** [github.com/major/imagebuilder-containerized](https://github.com/major/imagebuilder-containerized/blob/main/.github/workflows/main.yml) <span class='md-tag md-tag--info'>⭐ 1</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-72c4b366" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 4 L 20 6 L 30 5 L 40 9 L 50 12" fill="none" stroke="url(#spark-grad-72c4b366)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An active GitHub Actions workflow blueprint orchestrating containerized OS image compilation. Demonstrates clean, multi-step pipeline actions to automatically package, build, and push customized bootable operating system images directly from GitHub.
### Automated Testing

#### Ephemeral K3s Cluster

  - **(2022)** [debianmaster/actions-k3s](https://github.com/debianmaster/actions-k3s) <span class='md-tag md-tag--info'>⭐ 109</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c19b33dd" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 13 L 20 5 L 30 11 L 40 3 L 50 3" fill="none" stroke="url(#spark-grad-c19b33dd)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A lightweight community action creating custom, ephemerally provisioned K3s Kubernetes instances directly within GitHub Actions runtime runner VMs. Extremely valuable for running end-to-end integration tests on fully functional clusters.
#### Pytest and GitHub Actions

  - **(2022)** [linkedin: Test Automation - How To Build a CI/CD Pipeline Using Pytest and GitHub Actions](https://www.linkedin.com/pulse/test-automation-how-build-cicd-pipeline-using-pytest-nir-tal) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to build automated validation checkpoints within GitHub Actions. Outlines the orchestration of Python-based Pytest test suites triggered on repository push, focusing on reliable quality gates and test reporting pipelines.
### Azure DevOps Solutions

#### GitHub Actions Integration

  - **(2023)** [docs.microsoft.com: Build and deploy applications to Azure by using GitHub Actions 🌟](https://learn.microsoft.com/en-us/training/modules/github-actions-cd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The canonical Microsoft Learning Module establishing standard pipelines for Azure. Outlines the design of multi-environment workflows, secrets isolation, security scanning, and deployment mechanisms targeting AKS and web workloads.
### Data Engineering

#### Automated Data Pipelines

  - **(2022)** [codeproject.com: Making a Simple Data Pipeline Part 4: CI/CD with GitHub Actions](https://www.codeproject.com/Articles/5320647/Making-a-Simple-Data-Pipeline-Part-4-CI-CD-with-Gi) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to wrap custom automated validation loops around analytical data collection platforms. Focuses on orchestrating deployments, executing scheduled task checks, and validating ingestion schemas using GitHub Actions workflows.
### Multi-Cluster GitOps

#### ArgoCD Orchestrations

  - **(2022)** [itnext.io: Github: Github Actions overview and ArgoCD deployment example](https://itnext.io/github-github-actions-overview-and-argocd-deployment-example-b6cf0cf6f832) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Bridges modern CI with GitOps CD workflows. Demonstrates a full software delivery pipeline where GitHub Actions automatically processes build phases and updates configuration repositories to trigger GitOps-driven deployment via ArgoCD.
### Security and Compliance

#### DevSecOps Integration

  - **(2022)** [judebantony.github.io: DevSecOps with GitHub Action and SaaS Tools](https://judebantony.github.io/cicd-github-action-example) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details a practical approach to modern DevSecOps pipeline construction. Highlights step-by-step additions of static application security testing (SAST), software composition analysis (SCA), and secrets auditing inside automated GitHub Actions runs.
#### GitHub Actions Security

  - **(2023)** [github.com/GitHubSecurityLab/actions-permissions: GitHub token permissions' Monitor and Advisor actions](https://github.com/GitHubSecurityLab/actions-permissions) <span class='md-tag md-tag--info'>⭐ 369</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e7f71c62" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 9 L 20 8 L 30 6 L 40 5 L 50 8" fill="none" stroke="url(#spark-grad-e7f71c62)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A pivotal security action from GitHub Security Lab designed to automatically audit, advise, and enforce least-privilege token policies in GitHub Actions workflows. Minimizes risks from repository injection and credential leaks.
## Cloud IoT

### Digital Twins

#### API Management

  - **(2020)** [==github.com/microsoft/azure-digital-twins-postman-samples==](https://github.com/microsoft/azure-digital-twins-postman-samples) <span class='md-tag md-tag--info'>⭐ 21</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c925976c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 6 L 20 6 L 30 5 L 40 7 L 50 8" fill="none" stroke="url(#spark-grad-c925976c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A collection of pre-configured Postman templates and environment schemas designed to test, model, and automate Azure Digital Twins API endpoints. Simplifies validation tasks across graph topology manipulation and event routing controls.
## Cloud Learning

### Curriculum

#### Cloud Engineering

  - **(2026)** [learntocloud.guide](https://learntocloud.guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An open-source, highly structured educational roadmap designed to transition traditional sysadmins into proficient cloud engineers. It guides learners through networking, Linux administration, infrastructure as code, and cloud-native topologies. Live grounding highlights its massive adoption within the DevOps community.
## Cloud Native

### Security

#### Policy Enforcement

  - **(2020)** [chrisns/k8s-opa-boilerplate](https://github.com/chrisns/k8s-opa-boilerplate) <span class='md-tag md-tag--info'>⭐ 18</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0c5edf9a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 2 L 20 7 L 30 5 L 40 13 L 50 6" fill="none" stroke="url(#spark-grad-0c5edf9a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[REGO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A minimal, highly instructional boilerplate repository demonstrating Open Policy Agent (OPA) integration inside Kubernetes using Gatekeeper. Helps bootstrap policy-as-code paradigms to secure deployments and enforce structural admission controls.
## Cloud Native Architecture

### Kubernetes

#### Fundamentals

  - **(2021)** [dyser/kubernetes-intro](https://github.com/dsyer/kubernetes-intro) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory educational repository containing configurations and setups for running basic Spring boot workloads in Kubernetes. Created by JVM leader Dave Syer, it provides minimal, clean manifests that demystify container networking and volumes. This repository remains a stable reference for those starting their cloud-native journey.
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

  - **(2024)** [**stefanprodan/podinfo**](https://github.com/stefanprodan/podinfo) <span class='md-tag md-tag--info'>⭐ 5917</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-afb540d1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 7 L 20 6 L 30 7 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-afb540d1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A premium go-to microservice web application written in Go, specifically designed to showcase best practices in Kubernetes deployment, health checking, instrumentation (Prometheus/Jaeger), and progressive delivery validation (such as Flagger/Istio canary releases).
## Cloud Native Platforms

### Red Hat OpenShift

#### Automation Grading

##### Academic Homework

  - **(2021)** [Grading Pipeline for OpenShift 4 Advanced Application Deployment Homework Assignment](https://github.com/redhat-gpte-devopsautomation/ocp4_app_deploy_homework_grading) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight frames this as a grading pipeline automated for assessing advanced application deployment homework on OpenShift 4. Live Grounding indicates it uses script-based compliance checks to programmatically evaluate multi-tier deployments. This architecture is valuable for automated environment auditing and continuous validation platforms.
#### Jenkins Pipelines

##### Deployment Automation

  - **(2019)** [github.com/gnunn1/openshift-basic-pipeline](https://github.com/gnunn1/openshift-basic-pipeline) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight highlights this duplicate resource as a persistent reference point for the basic OpenShift pipeline. Live Grounding reinforces that its utility lies in simple demonstrations of source-to-image (S2I) pipelines. It highlights the simplicity of legacy OpenShift-Jenkins plugins before the emergence of cloud-native Tekton workflows.
##### Lab Environments

  - **(2019)** [github.com/deweya/OpenShift-Jenkins-Lab](https://github.com/deweya/OpenShift-Jenkins-Lab) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight identifies this repository as a sandbox lab configuration for teaching Jenkins deployment patterns inside OpenShift clusters. Live Grounding confirms it provides hands-on instructions for configuring webhooks and build triggers. It serves as a structural blueprint for configuring self-contained pipeline demonstrations.
#### Local Development (2)

##### CodeReady Containers

  - **(2021)** [Red Hat CodeReady Containers (Minishift equivalent for OpenShift 4.2 or newer) - step-by-step demo guides](https://github.com/marcredhat/crcdemos) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight positions this project as a step-by-step demo guide for Red Hat CodeReady Containers (CRC), representing the modern equivalent of local Minishift. Live Grounding reveals CRC is an essential local development environment simulating multi-node OpenShift setups. The demos illustrate localized microservice deployment and validation before pushing to enterprise stages.
## Cloud Platform

### Microsoft Azure

#### Sample Architecture

  - **(2026)** [github.com/Azure-Samples 🌟](https://github.com/Azure-Samples) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Central directory of Azure engineering samples. Provides production-ready templates, deployment scripts, and reference implementations spanning Serverless, Azure Kubernetes Service, container orchestration, and multi-tenant systems.
## Cloud Providers

### AWS

#### Workshops (1)

  - **(2018)** [blog.openshift.com: AWS and red hat quickstart workshop](https://www.redhat.com/en/blog/aws-and-red-hat-quickstart-workshop) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical workshop manual detailing early CloudFormation blueprints for hosting OpenShift instances on AWS. Replaced entirely by contemporary ROSA (Red Hat OpenShift Service on AWS) implementations.
### AWS EKS

#### Foundational

  - **(2021)** [aws.amazon.com: Deploy a kubernetes application](https://docs.aws.amazon.com/eks/latest/userguide/sample-deployment.html) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official AWS documentation presenting core application deployment workflows on Amazon EKS. Walks through basic VPC considerations, creating standard manifests, exposing application services, and utilizing classic dynamic volume provisioning.
#### GitOps Tooling

  - **(2021)** [aws blogs: Git Push to Deploy Your App on EKS](https://aws.amazon.com/blogs/opensource/git-push-deploy-app-eks-gitkube) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the deployment of Gitkube on AWS Elastic Kubernetes Service (EKS) for git-push deployment mechanics. Historically useful for early rapid prototyping loops, though in 2026 this pattern is largely superseded by enterprise GitOps frameworks like Flux or ArgoCD.
#### Masterclass

  - **(2022)** [github.com/stacksimplify/aws-eks-kubernetes-masterclass 🌟](https://github.com/stacksimplify/aws-eks-kubernetes-masterclass) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extensive educational repository focusing on EKS operations. Showcases production patterns including IAM Roles for Service Accounts (IRSA), configuring AWS Load Balancer Controller, external DNS integrations, and persistent cluster volume setups.
#### Provisioning

  - **(2021)** [dzone: deploying a kubernetes cluster with amazon eks 🌟](https://dzone.com/articles/deploying-a-kubernetes-cluster-with-amazon-eks) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A guide detailing the deployment of Amazon Elastic Kubernetes Service clusters. Guides readers through VPC subnets subnet planning, configure public/private node isolation, security settings, and kubectl client integration.
### Google GKE

#### Application Dev

  - **(2021)** [github.com/MatthewCYLau: TypeScript Node Express Google Kubernetes Engine' (GKE)](https://github.com/MatthewCYLau/node-express-typescript-k8-gke) <span class='md-tag md-tag--info'>⭐ 11</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-409059fc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 6 L 30 10 L 40 2 L 50 10" fill="none" stroke="url(#spark-grad-409059fc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical developer bootstrap repository containing configurations to build, package, and orchestrate a containerized TypeScript Node Express API application on Google Kubernetes Engine (GKE) under standard ingress architectures.
#### Provisioning (1)

  - **(2021)** [github.com/MatthewCYLau: React App on Google Kubernetes Engine (GKE) with' Terraform](https://github.com/MatthewCYLau/gcp-react-gke-terraform) <span class='md-tag md-tag--info'>⭐ 15</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d472ff02" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 10 L 20 13 L 30 6 L 40 12 L 50 4" fill="none" stroke="url(#spark-grad-d472ff02)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Infrastructure-as-Code repository containing templates to construct a secure Google Kubernetes Engine (GKE) cluster via Terraform. Deploys an automated frontend React framework alongside its required networking and load balancing constructs.
## Cloud Security

### Identity and Access Management

#### OIDC Providers

  - **(2022)** [dev.to/aws-builders: From Scratch: OIDC Providers](https://dev.to/aws-builders/from-scratch-oidc-providers-252d) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the configuration of OpenID Connect (OIDC) providers to establish a trust relationship between multi-cloud workloads and AWS IAM. Discusses keyless authentication paradigms and JSON Web Token (JWT) validation without requiring long-lived access keys.
## Cloud-Native Application Development

### Go Development

#### Microservices (1)

  - **(2023)** [github.com/learning-cloud-native-go/myapp: Learning Cloud Native Go -' myapp 🌟](https://github.com/learning-cloud-native-go/myapp) <span class='md-tag md-tag--info'>⭐ 1093</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-5e282842" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 8 L 10 8 L 20 7 L 30 4 L 40 10 L 50 4" fill="none" stroke="url(#spark-grad-5e282842)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A reference Go application engineered specifically to demonstrate cloud-native design principles, featuring integrated telemetry endpoints, structured JSON logging, health probes (/healthz, /ready), and graceful termination handles. (Live Grounding: Serves as a textbook design blueprint for Golang microservices deployed within Kubernetes environments).
### Open Source Software

#### Reference Implementations

  - **(2021)** [todaywasawesome/oss-apps: OSS Applications](https://github.com/todaywasawesome/oss-apps) <span class='md-tag md-tag--warning'>[YAML/HELM CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A collection of production-ready, open-source application stack blueprints formatted for modern container and cloud platform environments. (Live Grounding: Serves as a reference baseline for application engineers evaluating functional cloud-native topologies).
## Cloud-Native Applications

### Java Microservices

#### Azure Container Apps (1)

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

#### Cluster Access Security

  - **(2020)** [blog.scottlowe.org: Using kubectl via an SSH Tunnel](https://blog.scottlowe.org/2020/06/16/using-kubectl-via-an-ssh-tunnel) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides step-by-step instructions for establishing secure SSH tunnels to reach private Kubernetes cluster control planes. Solves public exposure issues of the Kubernetes API server using proxy forwarding. (Live Grounding: Standard fallback security access pattern, often replaced by modern Zero Trust Network Access (ZTNA) brokers in larger companies).
#### Container Deployments

  - **(2020)** [codeburst.io: getting started with kubernetes, deploy a docker container in 5 minutes](https://codeburst.io/getting-started-with-kubernetes-deploy-a-docker-container-with-kubernetes-in-5-minutes-eb4be0e96370) <span class='md-tag md-tag--warning'>[YAML/SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A rapid prototyping guide targeting beginners to container orchestration, showcasing how to deploy an existing Docker container onto a Kubernetes cluster in under five minutes. (Live Grounding: Excellent for quick onboarding, though skips advanced security context configurations and networking rules).
#### Declarative Templates

  - **(2024)** [Kubernetes Examples](https://github.com/ContainerSolutions/kubernetes-examples) <span class='md-tag md-tag--info'>⭐ 1421</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3b90864a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 4 L 20 13 L 30 10 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-3b90864a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly utilized, production-tested blueprint repository containing foundational Kubernetes manifests. It spans standard ingress rules, complex stateful configurations, and container startup patterns. (Live Grounding: An essential reference repository for platform engineers bootstrapping cloud topologies with validated standards).
#### Storage Operations

  - **(2021)** [itnext.io: K8s raise StatefulSet volume size with low impact](https://itnext.io/k8s-raise-statefulset-volume-size-with-low-impact-33fe1e2576f6) <span class='md-tag md-tag--warning'>[YAML/SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A crucial operations guide detailing how to safely expand Persistent Volume Claims (PVCs) bound to StatefulSets with minimal workload impact. Covers volume expansion capability (VolumeExpansion) within storage classes and live file-system resizing. (Live Grounding: Fundamental knowledge for running high-throughput production databases without service degradation).
#### Workload Management

  - **(2021)** [howtoforge.com: How to create a Deployment in Kubernetes](https://www.howtoforge.com/create-a-deployment-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step procedural tutorial explaining the structure of a standard Kubernetes Deployment manifest, dynamic replica scaling, and seamless rollout update strategies. (Live Grounding: Fundamental foundational knowledge for setting up standard declarative app workloads).
### Learning Resources

#### Containerization Workshops

  - **(2022)** [github.com/kubernetes-course/container_workshops](https://github.com/kubernetes-course/container_workshops) <span class='md-tag md-tag--warning'>[SHELL/DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Workshop curriculum dedicated to fundamental container internals, isolation concepts, namespaces, and runtime interactions. (Live Grounding: Serves as an excellent fundamental base for engineers seeking to demystify low-level OCI runtime mechanisms).
#### IaC

  - **(2025)** [github.com/wardviaene (kubernetes, terraform, ansible, docker, etc) 🌟](https://github.com/wardviaene) <span class='md-tag md-tag--warning'>[HCL/YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A public code profile hosting highly referenceable configuration setups across Terraform, Ansible, Docker, and Kubernetes. The repositories serve as companion code for prominent DevOps bootcamps, detailing clean infrastructure-as-code patterns. (Live Grounding: Continually referenced by global practitioners transitioning to cloud infrastructure specialties).
#### Kubernetes Courses

  - **(2024)** [**wardviaene/kubernetes-course**](https://github.com/wardviaene/kubernetes-course) <span class='md-tag md-tag--info'>⭐ 1732</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-9d6612bb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 12 L 20 8 L 30 9 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-9d6612bb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML/GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Accompanying codebase for Ward Viaene's comprehensive Kubernetes course, demonstrating deployments, configurations, microservice communication patterns, and cloud migrations. (Live Grounding: Widely trusted community-backed repository illustrating production-grade YAML configurations).
#### Kubernetes Playgrounds

  - **(2025)** [Free Kubernetes 🌟🌟](https://github.com/learnk8s/free-kubernetes) <span class='md-tag md-tag--info'>⭐ 1158</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-03206234" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 10 L 20 9 L 30 3 L 40 3 L 50 4" fill="none" stroke="url(#spark-grad-03206234)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly-rated index of free Kubernetes sandboxes, development clusters, managed trials, and learning environments. Designed to lower the financial entry barrier for developers. (Live Grounding: Continually updated to include current free tiers, allowing quick architectural sandboxing without infrastructure bills).
#### Kubernetes Workshops

  - **(2021)** [github.com/eon01/kubernetes-workshop](https://github.com/eon01/kubernetes-workshop) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Hands-on introductory workshop materials covering fundamental Kubernetes concepts, including Pods, Services, Deployments, and ingress controller definitions. (Live Grounding: Solid reference for classroom-based learning or self-paced platform orchestration upskilling).
  - **(2020)** [Kubernetes workshop in a box](https://archive.kabisa.nl/tech/k8s-workshop-in-a-box) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — An archival portal hosting a self-contained, offline-capable 'Kubernetes Workshop in a Box.' Designed to run interactive tutorials without reliable internet connections. (Live Grounding: While some container tooling patterns are archived, the offline structure is a highly referenced model for local development isolation).
## Cloud-Native Java (1)

### Runtimes

#### JBoss EAP

##### MicroProfile

  - **(2020)** [developers.redhat.com: Red Hat JBoss Enterprise Application Platform expansion pack 1.0 (JBoss EAP XP) released](https://developers.redhat.com/blog/2020/06/17/red-hat-jboss-enterprise-application-platform-expansion-pack-1-0-released) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The release announcement for Red Hat JBoss EAP Expansion Pack (XP) 1.0, enabling support for MicroProfile specifications on top of enterprise application servers. Live Grounding indicates JBoss EAP XP has become a core element for Red Hat customers modernization strategies, providing a bridge between traditional and cloud-native application patterns.
## Container Orchestration

### Kubernetes (1)

#### Application Migration (1)

  - **(2018)** [github.com/paulczar/k8s-spring-petclinic](https://github.com/paulczar/k8s-spring-petclinic) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — An archived community demonstration showing the deployment of the legacy Spring PetClinic application to raw Kubernetes. Utilizes direct YAML manifests and basic service discovery, serving as a historical baseline for modern Helm/Kustomize deployments.
#### Java Deployment Guides

  - **(2018)** [tech.paulcz.net/blog/spring-into-kubernetes-part-1](https://tech.paulcz.net/blog/spring-into-kubernetes-part-1) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational blog post walking through the process of containerizing and deploying a Spring Boot application onto a Kubernetes cluster. Details the transition from local JAR execution to containerized environments, highlighting early JVM memory footprint challenges.
## Containerization (2)

### AWS ECS

#### JFrog Artifactory

  - **(2020)** [jfrog.com: 5 Steps to Hosting Your Application on Amazon Cloud Container Service](https://jfrog.com/blog/5-steps-to-hosting-your-application-on-amazon-cloud-container-service) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the fundamentals of deploying containerized applications into Amazon Elastic Container Service (ECS). Emphasizes secure image registry integration using JFrog Artifactory as a secure staging area.
### Docker (1)

#### Prebuilt Images

  - **(2023)** [ref 5 arey/springboot-petclinic](https://hub.docker.com/r/arey/springboot-petclinic) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly pulled, community-maintained Spring Boot Petclinic image optimized for lean runtimes. Includes built-in multi-architecture CPU support (ARM64/AMD64) ideal for localized testing and local Kubernetes clusters.
  - **(2020)** [ref 3](https://hub.docker.com/r/bmoussaud/petclinic) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Docker image for the Spring Petclinic application instrumented with APM and monitoring agents. Useful for evaluating telemetry collection, performance profiling, and tracing agents inside isolated container runs.
  - **(2019)** [ref 2](https://hub.docker.com/r/sarjunkumar24391/petclinic) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A community-packaged Docker image of the classic Spring Petclinic application. Created primarily to facilitate rapid deployment testing on container runtimes without local Maven compilation overhead.
  - **(2018)** [ref 6](https://hub.docker.com/r/anthonydahanne/spring-petclinic) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Historical community Docker image containing early builds of the Spring Petclinic framework. Used primarily for legacy workshop labs and testing Docker runtime backwards compatibility.
  - **(2015)** [ref 7](https://hub.docker.com/r/jbrisbin/spring-petclinic) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — One of the oldest legacy Docker images of the Spring PetClinic project. Demonstrates early containerization methodologies using heavy base operating system layers and older Java Virtual Machine (JVM) versions.
### NGINX

#### React Production

  - **(2023)** [freecodecamp.org: How to Deploy a React App to Production Using Docker and NGINX with API Proxies](https://www.freecodecamp.org/news/how-to-deploy-react-apps-to-production) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep guide details how to bundle React applications into high-performance production Docker images using multi-stage builds. Implements security headers and API reverse proxy routing directly within NGINX configs.
## Core Orchestration

### Workloads

#### Examples

  - **(2022)** [github.com/AdminTurnedDevOps/kubernetes-examples](https://github.com/AdminTurnedDevOps/kubernetes-examples) <span class='md-tag md-tag--info'>⭐ 755</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-f71c6b1d" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 7 L 20 13 L 30 10 L 40 9 L 50 13" fill="none" stroke="url(#spark-grad-f71c6b1d)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A clean, community-curated collection of fundamental manifest configurations. Serves as a useful rapid-lookup repository containing validated yaml schemas for Deployments, ConfigMaps, Secrets, Ingress, and persistent volume abstractions.
#### Foundational (1)

  - **(2021)** [howtoforge.com: How to deploy your first pod on a Kubernetes Cluster](https://www.howtoforge.com/how-to-deploy-your-first-pod-on-a-kubernetes-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Foundational technical walkthrough outlining the basic architecture of Pod components. Demystifies core scheduling mechanisms, declaring multi-container environments, configuring volumes, and validating basic cluster reachability for initial workload tests.
## Data Engineering (1)

### Azure Data Factory

#### CICD Pipelines (2)

  - **(2021)** [doylestowncoder.com: Building CI/CD Pipelines with Azure Data Factory: Part 1](https://travelrasik.com/category/asia) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Multi-part technical walk-through detailing automated deployment patterns for Azure Data Factory (ADF) pipelines. Highlights ARM template generation, parameterization strategies, and continuous integration workflows via Azure DevOps.
### Event Streaming

#### Change Data Capture

  - **(2022)** [itnext.io: Hydrating a Data Lake using Log-based Change Data Capture (CDC) with Debezium, Apicurio, and Kafka Connect on AWS](https://itnext.io/hydrating-a-data-lake-using-log-based-change-data-capture-cdc-with-debezium-apicurio-and-kafka-799671e0012f) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-density technical architecture study detailing data lake hydration. Coordinates Kafka Connect, Debezium, Apicurio schema registry, and AWS S3 to capture schema-validated database logs in near real-time.
## Data Science

### Tooling

#### Data Wrangling

  - **(2023)** [**Getting Started with Data Wrangler in VS Code**](https://code.visualstudio.com/docs/datascience/data-wrangler) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight outlines VS Code's visual data preparation extension. Live Grounding shows that Data Wrangler bridges the visual gap in exploratory data analysis (EDA), generating reproducible Python code in Pandas and Polars dialects directly inside Jupyter environments.
## Data Storage

### Databases

#### Operators

  - **(2021)** [blog.flant.com: Our experience with Postgres Operator for Kubernetes by Zalando](https://palark.com/blog/our-experience-with-postgres-operator-for-kubernetes-by-zalando) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analytical review assessing operational outcomes using Zalando's PostgreSQL Operator in high-throughput environments. Investigates performance metrics, replication latency under Patroni-driven clustering, backup and recovery operations (WAL-G/S3), dynamic volume expansion, and node failure scenarios.
## Database and Storage

### Stateful Workloads

#### PostgreSQL

  - **(2020)** [Deploying PostgreSQL in MiniShift/OpenShift 3](https://www.dbi-services.com/blog/deploying-postgresql-in-minishiftopenshift) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides users through deploying PostgreSQL on Minishift/OpenShift 3, highlighting standard volume mounting processes. Due to the deprecation of both OpenShift 3 and Minishift, modern applications utilize OpenShift Local and PostgreSQL Operator frameworks.
## DevOps

### CICD (1)

#### GitHub Actions (2)

  - **(2021)** [thomasthornton.cloud: If, elseif or else in GitHub Actions](https://thomasthornton.cloud/if-elseif-or-else-in-github-actions) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This architectural guide details the execution of complex conditional routing syntax (if-elif-else) within GitHub Actions workflows. It highlights the evaluation patterns of workflow-level expressions, env-context variables, and pipeline optimization mechanics.
### CICD Platforms

#### Jenkins (1)

##### Azure DevOps Integration

  - **(2020)** [youtube: CI CD Pipeline Using Jenkins | Continuous Integration and Deployment using Azure Devops | K21Academy](https://www.youtube.com/watch?v=LhB8-sAx3pM&ab_channel=K21Academy) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight highlights this video tutorial as a walkthrough for establishing baseline CI/CD pipelines using Jenkins alongside Azure DevOps. Live Grounding indicates that while Jenkins remains prevalent for legacy enterprise systems, modern engineering in 2026 has transitioned toward cloud-native GitOps paradigms. The tutorial provides foundational knowledge on orchestrating build-test-deploy cycles across heterogeneous cloud landscapes.
##### Docker Containerization

  - **(2020)** [liatrio.com: building with docker using jenkins pipelines](https://www.liatrio.ai/resources/blog) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the methodologies for assembling and building container images from within a Jenkins declarative pipeline execution block. Live Grounding indicates that using modern agent strategies (such as Kaniko or podman) has superseded dind (Docker in Docker) configurations to secure enterprise clusters. This post offers foundational Docker container pipeline strategies.
  - **(2018)** [github.com/arun-gupta/docker-jenkins-pipeline: Docker + Java + Jenkins Pipeline](https://github.com/arun-gupta/docker-jenkins-pipeline) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight structures this repository around running Docker-integrated Java application compilation inside Jenkins Pipelines. Live Grounding shows that mounting the Docker socket inside Jenkins agents remains a common albeit security-sensitive approach. It serves as a historical and practical reference for building containerized Java workloads using declarative pipelines.
##### GitHub Integration

  - **(2020)** [towardsdatascience.com: Create your first CI/CD pipeline with Jenkins and GitHub](https://towardsdatascience.com/create-your-first-ci-cd-pipeline-with-jenkins-and-github-6aefe21c9240) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight identifies this article as a starter guide for constructing initial CI/CD pipelines bridging GitHub with a Jenkins instance. Live Grounding indicates it relies on standard webhook configurations and SSH deployment keys. This resource serves as an educational baseline for engineers learning automated testing integration.
##### Modular Pipeline Library

  - **(2021)** [==griddynamics/mpl==](https://github.com/griddynamics/mpl) <span class='md-tag md-tag--info'>⭐ 165</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8548b813" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 2 L 20 10 L 30 7 L 40 11 L 50 4" fill="none" stroke="url(#spark-grad-8548b813)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight presents the Modular Pipeline Library (MPL) from Grid Dynamics as a tool for creating clean, maintainable Jenkins pipelines. Live Grounding confirms that MPL significantly reduces Groovy boilerplate by introducing modular execution configurations and reusable testing frameworks. This represents an exceptionally scalable design pattern for large-scale enterprise environments.
  - **(2021)** [youtube: Modular Pipeline Library: 4. Petclinic Pipeline 🌟](https://www.youtube.com/watch?v=GLtvxY1S3Aw) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights this video showcase mapping the Modular Pipeline Library (MPL) against a real-world Petclinic continuous integration execution flow. Live Grounding validates that illustrating modular configuration structures gives developers a tangible example of pipeline inheritance. This pattern minimizes repetitive pipeline coding efforts across diverse teams.
##### Multibranch Pipelines

  - **(2023)** [lambdatest.com: How To Create Jenkins Multibranch Pipeline 🌟](https://www.testmuai.com/blog/how-to-create-jenkins-multibranch-pipeline) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details this guide as a step-by-step approach to configuring Jenkins Multibranch Pipelines for automated branch detection. Live Grounding emphasizes that Multibranch setups are highly robust for complex git workflows, automatically provisioning pipeline branches. This architectural pattern prevents manual job pollution and ensures consistent integration testing across feature branches.
##### Spring Petclinic Pipeline

  - **(2020)** [deors/deors-demos-petclinic jenkinsfile](https://github.com/deors/deors-demos-petclinic/blob/master/Jenkinsfile) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details a functional Jenkinsfile built specifically to build and compile the Spring Petclinic application. Live Grounding illustrates how multi-stage Docker builds can be integrated cleanly within a declarative Jenkins template to produce production-ready container images. It is a highly practical execution reference.
### Cloud Native CICD

#### GitLab Integration

##### Kubernetes Native Setup

  - **(2020)** [piotrminkowski.com: GitLab CI/CD on Kubernetes](https://piotrminkowski.com/2020/10/19/gitlab-ci-cd-on-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight features this comprehensive guide for establishing GitLab CI/CD pipelines running directly inside Kubernetes. Live Grounding reveals GitLab's Kubernetes runners are incredibly popular due to their low overhead and high-density container scheduling. It represents an excellent alternative architecture to Jenkins.
#### Jenkins X

##### AWS EKS Integration

  - **(2021)** [Modernize Your CI/CD Pipeline Using Jenkins X with Amazon EKS](https://aws.amazon.com/blogs/apn/modernize-your-ci-cd-pipeline-using-jenkins-x-with-amazon-eks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight shares an AWS APN blog focusing on modernizing pipelines using Jenkins X with Amazon EKS. Live Grounding clarifies that Jenkins X differs entirely from classic Jenkins, utilizing Tekton, GitOps, and Kubernetes-native configurations under the hood. It acts as an instructional benchmark for organizations moving toward declarative development environments.
### Continuous Delivery

#### Infrastructure Provisioning

##### Crossplane Spinnaker Integration

  - **(2021)** [amazon.com: Declarative provisioning of AWS resources with Spinnaker and Crossplane](https://aws.amazon.com/blogs/opensource/declarative-provisioning-of-aws-resources-with-spinnaker-and-crossplane) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight showcases the declarative provisioning of AWS infrastructure using Spinnaker unified with Crossplane. Live Grounding shows that combining Crossplane's Kubernetes Control Plane model with Spinnaker's application pipelines represents an advanced platform engineering paradigm. This enables application developers to spin up dependencies dynamically without custom script hooks.
#### Spinnaker Setup

##### Kubernetes Deployment Models

  - **(2020)** [wardviaene/advanced-kubernetes-course/spinnaker 🌟](https://github.com/wardviaene/advanced-kubernetes-course/tree/master/spinnaker) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight points to a companion repository for an advanced Kubernetes Spinnaker course. Live Grounding emphasizes its utility in demonstrating advanced deployment strategies (such as blue-green and canary analysis) directly inside Kubernetes clusters using Spinnaker's pipeline GUI. It remains a reliable hands-on learning lab.
  - **(2020)** [imperialwicket/spinnaker-demo](https://github.com/imperialwicket/spinnaker-demo) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents this repository as a demo application configuration designed to show basic pipeline execution within Spinnaker. Live Grounding highlights that configuring Spinnaker's cloud drivers and halyard configurations is notoriously challenging, and this repo provides valuable baseline configurations to bypass common initial setup hurdles.
##### Kubernetes Native Deployment

  - **(2019)** [hackernoon: Using Spinnaker with Kubernetes for CI/CD](https://hackernoon.com/using-spinnaker-with-kubernetes-for-cicd-52w3uo9) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight outlines utilizing Spinnaker's cloud native engine as an external continuous delivery pipeline for Kubernetes applications. Live Grounding validates that separating build execution (CI) from application delivery (CD) using a dedicated tool like Spinnaker prevents pipeline scaling bottlenecks. This pattern decouples deployment safety from runner nodes.
##### Orchestration Concepts

  - **(2019)** [codeburst.io: Spinnaker by Example: Part 1](https://codeburst.io/spinnaker-by-example-part-1-c4de9180d689) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight targets the first installment of a practical multi-part series exploring foundational Spinnaker patterns. Live Grounding points to this series as a highly detailed breakdown of pipelines, stages, and execution models. It is highly recommended for understanding Spinnaker's state machine execution logic.
  - **(2019)** [codeburst.io: Spinnaker by Example: Part 2](https://codeburst.io/spinnaker-by-example-part-2-6f92a1fdaedf) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight covers the second installment of 'Spinnaker by Example', shifting focus toward manual judgements and validation triggers. Live Grounding confirms that incorporating human gates into automated delivery pathways is crucial for enterprise governance. The examples remain valuable for compliance-focused teams.
  - **(2019)** [codeburst.io: Spinnaker by Example: Part 3](https://codeburst.io/spinnaker-by-example-part-3-c6ed9ac5f8ce) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight details the third installment of the series, showing advanced stage configurations and automated rollback procedures. Live Grounding validates that automated rollback on application health degradation is Spinnaker's premier capability. This design pattern minimizes production downtime during problematic deployments.
##### Orchestration Engines

  - **(2022)** [Demo/Evaluation Installations](https://spinnaker.io/docs/setup/install) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight covers the official installation and evaluation setup parameters for Spinnaker. Live Grounding shows Spinnaker remains a highly sophisticated CD platform designed for multi-cloud deployments, though its complex architecture makes it less popular for lightweight Kubernetes setups compared to modern GitOps tools. It is best suited for legacy VM and complex cluster canary rollouts.
### Environment Management

#### SDKMAN (1)

  - **(2026)** [==SdkMan==](https://sdkman.io) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The homepage for SDKMAN!, a command-line tool designed to manage parallel versions of multiple Software Development Kits, with a strong focus on the JVM ecosystem. Live Grounding confirms it as the definitive tool for local environments, facilitating zero-friction switches between different Java, Maven, Gradle, and Scala runtimes.
### Infrastructure as Code

#### Jenkins Configuration as Code

##### Docker Hook Scripts

  - **(2021)** [==Demo of Jenkins Configuration-As-Code with Docker and Groovy Hook Scripts (java11-support branch) 🌟🌟==](https://github.com/oleg-nenashev/demo-jenkins-config-as-code/tree/java11-support) <span class='md-tag md-tag--info'>⭐ 173</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-973f87d2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 10 L 20 2 L 30 9 L 40 3 L 50 4" fill="none" stroke="url(#spark-grad-973f87d2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight presents this demo of Jenkins Configuration-as-Code (JCasC) utilizing Docker and Groovy hook scripts. Live Grounding confirms JCasC has revolutionized Jenkins operations by defining configurations within declarative YAML. The inclusion of Java 11 support hooks ensures robust security and plug-in stability in enterprise automation environments.
##### Kubernetes Native Setup (1)

  - **(2021)** [Jenkins Configuration as Code on Kubernetes 🌟](https://github.com/nubenetes/jenkins-CasC-kubernetes-demo) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights this Nubenetes demo as a primary method for running JCasC on Kubernetes. Live Grounding confirms its effectiveness in eradicating persistent storage drift by configuring dynamic build agents via YAML definitions. This serves as an outstanding baseline architecture for cloud-native Jenkins execution environments.
  - **(2020)** [Configuration as Code of Jenkins (for Kubernetes) 🌟🌟](https://github.com/figaw/configuration-as-code-jenkins-k8s) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight points to this resource for implementing Jenkins Configuration as Code on Kubernetes. Live Grounding shows that by mapping JCasC YAML onto Kubernetes ConfigMaps, administrators can fully decouple configuration state from ephemeral container lifecycles. This practice mitigates drift and enables rapid restoration in disaster recovery scenarios.
#### Jenkins JobDSL

##### Freestyle Migration

  - **(2020)** [Meetup event: From Freestyle jobs to Pipeline, with JobDSL](https://www.meetup.com/jenkins-online-meetup/events/270600737) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight hosts a comprehensive migration strategy moving legacy manual Freestyle jobs to programmatic JobDSL configurations. Live Grounding indicates that transitioning to JobDSL represents a crucial step toward fully declarative pipelines. The repository outlines reproducible seed jobs that dynamically provision child pipelines with minimal manual intervention.
### Kubernetes Integration

#### AWS EKS (1)

##### Jenkins Pipelines (1)

  - **(2021)** [youtube: How to set up AWS Kubernetes Jenkins pipeline](https://www.youtube.com/watch?v=zI7_8M2KtRI&ab_channel=MicroserviceFactory) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents this video guide as a roadmap to deploying and running Jenkins pipelines on AWS EKS Kubernetes clusters. Live Grounding highlights the use of IAM Roles for Service Accounts (IRSA) to dynamically authorize cloud resource creation directly from Jenkins pods. This pattern avoids insecure long-lived static AWS access credentials.
### Observability

#### Metrics Collection

##### Grafana InfluxDB Integration

  - **(2020)** [Mostrando resultados de Jenkins en Grafana mediante InfluxDB 🌟](https://www.enmilocalfunciona.io/mostrando-resultados-de-jenkins-en-grafana-mediante-influxdb) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight details a pipeline monitoring design pattern utilizing InfluxDB and Grafana to visualize Jenkins build metrics and durations. Live Grounding highlights that rendering historical telemetry is crucial for detecting performance regressions in CI/CD runner pools. While OpenTelemetry is standardizing in 2026, the legacy InfluxDB exporter remains heavily deployed.
### Pipeline Execution Engine

#### Groovy CPS

##### Continuation Passing Style

  - **(2021)** [==Continuation Passing Style (CPS)==](https://github.com/cloudbees/groovy-cps) <span class='md-tag md-tag--info'>⭐ 95</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ff2f3a9c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 12 L 20 7 L 30 9 L 40 9 L 50 12" fill="none" stroke="url(#spark-grad-ff2f3a9c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight introduces the underlying Continuation Passing Style (CPS) engine used for executing asynchronous Groovy scripts in Jenkins pipelines. Live Grounding reveals that understanding CPS is critical for debugging serialization errors during master restarts. This technical library ensures execution state can survive controller crashes and resume safely.
## DevOps and CICD

### AWS EKS (2)

#### CodePipeline

  - **(2024)** [stacksimplify.com: DevOps with AWS CodePipeline on AWS EKS](https://docs.stacksimplify.com/aws-eks/aws-devops-eks/learn-to-master-devops-on-aws-eks-using-aws-codecommit-codebuild-codepipeline) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Thorough technical learning guide configuring CI/CD pipelines targeting AWS EKS. Integrates AWS native tools like CodeCommit, CodeBuild, and CodePipeline with modern container orchestration standards.
### AWS Infrastructure

#### DevOps Guides

  - **(2025)** [==AdminTurnedDevOps/DevOps-The-Hard-Way-AWS==](https://github.com/AdminTurnedDevOps/DevOps-The-Hard-Way-AWS) <span class='md-tag md-tag--info'>⭐ 2420</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e325dfd1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 12 L 20 10 L 30 9 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-e325dfd1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive learning curriculum covering real-world cloud operations on AWS. Hands-on modules include terraforming network segments, setting up pipelines, security scanning, and establishing resilient monitoring.
### Azure DevOps

#### Build Automation (1)

  - **(2024)** [lambdatest.com: How To Build a CI/CD Pipeline In Azure DevOps ?](https://www.testmuai.com/blog/build-ci-cd-pipeline-in-azure-devops) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step introduction guide detailing how to construct and validate pipelines within Azure DevOps Services. Addresses multi-stage environments, secure service connection creation, and automated test suite execution.
#### Infrastructure Governance

  - **(2022)** [Azure DevOps Demo Generator is now open source](https://devblogs.microsoft.com/devops/azure-devops-demo-generator-is-now-open-source) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announcement highlighting the open-sourcing of the Azure DevOps Demo Generator engine. Allows infrastructure teams to package, distribute, and automatically spin up fully populated Azure DevOps project spaces.
#### Onboarding Engine

  - **(2024)** [Get started creating and populating demo Azure DevOps Services projects](https://learn.microsoft.com/en-us/azure/devops/demo-gen/use-demo-generator-v2?view=azure-devops) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Microsoft learning guide outlining the usage patterns of the Demo Generator v2 platform. Focuses on setting up pre-populated source code repos, agile work boards, and deployment pipelines.
#### YAML Pipelines

  - **(2024)** [docs.microsoft.com: Create a build pipeline with Azure Pipelines](https://learn.microsoft.com/en-gb/azure/devops/pipelines/build/ci-build-git?view=azure-devops) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Microsoft learning path focusing on declaring Azure Pipelines build logic using YAML configurations. Covers caching mechanisms, parallel task execution strategies, and code analysis plugin integrations.
### Continuous Delivery (1)

#### Docker Images

  - **(2020)** [ref 1](https://hub.docker.com/r/ibuchh/petclinic-spinnaker-jenkins) <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A legacy Docker Hub image combining PetClinic deployment artifacts with Spinnaker and Jenkins orchestration capabilities. Serves as a historical artifact of early multi-cloud continuous delivery pipelines built on top of traditional JVM monoliths.
### Jenkins (2)

#### Kubernetes Agents

  - **(2021)** [pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images 🌟](https://pushbuildtestdeploy.com/jenkins-on-kubernetes-building-docker-images) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive technical guide exploring the orchestration of Jenkins agents inside Kubernetes. Illustrates how to dynamically provision agent pods to build and push Docker images using secure mechanisms like Kaniko or Docker-in-Docker (DinD).
#### Pipeline-as-Code

  - **(2017)** [github.com/kohsuke/petclinic Jenkinsfile](https://github.com/kohsuke/petclinic/blob/master/Jenkinsfile) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A historical Jenkinsfile configuration by Kohsuke Kawaguchi showcasing early Declarative Pipeline patterns for Java projects. Illustrates stage definitions, testing cycles, and artifact archival within a self-hosted Jenkins master node environment.
## DevOps and Platform Engineering

### Infrastructure Automation

#### Academic Materials

  - **(2022)** [jose-r-lopez/SSI_Materials](https://github.com/jose-r-lopez/SSI_Infraestructure_Automation_Materials) <span class='md-tag md-tag--info'>⭐ 44</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-af67ea0e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 11 L 20 5 L 30 10 L 40 4 L 50 13" fill="none" stroke="url(#spark-grad-af67ea0e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML/VAGRANTFILE CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured repository containing laboratory manuals, automation scripts, and server-provisioning blueprints. Optimized for teaching systems administration and automation using Ansible and Vagrant. (Live Grounding: Excellent academic/foundational resource for mapping traditional configurations to automated workflows).
### Interview Preparation

#### Reference Guides

  - **(2026)** [==bregman-arie/devops-exercises 🌟==](https://github.com/bregman-arie/devops-exercises) <span class='md-tag md-tag--info'>⭐ 82758</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7d8c130e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 8 L 20 12 L 30 9 L 40 12 L 50 3" fill="none" stroke="url(#spark-grad-7d8c130e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON/YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A massive curated repository containing thousands of questions, answers, and hands-on exercises covering Linux, Jenkins, Docker, Kubernetes, Ansible, Terraform, AWS, and system design. (Live Grounding: With over 82k stars, it stands in 2026 as the preeminent resource for preparing systems engineers and validating platform architecture skills).
### Learning Resources (1)

#### Methodologies

  - **(2024)** [DEVOPS Library](https://devopslibrary.com) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive portal offering structured DevOps lessons, covering CI/CD pipelines, configuration management (Ansible, Chef), infrastructure automation, and container orchestrations. (Live Grounding: Provides foundational patterns useful for junior-to-mid level engineers to grasp traditional infrastructure transition to cloud-native paradigms).
### Project Blueprints

#### Infrastructure Showcase

  - **(2021)** [yankils/Simple-DevOps-Project](https://github.com/yankils/Simple-DevOps-Project) <span class='md-tag md-tag--warning'>[SHELL/DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical demonstration codebase combining core DevOps components, including automated provisioning scripts and simple pipeline files, to launch a basic application stack. Designed for educational labs. (Live Grounding: Good for foundational learning, though not suited for enterprise-scale zero-trust environments).
## DevOps Philosophy

### Software Engineering

#### No Code Movement

  - **(2020)** [==github.com/kelseyhightower/nocode==](https://github.com/kelseyhightower/nocode) <span class='md-tag md-tag--info'>⭐ 65387</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d0b15bc1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 2 L 20 11 L 30 11 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-d0b15bc1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Kelsey Hightower's legendary satirical repository highlighting that the best way to write secure, bug-free, and highly maintainable software is by writing 'no code' at all. Highly popular and philosophically beloved in the cloud-native ecosystem.
## DevSecOps and Automation

### End-to-End Pipelines

#### Multi-Version Deployments

  - **(2023)** [mrcloudbook.com: Automating Tetris Deployments: DevSecOps with ArgoCD, Terraform, and Jenkins for Two Game Versions](https://mrcloudbook.com/automating-tetris-deployments-devsecops-with-argocd-terraform-and-jenkins-for-two-game-versions) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents an end-to-end DevSecOps execution path deploying two independent versions of a Tetris application. Coordinates Terraform for EKS infrastructure creation, Jenkins for CI builds, security scanning, and Argo CD for final GitOps delivery.
### Jenkins-based CI-CD

#### AWS and Jenkins

  - **(2020)** [bitbucket.org: setting up a cicd pipeline with spring mvc and kubernetes on aws](https://www.atlassian.com/blog/bitbucket/setting-up-a-ci-cd-pipeline-with-spring-mvc-jenkins-and-kubernetes-on-aws) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines constructing a complete continuous integration pipeline using Bitbucket, Jenkins, and AWS EKS. Covers maven compilation, Docker Hub image pushes, and automated rolling deployments on target host nodes.
  - **(2020)** [aws.amazon.com: Integrating Jenkins with AWS CodeArtifact to publish and consume Python artifacts](https://aws.amazon.com/blogs/devops/using-jenkins-with-codeartifact) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to authenticate Jenkins runner nodes securely with AWS CodeArtifact. Focuses on resolving and publishing Python artifact packages safely through automated build lifecycles.
#### Jenkins Architecture

  - **(2021)** [==cloudogu/jenkinsfiles 🌟🌟🌟==](https://github.com/cloudogu/jenkinsfiles) <span class='md-tag md-tag--info'>⭐ 299</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-31f1ff54" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 11 L 20 5 L 30 2 L 40 9 L 50 12" fill="none" stroke="url(#spark-grad-31f1ff54)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive repository of production-ready Jenkinsfiles designed for modern enterprise software lifecycles. Offers reusable build scripts, container integration routines, and test suite automation loops.
  - **(2021)** [devopscube.com: How to Setup Jenkins Build Agents on Kubernetes Cluster 🌟](https://devopscube.com/jenkins-build-agents-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an architectural step-by-step setup of self-scaling Jenkins Build Agents using the Kubernetes Jenkins plugin. Configures persistent volumes and resource constraints for ephemeral executors.
  - **(2020)** [piotrminkowski.com: Continuous Integration with Jenkins on Kubernetes 🌟](https://piotrminkowski.com/2020/11/10/continuous-integration-with-jenkins-on-kubernetes) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details executing dynamically provisioned Jenkins agent pods inside a target Kubernetes cluster. Explores mounting credentials, executing parallel pipeline workloads, and cleanup phases to optimize compute budgets.
#### Jenkins Basics

  - **(2021)** [simplilearn.com: What is CI/CD Pipeline and How to Implement it Using Jenkins?](https://www.simplilearn.com/tutorials/jenkins-tutorial/ci-cd-pipeline) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Basic tutorial outlining CI/CD life cycles, illustrating how continuous deployment patterns differ from continuous delivery, and implementing simple pipelines using standard Jenkins components.
#### Jenkins Shared Libraries

  - **(2020)** [github.com/monodot/pipeline-library-demo 🌟](https://github.com/tutorialworks/pipeline-library-demo) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reference repository demonstrating the architectural setup of reusable Jenkins Shared Libraries. Emphasizes centralizing redundant tasks (like Slack messaging and build wrappers) to keep multi-repo setups clean.
#### Mobile Workflows

  - **(2021)** [youtube: Simple DevOps Project | Publish Android APK to App Center | Beginner Pipeline](https://www.youtube.com/watch?v=KgH0QzMHXLs) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational project walk-through deploying compiled Android APK binaries to Visual Studio App Center via automated Jenkins runner jobs. Discusses signing profiles and deployment triggers.
## DevSecOps and IDEs

### Eclipse Che

#### Cloud IDE Templates

  - **(2024)** [github.com/che-samples](https://github.com/che-samples) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official template repository containing devfile configurations and cloud-native project workspace definitions for Eclipse Che. Accelerates development setup by declaring containers, tools, and runtimes as code.
### Google Cloud Code

#### Developer Experience

  - **(2024)** [==github.com/GoogleCloudPlatform/cloud-code-samples 🌟==](https://github.com/GoogleCloudPlatform/cloud-code-samples) <span class='md-tag md-tag--info'>⭐ 437</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c0cf791a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 12 L 30 4 L 40 8 L 50 2" fill="none" stroke="url(#spark-grad-c0cf791a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curated templates and setup workflows targeting GCP's Cloud Code extension. Helps developers structure containerized services locally before auto-deploying to Google Kubernetes Engine (GKE).
#### Enterprise Templates

  - **(2021)** [cloud.google.com: Follow your org’s app dev best practices with Cloud Code custom samples 🌟](https://cloud.google.com/blog/products/application-development/access-an-orgs-custom-code-repo-from-cloud-code-ides) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on establishing unified developer standards using Cloud Code. Outlines mechanisms for setting up private template repositories to govern cloud application scaffolding across large software organizations.
### Quality Assurance

#### Azure Cloud Testing

  - **(2024)** [==github.com/microsoft: Contoso Traders - Cloud testing tools demo app==](https://github.com/microsoft/contosotraders-cloudtesting) <span class='md-tag md-tag--info'>⭐ 168</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e6404a69" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 3 L 20 11 L 30 12 L 40 13 L 50 4" fill="none" stroke="url(#spark-grad-e6404a69)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive, multi-platform microservices demonstration application showcasing Azure cloud testing solutions. Features Playwright end-to-end tests, load testing scenarios, and automated regression validations.
## Developer Experience (1)

### Inner Loop Development

#### Local Tooling

  - **(2023)** [==Azure/Draft 🌟==](https://github.com/Azure/draft) <span class='md-tag md-tag--info'>⭐ 642</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2026e583" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 6 L 20 4 L 30 12 L 40 8 L 50 8" fill="none" stroke="url(#spark-grad-2026e583)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Azure Draft simplifies early-stage developer onboarding onto Kubernetes. By scanning source code directories, it automatically generates containerization assets including Dockerfiles, Kubernetes manifests, Helm charts, and deployment workflows.
## Developer Tools (1)

### Quarkus CLI

#### Local Development (3)

  - **(2020)** [aalmiray/q-cli](https://github.com/aalmiray/q-cli) <span class='md-tag md-tag--info'>⭐ 11</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0761b2c7" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 9 L 20 3 L 30 9 L 40 5 L 50 10" fill="none" stroke="url(#spark-grad-0761b2c7)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early community command-line interface helper for bootstrapping and managing Quarkus projects. While the official Quarkus CLI eventually integrated these capabilities, this repository represents a pivotal step in Quarkus DX history.
## Education

### Certification

#### CKAD

  - **(2020)** [Kubernetes CKAD Example Exam Questions Practical Challenge Series](https://codeburst.io/kubernetes-ckad-weekly-challenges-overview-and-tips-7282b36a2681) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-yield challenge series tailored for the Certified Kubernetes Application Developer (CKAD) exam. Focuses on masterclass proficiency in fast imperative CLI commands, multi-container configurations, config-injection, and network troubleshooting techniques.
## Enterprise Architecture

### Business Process Management

#### RHPAM (1)

  - **(2020)** [gitlab.com: Red Hat Process Automation Manager - Signal Marketing Demo](https://gitlab.com/bpmworkshop/rhpam-signal-marketing-demo) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A demonstration application built on Red Hat Process Automation Manager (RHPAM) modeling signal marketing workflows. Integrates Complex Event Processing (CEP) engine features, showcasing declarative state orchestration within microservice platforms.
## Enterprise Integration

### SAP Cloud Integration

#### Azure Blob Storage

  - **(2021)** [blogs.sap.com: Cloud Integration with Commerce Azure Blob Storage using REST API – Part 1](https://blogs.sap.com/2021/07/04/cloud-integration-with-commerce-azure-blob-storage-using-rest-api) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step guide illustrating SAP Cloud Integration connectivity to Azure Blob Storage via REST APIs. Outlines security header formulation, token acquisition flows, and early payload transformations.
  - **(2021)** [blogs.sap.com: Cloud Integration with Commerce Azure Blob Storage using REST API – Part 2](https://blogs.sap.com/2021/12/26/cloud-integration-with-commerce-azure-blob-storage-using-rest-api-part-2) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Continuing the architectural sequence, this guide centers on advanced REST payloads, handling massive binary files, implementing robust retry policies, and tracking upload failures inside SAP landscapes.
## Event-Driven Architectures

### Cloud-Native Java (2)

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
## Extensibility

### Admission Controllers

#### JVM Configurations

  - **(2020)** [nfrankel/jvm-controller](https://github.com/nfrankel/jvm-controller) <span class='md-tag md-tag--warning'>[KOTLIN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates building a custom Java Virtual Machine (JVM) admission controller. Programmatically dynamically intercepts Pod specifications inside a validating or mutating webhook to inject appropriate runtime flags (such as JVM memory heap ergonomics) aligned with CPU and RAM resource limits.
### Event-Driven (1)

#### Webhooks

  - **(2021)** [webhooks.app](https://webhooks.app) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Utility software engineered to facilitate fast interception, logging, inspection, and local validation of webhooks. Proves useful when debugging live Kubernetes Mutating Webhook Admission Controllers or debugging automated external event triggers.
## GitOps (2)

### Continuous Deployment

#### Flux v2

  - **(2023)** [flux2-kustomize-helm-example 🌟](https://github.com/fluxcd/flux2-kustomize-helm-example) <span class='md-tag md-tag--info'>⭐ 1268</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-98dba493" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 9 L 20 6 L 30 13 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-98dba493)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The canonical Flux v2 reference architecture. Provides production-tested blueprints for structuring multi-environment repositories, configuring Kustomize hierarchies, packaging Helm releases, and enforcing namespace isolation patterns.
### OpenShift (1)

#### Enterprise Dev

  - **(2021)** [youtube: GitOps Guide to the Galaxy (Ep 12): Flux On OpenShift](https://www.youtube.com/watch?v=W_rcYPZkhFg&ab_channel=RedHat) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Video guide examining GitOps operations using Flux v2 inside Red Hat OpenShift. Discusses enterprise concerns such as overcoming strict Security Context Constraints (SCC) and integrating with corporate OAuth configurations.
## GitOps and Declarative Git

### Developer Platforms (1)

#### GitHub Actions (3)

  - **(2021)** [shipa.io: GitOps in Kubernetes, the easy way–with GitHub Actions and Shipa](https://shipa.io/gitops) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Explores combining the ease of GitHub Actions workflows with Shipa's application management plane to implement secure GitOps pipelines. (Live Grounding: Proves early efforts in platform engineering to bridge continuous integration directly into abstract application runtimes).
### Enterprise GitOps

#### Anthos

  - **(2022)** [youtube.com: Cloud Native GitOps with Anthos and JFrog Artifactory](https://www.youtube.com/watch?v=HSjm6-ACmWQ&ab_channel=JFrog) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A collaborative session displaying how Anthos Config Management dynamically orchestrates multi-cluster topologies in tandem with JFrog Artifactory as a secure, enterprise container registry. (Live Grounding: Portrays the classic zero-trust artifact distribution pattern used in modern multi-cloud platform deployments).
### GitOps Tools

#### Flux and Helm

  - **(2022)** [mytechramblings.com: A practical example of GitOps using Azure DevOps, Azure Container Registry, Helm, Flux and Kubernetes](https://www.mytechramblings.com/posts/gitops-with-azure-devops-helm-acr-flux-and-k8s) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Presents a comprehensive GitOps architectural blueprint combining Azure DevOps, Helm, and ACR under the control of Flux inside a Kubernetes cluster to manage automated continuous rollouts. (Live Grounding: Flux v2 continues to represent a core declarative deployment vehicle, serving as a pillar for automated continuous delivery).
## Governance and Security

### Platform Comparisons

#### OpenShift vs Kubernetes

  - **(2021)** [developer.ibm.com: Example exercises to differentiate OpenShift and Kubernetes](https://developer.ibm.com/tutorials/examples-differentiate-openshift-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A step-by-step practical guide comparing vanilla Kubernetes to enterprise OpenShift platforms. Illustrates differences in router configs, Security Context Constraints (SCCs), build mechanisms, and deployment strategies.
### Policy Enforcement (1)

#### OPA Gatekeeper

  - **(2021)** [opensource.com: Implement governance on your Kubernetes cluster](https://opensource.com/article/21/12/kubernetes-gatekeeper) <span class='md-tag md-tag--warning'>[YAML / REGO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the installation and lifecycle management of OPA Gatekeeper inside Kubernetes. Demonstrates how to design ConstraintTemplates and Constraints to programmatically enforce organizational governance rules, highlighting its capability to validate, mutate, and deny container creation requests before deployment execution.
## Hybrid Cloud Platforms

### Anthos (1)

#### Multi-Cluster Mesh

  - **(2022)** [Tutorial: Connect Amazon EKS and Azure AKS Clusters with Google Anthos](https://thenewstack.io/tutorial-connect-amazon-eks-and-azure-aks-clusters-with-google-anthos) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Multi-cloud tutorial explaining cluster federation workflows using Google Anthos. Coordinates the management, communication policies, and service mesh definitions across Amazon EKS and Microsoft Azure AKS clusters.
### OpenShift (2)

#### Developer Workspaces

  - **(2024)** [OpenShift.io Samples 🌟🌟](https://workspaces.openshift.com) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enterprise cloud developer templates optimized for Red Hat OpenShift Workspaces (Eclipse Che). Facilitates the rapid provisioning of secure, IDE-integrated environments for compiling and deploying cloud-native workloads.
## Hybrid Cloud Solutions

### Multi-Cloud Architectures

#### Anthos with EKS

  - **(2020)** [Tutorial: Deploy Anthos Apps from GCP Marketplace into Amazon EKS Cluster](https://thenewstack.io/tutorial-deploy-anthos-apps-from-gcp-marketplace-into-amazon-eks-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates cross-cloud portability by deploying Google Cloud Marketplace containerized applications directly into Amazon EKS clusters via Anthos. Discusses multi-cloud identity mappings, ingress controller configurations, and registration procedures required to bridge GCP's service ecosystem into AWS workloads.
### Multi-Cluster GitOps (1)

#### Anthos Config Management

  - **(2020)** [Tutorial: GitOps in Multicluster Environments with Anthos Config Management](https://thenewstack.io/tutorial-gitops-in-multicluster-environments-with-anthos-config-management) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive guide on establishing declarative configuration management in multi-cluster environments using Anthos Config Management (ACM). The tutorial details Git-to-cluster synchronization protocols, security policies via Config Controller, and cluster-state reconciliation mechanisms, representing a stable paradigm for enterprise hybrid-cloud control planes.
## Infrastructure (1)

### Artifact Management

#### Nexus3 Deployment

##### Kubernetes Helm Setup

  - **(2021)** [Proof of Concept: Nexus3 Chart configuration on Kubernetes](https://github.com/nubenetes/nexus3-helm-chart) <span class='md-tag md-tag--warning'>[SMARTY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight presents this proof-of-concept Nexus3 Helm chart deployment pattern on Kubernetes. Live Grounding confirms that hosting a dedicated private repository manager inside the cluster remains critical for sovereign enterprise setups. The manifest coordinates dynamic ingress rules and persistent storage volume allocations.
### Edge Computing

#### Minimalist Clusters

  - **(2020)** [todaywasawesome/atomic-cluster: The Atomic Cluster](https://github.com/todaywasawesome/atomic-cluster) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> — An experimental framework built to explore deployment lifecycles of highly compact, ephemeral Kubernetes engines at the edge. Optimizes cluster-state storage engine footprints and reduces node bootstrapping overhead for edge nodes and rapid local testing setups.
### Production Hardening

#### Examples (1)

  - **(2022)** [github.com/AdminTurnedDevOps/kubernetes-in-production-examples](https://github.com/AdminTurnedDevOps/kubernetes-in-production-examples) <span class='md-tag md-tag--info'>⭐ 79</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c90d4027" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 6 L 20 3 L 30 4 L 40 7 L 50 7" fill="none" stroke="url(#spark-grad-c90d4027)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced enterprise-readiness blueprint repository. Highlights essential security context layers, proper resource constraint mechanisms (CPU/Memory requests and limits), NetworkPolicies, Horizontal Pod Autoscalers, and liveness/readiness probe best practices for production deployments.
### Provisioning (2)

#### High Availability (1)

  - **(2021)** [github.com/developer-guy: Set up HA k3s cluster on DigitalOcean using Terraform' + Ansible](https://github.com/developer-guy/kubernetes-cluster-setup-using-terraform-and-k3s-on-digitalocean) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An infrastructure-as-code repository detailing the programmatic deployment of a highly available, light K3s cluster topology on DigitalOcean. Harnesses Terraform for provisioning underlying hypervisors and networking, combined with Ansible for control-plane configuration and secure node-pooling.
### Stateful Applications

#### Mail Services

  - **(2021)** [kruyt.org: Running a mailserver in Kubernetes](https://kruyt.org/running-a-mailserver-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical deployment architectural guide detailing the orchestration of high-availability mail servers on Kubernetes. Analyzes the complexities of handling persistent storage for mail stores (via PV/PVC), dynamic IMAP/SMTP routing setups, and the crucial network security protocols (DKIM, SPF, DMARC) required to maintain high IP reputation inside cloud infrastructures.
## Infrastructure and DevOps

### CI-CD Concepts

#### Jenkins Tutorials

  - **(2020)** [wardviaene/jenkins-course](https://github.com/wardviaene/jenkins-course) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly practical repository containing configuration examples, scripts, and multi-stage pipeline templates for various programming languages. Designed to serve as hands-on exercises for developers studying infrastructure-as-code and configuration-as-code fundamentals.
### Shared Libraries

#### Production Blueprints

  - **(2021)** [Pipeline Global Library for ci.jenkins.io](https://github.com/jenkins-infra/pipeline-library) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The real-world production Global Shared Pipeline Library utilized by the official Jenkins infrastructure project (ci.jenkins.io). Serves as an excellent architectural blueprint of highly robust, scalable, and modular pipeline development.
## Infrastructure and Operations

### Cost Optimization and Metering

#### Metering Operator

  - **(2020)** [Writing Customized Reports Using Metering Operator](https://www.redhat.com/en/blog/writing-customized-reports-using-metering-operator) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Explores authoring custom resource and cost allocation reports using the OpenShift Metering Operator. Note: The Metering Operator has since been deprecated in favor of OpenShift Cost Management.
### Enterprise Cluster Management

#### OKD Community Platform

  - **(2020)** [openshift.com: Recap: OKD 4 Testing and Deployment Workshop - Videos and Additional Resources](https://www.redhat.com/en/blog/recap-okd-4-testing-and-deployment-workshop-videos-and-additional-resources) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compiles core workshop resources on OKD 4 deployment, testing, and lifecycle patterns. Explores underlying Fedora CoreOS operating mechanics and bootstrap procedures for community-led OpenShift clusters.
#### Red Hat ACM

  - **(2020)** [Advanced Cluster Management Demos](https://www.youtube.com/playlist?list=PLbMP1JcGBmSFA56rykbH2fg1F9Tozk4of)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated playlist of technical capabilities inside Red Hat Advanced Cluster Management (ACM), focusing on policy enforcement, lifecycle orchestration, and multi-cluster visualization.
### Ingress and Routing

#### Argo CD Deployment

  - **(2020)** [itnext.io: Deploy Argo CD with Ingress and TLS in Three Steps: No YAML Yak Shaving Required 🌟](https://itnext.io/deploy-argo-cd-with-ingress-and-tls-in-three-steps-no-yaml-yak-shaving-required-bc536d401491) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates Ambassador Edge Stack's scaffolding tool to deploy Argo CD quickly with TLS and Ingress settings. Eliminates tedious manual manifest authoring by automating TLS certificate generation and routing definitions for administrative dashboards.
### Observability and Service Mesh

#### Grafana and ACM

  - **(2021)** [cloud.redhat.com: How to Observe your Clusters with Red Hat Advanced Cluster Management - Customize the Grafana Dashboard](https://www.redhat.com/en/blog/how-to-observe-your-clusters-with-red-hat-advanced-cluster-management-customize-the-grafana-dashboard) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides readers in customizing Multi-Cluster Grafana Dashboards under ACM. Centralizes metric aggregation pipelines and tailors performance panels across heterogeneous cluster landscapes.
#### OpenShift ServiceMesh

  - **(2021)** [Monitoring Services like an SRE in OpenShift ServiceMesh](https://www.redhat.com/en/blog/monitoring-services-like-an-sre-in-openshift-servicemesh) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Unpacks Site Reliability Engineering (SRE) monitoring patterns using OpenShift Service Mesh. Synthesizes Istio, Kiali, and Prometheus telemetry to isolate performance bottlenecks and measure Golden Signals.
## Infrastructure and Platform

### Autoscaling

#### Event-Driven Scaling

  - **(2021)** [tomd.xyz: Event-driven integration on Kubernetes with Camel & KEDA 🌟](https://tomd.xyz/kubernetes-event-driven-keda) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to run Apache Camel integration microservices on Kubernetes, leveraging KEDA to dynamically scale Camel routes based on incoming message rates. Synthesizes enterprise integration patterns (EIP) with modern cloud-native autoscaling.
## Infrastructure as Code (1)

### AI-Assisted IaC

#### AKS and ACR Deployments

  - **(2023)** [patrickkoch.dev: Terraform on Azure with GitHub Copilot - Creating a Kubernetes Cluster and a Container Registry](https://www.patrickkoch.dev/posts/post_31) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the intersection of generative AI and Infrastructure as Code by walking through the creation of an AKS (Azure Kubernetes Service) and ACR (Azure Container Registry) using GitHub Copilot to accelerate Terraform writing workflows.
### Kubernetes Management

#### Infrastructure Blueprints

  - **(2021)** [StarpTech/k-andy](https://github.com/StarpTech/k-andy) <span class='md-tag md-tag--info'>⭐ 157</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-0119eda1" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 6 L 20 13 L 30 10 L 40 12 L 50 8" fill="none" stroke="url(#spark-grad-0119eda1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A consolidated project featuring curated Kubernetes deployment manifests and Helm configurations. Highlights patterns for bootstrapping monitoring stacks, storage drivers, and load-balancer integration with localized container configurations.
### OpenShift Virtualization

#### GitOps VMs

  - **(2021)** [cloud.redhat.com: Virtual Machines as Code with OpenShift GitOps and OpenShift Virtualization](https://www.redhat.com/en/blog/virtual-machines-as-code-with-openshift-gitops-and-openshift-virtualization) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Details running legacy virtual machines side-by-side with containers using OpenShift Virtualization. Outlines declarative patterns for orchestrating VM lifecycles through GitOps practices using Argo CD.
### Serverless Deployment

#### Terraform and AWS Lambda

  - **(2022)** [dev.to: Creating a Rest API with Infrastructure as Code (Terraform) & Serverless (Lambda + Python) - Part 2 CI/CD](https://dev.to/aws-builders/creating-a-rest-api-with-infrastructure-as-code-terraform-serverless-lambda-python-part-2-cicd-g8h) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a modern serverless deployment loop, coupling HashiCorp Terraform with AWS API Gateway and Lambda functions. Part 2 focuses on constructing automated GitHub Actions CI/CD deployment pipelines for infrastructure and application code layers.
### Terraform

#### AWS Networking

  - **(2024)** [==aws-samples/aws-network-hub-for-terraform: Network Hub Account with Terraform==](https://github.com/aws-samples/aws-network-hub-for-terraform) <span class='md-tag md-tag--info'>⭐ 103</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-eee24756" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 12 L 30 9 L 40 10 L 50 2" fill="none" stroke="url(#spark-grad-eee24756)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Structured Terraform blueprints for provisioning centralized Transit Gateway or Cloud WAN hubs. Implements hub-and-spoke networking topology across multi-account enterprise structures safely.
#### Azure Security

  - **(2023)** [davidsr.me: Deploy Azure WAF with Terraform and Azure DevOps](https://davidsr.me/deploy-azure-waf-with-terraform-and-azure-devops) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical tutorial detailing how to declare Azure Web Application Firewall (WAF) rule sets as Terraform variables. Configures Azure DevOps pipelines for automated validation and execution of the plans.
#### GCP Provisioning

  - **(2023)** [==Terraform Automation Demo using Google Cloud Provider==](https://github.com/tfxor/terraform-google-automation-demo) <span class='md-tag md-tag--info'>⭐ 10</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c233e75e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 4 L 20 3 L 30 7 L 40 10 L 50 8" fill="none" stroke="url(#spark-grad-c233e75e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Technical repository containing IaC templates to provision GCP infrastructure via HashiCorp Terraform. Showcases structured folder hierarchies, backend state locks, and resource declarations for VPCs, compute instances, and firewalls.
### Terraform Ecosystem

#### AWS Compute Provisioning

  - **(2021)** [k21academy.com: Automate AWS Virtual Machine using Terraform – Creation Demo](https://k21academy.com/terraform/terraform-automate-aws-vm) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A step-by-step introduction demonstrating the creation and lifecycle management of AWS Elastic Compute Cloud (EC2) instances using Terraform. Excellent for understanding simple provider declarations, variables, and resource destruction.
#### AWS RDS Databases

  - **(2022)** [devopscube.com/terraform-aws-rds](https://devopscube.com/terraform-aws-rds) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details production-grade Terraform configurations for deploying RDS databases. Illustrates high-availability multi-AZ architectures, automated backup retention, integration with AWS Secrets Manager, and proper configuration of private DB subnets.
  - **(2021)** [adamtheautomator.com: How To Build a Database Instance with Terraform and AWS RDS](https://adamtheautomator.com/terraform-and-aws-rds) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive operational blueprint for deploying managed relational databases on AWS RDS via Terraform. Demonstrates critical database reliability configurations, security groups, database subnet groups, and encrypted secret management parameters.
#### AWS S3 Storage

  - **(2023)** [blog.awsfundamentals.com: Using S3 with Terraform](https://awsfundamentals.com/blog/using-s3-with-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structural guide explaining how to declare and maintain AWS Simple Storage Service (S3) buckets using Terraform. Focuses on security defaults, bucket access control lists (ACLs), versioning configurations, and cross-region replication strategies.
#### Advanced HCL Loopings

  - **(2021)** [middlewareinventory.com: Terraform Create Multiple EC2 with different Configs – for_each and count together](https://www.middlewareinventory.com/blog/terraform-create-multiple-ec2-different-config) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Dives deep into dynamic loop structures using Terraform's for_each and nested map configurations. Explains how to scale and tailor individual virtual machines under a single module declaration without resorting to repetitive, static configuration blocks.
#### Azure Deployments

  - **(2021)** [azapril.dev: Deploying a LogicApp with Terraform (Bonus: in an AzDO pipeline)](https://azapril.dev/2021/04/12/deploying-a-logicapp-with-terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers through deploying serverless workflows using Azure Logic Apps managed by Terraform, integrated with Azure DevOps CI/CD pipelines. Emphasizes deployment pipelines, environment parameters, and infrastructure security.
#### Beginner Blueprints

  - **(2021)** [github.com/venkateshk111/terraform-beginners-guide 🌟](https://github.com/venkateshk111/terraform-beginners-guide) <span class='md-tag md-tag--info'>⭐ 107</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3d322ceb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 6 L 20 13 L 30 13 L 40 13 L 50 2" fill="none" stroke="url(#spark-grad-3d322ceb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A structured, accessible community repository offering clear code snippets, common commands, and hands-on scenarios designed to accelerate early learning curves for DevOps engineers adopting HashiCorp Terraform.
#### EKS and IAM Security

  - **(2021)** [brennerm.github.io: Setting up an EKS cluster with IAM/IRSA integration](https://shipit.dev/posts/setting-up-eks-with-irsa-using-terraform.html) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A critical security tutorial detailing the configuration of IAM Roles for Service Accounts (IRSA) on AWS EKS using Terraform. Walks through building OpenID Connect (OIDC) identity providers and defining strict, least-privilege IAM policies directly mapped to Kubernetes ServiceAccounts.
#### Fundamental Syntaxes

  - **(2021)** [https://github.com/chenjd/terraform-101 🌟](https://github.com/chenjd/terraform-101) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly practical beginner-level code index focusing on Terraform basics, state management, module syntax, and provider declarations for deploying cloud infrastructure safely.
#### Kubernetes Provider

  - **(2020)** [opensource.com: A guide to Terraform for Kubernetes beginners](https://opensource.com/article/20/7/terraform-kubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to use HashiCorp Terraform to directly manage Kubernetes resources and objects. Highlights the trade-offs of using Terraform versus Helm/kubectl for standard resource templating, state tracking, and lifecycle operations.
#### Learning Platforms

  - **(2022)** [terraform.collabnix.com](https://collabnix.github.io/terraform) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A collaborative, multi-step reference hub designed to systematically introduce DevOps engineers to Terraform. Covers declarative state files, modular organization, provider configurations, and deployment strategies across multiple hyper-scale cloud providers.
## Infrastructure as Code and CI-CD

### Configuration Management

#### Ansible

  - **(2021)** [redhat.com: Build a lab in 36 seconds with Ansible](https://www.redhat.com/en/blog/build-VM-fast-ansible) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the extreme velocity benefits of programmatic infrastructure by spinning up a full VM-based training lab environment inside of 36 seconds using Ansible automation. (Live Grounding: Shows how standardized playbooks reduce system bootstrap overhead to near zero).
#### Ansible Galaxy

  - **(2025)** [galaxy.ansible.com/ansible/product_demos 🌟](https://galaxy.ansible.com/ansible/product_demos) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official catalog of production-ready Ansible product demos hosted on Ansible Galaxy. Contains modular roles and collections designed to streamline enterprise cloud deployments. (Live Grounding: Serves as a vital asset directory for platform engineering teams utilizing Ansible Automation Platform).
#### Ansible Inventory

  - **(2021)** [blog.stephane-robert.info: Ansible - Utiliser MySQL comme inventaire dynamique (Use MySQL as a dynamic inventory)](https://blog.stephane-robert.info/post/ansible-utiliser-mysql-comme-inventaire-dynamique) <span class='md-tag md-tag--warning'>[YAML/PYTHON/SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical deep-dive on configuring Ansible to query a MySQL database dynamically to build asset inventories. Eliminates hardcoded static host files by relying on runtime query configurations. (Live Grounding: Essential for hybrid-cloud setups where IP address spaces change rapidly and dynamically).
#### Ansible Tower

  - **(2023)** [Red Hat Ansible Tower - Workshop and Demo](https://github.com/network-automation/toolkit) <span class='md-tag md-tag--info'>⭐ 127</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-8b207dc2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 4 L 20 12 L 30 2 L 40 10 L 50 2" fill="none" stroke="url(#spark-grad-8b207dc2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML/PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — A specialized automation toolkit for Red Hat Ansible Tower/AWX focused on network architectures. Emphasizes role-based access controls, standardized workflow templates, and central log telemetry. (Live Grounding: Highlights critical patterns for bringing deterministic software-defined networking concepts to legacy environments).
#### Ansible Workshops

  - **(2025)** [ansible.github.io/workshops/demos : Red Hat Ansible Automation Platform Workshops](https://labs.demoredhat.com/demos) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Red Hat Ansible workshops repository, highlighting hands-on scenarios for cloud provisioning, configuration management, network automation, and security playbooks. (Live Grounding: Serves as the authoritative source for enterprise teams to upskill in Ansible Automation Platform strategies).
### Developer Platforms (2)

#### CI-CD Pipelines

  - **(2021)** [shipa.io: A Developer focused CI/CD pipeline for Kubernetes](https://shipa.io/a-developer-focused-ci-cd-pipeline-for-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines designing application-centric CI/CD pipelines that leverage developer platform layers to remove raw Kubernetes configuration friction. (Live Grounding: Highlights the evolving landscape of platform engineering where developers focus on code deliverables while security/infrastructure is handled declaratively by platforms).
### GitOps and Declarative Git (1)

#### Ansible and Helm

  - **(2020)** [opensource.com: Build a Kubernetes Minecraft server with Ansible's Helm modules](https://opensource.com/article/20/10/kubernetes-minecraft-ansible) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates utilizing Ansible's native Helm modules to declare and manage deployments within a Kubernetes cluster, illustrated by spinning up a stateful Minecraft server instance. (Live Grounding: Highlights the cross-functional utility of leveraging Ansible playbooks to drive Kubernetes native packaging models).
## Java Cloud Native

### Spring Cloud (1)

#### Kubernetes Integration (1)

  - **(2026)** [==github: Spring Cloud Kubernetes 🌟==](https://github.com/spring-cloud/spring-cloud-kubernetes) <span class='md-tag md-tag--info'>⭐ 3534</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7e7215a0" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 11 L 20 12 L 30 9 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-7e7215a0)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized integration library that allows Spring Cloud applications to run transparently on Kubernetes. It maps Kubernetes ConfigMaps and Secrets to Spring's Environment, and translates discovery mechanisms to native Kubernetes endpoints. It bridges the gap between Cloud Native infrastructure patterns and Java application logic.
## Kubernetes Tools

### General Reference

  - [kubernetesbyexample.com](https://kubernetesbyexample.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kubernetesbyexample.com in the Kubernetes Tools ecosystem.
  - [k8s Initializer 🌟](https://blackbird.a8r.io/initializer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blackbird.a8r.io in the Kubernetes Tools ecosystem.
  - [blog.jetstack.io: Istio OIDC Authentication](https://developer.cyberark.com/blog/istio-oidc-authentication)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developer.cyberark.com in the Kubernetes Tools ecosystem.
  - [trstringer.com: Deploy to AKS Using a Managed Identity from a GitHub Actions Self-Hosted Runner 🌟](https://trstringer.com/deploy-to-aks-from-github-actions/-self-hosted)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering trstringer.com in the Kubernetes Tools ecosystem.
  - [Clustering WildFly on Openshift](https://www.mastertheboss.com/soa-cloud/openshift/clustering-wildfly-on-openshift-using-wildfly-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [Java EE example on Openshift](https://www.mastertheboss.com/soa-cloud/openshift/java-ee-example-application-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [Microprofile example on Openshift](https://www.mastertheboss.com/soa-cloud/openshift/running-microprofile-applications-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [Deploying WildFly apps on Openshift](https://www.mastertheboss.com/soa-cloud/openshift/using-wildfly-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [Running Thorntail apps on Openshift](https://www.mastertheboss.com/soa-cloud/openshift/thorntail-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [Running Spring Boot applications on Openshift](https://www.mastertheboss.com/jboss-frameworks/spring/deploy-your-springboot-applications-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.mastertheboss.com in the Kubernetes Tools ecosystem.
  - [SysAdmin Casts](https://sysadmincasts.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering SysAdmin Casts in the Kubernetes Tools ecosystem.
  - [DevStack](https://devstack.in)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering DevStack in the Kubernetes Tools ecosystem.
  - [kubernetes-advocate.medium.com 🌟](https://kubernetes-advocate.medium.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kubernetes-advocate.medium.com 🌟 in the Kubernetes Tools ecosystem.
  - [swissarmydevops.com](https://swissarmydevops.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering swissarmydevops.com in the Kubernetes Tools ecosystem.
  - [dzone: DIY DevOps, CI, and CD with GitHub, Docker and a VPS](https://dzone.com/articles/diy-devops-ci-and-cd-with-github-docker-and-a-vps)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: DIY DevOps, CI, and CD with GitHub, Docker and a VPS in the Kubernetes Tools ecosystem.
  - [kubernetes-advocate.medium.com: Website Deployment to AWS with Ansible](https://kubernetes-advocate.medium.com/how-to-deploy-a-website-to-aws-with-ansible-e878a63dd93)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kubernetes-advocate.medium.com: Website Deployment to AWS with Ansible in the Kubernetes Tools ecosystem.
  - [konstruktoid.medium.com: Running a NGINX container using rootless Docker' with Ansible](https://konstruktoid.medium.com/running-a-nginx-container-using-rootless-docker-with-ansible-a2bfcedd3b07)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering konstruktoid.medium.com: Running a NGINX container using rootless Docker' with Ansible in the Kubernetes Tools ecosystem.
  - [kmahi2600.medium.com: Launching A WordPress Application With MYSQL Database' in K8S Cluster On AWS Using Ansible](https://kmahi2600.medium.com/launching-a-wordpress-application-with-mysql-database-in-k8s-cluster-on-aws-using-ansible-a78d6bf12b1a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kmahi2600.medium.com: Launching A WordPress Application With MYSQL Database' in K8S Cluster On AWS Using Ansible in the Kubernetes Tools ecosystem.
  - [faun.pub: Automation: Deploying an app in GKE using Ansible](https://faun.pub/automation-deploying-an-app-in-gke-using-ansible-4b6687967ac3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Automation: Deploying an app in GKE using Ansible in the Kubernetes Tools ecosystem.
  - [ankush-chavan.medium.com: Creating Multi-Cloud Kubernetes Cluster on AWS,' Azure, and GCP cloud](https://ankush-chavan.medium.com/creating-multi-cloud-kubernetes-cluster-on-aws-azure-and-gcp-cloud-92d64633bdfc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ankush-chavan.medium.com: Creating Multi-Cloud Kubernetes Cluster on AWS,' Azure, and GCP cloud in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Clean Up Your Kubernetes Deployments Using Ansible](https://betterprogramming.pub/clean-up-your-kubernetes-deployments-using-ansible-10a000db313b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Clean Up Your Kubernetes Deployments Using Ansible in the Kubernetes Tools ecosystem.
  - [praveendandu24.medium.com: Ensuring AWS Infrastructure Consistency with' Ansible Playbooks](https://praveendandu24.medium.com/ansible-infrastructure-testing-to-test-aws-resources-bd8bdba9ab7c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering praveendandu24.medium.com: Ensuring AWS Infrastructure Consistency with' Ansible Playbooks in the Kubernetes Tools ecosystem.
  - [medium.com/@Kubernetes_Advocate 🌟](https://medium.com/@Kubernetes_Advocate)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@Kubernetes_Advocate 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Efficient Node Out-of-Resource Management in Kubernetes](https://medium.com/kubernetes-tutorials/efficient-node-out-of-resource-management-in-kubernetes-67f158da6e59)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Efficient Node Out-of-Resource Management in Kubernetes in the Kubernetes Tools ecosystem.
  - [medium: Prometheus-Grafana on K8s](https://medium.com/@sdhah1999/prometheus-grafana-on-k8s-6efee4af4036)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Prometheus-Grafana on K8s in the Kubernetes Tools ecosystem.
  - [trainings.kubernauts.sh](https://trainings.kubernauts.sh)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering trainings.kubernauts.sh in the Kubernetes Tools ecosystem.
  - [magalix.com: How To Integrate OPA Into Your Kubernetes Cluster Using Kube-mgmt](https://www.magalix.com/blog/how-to-integrate-opa-into-your-kubernetes-cluster-using-kube-mgmt)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering magalix.com: How To Integrate OPA Into Your Kubernetes Cluster Using Kube-mgmt in the Kubernetes Tools ecosystem.
  - [medium: Build a Federation of Multiple Kubernetes Clusters With Kubefed' V2](https://medium.com/better-programming/build-a-federation-of-multiple-kubernetes-clusters-with-kubefed-v2-8d2f7d9e198a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Build a Federation of Multiple Kubernetes Clusters With Kubefed' V2 in the Kubernetes Tools ecosystem.
  - [medium: Single Sign-On in Kubernetes](https://medium.com/@andriisumko/single-sign-on-in-kubernetes-1ad9528350ed)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Single Sign-On in Kubernetes in the Kubernetes Tools ecosystem.
  - [medium: Kubernetes in a nutshell — tutorial for beginners 🌟🌟](https://medium.com/swlh/kubernetes-in-a-nutshell-tutorial-for-beginners-caa442dfd6c0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Kubernetes in a nutshell — tutorial for beginners 🌟🌟 in the Kubernetes Tools ecosystem.
  - [dzone: Bootstrapping Java Kubernetes Apps With Spring Initializr and K8s' Initializer 🌟](https://dzone.com/articles/bootstrapping-java-kubernetes-apps-no-yaml)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Bootstrapping Java Kubernetes Apps With Spring Initializr and K8s' Initializer 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Production Ready CI/CD Pipeline with Kubernetes](https://medium.com/awsblogs/ci-cd-with-kubernetes-3c29e8073c38)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Production Ready CI/CD Pipeline with Kubernetes in the Kubernetes Tools ecosystem.
  - [myweblearner.com: Kubernetes(k8s) Readiness and Liveness Probe](https://myweblearner.com/springboot_k8s_readiness_liveness.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering myweblearner.com: Kubernetes(k8s) Readiness and Liveness Probe in the Kubernetes Tools ecosystem.
  - [medium.com: Attacking Kubernetes clusters using the Kubelet API](https://medium.com/faun/attacking-kubernetes-clusters-using-the-kubelet-api-abafc36126ca)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: Attacking Kubernetes clusters using the Kubelet API in the Kubernetes Tools ecosystem.
  - [itnext.io: Breaking down and fixing Kubernetes](https://itnext.io/breaking-down-and-fixing-kubernetes-4df2f22f87c3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering itnext.io: Breaking down and fixing Kubernetes in the Kubernetes Tools ecosystem.
  - [ishantgaurav.in: Complete Application Deployment using Kubernetes](https://ishantgaurav.in/2021/06/22/complete-application-deployment-using-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ishantgaurav.in: Complete Application Deployment using Kubernetes in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Deploy a Python API With Docker and Kubernetes](https://betterprogramming.pub/python-fastapi-kubernetes-gcp-296e0dc3abb6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Deploy a Python API With Docker and Kubernetes in the Kubernetes Tools ecosystem.
  - [cncf.io: Kubernetes Ingress gRPC example with a Dune quote service](https://www.cncf.io/blog/2021/09/24/kubernetes-ingress-grpc-example-with-a-dune-quote-service)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io: Kubernetes Ingress gRPC example with a Dune quote service in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: How To Create a NoOps Deployment With GitHub Actions' Kubernetes and Shipa](https://betterprogramming.pub/how-to-create-a-noops-deployment-with-github-actions-kubernetes-and-shipa-18aab208fe7a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: How To Create a NoOps Deployment With GitHub Actions' Kubernetes and Shipa in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: Deploying a Simple Golang Web App to Kubernetes](https://levelup.gitconnected.com/deploying-simple-golang-webapp-to-kubernetes-25dc1736dcc4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: Deploying a Simple Golang Web App to Kubernetes in the Kubernetes Tools ecosystem.
  - [medium.com/groupon-eng: LoadBalancer Services using Kubernetes in Docker' (kind)](https://medium.com/groupon-eng/loadbalancer-services-using-kubernetes-in-docker-kind-694b4207575d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/groupon-eng: LoadBalancer Services using Kubernetes in Docker' (kind)== in the Kubernetes Tools ecosystem.
  - [devxblog.hashnode.dev: Deploying Microservices with Persistent Volumes in' Kubernetes - Kubernetes Microservice Flask Application](https://devxblog.hashnode.dev/kubernetes-microservice-flask-application-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering devxblog.hashnode.dev: Deploying Microservices with Persistent Volumes in' Kubernetes - Kubernetes Microservice Flask Application in the Kubernetes Tools ecosystem.
  - [medium.com/@hmquan08011996: Setup Microservices on Kubernetes — Write a' Configuration File](https://medium.com/@hmquan08011996/set-up-microservice-on-kubernetes-write-config-file-8df7c2b07a4c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@hmquan08011996: Setup Microservices on Kubernetes — Write a' Configuration File in the Kubernetes Tools ecosystem.
  - [baeldung.com: Deploy a Spring Boot Application to OpenShift with Spring' Cloud Kubernetes 🌟](https://www.baeldung.com/spring-boot-deploy-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering baeldung.com: Deploy a Spring Boot Application to OpenShift with Spring' Cloud Kubernetes 🌟 in the Kubernetes Tools ecosystem.
  - [hashicorp.com: Getting Started with Ambassador and Consul Using Kubernetes' Initializer](https://www.hashicorp.com/blog/getting-started-with-ambassador-and-consul-using-kubernetes-initializer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering hashicorp.com: Getting Started with Ambassador and Consul Using Kubernetes' Initializer in the Kubernetes Tools ecosystem.
  - [medium: Consul-Kubernetes Ingress Gateways and L7 Traffic Management](https://medium.com/hashicorp-engineering/consul-kubernetes-ingress-gateways-and-l7-traffic-management-178957dcd934)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Consul-Kubernetes Ingress Gateways and L7 Traffic Management in the Kubernetes Tools ecosystem.
  - [medium: Kittens-as-a-Service: Layer 7 Traffic Management & Security with' Consul Connect](https://medium.com/hashicorp-engineering/kittens-as-a-service-layer-7-traffic-management-security-with-consul-connect-f5965fac5aa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Kittens-as-a-Service: Layer 7 Traffic Management & Security with' Consul Connect in the Kubernetes Tools ecosystem.
  - [cncf.io: Implementing GitOps on Kubernetes Using K3s, Rancher, Vault and' Argo CD](https://www.cncf.io/blog/2020/11/12/implementing-gitops-on-kubernetes-using-k3s-rancher-vault-and-argo-cd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cncf.io: Implementing GitOps on Kubernetes Using K3s, Rancher, Vault and' Argo CD in the Kubernetes Tools ecosystem.
  - [eksworkshop.com/x-ray/microservices](https://eksworkshop.com/x-ray/microservices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering eksworkshop.com/x-ray/microservices in the Kubernetes Tools ecosystem.
  - [eksworkshop.com: Configure Cluster Autoscaler (CA)](https://eksworkshop.com/scaling/deploy_ca)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering eksworkshop.com: Configure Cluster Autoscaler (CA) in the Kubernetes Tools ecosystem.
  - [medium: create your first application on aws eks kubernetes](https://medium.com/faun/create-your-first-application-on-aws-eks-kubernetes-cluster-874ee9681293)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: create your first application on aws eks kubernetes in the Kubernetes Tools ecosystem.
  - [AWS App Mesh with EKS and Canary deployment](https://medium.com/@anupam.s1602/aws-app-mesh-with-eks-and-canary-deployment-5503d9ba95d6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering AWS App Mesh with EKS and Canary deployment in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Deploying Application on Amazon EKS](https://aws.plainenglish.io/deploying-application-on-amazon-eks-211eb46c069c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Deploying Application on Amazon EKS in the Kubernetes Tools ecosystem.
  - [medium.com/bb-tutorials-and-thoughts: How to Build and Deploy MERN Stack' on Azure AKS](https://medium.com/bb-tutorials-and-thoughts/how-to-build-and-deploy-mern-stack-on-azure-aks-c25eaf27b9d0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/bb-tutorials-and-thoughts: How to Build and Deploy MERN Stack' on Azure AKS in the Kubernetes Tools ecosystem.
  - [medium: Verifying container signatures on Kubernetes with Gatekeeper](https://medium.com/@LachlanEvenson/verifying-container-signatures-on-kubernetes-with-gatekeeper-19a4519c3016)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Verifying container signatures on Kubernetes with Gatekeeper in the Kubernetes Tools ecosystem.
  - [medium: Mutating Kubernetes resources with Gatekeeper](https://medium.com/@LachlanEvenson/mutating-kubernetes-resources-with-gatekeeper-3e5585d49ead)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Mutating Kubernetes resources with Gatekeeper in the Kubernetes Tools ecosystem.
  - [medium.com/@hari.balagopal: Create a Helm chart automatically from Kubernetes' YAMLs](https://medium.com/@hari.balagopal/create-a-helm-chart-automatically-from-kubernetes-yamls-91a4c1bf8cc5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/@hari.balagopal: Create a Helm chart automatically from Kubernetes' YAMLs== in the Kubernetes Tools ecosystem.
  - [redhatdemocentral.gitlab.io](https://redhatdemocentral.gitlab.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering redhatdemocentral.gitlab.io in the Kubernetes Tools ecosystem.
  - [developers.redhat.com: Developing on OpenShift (katacoda interactive learning)' 🌟](https://developers.redhat.com/courses/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com: Developing on OpenShift (katacoda interactive learning)' 🌟 in the Kubernetes Tools ecosystem.
  - [Deploying Docker Images to OpenShift](https://dzone.com/articles/deploying-docker-images-to-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Deploying Docker Images to OpenShift in the Kubernetes Tools ecosystem.
  - [medium: Tutorial : Secure your API with x509 Mutual Authentication with' Spring Boot on OpenShift4](https://medium.com/@erfin.feluzy/tutorial-secure-your-api-with-x509-mutual-authentication-with-spring-boot-on-openshift4-416a00a47af8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Tutorial : Secure your API with x509 Mutual Authentication with' Spring Boot on OpenShift4 in the Kubernetes Tools ecosystem.
  - [medium.com: Red Hat OpenShift Virtualization in nested VMware vSphere Cluster](https://medium.com/@carlosedp/red-hat-openshift-virtualization-in-nested-vmware-vsphere-56c5e5d76a80)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: Red Hat OpenShift Virtualization in nested VMware vSphere Cluster in the Kubernetes Tools ecosystem.
  - [JBoss Web Server Operator 🌟](https://access.redhat.com/documentation/en-us/red_hat_jboss_web_server/5.4/html-single/red_hat_jboss_web_server_for_openshift/index)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering JBoss Web Server Operator 🌟 in the Kubernetes Tools ecosystem.
  - [developers.redhat.com: How to deploy a Java application on Kubernetes in' minutes](https://developers.redhat.com/developer-sandbox/how-to-deploy-java-application-in-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com: How to deploy a Java application on Kubernetes in' minutes in the Kubernetes Tools ecosystem.
  - [developers.redhat.com: Welcome to the Developer Sandbox for Red Hat OpenShift.' Part 1: Deploying full-stack JavaScript applications to the Developer Sandbox for Red Hat OpenShift](https://developers.redhat.com/developer-sandbox/activities/deploying-full-stack-javascript-applications-to-the-sandbox/part1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com: Welcome to the Developer Sandbox for Red Hat OpenShift.' Part 1: Deploying full-stack JavaScript applications to the Developer Sandbox for Red Hat OpenShift in the Kubernetes Tools ecosystem.
  - [IBM Cloud Pak Playbook](https://cloudpak8s.io/apps/cp4a_overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering IBM Cloud Pak Playbook in the Kubernetes Tools ecosystem.
  - [docs.openshift.com: OpenShift GitOps](https://docs.openshift.com/container-platform/4.8/cicd/gitops/understanding-openshift-gitops.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.openshift.com: OpenShift GitOps in the Kubernetes Tools ecosystem.
  - [medium.com/adaltas: GitOps in practice, deploy Kubernetes applications with' ArgoCD](https://medium.com/adaltas/gitops-in-practice-deploy-kubernetes-applications-with-argocd-ca170ce8aba3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/adaltas: GitOps in practice, deploy Kubernetes applications with' ArgoCD in the Kubernetes Tools ecosystem.
  - [gokuldevops.medium.com: Argo CD-Sample app deployment](https://gokuldevops.medium.com/argo-cdsample-app-deployment-56b36601f279)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering gokuldevops.medium.com: Argo CD-Sample app deployment in the Kubernetes Tools ecosystem.
  - [medium.com/@martin.hodges: Spring Boot CI/CD on Kubernetes using Terraform,' Ansible and GitHub: Part 12](https://medium.com/@martin.hodges/use-terraform-ansible-and-github-actions-to-automate-running-your-spring-boot-application-on-e82424da828e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@martin.hodges: Spring Boot CI/CD on Kubernetes using Terraform,' Ansible and GitHub: Part 12 in the Kubernetes Tools ecosystem.
  - [medium.com: Installing an OKD 4.5 Cluster](https://medium.com/@craig_robinson/guide-installing-an-okd-4-5-cluster-508a2631cbee)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com: Installing an OKD 4.5 Cluster in the Kubernetes Tools ecosystem.
  - [wkrzywiec.medium.com: How to deploy application on Kubernetes with Helm](https://wkrzywiec.medium.com/how-to-deploy-application-on-kubernetes-with-helm-39f545ad33b8)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering wkrzywiec.medium.com: How to deploy application on Kubernetes with Helm in the Kubernetes Tools ecosystem.
  - [josephrodriguezg.medium.com: Deploying a Spring Boot microservice in Kubernetes' using Helm charts](https://josephrodriguezg.medium.com/deploying-a-spring-boot-application-in-kubernetes-using-helm-charts-5c04c2d46e16)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering josephrodriguezg.medium.com: Deploying a Spring Boot microservice in Kubernetes' using Helm charts in the Kubernetes Tools ecosystem.
  - [Part 1](https://medium.com/@simionrazvan/simple-spring-boot-microservice-deployed-in-kubernetes-using-docker-and-nexus-part-1-b581e3ca8916)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Part 1 in the Kubernetes Tools ecosystem.
  - [kubernetes-advocate.medium.com: CI/CD with Dockers and Jenkins 🌟](https://kubernetes-advocate.medium.com/ci-cd-with-dockers-and-jenkins-70b6f801f9f7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kubernetes-advocate.medium.com: CI/CD with Dockers and Jenkins 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@devml2016: Let’s Start Automation using Jenkins, Docker, GitHub](https://medium.com/@devml2016/lets-start-automation-using-jenkins-docker-github-d5f8d019ec4a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@devml2016: Let’s Start Automation using Jenkins, Docker, GitHub in the Kubernetes Tools ecosystem.
  - [medium: Just commit your code and your docker server is ready (jenkins +' github + docker)](https://medium.com/@deepanshuyadavv11/task1-integrating-github-jenkins-and-docker-d66a817774be)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Just commit your code and your docker server is ready (jenkins +' github + docker) in the Kubernetes Tools ecosystem.
  - [ittroubleshooter.in: Run Parallel Builds in Kubernetes Cluster with Jenkins' Pipeline 🌟](https://ittroubleshooter.in/run-parallel-build-kubernetes-cluster-jenkins)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ittroubleshooter.in: Run Parallel Builds in Kubernetes Cluster with Jenkins' Pipeline 🌟 in the Kubernetes Tools ecosystem.
  - [medium: DevOps CI/CD Pipeline with Jenkins, Kubernetes & GitHub: Part 1' 🌟](https://medium.com/the-programmer/ci-cd-pipeline-with-jenkins-github-part-1-c057a31b5297)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: DevOps CI/CD Pipeline with Jenkins, Kubernetes & GitHub: Part 1' 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Building CI/CD Pipeline with Jenkins, Kubernetes & GitHub: Part' 2 🌟](https://medium.com/the-programmer/building-ci-cd-pipeline-with-jenkins-kubernetes-github-part-2-cbb6c366aa41)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Building CI/CD Pipeline with Jenkins, Kubernetes & GitHub: Part' 2 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Deploy Docker Image To Kubernetes Cluster Using Jenkins 🌟](https://medium.com/codex/deploy-docker-image-to-kubernetes-cluster-using-jenkins-8182cc0a8de7)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Deploy Docker Image To Kubernetes Cluster Using Jenkins 🌟 in the Kubernetes Tools ecosystem.
  - [lakshaws.medium.com: CI/CD Pipeline for Dockerized Applications](https://lakshaws.medium.com/ci-cd-pipeline-for-dockerized-applications-f1003e821812)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering lakshaws.medium.com: CI/CD Pipeline for Dockerized Applications in the Kubernetes Tools ecosystem.
  - [praveendavidmathew.medium.com: Data driven testing per request without using' data file](https://praveendavidmathew.medium.com/data-driven-testing-per-request-without-using-data-file-aeb573b4f63a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering praveendavidmathew.medium.com: Data driven testing per request without using' data file in the Kubernetes Tools ecosystem.
  - [dzone: Continuous Deployment on Kubernetes With Spinnaker](https://dzone.com/articles/continuous-deployment-on-kubernetes-with-spinnaker)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Continuous Deployment on Kubernetes With Spinnaker in the Kubernetes Tools ecosystem.
  - [medium.com/@kachidude007: Setting up an Access Token in GitLab for a Jenkins' Pipeline](https://medium.com/@kachidude007/setting-up-an-access-token-in-gitlab-for-a-jenkins-pipeline-a688dd6c994a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@kachidude007: Setting up an Access Token in GitLab for a Jenkins' Pipeline in the Kubernetes Tools ecosystem.
  - [blog.griddynamics.com: Developing a modular pipeline library to improve' DevOps collaboration](https://blog.griddynamics.comdeveloping-a-modular-pipeline-library-to-improve-devops-collaboration)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.griddynamics.com: Developing a modular pipeline library to improve' DevOps collaboration in the Kubernetes Tools ecosystem.
  - [cyberciti.biz: How to create MySQL user and grant permissions in AWS RDS](https://www.cyberciti.biz/faq/how-to-create-mysql-user-and-grant-permissions-in-aws-rds)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cyberciti.biz: How to create MySQL user and grant permissions in AWS RDS in the Kubernetes Tools ecosystem.
  - [medium: Fetch Application Inventory using Systems Manager](https://medium.com/cloud-techies/application-inventory-using-system-manager-f3eeb75d3279)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Fetch Application Inventory using Systems Manager in the Kubernetes Tools ecosystem.
  - [dzone.com: From Spring Boot Microservices to Lambda Functions 🌟🌟](https://dzone.com/articles/from-java-microservices-to-lambda-functions-a-jour)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone.com: From Spring Boot Microservices to Lambda Functions 🌟🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/@adrianarba: CI/CD defined through terraform using AWS CodePipeline,' AWS CodeCommit, and AWS CodeBuild](https://medium.com/@adrianarba/ci-cd-defined-through-terraform-using-aws-codepipeline-aws-codecommit-and-aws-codebuild-12ade4d9cfa3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==medium.com/@adrianarba: CI/CD defined through terraform using AWS CodePipeline,' AWS CodeCommit, and AWS CodeBuild== in the Kubernetes Tools ecosystem.
  - [faun.pub: Using AWS Session Manager With Ansible To Execute Playbook On' EC2](https://faun.pub/using-aws-session-manager-with-ansible-to-execute-playbook-on-ec2-ac97fa17b187)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Using AWS Session Manager With Ansible To Execute Playbook On' EC2 in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Build a Cloud-Native Multiprocessing Framework](https://betterprogramming.pub/build-a-cloud-native-multiprocessing-framework-b33cfc2c02b9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Build a Cloud-Native Multiprocessing Framework in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Trigger, Function, Message | Brandi McCall](https://aws.plainenglish.io/trigger-function-message-12f117b7f067)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Trigger, Function, Message | Brandi McCall in the Kubernetes Tools ecosystem.
  - [towardsaws.com: Integrating Python, Amazon API Gateway, Lambda, SQS, and' SNS Services | Brandi McCall](https://towardsaws.com/integrating-python-amazon-api-gateway-lambda-sqs-and-sns-services-6015631d5527)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering towardsaws.com: Integrating Python, Amazon API Gateway, Lambda, SQS, and' SNS Services | Brandi McCall in the Kubernetes Tools ecosystem.
  - [Azure DevOps Demo Generator 🌟](https://azuredevopsdemogenerator.azurewebsites.net)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Azure DevOps Demo Generator 🌟 in the Kubernetes Tools ecosystem.
  - [reddit.com: Automate Infrastructure Deployments on Microsoft Azure with' Terraform and Jenkins](https://www.reddit.com/r/Terraform/comments/h0tdq3/automate_infrastructure_deployments_on_microsoft)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering reddit.com: Automate Infrastructure Deployments on Microsoft Azure with' Terraform and Jenkins in the Kubernetes Tools ecosystem.
  - [medium.com/tea-networks: Kubernetes & CI/CD Pipeline](https://medium.com/tea-networks/kubernetes-ci-cd-pipeline-c028aea17535)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/tea-networks: Kubernetes & CI/CD Pipeline in the Kubernetes Tools ecosystem.
  - [medium: Setting up KafkaSource to send data and displayed with Knative event-display](https://medium.com/@jweng1/setting-up-kafkasource-to-send-data-and-displayed-with-knative-event-display-33891b253442)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Setting up KafkaSource to send data and displayed with Knative event-display in the Kubernetes Tools ecosystem.
  - [medium: Install Istio on Azure Kubernetes cluster using Terraform](https://medium.com/@vipinagarwal18/install-istio-on-azure-kubernetes-cluster-using-terraform-214f6d3f611)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Install Istio on Azure Kubernetes cluster using Terraform in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Create an Amazon EKS Fargate Cluster and Managed' Node Group Using Terraform](https://betterprogramming.pub/with-latest-updates-create-amazon-eks-fargate-cluster-and-managed-node-group-using-terraform-bc5cfefd5773)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Create an Amazon EKS Fargate Cluster and Managed' Node Group Using Terraform in the Kubernetes Tools ecosystem.
  - [fsgeorgee.medium.com: Growing out of Heroku to Terraform, Docker and AWS](https://fsgeorgee.medium.com/growing-out-of-heroku-to-terraform-docker-and-aws-69e66df4132d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering fsgeorgee.medium.com: Growing out of Heroku to Terraform, Docker and AWS in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: Automate and Configure Your RDS Database With Terraform' 🌟](https://betterprogramming.pub/automate-and-configure-your-rds-database-with-terraform-898fd4b8990d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: Automate and Configure Your RDS Database With Terraform' 🌟 in the Kubernetes Tools ecosystem.
  - [the-tech-guy.in: Automating LAMP deployment using Terraform and Ansible](https://the-tech-guy.in/2022/03/08/automating-lamp-config-using-terraform-and-ansible)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering the-tech-guy.in: Automating LAMP deployment using Terraform and Ansible in the Kubernetes Tools ecosystem.
  - [betterprogramming.pub: All Hail the Monolith — Celebrating the Verbosity' of the Unified Architecture in Terraform](https://betterprogramming.pub/all-hail-the-monolith-celebrating-the-verbosity-of-the-unified-architecture-in-terraform-81b53e3a03ae)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering betterprogramming.pub: All Hail the Monolith — Celebrating the Verbosity' of the Unified Architecture in Terraform in the Kubernetes Tools ecosystem.
  - [faun.pub: AWS ECS Blue/Green Deployment Setup Using Terraform](https://faun.pub/aws-ecs-blue-green-deployment-setup-using-terraform-b56bb4f656ea)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: AWS ECS Blue/Green Deployment Setup Using Terraform in the Kubernetes Tools ecosystem.
  - [aws.plainenglish.io: Creating a custom EC2 module using Terraform](https://aws.plainenglish.io/creating-a-custom-ec2-module-using-terraform-59c9896c2df2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering aws.plainenglish.io: Creating a custom EC2 module using Terraform in the Kubernetes Tools ecosystem.
  - [medium.com/@zeloygabri: Deploying 2-Tier AWS Architecture using Terraform](https://medium.com/@zeloygabri/deploying-2-tier-aws-architecture-using-terraform-b4167b035751)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@zeloygabri: Deploying 2-Tier AWS Architecture using Terraform in the Kubernetes Tools ecosystem.
  - [christopher-lawshe.medium.com: Building infrastructure with Terraform: EC2,' Jenkins, S3 and more](https://christopher-lawshe.medium.com/building-infrastructure-with-terraform-ec2-jenkins-s3-and-more-4ec30f53a44a)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering christopher-lawshe.medium.com: Building infrastructure with Terraform: EC2,' Jenkins, S3 and more in the Kubernetes Tools ecosystem.
  - [towardsaws.com: How to Deploy Two-Tier AWS Architecture with Terraform?](https://towardsaws.com/how-to-deploy-two-tier-aws-architecture-with-terraform-59db7b11dd47)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering ==towardsaws.com: How to Deploy Two-Tier AWS Architecture with Terraform?== in the Kubernetes Tools ecosystem.
  - [mahira-technology.medium.com: Automating AWS CodePipeline Setup with Terraform:' Streamline Your CI/CD Workflow](https://mahira-technology.medium.com/deploying-aws-codepipeline-with-terraform-d6613979d0b6)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering mahira-technology.medium.com: Automating AWS CodePipeline Setup with Terraform:' Streamline Your CI/CD Workflow in the Kubernetes Tools ecosystem.
  - [medium.com/@Tyler.Gallimore: Deploying Apache Web Server on AWS EC2 with' Terraform and Docker](https://medium.com/@Tyler.Gallimore/deploying-apache-web-server-on-aws-ec2-with-terraform-and-docker-6c315c81c024)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@Tyler.Gallimore: Deploying Apache Web Server on AWS EC2 with' Terraform and Docker in the Kubernetes Tools ecosystem.
  - [medium.com/geekculture: Monitoring your system with Docker + Grafana + Prometheus' + Node](https://medium.com/geekculture/monitoring-your-system-with-docker-grafana-prometheus-node-d7fae11416f3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/geekculture: Monitoring your system with Docker + Grafana + Prometheus' + Node in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: GitOps: CI/CD using GitHub Actions and ArgoCD' on Kubernetes](https://levelup.gitconnected.com/gitops-ci-cd-using-github-actions-and-argocd-on-kubernetes-909d85d37746)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: GitOps: CI/CD using GitHub Actions and ArgoCD' on Kubernetes in the Kubernetes Tools ecosystem.
  - [medium.com/geekculture: GitOps — Github Actions K8s Deploy Workflow](https://medium.com/geekculture/gitops-github-actions-k8s-deploy-workflow-54f0d9a1d11b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/geekculture: GitOps — Github Actions K8s Deploy Workflow in the Kubernetes Tools ecosystem.
  - [eggboy.medium.com: CI/CD Java apps securely to Azure Kubernetes Service' with GitHub Action — Part 1](https://eggboy.medium.com/ci-cd-java-apps-securely-to-azure-kubernetes-service-with-github-action-part-1-16393af4d097)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering eggboy.medium.com: CI/CD Java apps securely to Azure Kubernetes Service' with GitHub Action — Part 1 in the Kubernetes Tools ecosystem.
  - [kaleshreya907.medium.com: GitHub Actions: Netflix Deployment](https://kaleshreya907.medium.com/step2a-install-docker-and-run-sonarqube-container-faa42d01f5fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering kaleshreya907.medium.com: GitHub Actions: Netflix Deployment in the Kubernetes Tools ecosystem.
  - [medium.com/@ebonyymonae: Github Actions and Automation](https://medium.com/@ebonyymonae/github-actions-and-automation-9637aa06af64)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@ebonyymonae: Github Actions and Automation in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: GitHub Actions, self-hosted runners on Amazon' EKS & spot instances](https://levelup.gitconnected.com/github-actions-self-hosted-runners-on-amazon-eks-spot-instances-bc3abcd5d38f)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: GitHub Actions, self-hosted runners on Amazon' EKS & spot instances in the Kubernetes Tools ecosystem.
  - [medium.com/@eduardo854: Building Your GitOps Pipeline with GitHub Actions,' DockerHub, and Helm Repository](https://medium.com/@eduardo854/building-your-gitops-pipeline-with-github-actions-dockerhub-and-helm-repository-553c4873116e)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@eduardo854: Building Your GitOps Pipeline with GitHub Actions,' DockerHub, and Helm Repository in the Kubernetes Tools ecosystem.
  - [blog.devgenius.io: Running the OpenTelemetry Demo App in Kubernetes](https://blog.devgenius.io/running-opentelemetry-demo-app-in-kubernetes-95dccd613e0b)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.devgenius.io: Running the OpenTelemetry Demo App in Kubernetes in the Kubernetes Tools ecosystem.
  - [sitepoint.com: A Guide to Serverless Functions and How to Deploy Them](https://www.sitepoint.com/gatsby-mdx-blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering sitepoint.com: A Guide to Serverless Functions and How to Deploy Them in the Kubernetes Tools ecosystem.
## Local Development (4)

### Legacy Cluster Tools

#### Minishift

  - **(2020)** [opensource.com: Set up Minishift and run Jenkins on Linux](https://opensource.com/article/20/11/minishift-linux) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Step-by-step guide outlining how to install Minishift on Linux and run a Jenkins instance inside it. This provides baseline knowledge of legacy platforms, but modern architectures should use OpenShift Local.
### Red Hat OpenShift Local

#### Installation

  - **(2020)** [youtube: CodeReady Containers - Easy OpenShift Container Platform 4.5 Installation](https://www.youtube.com/watch?v=CJMdSQVFVik) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video walk-through highlighting automated local configuration of OpenShift Platform 4.5 using CodeReady Containers. It simplifies hypervisor set up and cluster bootstrapping, serving as a historical baseline for modern Red Hat OpenShift Local techniques.
#### Process Automation (1)

  - **(2020)** [CodeReady Containers - Red Hat Decision Manager Install Demo](https://gitlab.com/redhatdemocentral/rhcs-rhdm-install-demo) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — An automated installation demo for launching Red Hat Decision Manager on CodeReady Containers (CRC). While valuable for understanding legacy deployment footprints, modern architectures replace CRC with Red Hat OpenShift Local and migrate Decision Manager patterns onto newer cloud-native rule engines.
  - **(2020)** [schabell.org: CodeReady Containers - Building a Cloud-Native Human Resources Process](https://www.schabell.org/2020/10/codeready-containers-building-cloud-native-hr-process.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details local development of a cloud-native Human Resources workflow using CodeReady Containers. Explains process containerization concepts on single-node platforms, though modern flows favor OpenShift Local frameworks.
## Networking

### Ingress

#### Nginx

  - **(2021)** [matthewpalmer.net: Kubernetes Ingress with Nginx Example 🌟](https://matthewpalmer.net/kubernetes-app-developer/articles/kubernetes-ingress-guide-nginx-example.html) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Step-by-step architectural breakdown of implementing an NGINX Ingress Controller to manage external-to-internal cluster routing. Synthesizes key routing constructs, TLS termination setups via cert-manager, virtual hosting paths, and session affinity configurations vital for modern production topologies.
### Multicluster

#### eBPF

  - **(2021)** [piotrminkowski.com: Kubernetes Multicluster with Kind and Cilium](https://piotrminkowski.com/2021/10/25/kubernetes-multicluster-with-kind-and-cilium) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — In-depth guide constructing a multi-cluster networking topology utilizing Kind and Cilium's eBPF-driven data plane. Outlines how to leverage ClusterMesh to enable secure, low-latency, and high-performance cross-cluster Pod-to-Pod communication without reliance on heavyweight external gateway mechanisms.
### Security (1)

#### Recipes

  - **(2021)** [==ahmetb/kubernetes-network-policy-recipes 🌟==](https://github.com/ahmetb/kubernetes-network-policy-recipes) <span class='md-tag md-tag--info'>⭐ 6144</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a2f52f76" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 11 L 20 2 L 30 4 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-a2f52f76)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The premier open-source repository for reusable NetworkPolicy templates. Provides validated configuration files to handle common cloud-native security patterns.
### eBPF (1)

#### Calico

  - **(2022)** [thenewstack.io: Maximize K3s Resource Efficiency with Calico eBPF Data Plane](https://thenewstack.io/maximize-k3s-resource-efficiency-with-calico-ebpf-data-plane) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Technical review examining performance and resource footprint improvements when deploying Calico's eBPF data plane inside lightweight K3s environments. Demonstrates significant CPU overhead reductions compared to legacy iptables architectures.
## Observability (1)

### Microservices Telemetry

#### Grafana Stack

  - **(2022)** [grafana.com: How Istio, Tempo, and Loki speed up debugging for microservices](https://grafana.com/blog/how-istio-tempo-and-loki-speed-up-debugging-for-microservices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details how to configure the unified Grafana observability stack (Loki for logs, Tempo for traces, Istio for mesh networking) to accelerate troubleshooting in microservices. Focuses on setting up automatic correlation IDs to jump from logs to tracing traces instantly.
### Monitoring

#### Message Brokers

  - **(2020)** [piotrminkowski.com: RabbitMQ Monitoring on Kubernetes](https://piotrminkowski.com/2020/09/29/rabbitmq-monitoring-on-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical tutorial focused on architecting a comprehensive RabbitMQ monitoring pipeline within Kubernetes. Illustrates how to configure Prometheus Operator's custom resources, register dedicated ServiceMonitors, and implement rich Grafana dashboard systems to observe telemetry metrics such as message rates, consumer connections, and disk storage alerts.
### OpenTelemetry

#### Governance

  - **(2021)** [devops.com: Measuring the Progress of the OpenTelemetry Project](https://devops.com/measuring-the-progress-of-the-opentelemetry-project) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical overview detailing the organizational velocity, community contributions, and consolidation patterns of the CNCF OpenTelemetry project. Synthesizes adoption telemetry and integration roadmaps with legacy APM frameworks.
#### Reliability Engineering

  - **(2022)** [itnext.io: OpenTelemetry — Understanding SLI and SLO with OpenTelemetry Demo](https://itnext.io/opentelemetry-understanding-sli-and-slo-with-opentelemetry-demo-74c1d0b263b0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural deep-dive evaluating Service Level Indicators (SLIs) and Service Level Objectives (SLOs) within an active OpenTelemetry distributed microservices demo. Explores Prometheus alerts, collector architecture, and structured telemetry processing.
### Troubleshooting

#### Azure AKS (1)

  - **(2021)** [channel9.msdn.com: Troubleshoot AKS cluster issues with AKS Diagnostics and AKS Periscope](https://learn.microsoft.com/en-us/shows/azure-friday/troubleshoot-aks-cluster-issues-with-aks-diagnostics-and-aks-periscope) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed video tutorial on troubleshooting AKS clusters with Azure Diagnostics and AKS Periscope. Explores advanced telemetry collection, container runtime log audits, network connectivity scans, and cluster-state snapshots for fast fault isolation.
#### Google GKE (1)

  - **(2021)** [cloud.google.com: Troubleshooting services on Google Kubernetes Engine by example 🌟](https://cloud.google.com/blog/products/operations/troubleshooting-services-on-google-kubernetes-engine) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official Google Cloud troubleshooting manual for GKE. Demonstrates diagnostic methodologies to address typical cluster faults, including CrashLoopBackOff states, Service route failures, Google Cloud load-balancing errors, and memory exhaustion trends.
## Observability and Testing (1)

### Metrics Monitoring

#### TPG Monitoring Stack

  - **(2022)** [docker-compose-tpg: Telegraf + Prometheus + Grafana Local Testing Environments](https://github.com/xiaopeng163/docker-compose-tpg) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A streamlined Docker Compose setup establishing a local monitoring stack with Telegraf, Prometheus, and Grafana. Excellent for local telemetry testing, dashboard debugging, and metric ingestion trials before scaling to Kubernetes systems.
## Orchestration

### AKS

#### Masterclass (1)

  - **(2023)** [**github.com/stacksimplify/azure-aks-kubernetes-masterclass 🌟**](https://github.com/stacksimplify/azure-aks-kubernetes-masterclass) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly comprehensive masterclass repository containing declarative HCL files and manifests to deploy AKS with Azure Disks, Azure Files, Application Gateway ingress, and active Azure AD integration.
### Kubernetes (2)

#### EKS Training

  - **(2025)** [eksworkshop.com](https://eksworkshop.com) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — The canonical AWS EKS workshop framework. Outlines standard cluster orchestration procedures, highlighting network configurations (AWS VPC CNI), identity management (IAM Roles for Service Accounts - IRSA), and modern storage drivers (EBS/EFS CSI).
### Kubernetes Security

#### RKE Best Practices

  - **(2021)** [stackrox.com: Part 1 - Rancher Kubernetes Engine (RKE) Security Best Practices for Cluster Setup 🌟](https://www.stackrox.io/blog/rancher-kubernetes-engine-security-part-1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Delineates critical security configurations and hardening guidelines for Rancher Kubernetes Engine (RKE) deployments. Explores secure etcd database clustering, role-based access control policies, TLS configuration, and master node network isolation.
## Platform Architecture

### CICD (2)

#### Legacy Jenkins

  - **(2022)** [==github - using jenkins pipelines with OKD==](https://github.com/openshift/origin/tree/main/examples/jenkins/pipeline) <span class='md-tag md-tag--info'>⭐ 8658</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-18bacd56" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 2 L 20 11 L 30 9 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-18bacd56)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Repository detailing baseline code configurations, sample pipelines, and deployment manifests engineered to execute scripted Jenkins procedures inside early versions of the OKD community container platform.
## Platform Deployment

### Quality Assurance (1)

#### Static Code Analysis

  - **(2020)** [SonarQube: An OpenShift-focused Docker build of Sonarqube](https://github.com/OpenShiftDemos/sonarqube-openshift-docker) <span class='md-tag md-tag--info'>⭐ 42</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-620b4685" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 13 L 20 7 L 30 2 L 40 6 L 50 3" fill="none" stroke="url(#spark-grad-620b4685)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[DOCKERFILE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A custom Docker build configuration designed to host SonarQube instances on OpenShift. Modern strategies prioritize official Helm charts or certified OpenShift Operator deployments, but this configuration highlights important historical patterns for handling stateful Java applications.
## Platform Engineering

### Architectural Insights

#### Ecosystem Tools

  - **(2025)** [**Portfolio Architecture Tooling**](https://redhatdemocentral.gitlab.io/portfolio-architecture-tooling) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A technical toolset and mapping library designed to programmatically generate clean, unified, and compliant architectural diagrams for hybrid cloud deployments. Enables platform teams to model complex networking, storage, and cluster connections cleanly.
#### Red Hat Ecosystem

  - **(2025)** [==Portfolio Architecture WorkShops 🌟==](https://redhatdemocentral.gitlab.io/portfolio-architecture-workshops) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Comprehensive architectural workshops presenting verified blueprints for complex hybrid cloud systems, retail edge strategies, and AI/ML model deployment operations. It serves as a highly detailed blueprint catalog for modern enterprise architects.
### CICD Platforms (1)

#### Azure DevOps (1)

  - **(2021)** [thomasthornton.cloud: A DevOps journey using Azure DevOps](https://thomasthornton.cloud/a-devops-journey-using-azure-devops) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive retrospective detailing the strategic transition and ongoing journey of adopting Azure DevOps for enterprise platform engineering. The guide explores centralizing pipeline definitions, managing environment gates, optimizing agent pools, and leveraging built-in boards and repositories. It highlights pragmatic challenges and structural lessons learned during real-world migrations to cloud-native delivery workflows.
### Custom Controller Patterns

#### Kubernetes Operators

  - **(2020)** [developers.redhat.com: ‘Hello, World’ tutorial with Kubernetes Operators](https://developers.redhat.com/blog/2020/08/21/hello-world-tutorial-with-kubernetes-operators) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines basic concepts of the Operator SDK to develop a "Hello World" Kubernetes custom controller. Focuses on reconciliation loop structures, Custom Resource Definition (CRD) setups, and deployment strategies.
### Enterprise Kubernetes

#### OpenShift (3)

  - **(2025)** [rcarrata.com](https://rcarrata.com) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Roberto Carratalá's technical blog features deep architectural explorations of OpenShift and enterprise Kubernetes setups. It is packed with real-world scenarios covering OAuth integrations, ingress routing configurations, and security hardeners.
### GitOps and CI-CD

#### AWS and Argo CD

  - **(2023)** [mrcloudbook.com: GitOps: Deploying Tetris on EKS Using ArgoCD](https://mrcloudbook.com/gitops-deploying-tetris-on-eks-using-argocd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A simplified tutorial mapping out the migration from manual deployments to automated GitOps workflows on AWS EKS using Argo CD. Focuses on setting up repositories, IAM credentials, and declarative reconciliations.
#### Argo ApplicationSets

  - **(2021)** [blog.argoproj.io: Getting started with ApplicationSets](https://blog.argoproj.io/getting-started-with-applicationsets-9c961611bcf0) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines technical use-cases for ApplicationSets in handling massive-scale Kubernetes rollouts, defining templating behaviors, and utilizing multi-source capabilities within modern GitOps workflows.
  - **(2020)** [blog.argoproj.io: Introducing the ApplicationSet Controller for Argo CD](https://blog.argoproj.io/introducing-the-applicationset-controller-for-argo-cd-982e28b62dc5) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Unveils the ApplicationSet Controller designed to orchestrate multi-cluster and multi-tenant Argo CD configurations from a single template. Enables automated templating of Kubernetes workloads using Git generators, directory generators, and cluster generators.
#### Argo CD and OpenShift Pipelines

  - **(2021)** [piotrminkowski.com: Kubernetes CI/CD with Tekton and ArgoCD 🌟](https://piotrminkowski.com/2021/08/05/kubernetes-ci-cd-with-tekton-and-argocd) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides the reader through building a Kubernetes-native CI/CD pipeline using Tekton for compiling, testing, and containerizing Java applications, combined with Argo CD for declarative GitOps delivery.
  - **(2020)** [developers.redhat.com: From code to production with OpenShift Pipelines and Argo CD](https://developers.redhat.com/blog/2020/09/10/from-code-to-production-with-openshift-pipelines-and-argo-cd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the deployment pipeline workflow integrating OpenShift Pipelines (based on Tekton) with Argo CD for declarative GitOps continuous delivery. The architecture promotes safe transitions from code repositories to production clusters via containerized build stages and automated resource reconciliation.
#### Argo CD Basics

  - **(2021)** [opensource.com: Get started with Argo CD 🌟](https://opensource.com/article/21/8/argo-cd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to core GitOps architectures using Argo CD. Outlines basic mechanics of reconciliation, syncing Helm charts, and navigating the GUI to verify actual and desired cluster states match.
  - **(2020)** [vzilla.co.uk: GitOps - Getting started with ArgoCD](https://vzilla.co.uk/vzilla-blog/gitops-getting-started-with-argocd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents an introductory guide to GitOps patterns using Argo CD on Kubernetes. Details installation steps, sync policies, and repo registration to facilitate baseline understanding of Git-declared state control.
#### Argo CD Plugins

  - **(2021)** [blog.argoproj.io: Introducing the AppSource Controller for ArgoCD](https://blog.argoproj.io/introducing-the-appsource-controller-for-argocd-52f21d28d643) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the AppSource controller, which enables developer self-service by letting teams define dynamic configurations without administrative intervention, improving workflow modularity.
#### Configuration Rollouts

  - **(2021)** [codefresh.io: Using Argo CD and Kustomize for ConfigMap Rollouts 🌟🌟](https://octopus.com/blog/using-argo-cd-and-kustomize-for-configmap-rollouts) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Resolves the issue of non-rolling updates for Kubernetes ConfigMaps. Leverages Kustomize hash generation alongside Argo CD to trigger rolling updates across associated deployments upon configuration changes.
#### GitLab Integration (1)

  - **(2021)** [openshift.com: Building GitLab Pipelines on OpenShift](https://www.redhat.com/en/blog/building-openshift-pipelines-with-gitlab) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details configuring GitLab CI runners inside an OpenShift environment to native execution. Addresses cluster authentication, caching mechanisms, and security contexts when executing pipeline scripts inside restricted Pod environments.
#### Multi-Cluster GitOps (2)

  - **(2021)** [infracloud.io: Multicluster GitOps with ArgoCD](https://www.infracloud.io/blogs/multicluster-gitops-argocd) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines architectural choices for orchestrating multi-cluster GitOps setups with Argo CD, focusing on hub-and-spoke topologies versus decentralized controls to manage cluster-level dependencies.
  - **(2020)** [developers.redhat.com: Introduction to Tekton and Argo CD for multicluster development](https://developers.redhat.com/blog/2020/09/03/introduction-to-tekton-and-argo-cd-for-multicluster-development) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains the synergy between Tekton tasks and Argo CD to drive multi-cluster continuous delivery. Defines the boundaries where Tekton controls cloud-native container builds while Argo CD manages drift resolution across remote target clusters.
#### Serverless Workflows

  - **(2020)** [developers.redhat.com: Building modern CI/CD workflows for serverless applications with Red Hat OpenShift Pipelines and Argo CD, Part 1](https://developers.redhat.com/blog/2020/10/01/building-modern-ci-cd-workflows-for-serverless-applications-with-red-hat-openshift-pipelines-and-argo-cd-part-1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates building CI/CD patterns for Knative-based serverless workloads using OpenShift Pipelines and Argo CD. Focuses on minimizing operational overhead and optimizing cold starts by isolating the build execution phase from deployment management.
#### Tool Assessment

  - **(2020)** [youtube: Exploring The Cloud-native Kubernetes CI/CD Pipeline Tool Landscape](https://www.youtube.com/watch?v=5XWwjyikWMQ&feature=emb_logo&ab_channel=Konveyor)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive landscape review of cloud-native CI/CD tooling, mapping out the evolution of Jenkins, Tekton, Argo, and Flux. Provides architectural guidelines for selecting pipeline engines based on scalability and declarative execution goals.
### GitOps and Deployment

#### Flux Ecosystem

  - **(2020)** [A Complete Step by Step Guide to Implementing a GitOps Workflow with Flux 🌟](https://managedkube.com/gitops/flux/weaveworks/guide/tutorial/2020/05/01/a-complete-step-by-step-guide-to-implementing-a-gitops-workflow-with-flux.html) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An early step-by-step tutorial outlining GitOps workflows with original Flux tools. Offers historical context but must be updated to Flux v2 and the modern GitOps Toolkit conventions.
### Machine Learning Operations

#### OpenShift AI

  - **(2023)** [==OpenShift AI Examples==](https://github.com/CastawayEGR/openshift-ai-examples) <span class='md-tag md-tag--info'>⭐ 25</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d70ac3e8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 5 L 20 12 L 30 9 L 40 2 L 50 6" fill="none" stroke="url(#spark-grad-d70ac3e8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A community collection of machine learning workflows and notebooks deployed on Red Hat OpenShift AI. Details deployment pipelines for distributed training, model serving, and GPU resource slicing.
## Provisioning (3)

### Bootstrapping

#### Bare Metal

  - **(2020)** [itnext.io: Up and running out of the cloud — How to setup the Masters using kubeadm bootstrap](https://itnext.io/kubernetes-journey-up-and-running-out-of-the-cloud-how-to-setup-the-masters-using-kubeadm-9a496a14fbc1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on manual describing how to deploy a HA multi-master Kubernetes cluster outside cloud environments using Kubeadm. Focuses on setting up an external load balancer to sit in front of the API servers, and configure stacked etcd pools on bare-metal systems.
## Public Cloud Providers

### AWS (1)

#### Amplify Development

  - **(2021)** [youtube: Build a Music Sharing App with Amazon S3 and AWS Amplify](https://www.youtube.com/watch?v=6W2TuBDaaiI&ab_channel=AliSpittel) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical video guide demonstrating rapid application development using AWS Amplify. Showcases integration with Amazon S3 for media storage, DynamoDB for metadata, and Cognito for user authentication.
#### Asset Management

  - **(2024)** [==github.com/aws-samples/aws-auto-inventory: AWS Automated Inventory 🌟==](https://github.com/aws-samples/aws-auto-inventory) <span class='md-tag md-tag--info'>⭐ 254</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-03c68d2a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 6 L 20 9 L 30 6 L 40 7 L 50 6" fill="none" stroke="url(#spark-grad-03c68d2a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An automated system designed to discover, track, and catalog AWS infrastructure assets across multiple regions and accounts. Leverages Serverless functions and AWS Config to maintain real-time compliance dashboards.
#### Best Practices

  - **(2026)** [github.com/aws-samples 🌟](https://github.com/aws-samples) <span class='md-tag md-tag--warning'>[MULTI CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The master organization containing AWS-curated reference architectures, deployment scripts, and code samples. Serves as a vital baseline for implementing multi-account strategies, serverless setups, and security blueprints.
#### DevOps Demos

  - **(2025)** [github.com/miztiik/AWS-Demos](https://github.com/miztiik/AWS-Demos) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A rich repository compiling hundreds of AWS hands-on architecture guides and automated scripts. Spans serverless computing, databases, event routing, and container-based architectural patterns.
#### Operational Excellence

  - **(2025)** [==github.com/aws-samples/aws-customer-playbook-framework 🌟==](https://github.com/aws-samples/aws-customer-playbook-framework) <span class='md-tag md-tag--info'>⭐ 661</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bda63131" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 6 L 20 8 L 30 13 L 40 13 L 50 2" fill="none" stroke="url(#spark-grad-bda63131)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive operational framework that helps organizations define, structure, and automate IT playbooks and runbooks on AWS. Enhances incident response protocols and disaster recovery simulations.
#### Resource Tagging

  - **(2023)** [==github.com/aws-samples: Guide to Resource Tagging Automation==](https://github.com/aws-samples/resource-tagging-automation) <span class='md-tag md-tag--info'>⭐ 55</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-91f30120" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 3 L 20 6 L 30 3 L 40 8 L 50 11" fill="none" stroke="url(#spark-grad-91f30120)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Automated cloud governance solution leveraging AWS Lambda to automatically append standardized metadata tags onto AWS resources. Simplifies enterprise cost allocation and compliance enforcement operations.
#### Security and WAF

  - **(2023)** [==github.com/aws-samples/aws-waf-ops-dashboards==](https://github.com/aws-samples/aws-waf-ops-dashboards) <span class='md-tag md-tag--info'>⭐ 56</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-53ba8f50" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 6 L 20 3 L 30 2 L 40 10 L 50 2" fill="none" stroke="url(#spark-grad-53ba8f50)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Contains CloudFormation templates and Athena query scripts to establish centralized dashboards for AWS Web Application Firewall (WAF) logs. Empowers security operations to detect anomalous traffic patterns.
#### Training Archives

  - **(2020)** [==github.com/aws-samples/aws-training-demo==](https://github.com/amazon-archives/aws-training-demo) <span class='md-tag md-tag--info'>⭐ 128</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d5ac2cc8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 8 L 30 13 L 40 6 L 50 6" fill="none" stroke="url(#spark-grad-d5ac2cc8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Archived AWS training demonstration repository. Grounding verification confirms this repository is formally archived by Amazon, meaning it should be treated purely as an architectural reference rather than a base for production provisioning templates.
### GCP

#### Enterprise Platform

  - **(2026)** [github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform) <span class='md-tag md-tag--warning'>[MULTI CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The master landing organization for Google Cloud Platform's open-source projects, APIs, and CLI utilities. Holds structural frameworks, SDKs, and enterprise infrastructure design tools.
## Quality Assurance (2)

### API Testing Automation

#### Newman Integration

##### Jenkins Pipelines (2)

  - **(2020)** [LerryAlexander: Postman + Newman API Automated Tests running on a Jenkins' Pipeline 🌟](https://github.com/LerryAlexander/postman_jenkins_api_tests) <span class='md-tag md-tag--info'>⭐ 3</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-04f3535c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 10 L 20 11 L 30 3 L 40 4 L 50 11" fill="none" stroke="url(#spark-grad-04f3535c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on running automated Postman test suites through Newman CLI inside a Jenkins Pipeline. Live Grounding confirms this is a standard integration step for end-to-end REST API verification. By surfacing test execution failures in Jenkins console output, teams can safely block regression deployments.
## Reference Architectures

### Artifact Registries

#### Docker Images (1)

  - **(2020)** [DockerHub OpenShift Demos](https://hub.docker.com/u/openshiftdemos) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Registry hosting pre-built container images optimized for the OpenShiftDemos organization. Though partially legacy due to secure private registry practices, it serves as a valuable public catalog of application runtimes.
### Enterprise Demos

#### Community Repositories

  - **(2021)** [github.com/OpenShiftDemos 🌟](https://github.com/OpenShiftDemos) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A central repository for community-created deployment scenarios and platform showcases on OpenShift. Offers infrastructure engineers access to ready-to-use cluster testing configurations and tool deployments.
  - **(2020)** [github.com/openshiftdemos 🌟](https://github.com/openshiftdemos) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — GitHub resource hosting active and archive-state templates designed to showcase enterprise tools on OpenShift. Features simple automation scripts, platform configuration files, and middleware integration recipes.
#### Red Hat Demo Central

  - **(2022)** [gitlab.com/redhatdemocentral 🌟](https://gitlab.com/redhatdemocentral) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational Git ecosystem containing reference architectures, workshop resources, and interactive deployment scenarios for Red Hat's core platforms. Designed for architects needing to spin up reproducible, full-stack configurations on OpenShift and middleware stacks.
### Industry Verticals

#### Healthcare

  - **(2022)** [gitlab.com/redhatdemocentral: Healthcare](https://gitlab.com/redhatdemocentral/portfolio-architecture-examples/-/blob/main/healthcare.adoc) <span class='md-tag md-tag--warning'>[ASCIIDOC CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly specialized reference architecture covering the integration of healthcare workflows, real-time messaging, and patient record databases on OpenShift. Explains how to reconcile strict data compliance directives (HL7/FHIR) with highly-scalable container orchestrations.
### Interactive Learning

#### OpenShift Labs

  - **(2023)** [github.com/openshift-labs 🌟](https://github.com/openshift-labs) <span class='md-tag md-tag--warning'>[GO / YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An official repository that runs web-accessible, sandbox-styled instructional courses for OpenShift. Guides engineers through Operator lifecycle development, security tuning, and multi-tenant networking setups.
## Resource Portal

### Video Tutorials

#### Cloud PoC

  - **(2023)** [cloud quick POCs](https://www.youtube.com/channel/UCv9MUffHWyo2GgLIDLVu0KQ) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A compiled collection of video tutorials and rapid proofs-of-concept demonstrating containerization, multi-tier cloud networking, and infrastructure provisioning patterns across AWS, Azure, and Google Cloud Platform.
## Security (2)

### Admission Control

#### Go Development (1)

  - **(2020)** [dev.to: Implementing a simple K8s admission controller in Go](https://dev.to/douglasmakey/implementing-a-simple-k8s-admission-controller-in-go-2dcg) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep dive into developing custom admission control hooks using Go. Examines the mechanical process of parsing AdmissionReview requests, implementing validation logic, producing secure JSON patches for mutating workflows, and setting up local TLS validation to communicate securely with the Kubernetes API server.
### Vulnerabilities

#### Hacking Labs

  - **(2024)** [**The Kubernetes Goat**](https://github.com/madhuakula/kubernetes-goat) <span class='md-tag md-tag--info'>⭐ 5674</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d3ec5f02" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 10 L 20 5 L 30 6 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-d3ec5f02)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The premier interactive security training platform containing an intentionally vulnerable Kubernetes cluster. Designed as an educational sandbox to demonstrate real-world cluster vulnerabilities, RBAC privilege escalations, metadata exposure, and container breakout exploits.
## Security and Compliance (1)

### Cloud Security Assessments

#### AWS IAM Exploits

  - **(2022)** [BishopFox/iam-vulnerable](https://github.com/BishopFox/iam-vulnerable) <span class='md-tag md-tag--info'>⭐ 573</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-728ada7b" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 7 L 20 11 L 30 12 L 40 10 L 50 13" fill="none" stroke="url(#spark-grad-728ada7b)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[HCL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A crucial hands-on sandbox repository that deploys a library of intentionally weak and misconfigured AWS IAM privilege escalation paths using Terraform. Ideal for security engineers looking to safely simulate and audit IAM security posture.
## Security and Governance

### Identity and Access

#### OpenShift GitOps

  - **(2021)** [openshift.com: SSO Integration for the OpenShift GitOps Operator](https://www.redhat.com/en/blog/sso-integration-for-the-openshift-gitops-operator) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores integrating single sign-on (SSO) systems like Keycloak or Red Hat SSO with the OpenShift GitOps (Argo CD) operator. Facilitates role-based access control (RBAC) mappings for secure enterprise deployments.
### Platform Security

#### GitOps Security

  - **(2021)** [developers.redhat.com: Managing GitOps control planes for secure GitOps practices 🌟](https://developers.redhat.com/articles/2021/08/03/managing-gitops-control-planes-secure-gitops-practices) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses access control models, repository structure strategies, and network isolation policies to harden GitOps control planes. Assures that malicious code or human errors are contained safely within individual tenant boundaries.
#### Resource Integrity

  - **(2020)** [opensift.com: K8s Integrity Shield (tech-preview): Protecting the Integrity of Kubernetes Resources with Signature](https://www.redhat.com/en/blog/k8s-integrity-shield-tech-preview-protecting-the-integrity-of-kubernetes-resources-with-signature) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates the Kubernetes Integrity Shield technology preview, enabling signature-based verification of cluster manifests. Restricts rogue manifest updates and unauthorized resource mutations at admission-time.
### Secret Management

#### Argo CD Plugins (1)

  - **(2021)** [itnext.io: Solving ArgoCD Secret Management with the argocd-vault-plugin 🌟](https://itnext.io/argocd-secret-management-with-argocd-vault-plugin-539f104aff05) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses securing GitOps workflows by integrating HashiCorp Vault with Argo CD through the argocd-vault-plugin. Details how to avoid committing plain-text secrets to Git by dynamically injecting secrets during manifest generation.
  - **(2021)** [openshift.com: How to Use HashiCorp Vault and Argo CD for GitOps on OpenShift](https://www.redhat.com/en/blog/how-to-use-hashicorp-vault-and-argo-cd-for-gitops-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep dive on using HashiCorp Vault within OpenShift to feed sensitive parameters safely to Argo CD workloads. Addresses authorization patterns, sidecar injection, and secure credential parsing in enterprise-grade pipelines.
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
## Serverless Architectures

### AWS Lambda

#### Java Performance

  - **(2024)** [==aws-samples/serverless-java-frameworks-samples: Lambda demo with common' Java application frameworks 🌟==](https://github.com/aws-samples/serverless-java-frameworks-samples) <span class='md-tag md-tag--info'>⭐ 159</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a648a2d8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 8 L 20 10 L 30 10 L 40 9 L 50 8" fill="none" stroke="url(#spark-grad-a648a2d8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="8" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Provides deep-dive comparison and code samples for building serverless workloads with Java on AWS Lambda. Evaluates cold-start strategies, optimization techniques, and framework comparisons like Spring Cloud Function, Micronaut, and Quarkus.
### AWS Serverless

#### Cloud-Native Demo

  - **(2020)** [github.com/unitypark/aws-serverless-demos](https://github.com/unitypark/aws-serverless-demos) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A playground containing several serverless infrastructure designs compiled via AWS CDK. Serves as reference implementations for combining DynamoDB, API Gateway, and Lambda.
### Knative

#### Spring Boot (1)

  - **(2021)** [ref 9 - I have a branch that adds Docker, Kubernetes and Knative into the mix - planning on submitting a PR at some point](https://github.com/trisberg/spring-petclinic) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specific fork's branching model implementing Knative and serverless attributes onto the Spring Petclinic application. Showcases scale-to-zero configurations and event-driven architectures running on top of Kubernetes.
## Service Mesh

### Consul

#### Ingress Gateways

  - **(2021)** [consul.io: Ingress Gateways on Kubernetes 🌟](https://developer.hashicorp.com/consul/docs/north-south/ingress-gateway/k8s) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official technical guide showing how to expose microservices secured under Consul Service Mesh to public clients via Consul Ingress Gateways. Directs configurations of ingress routing tables and end-to-end connection integrity.
#### Local Development (5)

  - **(2021)** [learn.hashicorp.com: Consul Service Discovery and Mesh on Minikube 🌟](https://developer.hashicorp.com/consul/tutorials/get-started-kubernetes/kubernetes-gs-deploy?in=consul%2Fkubernetes) <span class='md-tag md-tag--warning'>[HCL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical HashiCorp tutorial teaching how to bootstrap and configure Consul Service Mesh inside Minikube. Details transparent proxy routing, catalog synchronization rules, and enforcing secure service-to-service cryptographic identities.
### GitOps (3)

#### Progressive Delivery

  - **(2023)** [github.com/stefanprodan/gitops-istio: A GitOps recipe for Progressive Delivery' with Flux v2, Flagger and Istio 🌟](https://github.com/stefanprodan/gitops-istio) <span class='md-tag md-tag--info'>⭐ 668</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-685cc944" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 3 L 20 9 L 30 6 L 40 8 L 50 13" fill="none" stroke="url(#spark-grad-685cc944)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="13" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced progressive delivery architectural recipe integrating Flux v2, Flagger, and Istio. Automates metric-driven canary releases, utilizing real-time Prometheus statistics to roll back failing application revisions with minimal user impact.
### Istio

#### Hands-On

  - **(2020)** [blog.alexellis.io: A bit of Istio before tea-time](https://blog.alexellis.io/a-bit-of-istio-before-tea-time) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Accelerated developer tutorial detailing local installations and practical evaluations of the Istio service mesh. Covers microservice configuration injections, sidecar integrations, and foundational egress traffic testing in simple configurations.
## Software Development

### Microservices (2)

#### Reference Architecture

##### Spring Petclinic

  - **(2023)** [==github.com/spring-projects/spring-petclinic==](https://github.com/spring-projects/spring-petclinic) <span class='md-tag md-tag--info'>⭐ 9303</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-69684a1a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 4 L 20 12 L 30 5 L 40 4 L 50 3" fill="none" stroke="url(#spark-grad-69684a1a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight targets the actual source code repository for the Spring Petclinic community project. Live Grounding confirms this project is an invaluable asset across the software industry to demonstrate testing, framework upgrades, Docker containerization, and platform deployment strategies. It serves as the baseline target for countless CI/CD benchmarks.
  - **(2022)** [spring-petclinic.github.io](https://spring-petclinic.github.io) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight highlights the official Spring Petclinic documentation as the premier reference application for modern Java software architectures. Live Grounding confirms its role as a testing bed for showcasing complex microservice interactions, database bindings, and telemetry configuration patterns.
##### Spring Petclinic Red Hat

  - **(2020)** [github.com/redhat-developer-demos/spring-petclinic 🌟](https://github.com/redhat-developer-demos/spring-petclinic) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight maps out Red Hat's customized developer demo fork of the Spring Petclinic project. Live Grounding indicates this version is heavily optimized for OpenShift deployments, featuring native integration with OpenShift build configs and Kubernetes secrets. It is ideal for illustrating red-hat native cloud development workflows.

---
💡 **Explore Related:** [Kubernetes](./kubernetes.md) | [Cheatsheets](./cheatsheets.md) | [Other Awesome Lists](./other-awesome-lists.md)

