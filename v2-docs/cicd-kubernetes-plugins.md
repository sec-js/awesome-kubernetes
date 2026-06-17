# CI/CD Kubernetes Plugins

!!! info "Architectural Context"
    Detailed reference for CI/CD Kubernetes Plugins in the context of Engineering Pipeline.

## Table of Contents

1. [CICD](#cicd)
  - [GitOps](#gitops)
    - [GitLab Integration](#gitlab-integration)
  - [OpenShift](#openshift)
    - [CLI Tools](#cli-tools)
    - [Pipelines](#pipelines)
    - [Synchronization](#synchronization)
1. [Software Engineering](#software-engineering)
  - [Collaborative Platforms](#collaborative-platforms)
    - [Kubernetes Integration](#kubernetes-integration)

## CICD

### GitOps

#### GitLab Integration

  - **(2024)** [==GitLab Kubernetes Agent==](https://docs.gitlab.com/user/clusters/agent) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A secure, bidirectional, and active cluster integration agent (now known as the GitLab Agent for Kubernetes) that enables enterprise GitOps workflows. Operating inside the target cluster, it pulls configurations from Git repositories, avoiding the security risk of exposing Kube-apiserver endpoints to external CI runners.
### OpenShift

#### CLI Tools

  - **(2022)** [==openshift-client==](https://plugins.jenkins.io/openshift-client) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A vital Jenkins plugin that packages and injects the OpenShift CLI (oc) command tool directly into pipeline execution containers. It enables automation scripts to easily authenticate, query, and manipulate OpenShift namespaces, security context constraints (SCCs), and route resources.
#### Pipelines

  - **(2022)** [==openshift-pipeline==](https://plugins.jenkins.io/openshift-pipeline) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A key Jenkins integration designed to trigger and coordinate OpenShift source-to-image (S2I) and binary-to-image build pipelines directly from Jenkins stages. It bridges traditional centralized orchestration with OpenShift-native application delivery models. Modern workloads are increasingly migrating toward Tekton-based OpenShift Pipelines.
#### Synchronization

  - **(2022)** [==openshift-sync==](https://plugins.jenkins.io/openshift-sync) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized Jenkins plugin designed to continuously synchronize Jenkins Job states, configurations, and build logs directly with OpenShift’s Build configurations and pipelines. By unifying build states, it provides developers with a single dashboard experience within the native OpenShift console interface.
## Software Engineering

### Collaborative Platforms

#### Kubernetes Integration

  - **(2021)** [about.gitlab.com: GitLab 14.1 released with Helm Chart Registry and Escalation Policies](https://docs.gitlab.com/releases) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details the GitLab 14.1 release, highlighting its integrated Helm chart registry and custom escalation policies. Explains how teams can store and manage Kubernetes deployment packaging files directly alongside their application source code.

---
💡 **Explore Related:** [Jenkins](./jenkins.md) | [Sonarqube](./sonarqube.md) | [Stackstorm](./stackstorm.md)

