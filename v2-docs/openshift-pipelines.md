---
description: "Top Openshift Pipelines resources for 2026, AI-ranked: GitHub: Eclipse JKube, Fabric8 Pipeline Library and more — curated Cloud Native tools, guides and references."
---
# OpenShift Pipelines

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/openshift-pipelines/).

!!! info "Architectural Context"
    Detailed reference for OpenShift Pipelines in the context of Engineering Pipeline.

## App Development

### CICD

#### Jenkins Pipelines

  - **(2018)** [Fabric8 Pipeline Library](https://github.com/fabric8io/fabric8-pipeline-library) <span class='md-tag md-tag--info'>⭐ 436</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b4183287" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 13 L 20 11 L 30 8 L 40 6 L 50 7" fill="none" stroke="url(#spark-grad-b4183287)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — A reusable Jenkins Pipeline helper library that supports automated environments, build phases, and release setups within OpenShift frameworks. It is largely deprecated, superseded by modern Jenkins plugins or native Tekton pipelines.
#### Legacy Frameworks

  - **(2018)** [CI/CD with fabric8](https://fabric8.io/guide/cdelivery.html) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Details the classic continuous delivery orchestration patterns supported by early versions of the Fabric8 framework. Although helpful for understanding early pipeline structures, these setups are largely replaced by native GitOps and modern cloud-native pipelines.
## CICD and DevOps

### Enterprise Jenkins

#### OpenShift Integration

  - **(2019)** [blog.openshift.com: Deploying OpenShift Applications to Multiple Datacenters (with Jenkins)](https://www.redhat.com/en/blog/deploying-openshift-applications-multiple-datacenters) <span class='md-tag md-tag--warning'>[GROOVY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Advanced architectural walkthrough on utilizing Jenkins to orchestrate synchronized microservice deployments across federated, multi-datacenter OpenShift cluster topologies.
### GitOps and Pipelines

#### GitHub Actions Integration

  - **(2020)** [developers.redhat.com: OpenShift Actions: Deploy to Red Hat OpenShift directly from your GitHub repository](https://developers.redhat.com/blog/2020/02/13/openshift-actions-deploy-to-red-hat-openshift-directly-from-your-github-repository) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide on utilizing official Red Hat OpenShift GitHub Actions. Empowers developers to directly interface GitHub workflow pipelines with OpenShift clusters, deploying applications seamlessly via container commands or oc CLI bindings.
### Source-To-Image

#### OpenShift S2I Workflow

  - **(2018)** [developers.redhat.com: Source versus binary S2I workflows with Red Hat OpenShift Application Runtimes](https://developers.redhat.com/blog/2018/09/26/source-versus-binary-s2i-workflows-with-red-hat-openshift-application-runtimes) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Structural analysis of S2I builders, explaining how source repositories are dynamically injected into standardized runtime base images to produce highly secure production containers.
## Cloud-Native Java

### Build Tools

#### Eclipse JKube

##### Source Code

  - **(2020)** [**GitHub: Eclipse JKube**](https://github.com/eclipse-jkube/jkube) <span class='md-tag md-tag--info'>⭐ 849</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2dc7ec48" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 13 L 20 4 L 30 5 L 40 12 L 50 6" fill="none" stroke="url(#spark-grad-2dc7ec48)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — The active GitHub repository for Eclipse JKube, housing Maven/Gradle plugins, extensions, and core libraries. Live Grounding indicates robust ongoing community support, enabling local resource generation, deployment, and hot-swapping inside active clusters. The project is crucial for bridging the gap between standard Java compilation and Kubernetes runtimes.
## Developer Experience

### Inner Loop Development

#### OpenShift Odo CLI

  - **(2024)** [==ODO: OpenShift Command line for Developers 🌟==](https://github.com/redhat-developer/odo) <span class='md-tag md-tag--info'>⭐ 841</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b8a707bf" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 13 L 20 9 L 30 10 L 40 12 L 50 9" fill="none" stroke="url(#spark-grad-b8a707bf)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official repository for odo, a developer-centric CLI for Kubernetes and OpenShift. Abstracting away complex Kubernetes YAML manifests, odo prioritizes fast iterative code deployments directly to the cluster from local IDE directories.
  - **(2021)** [piotrminkowski.com: Java Development on OpenShift with odo](https://piotrminkowski.com/2021/02/05/java-development-on-openshift-with-odo) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide walking through modern Java/Spring Boot development on OpenShift utilizing the odo CLI. Highlights rapid hot-reloading configurations, remote debugging execution, and container integration workflows.
  - **(2021)** [developers.redhat.com: Developing your own custom devfiles for odo 2.0](https://developers.redhat.com/blog/2021/02/12/developing-your-own-custom-devfiles-for-odo-2-0) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to design custom devfile definitions to adapt odo 2.0 pipelines to unique corporate microservice stacks. Unifies local dev environments with enterprise build rules.
  - **(2020)** [developers.redhat.com: Enterprise Kubernetes development with odo: The CLI tool for developers](https://developers.redhat.com/blog/2020/06/16/enterprise-kubernetes-development-with-odo-the-cli-tool-for-developers) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Enterprise developer introduction to the Red Hat odo CLI. Demonstrates how to write code, execute deployment commands, and inspect active microservices without needing deep knowledge of the underlying cluster APIs.
  - **(2020)** [developers.redhat.com: Kubernetes integration and more in odo 2.0](https://developers.redhat.com/blog/2020/10/06/kubernetes-integration-and-more-in-odo-2-0) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights structural improvements introduced in odo 2.0, notably standardizing configurations on Devfiles, which allows cross-platform, repeatable developer workspace environment definitions.
## Platform Architecture

### CICD (1)

#### Jenkins Pipelines (1)

  - **(2017)** [Simply Explained: OpenShift and Jenkins Pipelines](https://www.redhat.com/en/blog/jenkins-pipelines) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An explanatory article outlining the core architectural concepts of continuous integration pipelines inside enterprise containers. Focuses on orchestrating builds, scaling execution agents dynamically, and promoting stable application rollouts.
#### Tekton Pipelines

  - **(2021)** [openshift.com: OpenShift Pipelines Advanced Triggers Part 1 - Triggering Different Project Builds in the Same Repository](https://www.redhat.com/en/blog/openshift-pipelines-advanced-triggers-part-1-triggering-different-project-builds-in-the-same-repository) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides advanced architecture examples for configuring custom triggers with OpenShift Pipelines. Demonstrates how to write custom interceptors to execute discrete workflows when localized directory pathways change within shared code repos.
  - **(2020)** [github: OpenShift Pipelines Node.js Tutorial](https://github.com/csantanapr/faststart2020-pipelines-lab) <span class='md-tag md-tag--info'>⭐ 5</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7b45bf9a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 11 L 20 3 L 30 13 L 40 2 L 50 2" fill="none" stroke="url(#spark-grad-7b45bf9a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Specialized quick-start laboratory focusing on Node.js application continuous delivery with OpenShift Pipelines. Guides developers through configuring trigger conditions and executing basic Source-to-Image (S2I) build pipelines.
  - **(2020)** [developers.redhat.com: Modern web applications on OpenShift, Part 4: Openshift Pipelines](https://developers.redhat.com/blog/2020/04/27/modern-web-applications-on-openshift-part-4-openshift-pipelines) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Part of a series detailing modern web application architectures on OpenShift. Explores configuring Tekton pipelines to construct, optimize, and serve static frontend code alongside active microservices.
## Software Engineering

### Build Systems

#### Fabric8 Maven Plugin

  - **(2023)** [==github - fabric8, maven plugin==](https://github.com/fabric8io/fabric8-maven-plugin) <span class='md-tag md-tag--info'>⭐ 334</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bdcaaf1e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 11 L 10 2 L 20 3 L 30 7 L 40 2 L 50 4" fill="none" stroke="url(#spark-grad-bdcaaf1e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — A Maven plugin designed to package Java projects into lightweight Docker/OCI images and generate corresponding Kubernetes resource manifests automatically. Double-Evidence: Note that this project is archived and superseded by Eclipse JKube in modern development environments.

---
💡 **Explore Related:** [Jenkins Alternatives](./jenkins-alternatives.md) | [Keptn](./keptn.md) | [Gitops](./gitops.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

