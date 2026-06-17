# OCP 3

!!! info "Architectural Context"
    Detailed reference for OCP 3 in the context of The Container Stack.

## App Development

### Packaging

#### Helm Charts

  - **(2019)** [blog.openshift.com/: From Templates to Openshift Helm Charts](https://www.redhat.com/en/blog/from-templates-to-openshift-helm-charts) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on porting proprietary OpenShift templates into standard Helm Charts, improving cross-platform compatibility and simplifying application rollout processes.
  - **(2019)** [Templating on OpenShift: should I use Helm templates or OpenShift templates? 🌟](https://www.theodo.com/en-fr/blog/openshift-what-templates-should-you-use-helm-or-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--warning'>[EMERGING]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A comparative analysis contrasting OpenShift native templates with Helm charts. Outlines how Helm's global community, revision tracking, and subchart structures provide a superior template solution for complex microservice environments.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [Container-native virtualization allows to run and manage virtual machine workloads alongside container workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.2/html/container-native_virtualization/container-native-virtualization-2-1-release-notes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.redhat.com in the Kubernetes Tools ecosystem.
  - [learn.openshift.com: GitOps introduction](https://developers.redhat.com/learn/openshift/foundations-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering developers.redhat.com in the Kubernetes Tools ecosystem.
  - [blog.openshift.com/how-full-is-my-cluster-part-5-a-capacity-management-dashboard](https://www.redhat.com/en/blog/how-full-is-my-cluster-part-5-a-capacity-management-dashboard)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering www.redhat.com in the Kubernetes Tools ecosystem.
  - [Quotas setting per project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.2/html/applications/quotas#quotas-setting-per-project)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.redhat.com in the Kubernetes Tools ecosystem.
  - [Source-to-Image (S2I) Build](https://docs.redhat.com/en/documentation/openshift_container_platform/3.11/html/architecture/core-concepts#architecture-core-concepts-builds-and-image-streams)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering docs.redhat.com in the Kubernetes Tools ecosystem.
  - [dzone: 8 Options for Capturing Thread Dumps](https://dzone.com/articles/how-to-take-thread-dumps-7-options)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: 8 Options for Capturing Thread Dumps in the Kubernetes Tools ecosystem.
## CI-CD

### GitOps

#### Migration Strategies

  - **(2021)** [blog.openshift.com/: is it too late to integrate GitOps?](https://www.redhat.com/en/blog/is-it-too-late-to-integrate-gitops) 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — Curator Insight maps the path for legacy environments migrating to continuous sync models. Live Grounding reviews incremental conversion blueprints to safe declarative setups under OpenShift. It acts as an advisory piece for migration architects.
#### OpenShift

  - **(2020)** [**blog.openshift.com/: Introduction to GitOps with OpenShift**](https://www.redhat.com/en/blog/introduction-to-gitops-with-openshift) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight defines the OpenShift declarative application delivery model. Live Grounding details the Red Hat OpenShift GitOps operator powered by Argo CD. This is the official blueprint for establishing structured continuous integration on Red Hat environments.
## Kubernetes Cluster Operations

### Autoscaling

#### Vertical Pod Autoscaler

  - **(2020)** [**blog.openshift.com/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler**](https://www.redhat.com/en/blog/how-full-is-my-cluster-part-4-right-sizing-pods-with-vertical-pod-autoscaler) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Curator Insight focuses on the role of Vertical Pod Autoscalers (VPA). Live Grounding evaluates recommendation engines, safety limits, and automatic resource reallocations on OpenShift. Important reference for auto-scaling and efficiency.
### Multi-Cluster

#### Legacy Federation

  - **(2019)** [Multi-cluster Federation in OpenShift 4 is called **KubeFed**](https://www.redhat.com/en/blog/federation-v2-is-now-kubefed) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight introduces the KubeFed system in OpenShift 4. Live Grounding highlights its mechanism for template distribution and configuration sync across multiple clusters. Valuable for understanding historical cross-cluster patterns before modern gateway patterns.
  - **(2018)** [OpenShift 3.11 Multi-cluster Federation](https://www.redhat.com/en/blog/kubernetes-federation-v2-on-openshift-3-11) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight looks at multi-cluster federation on older OpenShift 3.11 setups. Live Grounding illustrates early architectural attempts to distribute workloads across cloud regions. Crucial historical context before modern GitOps and Cluster API paradigms took over.
### Resource Management

#### OpenShift (1)

  - **(2019)** [blog.openshift.com/full-cluster-capacity-management-monitoring-openshift](https://www.redhat.com/en/blog/full-cluster-capacity-management-monitoring-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight initiates a series on OpenShift capacity planning. Live Grounding details Prometheus and Grafana alerts, memory saturation metrics, and CPU scheduling limits. Essential for cluster administrators managing highly dense node resources.
  - **(2019)** [blog.openshift.com/full-cluster-part-2-protecting-nodes](https://www.redhat.com/en/blog/full-cluster-part-2-protecting-nodes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight focuses on securing host resources from rogue applications. Live Grounding details eviction thresholds, pod limits, and system-reserved configuration paths inside OpenShift clusters. Vital for maintaining node reliability.
  - **(2019)** [full-cluster-part-3-capacity-management](https://www.redhat.com/en/blog/full-cluster-part-3-capacity-management) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight reviews multi-tenant resource optimization. Live Grounding analyzes quotas, LimitRanges, and tenant isolation layers in enterprise workloads. Highly effective for designing multi-team cluster footprints.
## Kubernetes Storage

### Database Operations

#### OpenShift (2)

  - **(2021)** [How to Run HA Elasticsearch (ELK) on Red Hat OpenShift](https://portworx.com/blog/run-ha-elasticsearch-elk-red-hat-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight targets high-availability ELK stack patterns. Live Grounding outlines storage volume pairing, stateful replication rules, and failover topologies specific to OpenShift. A crucial reference for running enterprise log stacks safely.
## Platform Architecture

### Administration

#### Automation

  - **(2020)** [developers.redhat.com: Customizing OpenShift project creation 🌟](https://developers.redhat.com/blog/2020/02/05/customizing-openshift-project-creation) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Details dynamic project onboarding techniques for OpenShift administrators. Teaches how to configure customized templates that automatically enforce security contexts, default quotas, and custom networking parameters upon namespace creation.
### Automation (1)

#### Ansible

  - **(2023)** [GitHub redhat-cop: Ansible Role 🌟](https://github.com/redhat-cop/infra-ansible) <span class='md-tag md-tag--info'>⭐ 219</span> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A structured repository of Ansible automation roles customized for provisioning, maintaining, and configuring OpenShift resources. Simplifies operations such as authentication, user management, and day-2 configurations.
#### Community Tools

  - **(2026)** [Red Hat Communities of Practice](https://github.com/redhat-cop) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The master platform profile of Red Hat's Communities of Practice. Contains scripts, custom operator codes, and automated scaffolding for cluster setups, management, and resource governing processes.
### Core Concepts

#### Kubernetes Pods

  - **(2018)** [blog.openshift.com/ - Kubernetes: A Pod’s Life 🌟](https://www.redhat.com/en/blog/kubernetes-pods-life) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A fundamental exploration of the life cycle of a Kubernetes Pod. Outlines start sequences, init container routines, readiness/liveness checks, and termination processes, establishing a baseline for container orchestration troubleshooting.
### GitOps (1)

#### Modern Pipelines

  - **(2020)** [openshift.com: From Code to Production with GitOps, Tekton and ArgoCD 🌟](https://www.redhat.com/en/blog/from-code-to-production-with-gitops) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Introduces robust continuous delivery architectures utilizing Tekton for image construction and Argo CD for GitOps-based state syncs. Serves as the primary operational blueprint for enterprise microservice platforms in 2026.
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
### Resource Management (1)

#### Autoscaling (1)

  - **(2020)** [developers.redhat.com: Testing memory-based horizontal pod autoscaling on OpenShift 🌟](https://developers.redhat.com/blog/2020/03/19/testing-memory-based-horizontal-pod-autoscaling-on-openshift) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A diagnostic tutorial explaining how to design, execute, and inspect Horizontal Pod Autoscaler scaling metrics based on container RAM thresholds. Includes guidelines for generating stable test scenarios.
#### Governance

  - **(2020)** [OpenShift 4 Resource Management](https://www.youtube.com/watch?v=JC_PB1yZcIc) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An informative session demonstrating effective scheduling, configuration, and governing mechanics of OpenShift 4 resources. Highlights the use of LimitRanges, ResourceQuotas, and Node selectors.
  - **(2019)** [techbeatly.com: How to create, increase or decrease project quota](https://techbeatly.com/how-to-create-increase-or-decrease-project-quota-in-openshift/#.Xd5OE9WCGUk) <span class='md-tag md-tag--warning'>[BASH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides step-by-step guidance on managing project resource limits inside OpenShift namespaces. Explores configuring quotas via the oc CLI to enforce hard boundaries on CPU, RAM, and storage allocations.
### Resources

#### Learning paths

  - **(2019)** [certdepot.net: OpenShift Free available resources 🌟](https://www.certdepot.net/openshift-free-available-resources) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An educational index detailing free courses, interactive sandbox playgrounds, and study materials for professionals pursuing official Red Hat OpenShift certifications.
## Security

### Encryption

#### .NET Core

  - **(2018)** [developers.redhat.com: Securing .NET Core on OpenShift using HTTPS](https://developers.redhat.com/blog/2018/10/12/securing-net-core-on-openshift-using-https) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through configuring ASP.NET Core microservices with end-to-end TLS encryption on OpenShift. Discusses dynamic integration of local server certificates using OpenShift's service serving certificates feature.

---
💡 **Explore Related:** [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md) | [Kubernetes Storage](./kubernetes-storage.md) | [Docker](./docker.md)

