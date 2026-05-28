# OpenShift Container Platform

!!! info "Architectural Context"
    Detailed reference for OpenShift Container Platform in the context of The Container Stack.

## Standard Reference

  - [blog.openshift.com: OCP multi-node deployment on **AWS** using CloudFormation and Ansible (quickstart workshop)](https://www.redhat.com/en/blog/aws-and-red-hat-quickstart-workshop)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift.com](https://www.redhat.com/en/technologies/cloud-computing/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift blog 🌟](https://www.redhat.com/en/blog/channel/hybrid-cloud-infrastructure)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [try.openshift.com 🌟](https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [twitter.com/openshift](https://x.com/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift.tv](https://www.redhat.com/en/livestreaming)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Amazon Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift on Google Cloud](https://docs.cloud.google.com/compute/docs/containers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Microsoft Azure Red Hat OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift/azure)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat OpenShift on IBM Cloud](https://www.ibm.com/products/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat Marketplace](https://marketplace.redhat.com/sunset)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [aroworkshop.io 🌟](http://aroworkshop.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.microsoft.com: JBoss deployment with Red Hat on Azure 🌟](https://learn.microsoft.com/en-us/azure/developer/java/ee/jboss-eap-on-aro)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat's approach to Kubernetes 🌟](https://www.redhat.com/en/solutions/kubernetes-approach)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [O'Reilly Free Book: **DevOps with OpenShift**](https://www.redhat.com/en/resources)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [O'Reilly Free Book: **Openshift for developers**](https://www.redhat.com/en/technologies/cloud-computing/openshift/for-developers)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Installing OKD 3.10 on a Single Host 🌟](https://www.redhat.com/en/blog/installing-okd-3-10-on-a-single-host)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [uncontained.io: Installing a Highly Available OpenShift Cluster 🌟](http://uncontained.io/articles/openshift-ha-installation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: OpenShift 4.2 vSphere Install Quickstart](https://www.redhat.com/en/blog/openshift-4-2-vsphere-install-quickstart)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: OpenShift 4.2 vsphere install with static IPs 🌟](https://www.redhat.com/en/blog/openshift-4-2-vsphere-install-with-static-ips)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Troubleshooting OpenShift network performance with a netperf DaemonSet](https://www.redhat.com/en/blog/troubleshooting-openshift-network-performance-with-a-netperf-daemonset)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.openshift.com: Advanced Network customizations for OpenShift Install](https://www.redhat.com/en/blog/advanced-network-customizations-for-openshift-install)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [NetworkPolicies and Microsegmentation](https://www.redhat.com/en/blog/channel/hybrid-cloud-infrastructure/networkpolicies-and-microsegmentation)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Fully Automated Management of Egress IPs with the egressip-ipam-operator 🌟](https://www.redhat.com/en/blog/fully-automated-management-of-egress-ips-with-the-egressip-ipam-operator)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift and Network Security Zones: Coexistence Approaches 🌟🌟🌟](https://www.redhat.com/en/blog/openshift-and-network-security-zones-coexistence-approaches)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — - **Introduction:** Kubernetes and consequently OpenShift adopt a [flat Software Defined Network (SDN) model](https://kubernetes.io/docs/concepts/cluster-administration/networking), which means that all pods in the SDN are in the same logical network. Traditional network implementations adopt a zoning model in which different networks or zones are dedicated to specific purposes, with very strict communication rules between each zone. When implementing OpenShift in organizations that are using network security zones, the two models may clash. we will analyze a few options for coexistence. But first, let’s understand the two network models a bit more in depth.
    - Network Zones have been the widely accepted approach for building security into a network architecture. The general idea is to create separate networks, each with a specific purpose. Each network contains devices with similar security profiles. Communications between networks is highly scrutinized and controlled by firewall rules ([perimeter defense](https://en.wikipedia.org/wiki/All_round_defence)).
    - **Conclusion:** A company’s security organization must be involved when deciding how to deploy OpenShift with regard to traditional network zones. Depending on their level of comfort with new technologies you may have different options. If physical network separation is the only acceptable choice, you will have to build a cluster per network zone. If logical network type of separations can be considered, then there are ways to stretch a single OpenShift deployment across multiple network zones. This post presented a few technical approaches.
  - [Red Hat Container Catalog - RedHat Registry (registry.redhat.io) 🌟](https://catalog.redhat.com/en)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Get started with OpenShift Origin 3 and GitLab](https://about.gitlab.com/blog/get-started-with-openshift-origin-3-and-gitlab)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Atlassian Confluence6](https://github.com/nubenetes/confluence6-atlassian)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift.com: Introducing Red Hat OpenShift Service on AWS](https://www.redhat.com/en/blog/introducing-red-hat-openshift-service-on-aws)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Awesome Openshift 2](https://github.com/oscp/awesome-openshift3) <span class='md-tag md-tag--info'>⭐ 27</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Portfolio Architecture](https://redhatdemocentral.gitlab.io/portfolio-architecture-workshops/#)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redhatdemocentral.gitlab.io/portfolio-architecture-tooling](https://redhatdemocentral.gitlab.io/portfolio-architecture-tooling)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Rcarrata's blog](https://rcarrata.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Developer Sandbox for Red Hat OpenShift 🌟](https://developers.redhat.com/developer-sandbox)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [IBM Cloud Pak Playbook](https://cloudpak8s.io/apps/cp4a_overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Wikipedia.org: OpenShift](https://en.wikipedia.org/wiki/OpenShift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com 🌟](https://docs.openshift.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com 🌟](https://developers.redhat.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift Commons](https://commons.openshift.org)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift in DockerHub](https://hub.docker.com/u/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [reddit.com/r/openshift](https://www.reddit.com/r/openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [reddit.com/r/redhat](https://www.reddit.com/r/redhat)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [twitch.tv/redhatopenshift](https://www.twitch.tv/redhatopenshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift.io](https://openshift.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [openshift-ireland.com](https://openshift-ireland.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [I’m So Sorry OpenShift, I’ve Taken You for Granted 🌟](https://medium.com/swlh/im-so-sorry-openshift-i-ve-taken-you-for-granted-f36fb47ea4d9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: Enabling tab completion](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/configuring-cli.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: How to enable OpenShift oc bash auto completion](https://medium.com/@ismailyenigul/how-to-enable-openshift-oc-bash-auto-completion-958b80e56e17)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift 3.11: Configuring the cluster auto-scaler in AWS](https://docs.openshift.com/container-platform/3.11/admin_guide/cluster-autoscaler.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift 4.4: Applying autoscaling to an OpenShift Container Platform cluster](https://docs.openshift.com/container-platform/4.4/machine_management/applying-autoscaling.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [O’Reilly: Free ebook: **Kubernetes Operators: Automating the Container Orchestration' Platform**](https://www.redhat.com/en/resources/oreilly-kubernetes-operators-automation-ebook)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Manning: **Openshift in action**](https://www.manning.com/books/openshift-in-action)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Kubernetes e-Books](https://awesome-kubernetes.readthedocs.io/kubernetes/#e-books)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [learn.openshift.com](https://learn.openshift.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [udemy.com: Red Hat OpenShift With Jenkins: DevOps For Beginners](https://www.udemy.com/red-hat-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [udemy.com: OpenShift Enterprise v3.2 Installation and Configuration](https://www.udemy.com/openshift-enterprise-installation-and-configuration/learn/v4/overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [udemy.com: Ultimate Openshift (2018) Bootcamp by School of Devops 🌟](https://www.udemy.com/ultimate-openshift-bootcamp-by-school-of-devops)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Udemy: OpenShift 4 desde cero 🌟](https://www.udemy.com/course/openshift-4-desde-cero)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: **Red Hat Container Development Kit**](https://developers.redhat.com/products/cdk/overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/redhatdemocentral: OpenShift Container Platform Install Demo' 🌟](https://github.com/redhatdemocentral/ocp-install-demo)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [schabell.org: Cloud-native development - A blueprint 🌟](https://www.schabell.org/2020/05/cloud-native-development-a-blueprint.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [gitlab.com: Project Examples](https://gitlab.com/redhatdemocentral/portfolio-architecture-examples)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube.com: OpenShift Origin is now OKD. Installation of OKD 3.10 from' start to finish](https://www.youtube.com/watch?v=ZkFIozGY0IA)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Install RedHat OKD 3.10 on your development box:](https://github.com/gshipley/installcentos)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/openshift/installer openshift installer 🌟](https://github.com/openshift/installer) <span class='md-tag md-tag--info'>⭐ 1546</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [reddit](https://www.reddit.com/r/openshift/comments/e1kw48/openshift_42_vsphere_install)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [youtube: Deploy OpenShift 4 to vSphere using OpenShift's UPI](https://www.youtube.com/watch?v=DLB9m17aGus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Using sidecars to analyze and debug network traffic in OpenShift and Kubernetes pods](https://developers.redhat.com/blog/2019/02/27/sidecars-analyze-debug-network-traffic-kubernetes-pod)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [developers.redhat.com: Skupper.io: Let your services communicate across' Kubernetes clusters](https://developers.redhat.com/blog/2020/01/01/skupper-io-let-your-services-communicate-across-kubernetes-clusters)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [itnext.io: Adding security layers to your App on OpenShift — Part 1: Deployment' and TLS Ingress 🌟](https://itnext.io/adding-security-layers-to-your-app-on-openshift-part-1-deployment-and-tls-ingress-9ef752835599)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: OpenShift 3 Overview](https://docs.openshift.com/container-platform/3.11/architecture/index.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: OpenShift 3 Securing the Container Platform](https://docs.openshift.com/container-platform/3.11/security/securing_container_platform.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ocs.openshift.com: OpenShift 4 Understanding Authentication](https://docs.openshift.com/container-platform/4.4/authentication/understanding-authentication.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: Managing Security Context Constraints](https://docs.openshift.com/container-platform/3.11/admin_guide/manage_scc.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: Managing Security Context Constraints. Security Context' Constraints](https://docs.openshift.com/container-platform/3.11/architecture/additional_concepts/authorization.html#security-context-constraints)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [ref3](https://dzone.com/articles/understanding-openshift-security-context-constrain)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [docs.openshift.com: Understanding networking](https://docs.openshift.com/container-platform/4.4/networking/understanding-networking.html)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [GitHub: redhat-cop OpenShift Toolkit Network Policy 🌟](https://github.com/redhat-cop/openshift-toolkit/tree/master/networkpolicy) <span class='md-tag md-tag--info'>⭐ 236</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [redhat.com: Network traffic control for containers in Red Hat OpenShift' 🌟](https://www.redhat.com/en/blog/network-traffic-control-containers-red-hat-openshift)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [stackoverflow.com: Is that possible to deploy an openshift or kubernetes' in DMZ zone? 🌟](https://stackoverflow.com/questions/59518363/is-that-possible-to-deploy-an-openshift-or-kubernetes-in-dmz-zone)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloud.ibm.com: OpenShift Ingress](https://cloud.ibm.com/docs/openshift?topic=openshift-ingress)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [dzone: OpenShift Egress Options](https://dzone.com/articles/openshift-egress-options)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/sclorg/](https://github.com/sclorg)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [github.com/sclorg/mariadb-container](https://github.com/sclorg/mariadb-container) <span class='md-tag md-tag--info'>⭐ 32</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [hub.docker.com/r/sonatype/nexus3/](https://hub.docker.com/r/sonatype/nexus3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [opensource.com: Why choose Rocket.Chat for your open source chat tool](https://opensource.com/article/22/1/rocketchat-data-privacy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [IBM Cloud Pak Playbook: cloudpak8s.io](https://cloudpak8s.io)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat OpenShift Dedicated price reduction: Price lowered by 75% on average,' SLA improved to 99.95% 🌟](https://www.redhat.com/en/blog/red-hat-openshift-dedicated-price-reduction)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [kubernetes.io: The Kubernetes network model. How to implement the Kubernetes' networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [OpenShift 4 on AWS Quick Starts 🌟](https://aws.amazon.com/blogs/opensource/openshift-4-on-aws-quick-start)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud Infrastructure

### Kubernetes Distributions

#### Enterprise Platforms

  - **(2026)** [==OKD==](https://okd.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — OKD is the open-source upstream community distribution of Red Hat OpenShift, fully integrating containerized virtualization, developer tools, and operators. Built on Fedora CoreOS, OKD provides cloud architects with a platform-as-a-service engine optimized for continuous deployment and complex multi-tenant operations.
## Cloud Native AI

### Batch Workloads

#### Kueue Scheduling

  - [Red Hat Build of Kueue](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/ai_workloads/red-hat-build-of-kueue#about-kueue) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Documentation for the Red Hat Build of Kueue scheduler within OpenShift.
Live Grounding: Kueue offers advanced queueing mechanism controls, priority groupings, and resource quotas, making it the premier platform tool for managing AI/ML and batch workloads.
## Education

### Interactive Learning

#### Platforms

  - [katacoda.com](https://www.katacoda.com)  <span class='md-tag md-tag--info'>[LEGACY]</span> — Formerly the premier interactive browser-based terminal platform for testing and learning Kubernetes, Docker, and Linux configuration on-demand. Live Grounding indicates the platform was retired by O'Reilly, rendering it a legacy archive link.
## Observability and Performance

### Kubernetes Internals

#### Autotuning

  - [How Kruize Optimizes OpenShift Workloads](https://developers.redhat.com/articles/2025/06/25/how-kruize-optimizes-openshift-workloads#what_is_kruize_autotune_) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a comprehensive overview of how Kruize Autotune optimizes resource efficiency in OpenShift and Kubernetes workloads. Evaluates real-time scaling mechanisms and automated recommendations to reduce resource waste.
## Platform Engineering

### Enterprise Linux

#### Training

  - **(2025)** [redhatgov.io](http://redhatgov.io) 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's dedicated architectural training blueprint designed for secure governmental and enterprise environments. Focuses on orchestrating compliant private clouds and enterprise Linux configurations.
## Public Cloud Infrastructure

### AWS Architecture

#### Multi-Region Blueprints

  - **(2021)** [**Multi-Region Infrastructure Deployment**](https://aws.amazon.com/solutions) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: AWS Solutions library offering reference architectures for high-availability setups.
Live Grounding: Provides automated CloudFormation and CDK deployment configurations to orchestrate secure application instances across multiple geographical AWS regions.
## Training and Certification

### Red Hat Ecosystem

#### Learning Platforms

  - [Red Hat Training & Certification Community](https://access.redhat.com/community/learn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official educational resources and certification preparation portal curated by Red Hat. Serves as a vital reference for mastering OpenShift and enterprise Linux engineering architectures.

---
💡 **Explore Related:** [Kubernetes Bigdata](./kubernetes-bigdata.md) | [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md) | [OCP 4](./ocp4.md)

