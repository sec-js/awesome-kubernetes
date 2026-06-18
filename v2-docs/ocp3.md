# OCP 3

!!! info "Architectural Context"
    Detailed reference for OCP 3 in the context of The Container Stack.

## Table of Contents

1. [App Development](#app-development)
  - [Packaging](#packaging)
    - [Helm Charts](#helm-charts)
1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Observability](#observability)
  - [Application Monitoring](#application-monitoring)
    - [Java JMX](#java-jmx)
1. [Platform Architecture](#platform-architecture)
  - [Administration](#administration)
    - [Automation](#automation)
  - [Automation](#automation-1)
    - [Ansible](#ansible)
    - [Community Tools](#community-tools)
  - [Core Concepts](#core-concepts)
    - [Kubernetes Pods](#kubernetes-pods)
  - [High Availability](#high-availability)
    - [Disaster Recovery](#disaster-recovery)
    - [Stretch Clusters](#stretch-clusters)
  - [Infrastructure](#infrastructure)
    - [Comparisons](#comparisons)
  - [Local Dev](#local-dev)
    - [Legacy Platform](#legacy-platform)
  - [Multicluster](#multicluster)
    - [Disaster Recovery](#disaster-recovery-1)
    - [Kubernetes Federation](#kubernetes-federation)
  - [Resource Management](#resource-management)
    - [Autoscaling](#autoscaling)
    - [Governance](#governance)
  - [Resources](#resources)
    - [Learning paths](#learning-paths)
1. [Security](#security)
  - [Encryption](#encryption)
    - [.NET Core](#net-core)

## App Development

### Packaging

#### Helm Charts

  - **(2019)** [blog.openshift.com/: From Templates to Openshift Helm Charts](https://www.redhat.com/en/blog/from-templates-to-openshift-helm-charts) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on porting proprietary OpenShift templates into standard Helm Charts, improving cross-platform compatibility and simplifying application rollout processes.
  - **(2019)** [Templating on OpenShift: should I use Helm templates or OpenShift templates? 🌟](https://www.theodo.com/en-fr/blog/openshift-what-templates-should-you-use-helm-or-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comparative analysis contrasting OpenShift native templates with Helm charts. Outlines how Helm's global community, revision tracking, and subchart structures provide a superior template solution for complex microservice environments.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [developers.redhat.com: **Debugging applications** within Red Hat OpenShift containers](https://developers.redhat.com/blog/2020/01/09debugging-applications-within-red-hat-openshift-containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com in the Kubernetes Tools ecosystem.
  - [blog.openshift.com/how-full-is-my-cluster-part-5-a-capacity-management-dashboard](https://blog.openshift.com/how-full-is-my-cluster-part-5-a-capacity-management-dashboard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.openshift.com in the Kubernetes Tools ecosystem.
  - [**Uncontained.io**](https://uncontained.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering uncontained.io in the Kubernetes Tools ecosystem.
  - [blog.openshift.com: Introduction to GitOps with OpenShift](https://blog.openshift.comintroduction-to-gitops-with-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.openshift.com: Introduction to GitOps with OpenShift in the Kubernetes Tools ecosystem.
  - [learn.openshift.com: GitOps introduction](https://learn.openshift.com/introduction/gitops-introduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering learn.openshift.com: GitOps introduction in the Kubernetes Tools ecosystem.
  - [blog.openshift.com: is it too late to integrate GitOps?](https://blog.openshift.comis-it-too-late-to-integrate-gitops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.openshift.com: is it too late to integrate GitOps? in the Kubernetes Tools ecosystem.
  - [blog.openshift.com: OpenShift Authentication Integration with ArgoCD](https://blogopenshift.com/openshift-authentication-integration-with-argocd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.openshift.com: OpenShift Authentication Integration with ArgoCD in the Kubernetes Tools ecosystem.
  - [Container-native virtualization allows to run and manage virtual machine workloads alongside container workloads](https://access.redhat.com/documentation/en-us/openshift_container_platform/4.2/html/container-native_virtualization/container-native-virtualization-2-1-release-notes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Container-native virtualization allows to run and manage virtual machine workloads alongside container workloads in the Kubernetes Tools ecosystem.
  - [How to Run HA Elasticsearch (ELK) on Red Hat OpenShift](https://portworx.com/run-ha-elasticsearch-elk-red-hat-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering How to Run HA Elasticsearch (ELK) on Red Hat OpenShift in the Kubernetes Tools ecosystem.
  - [developers.redhat.com: Installing debugging tools into a Red Hat OpenShift' container with **oc-inject**](https://developers.redhat.com/blog/2020/01/15installing-debugging-tools-into-a-red-hat-openshift-container-with-oc-inject)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com: Installing debugging tools into a Red Hat OpenShift' container with **oc-inject** in the Kubernetes Tools ecosystem.
  - [dzone: 8 Options for Capturing Thread Dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: 8 Options for Capturing Thread Dumps in the Kubernetes Tools ecosystem.
  - [Quotas setting per project](https://docs.openshift.com/container-platform/4.2/applications/quotas/quotas-setting-per-project.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Quotas setting per project in the Kubernetes Tools ecosystem.
  - [Quotas setting across multiple projects](https://docs.openshift.com/container-platform/4.2/applications/quotas/quotas-setting-across-multiple-projects.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Quotas setting across multiple projects in the Kubernetes Tools ecosystem.
  - [Source-to-Image (S2I) Build](https://docs.openshift.com/container-platform/3.11/architecture/core_concepts/builds_and_image_streams.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Source-to-Image (S2I) Build in the Kubernetes Tools ecosystem.
## Observability

### Application Monitoring

#### Java JMX

  - **(2017)** [developers.redhat.com: Troubleshooting java applications on openshift (Jolokia)](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers on using Jolokia, an HTTP/JSON bridge for JMX, to securely query and troubleshoot Java microservices deployed inside Red Hat OpenShift pods.
## Platform Architecture

### Administration

#### Automation

  - **(2020)** [developers.redhat.com: Customizing OpenShift project creation 🌟](https://developers.redhat.com/blog/2020/02/05/customizing-openshift-project-creation) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details dynamic project onboarding techniques for OpenShift administrators. Teaches how to configure customized templates that automatically enforce security contexts, default quotas, and custom networking parameters upon namespace creation.
### Automation (1)

#### Ansible

  - **(2023)** [GitHub redhat-cop: Ansible Role 🌟](https://github.com/redhat-cop/infra-ansible) <span class='md-tag md-tag--info'>⭐ 219</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e0754050" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 6 L 20 13 L 30 10 L 40 10 L 50 12" fill="none" stroke="url(#spark-grad-e0754050)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="12" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A structured repository of Ansible automation roles customized for provisioning, maintaining, and configuring OpenShift resources. Simplifies operations such as authentication, user management, and day-2 configurations.
#### Community Tools

  - **(2026)** [Red Hat Communities of Practice](https://github.com/redhat-cop) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The master platform profile of Red Hat's Communities of Practice. Contains scripts, custom operator codes, and automated scaffolding for cluster setups, management, and resource governing processes.
### Core Concepts

#### Kubernetes Pods

  - **(2018)** [blog.openshift.com/ - Kubernetes: A Pod’s Life 🌟](https://www.redhat.com/en/blog/kubernetes-pods-life) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A fundamental exploration of the life cycle of a Kubernetes Pod. Outlines start sequences, init container routines, readiness/liveness checks, and termination processes, establishing a baseline for container orchestration troubleshooting.
### High Availability

#### Disaster Recovery

  - **(2019)** [blog.openshift.com/: Stateful Workloads and the Two Data Center Conundrum](https://www.redhat.com/en/blog/stateful-workloads-and-the-two-data-center-conundrum) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the persistence challenges associated with stateful microservices running across multi-site cluster architectures. Evaluates split-brain hazards and suggests synchronous storage configurations to guarantee data integrity.
#### Stretch Clusters

  - **(2019)** [blog.openshift.com/: How to survive an outage and live to tell about it!](https://www.redhat.com/en/blog/metro-area-openshift-stretch-cluster-how-to-survive-an-outage-and-live-to-tell-about-it) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Analyzes the design of Metro-Area stretch clusters on OpenShift, ensuring high availability in case of datacenter outages. Discusses network transit criteria, ETCD consensus configurations, and storage replications.
### Infrastructure

#### Comparisons

  - **(2020)** [claydesk.com: Google Cloud App Engine Vs Red Hat OpenShift](https://www.claydesk.com/ecampus/google-cloud-app-engine-vs-red-hat) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes key platform differences between Google Cloud App Engine and OpenShift. Compares scaling, cluster management boundaries, provider dependencies, and operational flexibility when deploying enterprise workloads.
### Local Dev

#### Legacy Platform

  - **(2018)** [blog.openshift.com/: Using OpenShift 3 on your **local environment** 🌟](https://blog.openshift.com/using-openshift-3-on-your-local-environment) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — An older guide outlining the local instantiation of OpenShift 3 development environments using Minishift. Today, OpenShift Local (formerly CodeReady Containers) is the recommended utility for spinning up a local OCP 4 instance.
### Multicluster

#### Disaster Recovery (1)

  - **(2021)** [blog.openshift.com/tag/multi-datacenter](https://www.redhat.com/en/blog?f[0]=taxonomy_blog_post_category_tid:107161&f[1]=taxonomy_topic_tid:75521) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A thematic curation of architectural entries covering multi-cluster synchronization, active-active topologies, global service routing, and deployment configurations utilizing Advanced Cluster Management.
#### Kubernetes Federation

  - **(2021)** [**KubeFed Operator**](https://operatorhub.io/operator/kubefed-operator) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The Kubernetes Federation (KubeFed) Operator designed to coordinate configurations across multiple distinct clusters. In 2026, KubeFed has been largely archived, superseded by Red Hat Advanced Cluster Management (RHACM) and Open Cluster Management (OCM).
### Resource Management

#### Autoscaling

  - **(2020)** [developers.redhat.com: Testing memory-based horizontal pod autoscaling on OpenShift 🌟](https://developers.redhat.com/blog/2020/03/19/testing-memory-based-horizontal-pod-autoscaling-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A diagnostic tutorial explaining how to design, execute, and inspect Horizontal Pod Autoscaler scaling metrics based on container RAM thresholds. Includes guidelines for generating stable test scenarios.
#### Governance

  - **(2020)** [OpenShift 4 Resource Management](https://www.youtube.com/watch?v=JC_PB1yZcIc) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An informative session demonstrating effective scheduling, configuration, and governing mechanics of OpenShift 4 resources. Highlights the use of LimitRanges, ResourceQuotas, and Node selectors.
  - **(2019)** [techbeatly.com: How to create, increase or decrease project quota](https://techbeatly.com/how-to-create-increase-or-decrease-project-quota-in-openshift) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on managing project resource limits inside OpenShift namespaces. Explores configuring quotas via the oc CLI to enforce hard boundaries on CPU, RAM, and storage allocations.
### Resources

#### Learning paths

  - **(2019)** [certdepot.net: OpenShift Free available resources 🌟](https://www.certdepot.net/openshift-free-available-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An educational index detailing free courses, interactive sandbox playgrounds, and study materials for professionals pursuing official Red Hat OpenShift certifications.
## Security

### Encryption

#### .NET Core

  - **(2018)** [developers.redhat.com: Securing .NET Core on OpenShift using HTTPS](https://developers.redhat.com/blog/2018/10/12/securing-net-core-on-openshift-using-https) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through configuring ASP.NET Core microservices with end-to-end TLS encryption on OpenShift. Discusses dynamic integration of local server certificates using OpenShift's service serving certificates feature.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Openshift](./openshift.md) | [Serverless](./serverless.md)

