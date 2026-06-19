# Security Policy as Code

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/securityascode/).

!!! info "Architectural Context"
    Detailed reference for Security Policy as Code in the context of Hardened Infrastructure.

## Table of Contents

1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Cloud Native Security](#cloud-native-security)
  - [Infrastructure Security](#infrastructure-security)
    - [IaC Scanning](#iac-scanning)
    - [Mergers and Acquisitions](#mergers-and-acquisitions)
    - [Runtime Analysis](#runtime-analysis)
  - [Policy-as-Code](#policy-as-code)
    - [Educational Video](#educational-video)
    - [Governance](#governance)
    - [Kyverno](#kyverno)
    - [Kyverno Training](#kyverno-training)
    - [OPA](#opa)
    - [OPA Wasm](#opa-wasm)
    - [Rego](#rego)
1. [Cloud-Native Platforms](#cloud-native-platforms)
  - [Infrastructure-as-Code](#infrastructure-as-code)
    - [Tagging and Auditing](#tagging-and-auditing)
  - [Kubernetes Reliability](#kubernetes-reliability)
    - [High Availability](#high-availability)
  - [Kubernetes Security](#kubernetes-security)
    - [EKS](#eks)
    - [GitOps](#gitops)
    - [Governance](#governance-1)
    - [Kyverno](#kyverno-1)
    - [Kyverno Policies](#kyverno-policies)
    - [Kyverno Releases](#kyverno-releases)
    - [Policy-as-Code](#policy-as-code-1)
    - [Upgrade Paths](#upgrade-paths)
  - [Kubernetes Storage](#kubernetes-storage)
    - [Policy-as-Code](#policy-as-code-2)
  - [Multi-Cloud Governance](#multi-cloud-governance)
    - [Compliance Engine](#compliance-engine)
  - [Multi-Cluster Management](#multi-cluster-management)
    - [Policy-as-Code](#policy-as-code-3)
  - [Security and Compliance](#security-and-compliance)
    - [Cloud Security](#cloud-security)
    - [Developer Tooling](#developer-tooling)
    - [IaC Security](#iac-security)
    - [Policy Library](#policy-library)
    - [Policy-as-Code](#policy-as-code-4)
  - [Security Reporting](#security-reporting)
    - [Observability](#observability)
  - [Supply Chain Security](#supply-chain-security)
    - [Container Governance](#container-governance)
    - [Container Verifying](#container-verifying)
    - [Cryptographic Signatures](#cryptographic-signatures)
1. [Public Cloud](#public-cloud)
  - [Azure Integration](#azure-integration)
    - [Cloud Governance](#cloud-governance)
1. [Security](#security)
  - [Policy Enforcement](#policy-enforcement)
    - [Admission Control](#admission-control)

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [IBM Vault 2.0 UI Enhancements and Reporting Improvements](https://t.co/cvOceuueCF)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering IBM Vault 2.0 UI Enhancements and Reporting Improvements in the Kubernetes Tools ecosystem.
  - [Web-Check](https://web-check.xyz)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Web-Check in the Kubernetes Tools ecosystem.
  - [Docker Hardened Images for Every Developer](https://www.docker.com/blog/docker-hardened-images-for-every-developer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Docker Hardened Images for Every Developer in the Kubernetes Tools ecosystem.
  - [IBM IAM for AI Agents](https://t.co/EKsVgKA4xn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering IBM IAM for AI Agents in the Kubernetes Tools ecosystem.
  - [medium: Automate policies enforcement with Policy-as-Code 🌟](https://medium.com/airwalk/automate-policies-enforcement-with-policy-as-code-2f20aac9e2b0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Automate policies enforcement with Policy-as-Code 🌟 in the Kubernetes Tools ecosystem.
  - [magalix.com: Integrating Open Policy Agent (OPA) With Kubernetes 🌟](https://www.magalix.com/blog/integrating-open-policy-agent-opa-with-kubernetes-a-deep-dive-tutorial)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering magalix.com: Integrating Open Policy Agent (OPA) With Kubernetes 🌟 in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Integrating Identity: OAUTH2 and OPENID CONNECT in Open' Policy Agent](https://blog.styra.com/blog/integrating-identity-oauth2-and-openid-connect-in-open-policy-agent)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Integrating Identity: OAUTH2 and OPENID CONNECT in Open' Policy Agent in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Rego Unit Testing](https://blog.styra.com/blog/rego-unit-testing)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Rego Unit Testing in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Dynamic Policy Composition for OPA](https://blog.styra.com/blog/dynamic-policy-composition-for-opa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Dynamic Policy Composition for OPA in the Kubernetes Tools ecosystem.
  - [blog.styra.com: 5 OPA Deployment Performance Models for Microservices](https://blog.styra.com/blog/5-opa-deployment-performance-models-for-microservices)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: 5 OPA Deployment Performance Models for Microservices in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Open Policy Agent: The Top 5 Kubernetes Admission Control' Policies](https://blog.styra.com/blog/open-policy-agent-the-top-5-kubernetes-admission-control-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Open Policy Agent: The Top 5 Kubernetes Admission Control' Policies in the Kubernetes Tools ecosystem.
  - [siegert-maximilian.medium.com: Ensure Content Trust on Kubernetes using' Notary and Open Policy Agent](https://siegert-maximilian.medium.com/ensure-content-trust-on-kubernetes-using-notary-and-open-policy-agent-485ab3a9423c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering siegert-maximilian.medium.com: Ensure Content Trust on Kubernetes using' Notary and Open Policy Agent in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Policy-based infrastructure guardrails with Terraform and' OPA 🌟](https://blog.styra.com/blog/policy-based-infrastructure-guardrails-with-terraform-and-opa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Policy-based infrastructure guardrails with Terraform and' OPA 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Automated Manifest File Validation Using Open Policy Agent and GitHub' Actions | Ravindu Sandeepa Rathugama](https://medium.com/@ravindursr/automated-manifest-file-validation-using-open-policy-agent-and-github-actions-697fa9fd74f0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Automated Manifest File Validation Using Open Policy Agent and GitHub' Actions | Ravindu Sandeepa Rathugama in the Kubernetes Tools ecosystem.
  - [inspektor.cloud: Evaluating open policy agent in rust using wasm](https://inspektor.cloud/blog/evaluating-open-policy-agent-in-rust-using-wasm)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering inspektor.cloud: Evaluating open policy agent in rust using wasm in the Kubernetes Tools ecosystem.
  - [medium.com/4th-coffee: What is Policy-as-Code? An Introduction to Open Policy' Agent](https://medium.com/4th-coffee/what-is-policy-as-code-an-introduction-to-open-policy-agent-6098463f8461)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/4th-coffee: What is Policy-as-Code? An Introduction to Open Policy' Agent in the Kubernetes Tools ecosystem.
  - [banzaicloud.com: Istio and Kubernetes ft. OPA policies](https://banzaicloud.com/blog/istio-opa)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering banzaicloud.com: Istio and Kubernetes ft. OPA policies in the Kubernetes Tools ecosystem.
  - [medium: Ensure Content Trust on Kubernetes using Notary and Open Policy' Agent](https://medium.com/@siegert.maximilian/ensure-content-trust-on-kubernetes-using-notary-and-open-policy-agent-485ab3a9423c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Ensure Content Trust on Kubernetes using Notary and Open Policy' Agent in the Kubernetes Tools ecosystem.
  - [medium: Deploying Open Policy Agent (OPA) on a GKE cluster — Step by Step](https://medium.com/linkbynet/deploying-opa-on-a-gke-cluster-da4d3d77812c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Deploying Open Policy Agent (OPA) on a GKE cluster — Step by Step in the Kubernetes Tools ecosystem.
  - [blog.styra.com: Using OPA with GitOps to speed Cloud-Native development](https://blog.styra.com/blog/using-opa-with-gitops-to-speed-cloud-native-development)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering blog.styra.com: Using OPA with GitOps to speed Cloud-Native development in the Kubernetes Tools ecosystem.
  - [medium.com/gitguardian: What is Policy-as-Code? An Introduction to Open' Policy Agent](https://medium.com/gitguardian/what-is-policy-as-code-an-introduction-to-open-policy-agent-dba1400bb030)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/gitguardian: What is Policy-as-Code? An Introduction to Open' Policy Agent in the Kubernetes Tools ecosystem.
  - [hashicorp.com: Securing Infrastructure In Application Pipelines](https://www.hashicorp.com/resources/securing-infrastructure-in-application-pipelines)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering hashicorp.com: Securing Infrastructure In Application Pipelines in the Kubernetes Tools ecosystem.
  - [venturebeat.com: How Nirmata plans to ‘conquer Kubernetes complexity’ with' open source Kyverno](https://venturebeat.com/2021/08/10/how-nirmata-plans-to-conquer-kubernetes-complexity-with-open-source-kyverno)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering venturebeat.com: How Nirmata plans to ‘conquer Kubernetes complexity’ with' open source Kyverno in the Kubernetes Tools ecosystem.
  - [movi.hashnode.dev: Simplify Kubernetes Cluster Management with Kyverno](https://movi.hashnode.dev/simplify-kubernetes-cluster-management-with-kyverno-ckt6yxjqy0duy95s14groe7h4)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering movi.hashnode.dev: Simplify Kubernetes Cluster Management with Kyverno in the Kubernetes Tools ecosystem.
  - [arun-sisodiya.medium.com: Kyverno — A Kubernetes native policy manager (Policy' as Code)](https://arun-sisodiya.medium.com/kyverno-a-policy-manager-for-kubernetes-286f6e082062)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering arun-sisodiya.medium.com: Kyverno — A Kubernetes native policy manager (Policy' as Code) in the Kubernetes Tools ecosystem.
  - [medium.com/compass-true-north: Governing Multi-Tenant Kubernetes Clusters' with Kyverno](https://medium.com/compass-true-north/governing-multi-tenant-kubernetes-clusters-with-kyverno-3e11ba4a64ad)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/compass-true-north: Governing Multi-Tenant Kubernetes Clusters' with Kyverno in the Kubernetes Tools ecosystem.
  - [medium.com/@haseebshaukat2: Kyverno — Policy Engine for Kubernetes | Muhammad' Haseeb Shaukat](https://medium.com/@haseebshaukat2/kyverno-policy-engine-for-kubernetes-b49f3fac43b9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@haseebshaukat2: Kyverno — Policy Engine for Kubernetes | Muhammad' Haseeb Shaukat in the Kubernetes Tools ecosystem.
  - [medium.com/@glen.yu: Why I prefer Kyverno over Gatekeeper for native Kubernetes' policy management](https://medium.com/@glen.yu/why-i-prefer-kyverno-over-gatekeeper-for-native-kubernetes-policy-management-35a05bb94964)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@glen.yu: Why I prefer Kyverno over Gatekeeper for native Kubernetes' policy management in the Kubernetes Tools ecosystem.
## Cloud Native Security

### Infrastructure Security

#### IaC Scanning

  - **(2021)** [Apolicy](https://www.sysdig.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Apolicy (acquired by Sysdig) provides advanced policy-as-code governance designed for shifting cloud security left. Scans Infrastructure-as-Code (IaC) templates and automatically matches security rules to production deployment settings.
#### Mergers and Acquisitions

  - **(2021)** [sysdig.com: Sysdig and Apolicy join forces to help customers secure Infrastructure As Code and automate remediation](https://www.sysdig.com/blog/sysdig-and-apolicy-join-forces-to-help-customer-secure-infrastructure-as-code) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry announcement detailing Sysdig's acquisition of Apolicy. Highlights the integration of IaC security analysis with runtime monitoring to establish unified, end-to-end security loops from Git commits to production containers.
#### Runtime Analysis

  - **(2024)** [Fugue: Container and Kubernetes. Runtime infrastructure security](https://snyk.io/product/container-vulnerability-management) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Fugue (now integrated under Snyk Container security suite) delivers continuous compliance and automated infrastructure monitoring for AWS, Azure, and Google Cloud alongside Kubernetes runtime configurations, mapping live states to CIS Benchmarks and SOC 2 frameworks.
### Policy-as-Code

#### Educational Video

  - **(2021)** [youtube: The Rise of Kubernetes Policy Engine | Ep 57](https://www.youtube.com/watch?v=0TvhTXddRGE) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An informative panel discussion examining the rise of Kubernetes policy engines. Tracks the evolution from manual auditing workflows to declarative, automated gatekeeping systems using OPA Gatekeeper and Kyverno.
#### Governance

  - **(2021)** [searchitoperations.techtarget.com: CNCF policy-as-code project bridges Kubernetes security gaps](https://www.techtarget.com/searchitoperations/news/252505548/CNCF-policy-as-code-project-bridges-Kubernetes-security-gaps) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industry report outlining CNCF policy-as-code initiatives designed to patch security deficiencies within container orchestration. Compares the operational paradigms of Rego-based OPA and YAML-native Kyverno for policy-driven environments.
#### Kyverno

  - **(2021)** [cloud.redhat.com: Automate Your Security Practices and Policies on OpenShift With Kyverno 🌟](https://www.redhat.com/en/blog/automate-your-security-practices-and-policies-on-openshift-with-kyverno) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates automated security practice implementation inside OpenShift clusters utilizing Kyverno. Explores Kyverno's YAML-native approach, highlighting how platform engineers write policies using standard Kubernetes resource models without learning new programming languages.
#### Kyverno Training

  - **(2023)** [appsecengineer.com: Kubernetes Policy Management with Kyverno](https://www.appsecengineer.com/courses-collection/kubernetes-policy-management-with-kyverno) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An educational course focusing on Kyverno-driven Kubernetes policy engineering. Walks developers and SREs through writing advanced manifest mutation, generation, and validation policies with real-world scenarios.
#### OPA

  - **(2020)** [searchitoperations.techtarget.com: Kubernetes policy project takes enterprise IT by storm](https://www.techtarget.com/searchitoperations/news/252467102/Kubernetes-policy-project-takes-enterprise-IT-by-storm) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the massive industry shift toward Open Policy Agent (OPA) for centralized, policy-as-code enforcement. Emphasizes OPA's ability to unify policy layers across different tools like Kubernetes admission controllers, API gateways, and CI/CD pipelines.
  - **(2020)** [blog.openshift.com: Fine-Grained Policy Enforcement in OpenShift with Open Policy Agent 🌟](https://www.redhat.com/en/blog/fine-grained-policy-enforcement-in-openshift-with-open-policy-agent) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive technical article by Red Hat showcasing fine-grained policy enforcement in OpenShift using Open Policy Agent. Details how to intercept Kubernetes API requests via admission controllers to block non-compliant resource deployments programmatically.
#### OPA Wasm

  - **(2025)** [==compile OpenPolicyAgent policies into WebAssembly and run them on the edge==](https://github.com/open-policy-agent/contrib/tree/main/wasm/cloudflare-worker) <span class='md-tag md-tag--info'>⭐ 348</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ba4855b5" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 3 L 20 8 L 30 10 L 40 4 L 50 6" fill="none" stroke="url(#spark-grad-ba4855b5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[WEBASSEMBLY CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source utility that compiles declarative Open Policy Agent (Rego) policies into high-performance WebAssembly (Wasm) modules. Designed for lightning-fast security and routing decisions at edge platforms like Cloudflare Workers and Envoy proxies.
#### Rego

  - **(2021)** [fugue.co: 5 tips for using the Rego language for Open Policy Agent (OPA)](https://snyk.io/blog) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An additional collection of advanced Rego development practices, focusing on unit-testing frameworks, mock injections, and playground emulator tools to ensure policy robustness and security governance.
## Cloud-Native Platforms

### Infrastructure-as-Code

#### Tagging and Auditing

  - **(2026)** [==yor.io==](https://yor.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source, extensible auto-tagging tool designed to dynamically trace infrastructure-as-code from code to cloud. It automatically adds ownership, lineage, and environment metadata tags during pull requests, allowing operations teams to seamlessly trace production resources back to their source repository.
  - **(2021)** [thenewstack.io: Yor Automates Tagging for Infrastructure as Code](https://thenewstack.io/yor-automates-tagging-for-infrastructure-as-code) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines the capabilities of Yor, an automated tagging engine designed to apply consistent metadata to IaC assets (Terraform, CloudFormation). Tracks resource ownership, drift, and git commit history through auto-injected tags, improving traceability and cloud financial operations (FinOps).
### Kubernetes Reliability

#### High Availability

  - **(2026)** [kyverno.io: Require PodDisruptionBudget](https://kyverno.io/policies/other/require_pdb) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A standardized Kyverno policy template ensuring that all mission-critical deployments are paired with active PodDisruptionBudgets (PDB). This governance rule guarantees cluster high-availability by guarding applications against node drain and cluster maintenance operations.
### Kubernetes Security

#### EKS

  - **(2021)** [dev.to: Using Kyverno To Enforce EKS Best Practices](https://dev.to/rinkiyakedad/using-kyverno-to-enforce-eks-best-practices-cad) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guided tutorial showing how platform engineers can utilize Kyverno to systematically lock down Amazon EKS clusters. Illustrates policy enforcement setups to enforce multi-tenant isolation, require standard resource limits, and disable host networking, using declarative Kubernetes manifests.
#### GitOps

  - **(2021)** [thenewstack.io: Weaveworks Adds Policy as Code to Secure Kubernetes Apps' (Magalix)](https://thenewstack.io/weaveworks-adds-policy-as-code-to-secure-kubernetes-apps) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reports on Weaveworks' acquisition and integration of Magalix to embed Policy-as-Code directly into GitOps pipelines. Details how declarative governance policies can be evaluated in continuous-delivery cycles prior to deployment, preventing misconfigured resources from ever entering a live cluster.
#### Governance (1)

  - **(2022)** [dev.to: Using Kyverno Policies for Kubernetes Governance](https://dev.to/mda590/using-kyverno-policies-for-kubernetes-governance-3e17) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains how organizations can use Kyverno to establish governance guardrails across shared development environments. Covers automating labels, validating ownership configurations, and managing resource consumption rules to ensure multi-tenant hygiene.
#### Kyverno (1)

  - **(2026)** [kyverno.io: Mutating Resources](https://kyverno.io/docs/writing-policies/mutate) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation detailing how Kyverno modifies incoming resource specifications dynamically using JSON patch operations. It covers mutating rules such as auto-injecting sidecar containers, adding node affinity constraints, and enforcing default labels on namespaces at creation time.
  - **(2026)** [kyverno.io: Generating resources into existing namespaces](https://kyverno.io/docs/writing-policies/generate) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official guide on retroactively generating Kubernetes objects, such as secrets or network rules, across pre-existing namespaces using Kyverno's dynamic policy synchronization engine. Eliminates manually syncing resources across namespaces created prior to policy deployment.
  - **(2026)** [kyverno.io: Auto-Gen Rules for Pod Controllers](https://kyverno.io/docs/writing-policies/autogen) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Illustrates how Kyverno automatically propagates policies applied to raw Pod specs to downstream controllers (Deployments, DaemonSets, StatefulSets). Simplifies security operations by validating configurations at high-level workloads rather than only catching errors at low-level pod schedulers.
  - **(2021)** [squadcast.com: Kyverno - Policy Management in Kubernetes 🌟](https://www.squadcast.com/blog/kyverno-policy-management-in-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the design patterns of Kyverno as a Kubernetes-native policy engine that eliminates the need to learn specialized programming languages. Highlights how Kyverno manages resource validation, mutation, and generation using declarative YAML configurations designed to fit existing GitOps workflows.
  - **(2020)** [neonmirrors.net: Exploring Kyverno: Part 3, Generation](https://neonmirrors.net/post/2020-12/exploring-kyverno-part3) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dive technical exploration into Kyverno's generation rules, demonstrating how the policy engine can automatically provision ancillary resources, like NetworkPolicies or ConfigMaps, whenever a new namespace is initialized. Optimizes cluster bootstrapping without custom operators.
  - **(2020)** [neonmirrors.net: Exploring Kyverno: Introduction 🌟](https://neonmirrors.net/post/2020-11/exploring-kyverno-intro) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A foundational introductory article dissecting the architecture and operational benefits of adopting Kyverno. Contrasts it with custom-coded validating webhooks and details its direct design philosophy of aligning container policy administration with idiomatic Kubernetes constructs.
#### Kyverno Policies

  - **(2026)** [kyverno.io: Add Pod Proxies](https://kyverno.io/policies/other/add-pod-proxies) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical documentation demonstrating how to use Kyverno to dynamically inject HTTP/HTTPS proxy environment variables into Pod containers upon admission. Solves enterprise proxy configuration demands automatically without requiring manual pod-by-pod updates from development teams.
  - **(2026)** [kyverno.io: Implementing your best practices is simple with kyverno](https://kyverno.io/policies/best-practices/require_probes/require_probes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Standard Kyverno policy design pattern focused on enforcing health probe settings (liveness, readiness, startup) across all deployed container payloads. This rule enforces Kubernetes operations best practices, safeguarding application lifecycle management and endpoint routing.
#### Kyverno Releases

  - **(2021)** [nirmata.com: Introducing Kyverno 1.4.2: Trusted And More Efficient!](https://nirmata.com/2021/08/18/introducing-kyverno-1-4-2-trusted-and-more-efficient) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Reviews release-specific improvements introduced in Kyverno v1.4.2, highlighting optimizations in validation speeds, improved caching models, and expanded schema support. Provides performance benchmarks of Kyverno when subjected to scale workloads across massive enterprise orchestrators.
#### Policy-as-Code (1)

  - **(2022)** [==k8s-security-policies==](https://github.com/raspbernetes/k8s-security-policies) <span class='md-tag md-tag--info'>⭐ 177</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-36066366" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 10 L 20 5 L 30 6 L 40 5 L 50 3" fill="none" stroke="url(#spark-grad-36066366)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="3" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — A repository hosting robust and ready-to-use security configurations for Kubernetes clusters, heavily focused on replacing deprecated PodSecurityPolicies with Kyverno and OPA alternatives. It is a highly practical compliance baseline library for platform teams seeking rapid deployment of security controls.
  - **(2021)** [amazon.com: Policy-based countermeasures for Kubernetes – Part 1](https://aws.amazon.com/blogs/containers/policy-based-countermeasures-for-kubernetes-part-1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed architectural guide on implementing declarative guardrails in EKS clusters to reduce attack surfaces. Focuses on the synergy between Kubernetes admission controllers and modern policy engines, illustrating how to validate and mutate payloads to block insecure configuration drift.
  - **(2021)** [aws.amazon.com: Policy-based countermeasures for Kubernetes – Part 1](https://aws.amazon.com/es/blogs/containers/policy-based-countermeasures-for-kubernetes-part-1) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spanish localized edition of AWS's architectural breakdown detailing policy-driven mitigations within Kubernetes runtime layers. Instructs platform engineers on configuring robust security guardrails using native Kubernetes controllers and cloud provider identity brokers to neutralize container vulnerabilities.
  - **(2021)** [neonmirrors.net: Kubernetes Policy Comparison: OPA/Gatekeeper vs Kyverno' 🌟](https://neonmirrors.net/post/2021-02/kubernetes-policy-comparison-opa-gatekeeper-vs-kyverno) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A seminal technical comparison contrasting the architecture and design patterns of OPA Gatekeeper (relying on the domain-specific Rego language) against Kyverno (which uses native Kubernetes YAML). Helps engineers evaluate resource consumption, developer velocity, and cognitive overhead for both systems.
  - **(2021)** [sesin.at: Securing Kubernetes with Kyverno: How to Protect Your Users From' Themselves by Ritesh Patel](https://www.sesin.at/2021/08/28/securing-kubernetes-with-kyverno-how-to-protect-your-users-from-themselves-by-ritesh-patel) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores security policy implementation using Kyverno to proactively safeguard users against unsafe configuration actions. Discusses deployment of best-practice guardrails, preventing privilege escalation, insecure mount paths, and other critical risks without impeding agile deployment workflows.
#### Upgrade Paths

  - **(2026)** [kyverno.io: Check deprecated APIs 🌟](https://kyverno.io/policies/best-practices/check_deprecated_apis) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Outlines a pre-configured Kyverno policy targeted at scanning incoming manifests to detect and block deprecated or removed Kubernetes API groups. Indispensable for preventing cluster upgrade blockages, validating manifests before execution on newer API-driven orchestrators.
### Kubernetes Storage

#### Policy-as-Code (2)

  - **(2021)** [dev.to: Default Kyverno Policies for OpenEBS](https://dev.to/niveditacoder/default-kyverno-policies-for-openebs-4abf) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Walks through establishing Kyverno policies optimized for workloads using OpenEBS as their persistent storage driver. Demonstrates how to automatically enforce volume attachment limits, dynamic volume provisioning policies, and validate container mount points for improved system stability.
### Multi-Cloud Governance

#### Compliance Engine

  - **(2026)** [==Cloud Custodian==](https://github.com/cloud-custodian/cloud-custodian) <span class='md-tag md-tag--info'>⭐ 6007</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6de45dba" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 12 L 20 4 L 30 8 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-6de45dba)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A robust, YAML-configured rules engine used by enterprise platform engineers to manage multi-cloud compliance, cost control, and security posture across AWS, Azure, and GCP. Automates cost-saving resource deletions, tag compliance, and real-time security remediation.
### Multi-Cluster Management

#### Policy-as-Code (3)

  - **(2021)** [kubermatic.com: Using Open Policy Agent With Kubermatic Kubernetes Platform](https://www.kubermatic.com/blog/using-open-policy-agent-with-kubermatic) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines the implementation of OPA Gatekeeper within Kubermatic Kubernetes Platform (KKP) for programmatic multi-cluster fleet management. Illustrates how operators can centrally define, distribute, and enforce admission controller policies across dozens of hybrid and multi-cloud Kubernetes deployments.
### Security and Compliance

#### Cloud Security

  - **(2026)** [==Selefra: Selefra is an open-source policy-as-code software that provides' analytics for multi-cloud and SaaS.==](https://github.com/selefra/selefra) <span class='md-tag md-tag--info'>⭐ 545</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-1224f44c" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 2 L 20 10 L 30 8 L 40 2 L 50 6" fill="none" stroke="url(#spark-grad-1224f44c)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An open-source policy-as-code platform engineered to analyze multi-cloud and SaaS configurations using SQL-based query patterns. This tool enables developers to scan cloud resources for compliance defects, security gaps, and operational overhead with rapid execution and modular plugins.
#### Developer Tooling

  - **(2021)** [==PolicyHub CLI, a CLI tool that makes Rego policies searchable 🌟==](https://github.com/policy-hub/policy-hub-cli) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A lightweight command-line utility engineered to improve discoverability and usability of Rego-based policies. This tool parses and indexes shared policy repositories, enabling infrastructure and platform engineers to search, validate, and integrate standard compliance policies directly from local environments.
#### IaC Security

  - **(2026)** [==checkov.io==](https://www.checkov.io) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A leading static code analysis utility designed to scan Infrastructure-as-Code configurations (Terraform, Kubernetes, CloudFormation, Helm, Dockerfile) for security misconfigurations. Features out-of-the-box policy libraries that enforce industry standards like CIS Benchmarks, SOC2, and HIPAA prior to deployment.
#### Policy Library

  - **(2021)** [==github.com/instrumenta/policies: A set of shared policies for use with Conftest' and other Open Policy Agent tools==](https://github.com/instrumenta/policies) <span class='md-tag md-tag--info'>⭐ 66</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-bfe49355" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 7 L 20 11 L 30 7 L 40 9 L 50 9" fill="none" stroke="url(#spark-grad-bfe49355)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="9" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[REGO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A structured directory of modular policy files for linting infrastructure-as-code deployments (Terraform, Kubernetes YAML, Helm charts). Designed to enforce standards like non-root container runs, memory limit boundaries, and forbidden network ingress setups early in CI/CD cycles.
#### Policy-as-Code (4)

  - **(2026)** [==OPA Open Policy Agent 🌟==](https://www.openpolicyagent.org) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — General-purpose policy engine designed to unify and enforce fine-grained authorization across microservices, Kubernetes, CI/CD, and API gateways. Uses the declarative query language Rego to decouple policy decisions from execution, serving as a critical cornerstone in modern Zero-Trust architectures.
  - **(2022)** [blog.gitguardian.com: What is Policy-as-Code? An Introduction to Open Policy' Agent](https://blog.gitguardian.com/what-is-policy-as-code-an-introduction-to-open-policy-agent) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Comprehensive introduction to Open Policy Agent (OPA) and its application of declarative, domain-agnostic policy enforcement using the Rego language. Evaluates the architectural shift of separating policy logic from application code, making security policies testable and auditable in Git repos.
  - **(2022)** [dev.to: Load external data into OPA: The Good, The Bad, and The Ugly](https://dev.to/permit_io/load-external-data-into-opa-the-good-the-bad-and-the-ugly-26lc) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyses the complex architectural patterns required for injecting dynamic runtime datasets into Open Policy Agent (OPA). Evaluates caching strategies, JWT validation, HTTP pull-push mechanisms, and their relative trade-offs regarding latency, scalability, and network failure tolerance inside authorization pathways.
  - **(2021)** [thenewstack.io: Getting Open Policy Agent Up and Running](https://thenewstack.io/getting-open-policy-agent-up-and-running) <span class='md-tag md-tag--warning'>[REGO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A pragmatic guide detailing bootstrap procedures for deploying Open Policy Agent (OPA) inside production systems. Guides the reader through daemon configuration, loading external data contexts, and integrating policy enforcement into Kubernetes via the Gatekeeper admission controller framework.
### Security Reporting

#### Observability

  - **(2026)** [==Policy Reporter 🌟==](https://github.com/kyverno/policy-reporter) <span class='md-tag md-tag--info'>⭐ 371</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-65952f03" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 8 L 20 9 L 30 3 L 40 13 L 50 10" fill="none" stroke="url(#spark-grad-65952f03)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A CNCF-recognized dashboard and reporter engineered to capture, aggregate, and visualize policy violations (like Kyverno or OPA findings) inside Kubernetes clusters. Converts abstract policy status reports into accessible web UI tables and distributes real-time alerts to Slack or Grafana.
### Supply Chain Security

#### Container Governance

  - **(2026)** [kyverno.io: Restrict Image Registries](https://kyverno.io/policies/best-practices/restrict_image_registries/restrict_image_registries) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official documentation outlining how to write Kyverno policies to block deployment of images from unapproved registries. Enforces a key tenant of secure container delivery by ensuring workloads only pull code from trusted, internally-vetted registry endpoints.
#### Container Verifying

  - **(2021)** [nirmata.com: Kubernetes Supply Chain Policy Management with Cosign and Kyverno](https://nirmata.com/2021/08/12/kubernetes-supply-chain-policy-management-with-cosign-and-kyverno) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Practical guide demonstrating how Nirmata utilizes Sigstore Cosign paired with Kyverno to authenticate digital signatures on incoming container images. Establishes programmatic cryptographic validation inside admission paths, preventing unverified or tampered binaries from launching in production environments.
#### Cryptographic Signatures

  - **(2022)** [blog.sigstore.dev: How to verify container images with Kyverno using KMS,' Cosign, and Workload Identity](https://blog.sigstore.dev/how-to-verify-container-images-with-kyverno-using-kms-cosign-and-workload-identity-1e07d2b85061) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An advanced technical exploration of enterprise container security architectures. Provides steps to construct a validation loop that verifies image signatures dynamically using Kyverno, integrated directly with KMS key stores, Sigstore Cosign, and OIDC-based Workload Identity.
## Public Cloud

### Azure Integration

#### Cloud Governance

  - **(2026)** [**Azure Policy**](https://nubenetes.com/azure/) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Specialized gateway and reference documentation for enforcing structural compliance, resource auditing, and governance across Azure resource environments. Explains custom definition policies, policy initiatives, and automated remediation workflows. Critical reference for maintaining operational guardrails in enterprise cloud architectures.
## Security

### Policy Enforcement

#### Admission Control

  - **(2022)** [MagTape](https://github.com/tmobile/magtape) <span class='md-tag md-tag--info'>⭐ 152</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-7aafde66" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 5 L 20 7 L 30 3 L 40 5 L 50 7" fill="none" stroke="url(#spark-grad-7aafde66)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="7" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--critical'>[LEGACY]</span> — An admission controller developed by T-Mobile that evaluates resources against organizational policy constraints during creation. Written in Node.js, it offered a lightweight alternative to OPA for specific JSON schema validations. By 2026, it has been largely archived, with developers migrating to Gatekeeper or Kyverno.

---
💡 **Explore Related:** [IaC](./iac.md) | [Terraform](./terraform.md) | [Chef](./chef.md)

