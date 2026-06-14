# Kubectl commands

!!! info "Architectural Context"
    Detailed reference for Kubectl commands in the context of The Container Stack.

## Standard Reference

  - [medium: 4 Simple Kubernetes Terminal Customizations to Boost Your Productivity](https://medium.com/better-programming/4-simple-kubernetes-terminal-customizations-to-boost-your-productivity-deda60a19924)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Ready-to-use commands and tips for kubectl](https://medium.com/flant-com/kubectl-commands-and-tips-7b33de0c5476)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Be fast with Kubectl 1.19 CKAD/CKA 🌟](https://medium.com/faun/be-fast-with-kubectl-1-18-ckad-cka-31be00acc443)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [pixelstech.net: Update & Delete Kubernetes resources in one-line command](https://www.pixelstech.net/article/1604225312-Update-&amp-Delete-Kubernetes-resources-in-one-line-command)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: One CKA/CKAD/CKS requirement: Mastering Kubectl](https://medium.com/nerd-for-tech/one-cka-ckad-cks-requirement-mastering-kubectl-85486bc0a3aa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium: Replication Controller Vs ReplicaSets in Kubernetes](https://medium.com/geekculture/replication-controller-vs-replicasets-in-kubernetes-7b780e4d09d5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [akhilsharma.work: Checking Kubernetes API Calls using kubectl](https://akhilsharma.work/checking-kubernetes-api-calls-using-kubectl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [cloudsavvyit.com: How to Restart Kubernetes Pods with Kubectl](https://www.cloudsavvyit.com/14587/how-to-restart-kubernetes-pods-with-kubectl)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [technos.medium.com: How kubectl apply command works?](https://technos.medium.com/how-kubectl-apply-command-works-d092121056d3)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blogs.nakam.org: What Happens When? K8s Edition 🌟](https://blogs.nakam.org/what-happens-when-k8s-edition)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/swlh: Break Down Kubernetes Server-Side Apply (Advanced kubectl)' 🌟](https://medium.com/swlh/break-down-kubernetes-server-side-apply-5d59f6a14e26)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: K8s — Manage Multiple Clusters Using kubectl at Scale](https://blog.devgenius.io/k8s-manage-multiple-clusters-using-kubectl-at-scale-9f200c692099)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [awstip.com: Kubernetes — Creating deployments via command line and with' YAML files](https://awstip.com/kubernetes-creating-deployments-via-command-line-and-with-yaml-files-783eaad7b3be)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@emmaliaocode: kubectl create vs kubectl apply. What’s the difference?](https://medium.com/@emmaliaocode/kubectl-create-vs-kubectl-apply-whats-the-differences-f6472f4c6c86)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/codex: Kubectl Output 101](https://medium.com/codex/kubectl-output-101-851f8e61fd51)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/geekculture: kubectl — Best Practices](https://medium.com/geekculture/kubectl-best-practices-c4ff809167dd)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [medium.com/@jake.page91: The guide to kubectl I never had](https://medium.com/@jake.page91/the-guide-to-kubectl-i-never-had-3874cc6074ff)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [blog.devgenius.io: Daily useful Kubernetes aliases](https://blog.devgenius.io/daily-useful-kubernetes-aliases-c35f7f411f39)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Copy secrets between namespaces](https://stackoverflow.com/questions/55515594/is-there-a-way-to-share-a-configmap-in-kubernetes-between-namespaces)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Automation

### Kubernetes

#### Ansible Modules

  - **(2024)** [Manage Kubernetes (K8s) objects](https://docs.ansible.com/collections.html) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation detailing Ansible's specialized `kubernetes.core.k8s` module capabilities. It focuses on declaratively orchestrating Kubernetes objects directly from Ansible playbooks, allowing organizations to cleanly bridge traditional VM configuration setups with modern containerized platform configurations.
## Cloud Native

### Kubernetes (1)

#### CICD and Builds

  - **(2026)** [container-registry.com: Lifting Developers’ Productivity 🌟](https://container-registry.com/posts/productivity-lift-buildkit-cli-for-kubectl) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analysis of the BuildKit CLI integration for 'kubectl'. It empowers developers to build container images directly within active Kubernetes execution scopes, leveraging distributed cache backends and eliminating local docker daemon dependencies.
#### CLI and Debugging

  - **(2026)** [==ahmetb/kubectl-aliases==](https://github.com/ahmetb/kubectl-aliases) <span class='md-tag md-tag--info'>⭐ 3691</span> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An automated system that generates systematic shell aliases for 'kubectl', significantly enhancing engineering productivity. It minimizes operational friction by programmatic expansion of over 800 permutations of flags and subcommands, allowing administrators to interface with Kubernetes clusters using succinct shorthand sequences.
  - **(2026)** [==github.com/trstringer/kubectl-example==](https://github.com/trstringer/kubectl-example) <span class='md-tag md-tag--info'>⭐ 13</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A reference repository providing curated template patterns and concrete command-line configurations for common 'kubectl' usage patterns. Designed to shorten the ramp-up time for operators, it acts as a declarative cheat-sheet for state transitions and diagnostic queries.
  - **(2026)** [==Flag export deprecated in kubernetes 1.14==](https://github.com/kubernetes/kubernetes/pull/73787) <span class='md-tag md-tag--info'>⭐ 123002</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The upstream Kubernetes pull request deprecating the '--export' flag in 'kubectl get'. Live grounding confirms that as of Kubernetes 1.18+, this flag was completely removed in favor of alternative serialization pipelines, requiring automation scripts to migrate away from this legacy pattern.
  - **(2026)** [kubectl explain](https://jamesdefabia.github.io/docs/user-guide/kubectl/kubectl_explain) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference documentation for 'kubectl explain', a critical utility for schema exploration within the Kubernetes API. Architecturally, it queries the cluster OpenAPI specification directly to output detailed structural layouts of specific resources, assisting developers in constructing valid declarative YAML manifests.
  - **(2026)** [itnext.io: Using ‘kubectl explain’ for Custom Resources](https://itnext.io/understanding-kubectl-explain-9d703396cc8) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An analytical guide showcasing how to leverage 'kubectl explain' to dynamically inspect Custom Resource Definitions (CRDs). By querying the discovery API, platform engineers can navigate deeply nested custom resource structures and ensure compliance with schemas registered via operator patterns.
  - **(2026)** [kubectl Shell Autocomplete](https://blog.heptio.com/kubectl-shell-autocomplete-heptioprotip-48dd023e0bf3) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep dive into setting up shell autocomplete for 'kubectl' across Bash, Zsh, and fish environments. From an operational efficiency perspective, autocompletion queries API resources dynamically, minimizing context switching and reducing manual spelling errors during incident response.
  - **(2026)** [itnext.io: Connect to containers using Kubectl Exec](https://itnext.io/connect-to-containers-using-kubectl-exec-b1fb5c171f03) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An operational walkthrough illustrating how to establish interactive terminal sessions inside container namespaces using 'kubectl exec'. The document details the transport layer over SPDY/HTTP/2 stream multiplexing and explores core configurations needed for standard output routing.
  - **(2026)** [hackernoon.com: How to Work With the Kubectl Debug Command](https://hackernoon.com/how-to-work-with-the-kubectl-debug-command) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth technical manual outlining the usage of 'kubectl debug'. It details how to troubleshoot crash-looping workloads by attaching ephemeral diagnostic containers into target Pod namespaces, effectively bypassing missing-shell constraints of distroless or minimal base images.
#### Security

  - **(2026)** [goteleport.com: kubectl exec vs SSH](https://goteleport.com/blog/ssh-vs-kubectl) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural comparison contrasting standard SSH access with the API-driven 'kubectl exec' command. From a security boundary posture, it highlights why 'kubectl exec' is preferred inside modern clusters as it eliminates secondary authentication pipelines and relies purely on Kubernetes RBAC structures.
## Deployment and Orchestration

### Cluster Provisioning

#### Remote Access

  - **(2020)** [blog.alexellis.io: Get kubectl access to your private cluster from anywhere](https://blog.alexellis.io/get-private-kubectl-access-anywhere) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores techniques for securely accessing the Kubernetes API control plane of isolated or private networks without exposing standard firewall ports. Explains how reverse-proxy tunnels provide secure endpoints. Live Grounding validates that tunnel mechanisms like inlets, Tailscale, or Cloudflare Tunnels have become common choices for secure edge environments.
## Developer Experience

### Shell

#### Productivity

  - **(2026)** [==complete-alias==](https://github.com/cykerway/complete-alias) <span class='md-tag md-tag--info'>⭐ 814</span> <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A shell integration tool designed to resolve completion mechanisms for aliased commands. For platform engineers running complex aliased 'kubectl' pipelines, this tool bridges the gap by enabling native parameter autocomplete for custom aliases, preserving system-level speed.
## Kubernetes (2)

### Developer Experience (1)

#### Container Builds

  - **(2021)** [==vmware-tanzu/buildkit-cli-for-kubectl (kubectl plugin)==](https://github.com/vmware-archive/buildkit-cli-for-kubectl) <span class='md-tag md-tag--info'>⭐ 505</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A kubectl plugin designed to execute container builds directly on remote BuildKit instances inside clusters. Live grounding confirms the project has been archived under VMware, steering teams to direct BuildKit operators or Kaniko.
### Operations

#### Kubectl Plugins

  - **(2025)** [Kubectl plugins and tools](https://nubenetes.com/kubernetes/#kubectl-plugins) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This reference compilation highlights external tools and kubectl extensions managed via Krew. It details how third-party plugins (like `neat`, `kns`, or security-focused extensions) expand basic kubectl operational debugging and cluster-inspection capabilities.
#### Productivity (1)

  - **(2021)** [Kubernetes productivity tips and tricks 🌟](https://www.theodo.com/en-fr/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practitioner's guide to enhancing CLI-based Kubernetes productivity. It explores advanced setups such as custom shell autocompletion, kubectx/kubens utilities, smart aliases, and log-tailing helpers designed to reduce cognitive overhead during real-time incident responses.
## Kubernetes Platform

### Cluster Administration

#### K8s Contexts

  - **(2020)** [**itnext.io: Kubernetes Contexts: Complete Guide for Developers**](https://itnext.io/kubernetes-contexts-complete-guide-for-developers-7ea5b2fc75c7) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Explains how kubeconfig context matrices are structured. Aids teams in safely managing user authorization levels across distinct dev, staging, and production clusters.
#### Kubectl Plugins (1)

  - **(2021)** [**shardul.dev: Most Useful kubectl Plugins**](https://shardul.dev/most-useful-kubectl-plugins) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Reviews highly useful extensions managed via the Krew plugins system. Showcases tools that expand administrator diagnostic capacities, log operations, and performance checks.
#### Kubectl Productivity


??? abstract "Architect's Technical Comparison Table"
    | Solution | Maturity | Primary Focus | Language | Stars |
    | :--- | :--- | :--- | :--- | :--- |
    | [opensource.com: 5 useful ways to manage Kubernetes with kubectl](https://opensource.com/article/21/7/kubectl) |  | Kubectl Productivity | English | 🌟🌟🌟🌟 |
    | [dev.to: Open a command prompt in a Kubernetes cluster](https://dev.to/eldadak/open-a-command-prompt-in-a-kubernetes-cluster-206g) |  | Kubectl Productivity | English | 🌟🌟🌟🌟 |
    | [itnext.io: How to Restart Kubernetes Pods With Kubectl 🌟](https://itnext.io/how-to-restart-kubernetes-pods-with-kubectl-2a7834a6b961) |  | Kubectl Productivity | English | 🌟🌟🌟🌟 |
    | [itnext.io: Boosting your kubectl productivity](https://itnext.io/boosting-your-kubectl-productivity-b348f7c25712) |  | Kubectl Productivity | English | 🌟🌟🌟🌟 |
    | [developers.redhat.com: Kubectl: Developer tips for the Kubernetes command' line 🌟](https://developers.redhat.com/blog/2020/11/20/kubectl-developer-tips-for-the-kubernetes-command-line) |  | Kubectl Productivity | English | 🌟🌟🌟🌟 |
    | [howtogeek.com: Getting Started With Kubectl to Manage Kubernetes Clusters](https://www.howtogeek.com/devops/getting-started-with-kubectl-to-manage-kubernetes-clusters) |  | Kubectl Productivity | English | 🌟🌟🌟 |

  - **(2021)** [**opensource.com: 5 useful ways to manage Kubernetes with kubectl**](https://opensource.com/article/21/7/kubectl) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Details five ways to manage deployments using kubectl options. Emphasizes namespace management, manifest validations via dry-runs, and rapid scaling tasks.
  - **(2021)** [**dev.to: Open a command prompt in a Kubernetes cluster**](https://dev.to/eldadak/open-a-command-prompt-in-a-kubernetes-cluster-206g) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Walks through initiating command sessions in target Kubernetes containers for diagnostics. Discusses ephemeral container usage and target debugging options without altering running code paths.
  - **(2021)** [**itnext.io: How to Restart Kubernetes Pods With Kubectl 🌟**](https://itnext.io/how-to-restart-kubernetes-pods-with-kubectl-2a7834a6b961) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Details methods for orchestrating safe container restarts via kubectl, such as the rollout restart command. Ensures zero-downtime restarts without dropping running traffic allocations.
  - **(2020)** [**itnext.io: Boosting your kubectl productivity**](https://itnext.io/boosting-your-kubectl-productivity-b348f7c25712) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Compiles productivity enhancements and aliases for kubectl command routines. Addresses custom terminal variables, prompt customizations, and configurations aimed at easing day-to-day cluster tasks.
  - **(2020)** [**developers.redhat.com: Kubectl: Developer tips for the Kubernetes command' line 🌟**](https://developers.redhat.com/blog/2020/11/20/kubectl-developer-tips-for-the-kubernetes-command-line) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Provides developer-focused kubectl practices for troubleshooting deployment issues on Red Hat configurations. Explores log parsing tricks and container shell executions.
  - **(2022)** [howtogeek.com: Getting Started With Kubectl to Manage Kubernetes Clusters](https://www.howtogeek.com/devops/getting-started-with-kubectl-to-manage-kubernetes-clusters) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational guide to managing clusters with kubectl. Outlines config structure concepts, baseline container commands, and standard diagnostics routines for new platform users.
#### Multi-Cluster Tools

  - **(2021)** [**hackerxone.com: How to Manage Single & Multiple Kubernetes Clusters using' kubectl & kubectx in Linux**](https://www.hackerxone.com/2021/07/10/how-manage-single-multiple-kubernetes-clusters-using-kubectl-kubectx-linux) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Outlines cluster and namespace administration workflows leveraging kubectx and kubens. Prevents accidental execution on incorrect environments during multi-cluster deployments.
#### Port Forwarding

  - **(2022)** [**inlets.dev: Fixing the Developer Experience of Kubernetes Port Forwarding**](https://inlets.dev/blog/2022/06/24/fixing-kubectl-port-forward.html) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Addresses stability issues inherent in standard kubectl port-forward operations. Explains how tunnels and reverse-proxy tools like Inlets provide developers with robust, persistent local connections.
#### Shell Environments

  - **(2020)** [**superbrothers/zsh-kubectl-prompt 🌟**](https://github.com/superbrothers/zsh-kubectl-prompt) <span class='md-tag md-tag--info'>⭐ 591</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Details a Zsh shell utility that displays current Kubernetes context and namespace info in the terminal prompt. Minimizes chances of entering execution instructions in wrong production sectors.
### K8s API and Development

#### Config Management

  - **(2023)** [**learnitguide.net: How to Create ConfigMap from Properties File Using K8s' Client**](https://www.learnitguide.net/2023/04/how-to-create-configmap-from-properties.html) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Demonstrates methods to compile Kubernetes ConfigMaps from structured properties files. Bridges common application configurations with native cloud manifest patterns.
## Observability

### Debugging

#### CLI Operations

  - **(2023)** [A Complete Guide to Kubectl exec](https://refine.dev/blog/kubectl-exec-command) <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Comprehensive guide explaining the inner workings of the 'kubectl exec' command. Breaks down how connection handshakes occur between the API server, Kubelet, and container runtimes (CRI).
## Operations and UX

### CLI Plugins

#### Output Formatting

  - **(2026)** [hidetatz/kubecolor 🌟](https://github.com/hidetatz/kubecolor) <span class='md-tag md-tag--info'>⭐ 1446</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kubecolor is a highly adopted command-line wrapper for kubectl that colorizes terminal outputs. It improves cluster observability by visually distinguishing resource types, labels, statuses, and namespaces during interactive CLI operations.

---
💡 **Explore Related:** [Kubernetes Operators Controllers](./kubernetes-operators-controllers.md) | [Kubernetes Storage](./kubernetes-storage.md) | [Docker](./docker.md)

