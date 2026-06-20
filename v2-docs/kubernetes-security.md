---
description: "Curated, AI-ranked Kubernetes Security resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Hardened Infrastructure)."
---
# Kubernetes Security

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/kubernetes-security/).

!!! info "Architectural Context"
    Detailed reference for Kubernetes Security in the context of Hardened Infrastructure.

## API Access Protection

### Teleport Access Control

  - **(2021)** [goteleport.com: Kubernetes API Access Security Hardening](https://goteleport.com/blog/kubernetes-api-access-security) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Assesses security postures for Kube-API exposure, outlining standard secure practices including zero-trust access, bastions, detailed telemetry streams, and short-lived credentials.
## Architecture

### Microservices

#### Application Lifecycle

  - **(2022)** [itnext.io: Journey Of A Microservice Application In The Kubernetes World 🌟](https://itnext.io/journey-of-a-microservice-application-in-the-kubernetes-world-6abd625c60fe)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Traces the structural lifecycle of a containerized microservice traversing deployment pipelines, service routing, and load balancing configurations. Provides practical insights into configuring readiness/liveness probes, autoscaling parameters, and ingress rules. Essential reference for microservice platform standardization.
## CKS Certification Study Guides

### Cluster Lifecycle Security

  - **(2020)** [==github.com/stackrox: Certified Kubernetes Security Specialist Study Guide' 🌟==](https://github.com/stackrox/Kubernetes_Security_Specialist_Study_Guide) <span class='md-tag md-tag--info'>⭐ 429</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-53687d8e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 12 L 20 7 L 30 11 L 40 3 L 50 2" fill="none" stroke="url(#spark-grad-53687d8e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A comprehensive community study handbook for the Linux Foundation CKS exam, detailing system hardening, threat mitigation, microservice security policies, and runtime compliance enforcement.
## CNI Network Vulnerabilities

### Network Penetration Testing

  - **(2020)** [cyberark.com: Attacking Kubernetes Clusters Through Your Network Plumbing: Part 1](https://www.cyberark.com/resources/threat-research-blog/attacking-kubernetes-clusters-through-your-network-plumbing-part-1) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Delves into how container network interfaces (CNIs) and underlying network configurations can be targets for spoofing, route injection, and MITM attacks within shared Kubernetes clusters.
## CVE Analysis

### Network Vulnerabilities

  - **(2020)** [empresas.blogthinkbig.com: Descubierta una vulnerabilidad en Kubernetes que permite acceso a redes restringidas (CVE-2020-8562)](https://empresas.blogthinkbig.com/descubierta-vulnerabilidad-kubernetes-permite-acceso-redes-restringidas-cve-2020-8562) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes CVE-2020-8562, a vulnerability allowing path-traversal/access bypass to internal restricted subnets through the Kubernetes API server, discussing standard mitigation strategies.
## Case Studies

### Historical Exploit Analysis

  - **(2021)** [thenewstack.io: Kubernetes: An Examination of Major Attacks 🌟](https://thenewstack.io/kubernetes-an-examination-of-major-attacks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Conducts retrospective post-mortems on major real-world Kubernetes security incidents, tracing malicious lateral movements, coin-miner deployments, and critical data breaches back to root posture issues.
## Cloud Native Networking

### Network Policies

#### Calico and Tigera Security

  - **(2020)** [tigera.io: Kubernetes security policy design: 10 critical best practices 🌟](https://www.tigera.io/blog/kubernetes-security-policy-10-critical-best-practices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A strategic framework for designing cluster-wide network policies, using tiered structures, explicit default-deny states, and labeling schemas to scale security dynamically.
#### Secure CNI Implementation

  - **(2021)** [itnext.io: How-To: Kubernetes Cluster Network Security 🌟](https://itnext.io/how-to-kubernetes-cluster-network-security-f19bc99161f5) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical tutorial covering secure network policy design. Guides readers through limiting pod egress/ingress, utilizing global network policies, and implementing namespaces as security perimeters.
## Cloud Native Security

### The 4Cs of Cloud Native Security

  - **(2020)** [kubernetes.io: Cloud native security for your clusters](https://kubernetes.io/blog/2020/11/18/cloud-native-security-for-your-clusters) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An authoritative review of the '4C's of Cloud Native Security' (Cloud, Cluster, Container, Code). Explains how defense-in-depth principles apply across all layers of the cloud-native application stack.
## Cluster Hardening

### Infrastructural Protection

  - **(2020)** [containerjournal.com: How to Secure Your Kubernetes Cluster 🌟](https://cloudnativenow.com/topics/cloudnativesecurity/how-to-secure-your-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Evaluates cluster configurations across storage, networking, and deployment lifecycles. Discusses the replacement of deprecated Pod Security Policies with built-in Pod Security Standards and third-party policy engines.
### Network Policies (1)

  - **(2019)** [==Kubernetes Security Best Practices 🌟==](https://github.com/freach/kubernetes-security-best-practice/blob/master/README.md) <span class='md-tag md-tag--info'>⭐ 2712</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-57be194f" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 4 L 20 5 L 30 4 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-57be194f)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A curated GitHub repository delineating hardened configurations for Kubernetes API servers, Kubelets, and network boundaries. It details port-level access rules, ingress/egress filtering, and cluster isolation tactics to defend against pivot attacks.
### Operational Security

  - **(2020)** [codeburst.io: 7 Kubernetes Security Best Practices You Must Follow](https://codeburst.io/7-kubernetes-security-best-practices-you-must-follow-ae32f1ed6444) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines fundamental security practices for Kubernetes workloads, focusing on enabling RBAC, using namespaces for boundary control, managing secrets securely, and upgrading Kubernetes control planes to address known CVEs.
### Runtime Secrets Scanning

  - **(2021)** [blog.gitguardian.com: Hardening Your Kubernetes Cluster - Guidelines (Pt. 2) 🌟](https://blog.gitguardian.com/hardening-your-k8s-pt-2) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The second part of a structural security guide detailing advanced settings such as RBAC limitations, audit logging targets, container engine isolation, and secrets scanning policies.
## Cluster Lifecycle Security (1)

### Operating System Paradigm

  - **(2020)** [thenewstack.io: How to Secure Kubernetes, the OS of the Cloud](https://thenewstack.io/how-to-secure-kubernetes-the-os-of-the-cloud) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the concept of Kubernetes operating as a cloud-native OS, presenting strategies for securing core services, container communication, and control plane boundaries.
## Cluster Misconfigurations

### Common Mistakes

  - **(2021)** [fairwinds.com: Discover the Top 5 Kubernetes Security Mistakes You're (Probably) Making](https://www.fairwinds.com/blog/top-5-kubernetes-security-mistakes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identifies common configuration mistakes like neglected CPU/memory limits, running containers as root, and using unvalidated base images, offering immediate structural remedies.
## Defense in Depth

### Cluster Hardening (1)

  - **(2020)** [thenewstack.io: Defend the Core: Kubernetes Security at Every Layer](https://thenewstack.io/defend-the-core-kubernetes-security-at-every-layer) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides an architectural approach to layered container defense. Examines the integration of secure hardware baselines, API rate limiting, network-level firewalls, and runtime analysis agents.
## Identity and Access Management

### SSO and OIDC Configuration

  - **(2020)** [talkingquickly.co.uk: Kubernetes Single Sign On - A detailed guide 🌟](https://www.talkingquickly.co.uk/kubernetes-sso-a-detailed-guide) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to integrate Kubernetes API access with external identity providers (OIDC) to enable secure Single Sign-On (SSO) and unify role assignments across developers.
## Industry Reports

### Archived Market Trends

  - **(2021)** [redhat.com: State of Kubernetes Security Report - Spring 2021 (PDF) 🌟](https://www.redhat.com/rhdc/managed-files/cl-state-kubernetes-security-report-ebook-f29117-202106-en.pdf) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive market study from Spring 2021 highlighting systemic security incidents and detailing key threat factors, infrastructure risks, and tooling choices among enterprise development teams.
### Enterprise Security Trends

  - **(2021)** [redhat.com: The State of Kubernetes Security](https://www.redhat.com/en/blog/state-kubernetes-security) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Red Hat's analysis of container security threats, identifying key issues such as misconfigurations, unpatched vulnerabilities, and integration friction in cloud-native operational environments.
## Kubernetes Platform Engine

### Cluster Installation and Hardening

#### Infrastructure Provisioning

  - **(2020)** [thenewstack.io: Best Practices for Securely Setting up a Kubernetes Cluster](https://thenewstack.io/best-practices-for-securely-setting-up-a-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Breaks down secure cluster bootstrapping steps, including encrypting secrets at rest in etcd, enabling control plane mutual TLS (mTLS), and minimizing public API endpoint exposure.
### Container Runtimes

#### Runtime Isolation

  - **(2020)** [thenewstack.io: A Security Comparison of Docker, CRI-O and Containerd 🌟](https://thenewstack.io/a-security-comparison-of-docker-cri-o-and-containerd) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares the security architecture and attack surfaces of primary container runtimes: Docker, CRI-O, and Containerd. Discusses rootless execution, sandboxed runtimes (Kata, gVisor), and syscall filtering.
## Networking

### CNI

#### Cilium

  - **(2026)** [cilium.io 🌟](https://cilium.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The main website for Cilium, the industry-standard networking, security, and observability engine powered by eBPF. Eliminates routing performance penalties and delivers deep API metrics.
## Observability and Monitoring

### Runtime Security

#### Falco and K3s Audit Logging

  - **(2021)** [Analyze Kubernetes Audit logs using Falco 🌟](https://github.com/developer-guy/falco-analyze-audit-log-from-k3s-cluster) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Demonstrates how to pipe Lightweight Kubernetes (K3s) API server audit logs directly into CNCF Falco. Perfect for resource-constrained edges and automated home lab deployments.
#### Security Industry Analysis

  - **(2021)** [infoworld.com: The race to secure Kubernetes at run time](https://www.infoworld.com/article/2270825/the-race-to-secure-kubernetes-at-runtime.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents the evolution of runtime threat defense in cloud-native platforms, discussing the industry shift toward kernel-level security telemetry leveraging eBPF technology.
#### Sysdig and Falco Audit Integration

  - **(2020)** [sysdig.com: Getting started with Kubernetes audit logs and Falco 🌟](https://www.sysdig.com/blog/kubernetes-audit-log-falco) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how to integrate Kubernetes API audit logs with CNCF Falco to capture real-time control plane actions and alert on malicious requests, credential abuse, or abnormal operational API traffic.
### eBPF Runtime Enforcement

#### Tetragon Platform

  - **(2022)** [==Tetragon (Cilium)==](https://github.com/cilium/tetragon) <span class='md-tag md-tag--info'>⭐ 4749</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-5d9825fc" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 3 L 20 11 L 30 3 L 40 5 L 50 2" fill="none" stroke="url(#spark-grad-5d9825fc)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An eBPF-powered security observability and runtime enforcement platform. It monitors and blocks system events at the kernel level, providing granular process execution, network activity, and file system audit streams with zero container overhead.
## Penetration Testing

### Security Operations

  - **(2020)** [youtube: Kubernetes Security: Attacking and Defending K8s Clusters - by Magno Logan](https://www.youtube.com/watch?v=OOHmg1J_8ck&ab_channel=RedTeamVillage) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical, demonstration-heavy guide outlining attack-and-defend methodologies for production clusters. Demonstrates common configuration exploits and dynamic remediation.
## Pod Privilege Escalation

### Vulnerability Exploitation

  - **(2020)** [labs.bishopfox.com: Bad Pods: Kubernetes Pod Privilege Escalation 🌟](https://bishopfox.com/blog/kubernetes-pod-privilege-escalation) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A highly cited technical analysis demonstrating how misconfigured container host namespaces, capabilities, and volume mounts can be exploited to escape container boundaries and gain full host-level access.
## Policy-as-Code

### Kyverno Administration

  - **(2020)** [kyverno.io 🌟](https://kyverno.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kyverno is a declarative Kubernetes-native policy engine. Designed specifically for Kubernetes, it simplifies policy management by allowing administrators to validate, mutate, and generate resources without writing complex Rego code.
### Kyverno Rules and Policies

  - **(2020)** [kyverno.io/policies 🌟](https://kyverno.io/policies) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official catalog of Kyverno policies, providing ready-to-deploy manifests for Pod Security standards, multi-tenant workspace isolation, label validation, and compliance auto-generation.
## RBAC and Authorization

### Privilege Escalation

  - **(2020)** [jeffgeerling.com: Everyone might be a cluster-admin in your Kubernetes cluster](https://www.jeffgeerling.com/blog/2020/everyone-might-be-cluster-admin-your-kubernetes-cluster) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates RBAC misconfigurations and overly permissive default service accounts that elevate microservice workloads to cluster-admin privileges. It provides actionable remediation strategies for locking down namespace-bound credentials.
## Risk Analysis and Auditing

### Threat Vector Modeling

  - **(2020)** [tldrsec.com: Risk8s Business: Risk Analysis of Kubernetes Clusters 🌟](https://tldrsec.com/?404=%2Fguides%2Fkubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive vulnerability catalog and risk analysis guide highlighting exploitation pathways in typical cluster deployments. Highlights the security impacts of insecure volume mounts and metadata service access.
## Secrets Management

### HashiCorp Vault Integration

  - **(2020)** [learn.hashicorp.com: Integrate a Kubernetes Cluster with an External Vault 🌟](https://developer.hashicorp.com/vault/tutorials/kubernetes-introduction/kubernetes-external-vault) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical implementation guide showcasing how to leverage the HashiCorp Vault Agent Injector sidecar to dynamically inject secrets directly into application pods via in-memory tmpfs mounts.
## Security

### Application Security

#### Client Security

  - **(2022)** [curity.io: Client Security](https://curity.io/resources/client-security)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on security patterns when structuring application clients that interface with identity ecosystems. Covers patterns like Token Handlers and Backend-for-Frontend (BFF) to safely abstract tokens away from client browsers or apps. Reduces target exposures to common cross-site scripting risks.
### IAM

#### SSO

  - **(2022)** [dev.to/gabrielbiasi: Automatic SSO in Kubernetes workloads using a sidecar container](https://dev.to/gabrielbiasi/automatic-sso-in-kubernetes-workloads-using-a-sidecar-container-3752)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines an automated SSO sidecar integration pattern inside Kubernetes pods, abstracting authentication logic away from application-level containers. Details OAuth token management and redirect intercept strategies executed transparently at the pod level. Simplifies identity integration across multiple microservices.
### Identity and Access

#### Authentication

##### Legacy Tools

  - **(2020)** [github.com/dvob/k8s-s2s-auth: Kubernetes Service Accounts 🌟](https://github.com/dvob/k8s-s2s-auth) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Curator Insight: Demonstrates internal service-to-service auth patterns utilizing raw Service Account tokens. Live Grounding: The repository has seen no recent development and is considered legacy. It is superseded by modern ephemeral TokenRequest APIs and service mesh mTLS integrations.
#### Microservice Identities

  - **(2023)** [learnk8s.io: Authentication between microservices using Kubernetes identities 🌟](https://learnkube.com/microservices-authentication-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A specialized guide analyzing how service-to-service communication can be secured natively. It demonstrates using Kubernetes ServiceAccount tokens as cryptographic identities to authenticate microservices without external overhead. This pattern reduces dependencies on heavy service meshes for simpler deployments.
#### OIDC

##### OAuth2 Proxy

  - **(2021)** [geek-cookbook.funkypenguin.co.nz: Using OAuth2 proxy for Kubernetes Dashboard](https://geek-cookbook.funkypenguin.co.nz/recipes/kubernetes/oauth2-proxy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A configuration guide describing how to wrap the Kubernetes Dashboard and sensitive internal APIs with oauth2-proxy, enabling secure OIDC integrations and SSO workflows.
#### Workload Identity

  - **(2021)** [linkerd.io: Using Kubernetes's new Bound Service Account Tokens for secure workload identity](https://linkerd.io/2021/12/28/using-kubernetess-new-bound-service-account-tokens-for-secure-workload-identity/index.html) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines Linkerd's transition to Kubernetes Bound Service Account Tokens (TokenRequest API). Explains the security benefits of using tokens containing specific audiences, node bindings, and short lifetimes to mitigate credential leakage risks.
### Identity and Access Management (1)

#### Access Control

  - [thenewstack.io: Cloud Native Identity and Access Management in Kubernetes](https://thenewstack.io/cloud-native-identity-and-access-management-in-kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Examines identity federation, user access management, and internal service-to-service authentication models. Curator insight details mapping cluster roles directly to organizational single sign-on identities. Live grounding indicates that decentralized identity and modern authentication are critical to maintaining least privilege in high-scale infrastructure.
### Kubernetes Security (1)

#### Secrets Management (1)

  - **(2021)** [Hands on your first Kubernetes secrets 🌟](https://www.theodo.com/en-uk/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — This hands-on tutorial guides developers through creating, decoding, and mounting native Kubernetes Secret resources within applications. It highlights base64 encoding limitations and advises on key architectural alternatives, such as HashiCorp Vault integration, Sealed Secrets, or CSI secret store drivers for production environments.
### Policy and Admission Control

#### Validating Webhooks

  - **(2022)** [trstringer.com: Create a Basic Kubernetes Validating Webhook](https://trstringer.com/kubernetes-validating-webhook) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Step-by-step technical guide for writing a custom validating admission controller webhook. Focuses on processing API requests, writing validation criteria in Go, and configuring TLS certificate pathways between the API server and the webhook pod.
### Secrets Management (2)

#### HashiCorp Vault

  - **(2021)** [itnext.io: Vault cluster with auto unseal on Kubernetes](https://itnext.io/vault-cluster-with-auto-unseal-on-kubernetes-8e469f9cdcfd) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed structural guide for configuring an enterprise-grade, highly available HashiCorp Vault cluster in Kubernetes. Features automated unsealing integrations using cloud KMS systems (AWS KMS/GCP KMS) to remove manual keys dependencies.
#### OWASP

  - **(2022)** [itnext.io: Kubernetes OWASP Top 10: Secrets Management](https://itnext.io/kubernetes-owasp-top-10-secrets-management-c996faa87b47)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Addresses Secrets Management under the OWASP Kubernetes threat framework. Details vulnerabilities of default etcd storage parameters and details using External Secrets Operator or HashiCorp Vault. Prevents secrets exposure via repository check-ins or pod environment parameters.
## Security Training and Playgrounds

### Kubernetes Goat Lab

  - **(2020)** [Kubernetes Goat 🌟](https://madhuakula.com/kubernetes-goat) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An intentionally vulnerable cluster environment designed for hands-on cybersecurity training. Includes self-contained scenarios exploring SSRF, container escape, secrets leakage, and misconfigured RBAC roles.
## Supply Chain Security

### Signature Verification and Ratify

  - **(2021)** [infoworld.com: Securing the Kubernetes software supply chain with Microsoft's Ratify](https://www.infoworld.com/article/2271333/securing-the-kubernetes-software-supply-chain.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on utilizing Ratify as an admission controller to verify container metadata, secure supply-chain signatures (via Cosign/Notation), and enforce strict provenance validation before execution.
## Threat Modeling

### MITRE ATTandCK Adaptation

  - **(2021)** [microsoft.com: Secure containerized environments with updated threat matrix for Kubernetes](https://www.microsoft.com/security/blog/2021/03/23/secure-containerized-environments-with-updated-threat-matrix-for-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses updates to Microsoft's threat matrix for Kubernetes, refining mapped attack vectors based on modern production compromise telemetry. Covers control plane compromises and cloud identity integrations.
### MITRE ATTandCK Framework

  - **(2020)** [Microsoft.com: Attack matrix for Kubernetes 🌟](https://www.microsoft.com/security/blog/2020/04/02/attack-matrix-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Microsoft's systematic adaptation of the MITRE ATT&CK framework mapping out K8s attack vectors from initial access to execution, persistence, privilege escalation, and impact. Helps security operators assess risks in orchestration configurations.
## Vulnerability Assessment Tools

### Kubestriker Scanner

  - **(2021)** [helpnetsecurity.com: Kubestriker: A security auditing tool for Kubernetes clusters 🌟](https://www.helpnetsecurity.com/2021/05/04/security-kubernetes) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews Kubestriker, a lightweight, agentless open-source security scanner that audits Kubernetes control plane configurations, insecure ports, and IAM roles for vulnerabilities.
## Workload Hardening

### Identity and Access Management (2)

  - **(2020)** [thenewstack.io: Laying the Groundwork for Kubernetes Security, Across Workloads, Pods and Users](https://thenewstack.io/laying-the-groundwork-for-kubernetes-security-across-workloads-pods-and-users) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the multi-dimensional security layers required for modern Kubernetes deployments, addressing workload isolation, Pod Security Standards (PSS), and secure developer workflow patterns.
### Pod Security Context

  - **(2020)** [snyk.io: 10 Kubernetes Security Context settings you should understand](https://snyk.io/blog/10-kubernetes-security-context-settings-you-should-understand) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed documentation of essential Security Context settings (e.g., `allowPrivilegeEscalation`, `readOnlyRootFilesystem`, and `runAsNonRoot`) used to harden workload runtimes.
### Pod Specifications

  - **(2021)** [blog.gitguardian.com: Kubernetes Hardening Tutorial Part 1: Pods](https://blog.gitguardian.com/kubernetes-tutorial-part-1-pods) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part one of GitGuardian's workload security tutorial, targeting critical pod configurations such as root user restrictions, secure namespaces, and minimizing host-level network sharing.

---
💡 **Explore Related:** [Securityascode](./securityascode.md) | [Ansible](./ansible.md) | [Devsecops](./devsecops.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

