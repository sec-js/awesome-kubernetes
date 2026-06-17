# OpenShift Pipelines

!!! info "Architectural Context"
    Detailed reference for OpenShift Pipelines in the context of Engineering Pipeline.

## App Development

### CICD

#### Jenkins Pipelines

  - **(2018)** [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library) <span class='md-tag md-tag--info'>⭐ 436</span> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A reusable Jenkins Pipeline helper library that supports automated environments, build phases, and release setups within OpenShift frameworks. It is largely deprecated, superseded by modern Jenkins plugins or native Tekton pipelines.
#### Legacy Frameworks

  - **(2018)** [CI/CD with fabric8](http://fabric8.io/guide/cdelivery.html) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> — Details the classic continuous delivery orchestration patterns supported by early versions of the Fabric8 framework. Although helpful for understanding early pipeline structures, these setups are largely replaced by native GitOps and modern cloud-native pipelines.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [OCP 4.2 - Jenkins image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.2/html/images/using-images#images-other-jenkins-agent)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.redhat.com in the Kubernetes Tools ecosystem.
  - [docs.openshift.com: OpenShift 3.11 Pipeline Builds with OpenShift Jenkins Image and OpenShift DSL](https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/developer_guide/tutorials#dev-guide-openshift-pipeline-builds)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.redhat.com in the Kubernetes Tools ecosystem.
  - [Dzone: 4 ways to build applications in openshift](https://dzone.com/articles/4-ways-to-build-applications-in-openshift-1)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Dzone: 4 ways to build applications in openshift in the Kubernetes Tools ecosystem.
  - [Dzone: a quick guide to deploying java apps on openshift](https://dzone.com/articles/a-quick-guide-to-deploying-java-apps-on-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Dzone: a quick guide to deploying java apps on openshift in the Kubernetes Tools ecosystem.
## CICD and DevOps

### Enterprise Jenkins

#### OpenShift Integration

  - **(2020)** [==Jenkins Docker Image for Openshift v3==](https://github.com/openshift/jenkins) <span class='md-tag md-tag--info'>⭐ 261</span> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Red Hat maintained OpenShift integration image for running Jenkins natively within OpenShift clusters. Includes pre-configured plugins, service-account integration, and S2I build configurations customized for enterprise OpenShift v3/v4 environments.
  - **(2020)** [cloudowski.com: Jenkins on OpenShift - how to use and customize it in a cloud-native way 🌟](https://cloudowski.com/articles/jenkins-on-openshift) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced engineering blog detailing customized, cloud-native deployments of Jenkins on OpenShift. Explains how to leverage dynamic provisioning, custom configurations, and cluster-wide persistent volumes to stabilize Jenkins infrastructure.
  - **(2020)** [github.com/siamaksade/jenkins-blueocean](https://github.com/siamaksade/jenkins-blueocean) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Public demonstration repository providing configured manifests for launching Jenkins Blue Ocean on OpenShift clusters. Acts as a blueprint for visualizing pipeline stages in Red Hat environments.
  - **(2019)** [blog.openshift.com: Deploying jenkins on openshift - part 1](https://www.redhat.com/en/blog/deploying-jenkins-on-openshift-part-1) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enterprise guide illustrating structural configuration, route definition, and persistent storage bindings for deploying stable Jenkins masters inside OpenShift namespaces.
  - **(2019)** [blog.openshift.com: Improving jenkins performance on openshift - part 2](https://www.redhat.com/en/blog/improving-jenkins-performance-on-openshift-part-2) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural performance tuning guide for running large-scale Jenkins deployments on OpenShift. Addresses JVM optimization, garbage collection configuration, build concurrency limit management, and persistent storage class optimizations.
  - **(2019)** [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.redhat.com/en/blog/deploying-openshift-applications-multiple-datacenters) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced architectural walkthrough on utilizing Jenkins to orchestrate synchronized microservice deployments across federated, multi-datacenter OpenShift cluster topologies.
  - **(2018)** [slideshare.net: OpenShift Container Platform CI/CD Build & Deploy 🌟](https://www.slideshare.net/mozillabros/openshift-container-platform-cicd-build-deploy) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Slides and architectural diagrams outlining automated CI/CD pipelines on OpenShift Container Platform. Covers deployment triggers, image stream lifecycles, and rolling updates.
### GitOps and Pipelines

#### GitHub Actions Integration

  - **(2020)** [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide on utilizing official Red Hat OpenShift GitHub Actions. Empowers developers to directly interface GitHub workflow pipelines with OpenShift clusters, deploying applications seamlessly via container commands or oc CLI bindings.
### Source-To-Image

#### OpenShift S2I Workflow

  - **(2018)** [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Structural analysis of S2I builders, explaining how source repositories are dynamically injected into standardized runtime base images to produce highly secure production containers.
## Cloud Native and K8s

### Kubernetes API

#### Go Client

  - **(2026)** [==kubernetes/client-go: Go client for Kubernetes 🌟==](https://github.com/kubernetes/client-go) <span class='md-tag md-tag--info'>⭐ 9837</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The official Go SDK for managing Kubernetes clusters. It features critical API client mechanics like Informers, Lister-Watchers, work queues, and rate-limiting structures to build high-performance production controllers.
## Cloud-Native Java

### Build Tools

#### Eclipse JKube

##### Source Code

  - **(2020)** [**GitHub: Eclipse JKube**](https://github.com/eclipse-jkube/jkube) <span class='md-tag md-tag--info'>⭐ 849</span> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The active GitHub repository for Eclipse JKube, housing Maven/Gradle plugins, extensions, and core libraries. Live Grounding indicates robust ongoing community support, enabling local resource generation, deployment, and hot-swapping inside active clusters. The project is crucial for bridging the gap between standard Java compilation and Kubernetes runtimes.
## Developer Experience

### Inner Loop Development

#### OpenShift Odo CLI

  - **(2024)** [==ODO: OpenShift Command line for Developers 🌟==](https://github.com/redhat-developer/odo) <span class='md-tag md-tag--info'>⭐ 841</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official repository for odo, a developer-centric CLI for Kubernetes and OpenShift. Abstracting away complex Kubernetes YAML manifests, odo prioritizes fast iterative code deployments directly to the cluster from local IDE directories.
  - **(2021)** [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide walking through modern Java/Spring Boot development on OpenShift utilizing the odo CLI. Highlights rapid hot-reloading configurations, remote debugging execution, and container integration workflows.
  - **(2021)** [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to design custom devfile definitions to adapt odo 2.0 pipelines to unique corporate microservice stacks. Unifies local dev environments with enterprise build rules.
  - **(2020)** [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enterprise developer introduction to the Red Hat odo CLI. Demonstrates how to write code, execute deployment commands, and inspect active microservices without needing deep knowledge of the underlying cluster APIs.
  - **(2020)** [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights structural improvements introduced in odo 2.0, notably standardizing configurations on Devfiles, which allows cross-platform, repeatable developer workspace environment definitions.
## Platform Architecture

### CICD (1)

#### Jenkins Pipelines (1)

  - **(2021)** [OpenShift Container Pipelines Samples 🌟](https://github.com/redhat-cop/container-pipelines) <span class='md-tag md-tag--info'>⭐ 160</span> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A repository of pipeline configurations originally curated by the Red Hat Community of Practice. Useful for understanding legacy configurations on OpenShift 3 and 4, though modern pipelines have shifted to Tekton architectures.
  - **(2021)** [OpenShift Pipeline Library 🌟](https://github.com/redhat-cop/pipeline-library) <span class='md-tag md-tag--info'>⭐ 51</span> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A collection of shared pipeline libraries providing modular groovy wrapper methods for OpenShift deployments. Most implementations are archived as enterprise standards have pivoted completely toward Tekton Pipelines and Argo CD GitOps pipelines.
  - **(2019)** [developers.redhat.com - Get started with Jenkins CI/CD in Red Hat OpenShift 4](https://developers.redhat.com/blog/2019/05/02/get-started-with-jenkins-ci-cd-in-red-hat-openshift-4) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A structured tutorial on initializing Jenkins-driven continuous delivery setups in early OpenShift 4 environments. Highlights configuration, service account configuration, and deploying pre-packaged Jenkins templates on-cluster.
  - **(2017)** [Simply Explained: OpenShift and Jenkins Pipelines](https://www.redhat.com/en/blog/jenkins-pipelines) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An explanatory article outlining the core architectural concepts of continuous integration pipelines inside enterprise containers. Focuses on orchestrating builds, scaling execution agents dynamically, and promoting stable application rollouts.
#### Legacy Jenkins

  - **(2022)** [==github - using jenkins pipelines with OKD==](https://github.com/openshift/origin/tree/main/examples/jenkins/pipeline) <span class='md-tag md-tag--info'>⭐ 8658</span> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — Repository detailing baseline code configurations, sample pipelines, and deployment manifests engineered to execute scripted Jenkins procedures inside early versions of the OKD community container platform.
  - **(2017)** [slideshare.net: CI/CD with Openshift and Jenkins 🌟](https://www.slideshare.net/arilivigni/cicd-with-openshift-and-jenkins) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical presentation showing continuous integration configurations on earlier OpenShift releases using Jenkins servers. Serves as a useful blueprint for examining migration paths from early Jenkins structures to cloud-native alternatives.
#### Tekton Pipelines

  - **(2026)** [github.com/openshift/pipelines-tutorial](https://github.com/openshift/pipelines-tutorial) <span class='md-tag md-tag--info'>⭐ 322</span> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comprehensive learning path and hands-on laboratory environment focused on Tekton. Provides configurations for Tasks, Pipelines, PipelineRuns, and Trigger EventListeners on OpenShift clusters, validating cloud-native automation patterns.
  - **(2020)** [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab) <span class='md-tag md-tag--info'>⭐ 5</span> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Specialized quick-start laboratory focusing on Node.js application continuous delivery with OpenShift Pipelines. Guides developers through configuring trigger conditions and executing basic Source-to-Image (S2I) build pipelines.
  - **(2021)** [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.redhat.com/en/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides advanced architecture examples for configuring custom triggers with OpenShift Pipelines. Demonstrates how to write custom interceptors to execute discrete workflows when localized directory pathways change within shared code repos.
  - **(2020)** [openshift.com: Cloud-Native CI/CD with OpenShift Pipelines based on Tekton](https://www.redhat.com/en/blog/cloud-native-ci-cd-with-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Introduces OpenShift Pipelines as the modern serverless, cloud-native standard built on the Tekton project. Explains how Tekton's CRD-first strategy delivers secure, isolated build containers without a centralized daemon or controller bottlenecks.
  - **(2020)** [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Part of a series detailing modern web application architectures on OpenShift. Explores configuring Tekton pipelines to construct, optimize, and serve static frontend code alongside active microservices.
### DevSecOps

#### Security Automation

  - **(2022)** [openshift.com: Using OpenShift Pipelines to Automate Red Hat Advanced Cluster Security for Kubernetes](https://www.redhat.com/en/blog/using-openshift-pipelines-to-automate-red-hat-advanced-cluster-security-for-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This architectural resource focuses on integrating container security scans directly into OpenShift Pipelines (Tekton) using Red Hat Advanced Cluster Security (RHACS). It provides continuous security analysis by scanning build environments and deployment configurations, automatically blocking vulnerable code prior to final deployment phases.
## Software Engineering

### Build Systems

#### Fabric8 Maven Plugin

  - **(2023)** [==github - fabric8, maven plugin==](https://github.com/fabric8io/fabric8-maven-plugin) <span class='md-tag md-tag--info'>⭐ 334</span> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A Maven plugin designed to package Java projects into lightweight Docker/OCI images and generate corresponding Kubernetes resource manifests automatically. Double-Evidence: Note that this project is archived and superseded by Eclipse JKube in modern development environments.

---
💡 **Explore Related:** [Argo](./argo.md) | [CI/CD](./cicd.md) | [Gitops](./gitops.md)

