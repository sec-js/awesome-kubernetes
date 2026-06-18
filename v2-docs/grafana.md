# Grafana

!!! info "Architectural Context"
    Detailed reference for Grafana in the context of Architectural Foundations.

## Table of Contents

1. [Infrastructure as Code](#infrastructure-as-code)
  - [Package Archives](#package-archives)
    - [Visualization](#visualization)
1. [Kubernetes and Cloud Native](#kubernetes-and-cloud-native)
  - [CICD](#cicd)
    - [Continuous Deployment](#continuous-deployment)
1. [Kubernetes Tools](#kubernetes-tools)
  - [General Reference](#general-reference)
1. [Middleware](#middleware)
  - [Messaging Orchestration](#messaging-orchestration)
    - [Artemis Extensions](#artemis-extensions)
1. [Observability](#observability)
  - [Infrastructure as Code](#infrastructure-as-code-1)
    - [Grafana Provisioning](#grafana-provisioning)
  - [Log Management](#log-management)
    - [Deployment Guides](#deployment-guides)
    - [Grafana Loki](#grafana-loki)
  - [Metrics](#metrics)
    - [High Availability Prometheus](#high-availability-prometheus)
    - [Kubernetes Scheduling](#kubernetes-scheduling)
  - [Scraping and Exporters](#scraping-and-exporters)
    - [JVM Monitoring](#jvm-monitoring)
  - [Telemetry](#telemetry)
    - [eBPF Application Monitoring](#ebpf-application-monitoring)
  - [Visualization](#visualization-1)
    - [Grafana Configuration](#grafana-configuration)
    - [Grafana Extensibility](#grafana-extensibility)
    - [Infrastructure as Code](#infrastructure-as-code-2)
    - [Product Updates](#product-updates)
    - [Unified Alerting](#unified-alerting)
1. [Observability and Delivery](#observability-and-delivery)
  - [Application Observability](#application-observability)
    - [Grafana Faro RUM](#grafana-faro-rum)
  - [Kubernetes Observability](#kubernetes-observability)
    - [Grafana Cloud](#grafana-cloud)
  - [Load Testing](#load-testing)
    - [k6 and OpenTelemetry](#k6-and-opentelemetry)
  - [Metrics Querying](#metrics-querying)
    - [PromQL Basics](#promql-basics)
  - [Network Monitoring](#network-monitoring)
    - [Advanced Prometheus](#advanced-prometheus)
    - [Prometheus snmp_exporter](#prometheus-snmpexporter)
  - [Platform Operations](#platform-operations)
    - [Managed Observability](#managed-observability)
  - [Synthetic Monitoring](#synthetic-monitoring)
    - [Grafana Alerting](#grafana-alerting)
  - [Visualization](#visualization-2)
    - [Dashboard Design](#dashboard-design)
    - [Grafana Cloud](#grafana-cloud-1)
    - [Grafana Cloud Integration](#grafana-cloud-integration)
    - [Grafana Plugins](#grafana-plugins)
    - [Grafana Releases](#grafana-releases)
1. [Observability and Monitoring](#observability-and-monitoring)
  - [Data Collection](#data-collection)
    - [Telemetry Agents](#telemetry-agents)
  - [Grafana Ecosystem](#grafana-ecosystem)
    - [AIOps and AI Observability](#aiops-and-ai-observability)
    - [Cloud and Enterprise Partnerships](#cloud-and-enterprise-partnerships)
    - [Cloud Integrations](#cloud-integrations)
    - [Community Dashboards](#community-dashboards)
    - [Dashboard-as-Code](#dashboard-as-code)
    - [Dashboards](#dashboards)
    - [Database Monitoring](#database-monitoring)
    - [Incident Management](#incident-management)
    - [Network Observability](#network-observability)
    - [Platform Evolution](#platform-evolution)
    - [Security and Access Control](#security-and-access-control)
    - [UX Best Practices](#ux-best-practices)
    - [User Experience and Usability](#user-experience-and-usability)
  - [Kubernetes Deployment](#kubernetes-deployment)
    - [Core Infrastructure Dashboards](#core-infrastructure-dashboards)
    - [Grafana Ecosystem](#grafana-ecosystem-1)
    - [Virtualization Monitoring](#virtualization-monitoring)
  - [Log Management](#log-management-1)
    - [Kubernetes Logging](#kubernetes-logging)
    - [Log Aggregation](#log-aggregation)
  - [Metrics Storage](#metrics-storage)
    - [Scalable TSDB](#scalable-tsdb)
  - [User Experience Monitoring](#user-experience-monitoring)
    - [Frontend Observability](#frontend-observability)

## Infrastructure as Code

### Package Archives

#### Visualization

  - **(2020)** [grafana-6.7.2-1.x86_64.rpm](https://grafana.com) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A legacy RPM binary package of Grafana 6.7.2. Kept as a reference point for historical dashboards and older enterprise network configurations.
## Kubernetes and Cloud Native

### CICD

#### Continuous Deployment

  - **(2020)** [jaxenter.com: CI/CD for Spring Boot Microservices: Part 2. Extending CI/CD: Kubernetes Continuous Deployment for Microservices](https://devm.io/blog) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Part two of the microservices CI/CD series, detailing continuous deployment onto active Kubernetes clusters. Focuses on orchestrating declarative manifest YAML files, configuring deployment strategies like rolling updates, and handling Kubernetes secrets securely.
## Kubernetes Tools

### General Reference

  - [magalix.com: Monitoring Kubernetes Clusters Through Prometheus & Grafana' 🌟](https://www.magalix.com/blog/monitoring-of-kubernetes-cluster-through-prometheus-and-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering magalix.com: Monitoring Kubernetes Clusters Through Prometheus & Grafana' 🌟 in the Kubernetes Tools ecosystem.
  - [medium: Why Grafana: Part II](https://medium.com/lightspeed-venture-partners/why-grafana-part-ii-2e7e42e0f7bb)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Why Grafana: Part II in the Kubernetes Tools ecosystem.
  - [alexandrev.medium.com: Grafana Alerting vs AlertManager: A Comparison of' Two Leading Monitoring Tools | Alex Vazquez](https://alexandrev.medium.com/grafana-alerting-vs-alertmanager-a-comparison-of-two-leading-monitoring-tools-5e262446a5f9)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering alexandrev.medium.com: Grafana Alerting vs AlertManager: A Comparison of' Two Leading Monitoring Tools | Alex Vazquez in the Kubernetes Tools ecosystem.
  - [sid-infinity-yadav.medium.com: Grafana Agent Kubernetes Operator](https://sid-infinity-yadav.medium.com/grafana-agent-kubernetes-operator-f89b744487f5)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering sid-infinity-yadav.medium.com: Grafana Agent Kubernetes Operator in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: Grafana Agent Flow: Simplifying Monitoring and' Telemetry Collection for Kubernetes Clusters](https://levelup.gitconnected.com/exploring-grafana-agent-flow-simplifying-monitoring-for-kubernetes-2a06a92614)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: Grafana Agent Flow: Simplifying Monitoring and' Telemetry Collection for Kubernetes Clusters in the Kubernetes Tools ecosystem.
  - [openlogic.com: How to develop Grafana Dashboards 🌟](https://www.openlogic.com/blog/how-visualize-prometheus-data-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering openlogic.com: How to develop Grafana Dashboards 🌟 in the Kubernetes Tools ecosystem.
  - [Prometheus Monitoring With Grafana. Prometheus Stats Dashboard and Prometheus Benchmark Dashboard](https://dzone.com/articles/prometheus-monitoring-with-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering Prometheus Monitoring With Grafana. Prometheus Stats Dashboard and Prometheus Benchmark Dashboard in the Kubernetes Tools ecosystem.
  - [medium.com/@dotdc: A set of modern Grafana dashboards for Kubernetes 🌟](https://medium.com/@dotdc/a-set-of-modern-grafana-dashboards-for-kubernetes-4b989c72a4b2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/@dotdc: A set of modern Grafana dashboards for Kubernetes 🌟 in the Kubernetes Tools ecosystem.
  - [medium.com/how-tos: How To Provisioning Dashboards In Grafana via Kubernetes](https://medium.com/how-tos/how-to-provisioning-dashboards-in-grafana-via-kubernetes-5d261508658d)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium.com/how-tos: How To Provisioning Dashboards In Grafana via Kubernetes in the Kubernetes Tools ecosystem.
  - [cleancloud-k8s.com: Handling Multiline Logs with Loki and Fluent Bit on' Kubernetes](https://cleancloud-k8s.com/2022/01/19/handling-multiline-logging-with-loki-and-fluent-bit-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering cleancloud-k8s.com: Handling Multiline Logs with Loki and Fluent Bit on' Kubernetes in the Kubernetes Tools ecosystem.
  - [faun.pub: Grafana, Prometheus, and Loki: Exploring Metrics and Logs](https://faun.pub/grafana-prometheus-and-loki-exploring-metrics-and-logs-f198637784fc)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering faun.pub: Grafana, Prometheus, and Loki: Exploring Metrics and Logs in the Kubernetes Tools ecosystem.
## Middleware

### Messaging Orchestration

#### Artemis Extensions

  - **(2024)** [==Artemis Prometheus Metrics Plugin==](https://github.com/rh-messaging/artemis-prometheus-metrics-plugin) <span class='md-tag md-tag--info'>⭐ 28</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-d9b8e9d6" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 10 L 20 9 L 30 7 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-d9b8e9d6)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Duplicates technical setup for the Artemis-Prometheus plugin, highlighting metrics formatting for queue lengths, active sessions, and underlying JVM memory states.
## Observability

### Infrastructure as Code (1)

#### Grafana Provisioning

  - **(2023)** [grafana.com: A complete guide to managing Grafana as code: tools, tips, and tricks](https://grafana.com/blog/a-complete-guide-to-managing-grafana-as-code-tools-tips-and-tricks) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An architectural guide detailing how to manage Grafana as code. Explores declarative tools, GitOps synchronization methods, and APIs (such as Grizzly, Terraform, and Kubernetes Operators) to achieve reproducible visualization dashboards, alert rules, and secure data sources inside multi-tenant configurations.
### Log Management

#### Deployment Guides

  - **(2021)** [youtube.com: Grafana Loki Promtail | Grafana Loki Setup And Configuration On CentOs](https://www.youtube.com/watch?v=iqpLXUdJ0Ro&ab_channel=Thetips4you)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video deployment guide demonstrating how to install and configure Grafana Loki and Promtail on CentOS systems. It covers host-level systemd service configuration, log routing patterns, and connecting local log collectors to centralized Loki nodes.
#### Grafana Loki

  - **(2020)** [Log Monitoring and Alerting with Grafana Loki](https://www.infracloud.io/blogs/grafana-loki-log-monitoring-alerting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed deployment guide focusing on log monitoring and alerting integration using Grafana Loki and Promtail. Loki's design indexing only log metadata allows clusters to achieve cost-efficient, low-latency log collection compared to full-text indexing solutions.
  - **(2019)** [thenewstack.io: Grafana Adds Logging to Its Enterprise Observability Stack 🌟](https://thenewstack.io/grafana-adds-logging-to-its-enterprise-observability-stack)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the commercial introduction of Grafana Loki as part of the Grafana Enterprise Observability Stack. This development unified metrics and logging in a single pane of glass, accelerating incident root-cause analysis for operations engineering teams.
### Metrics

#### High Availability Prometheus

  - **(2021)** [itnext.io: Monitoring Kubernetes workloads with Prometheus and Thanos](https://itnext.io/monitoring-kubernetes-workloads-with-prometheus-and-thanos-4ddb394b32c)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An in-depth article evaluating how to build a highly available, long-term metric monitoring system by integrating Prometheus with Thanos. It explores global query routing, object storage offloading strategies, and cross-cluster resource utilization metrics.
#### Kubernetes Scheduling

  - **(2021)** [openshift.com: Metrics-Driven Pod Constraints](https://www.redhat.com/en/blog/metrics-driven-pod-constraints)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural review detailing how OpenShift uses metrics-driven constraints to dynamically schedule workloads. By consuming Prometheus data points, the scheduler alters pod distribution thresholds based on actual node resource consumption.
### Scraping and Exporters

#### JVM Monitoring

  - **(2024)** [==Prometheus JMX Exporter 🌟==](https://github.com/prometheus/jmx_exporter) <span class='md-tag md-tag--info'>⭐ 3306</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e373ce5a" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 7 L 20 6 L 30 9 L 40 10 L 50 2" fill="none" stroke="url(#spark-grad-e373ce5a)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — A highly critical Prometheus collector that scrapes and formats JVM JMX mBeans. Widely utilized in enterprise legacy clusters running Java applications, Kafka, and Cassandra.
### Telemetry

#### eBPF Application Monitoring

  - **(2023)** [grafana.com: Grafana Beyla 1.0 release: zero-code instrumentation for application telemetry using eBPF](https://grafana.com/blog/grafana-beyla-1-0-release-zero-code-instrumentation-for-application-telemetry-using-ebpf) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Grafana Beyla 1.0, an eBPF-based auto-instrumentation tool designed to gather application telemetry (traces and RED metrics) without source code modification. Using eBPF, Beyla auto-detects web services and captures critical HTTP/S and gRPC latency data directly from the kernel space, making it highly valuable for heterogeneous, high-throughput microservice architectures.
### Visualization (1)

#### Grafana Configuration

  - **(2026)** [grafana.com: Provisioning Grafana 🌟](https://grafana.com/docs/grafana/latest/administration/provisioning) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official operational manual detailing Grafana's file-based provisioning system. By defining dashboards, notification integrations, and cluster data sources in declarative YAML, platform engineering teams can easily automate Grafana configuration via GitOps.
#### Grafana Extensibility

  - **(2020)** [scylladb.com: Building a Grafana Backend Plugin](https://www.scylladb.com/2020/10/01/building-a-grafana-backend-plugin)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A developer-oriented walkthrough showing how to construct custom backend data plugins for Grafana using Go. It focuses on implementing optimized query parsers, managing API secrets, and routing telemetry queries directly to non-native time-series databases.
#### Infrastructure as Code (2)

  - **(2026)** [==Grafana provisioning Ansible Role==](https://github.com/cloudalchemy/ansible-grafana) <span class='md-tag md-tag--info'>⭐ 503</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-55eda8f0" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 6 L 20 3 L 30 9 L 40 9 L 50 11" fill="none" stroke="url(#spark-grad-55eda8f0)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="11" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[ANSIBLE CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An automated Ansible role engineered by Cloud Alchemy to deploy, configure, and maintain Grafana services. It translates Grafana's file-based provisioning API parameters into clean Ansible playbooks, standardizing monitoring stack deployments across virtualized environments.
#### Product Updates

  - **(2021)** [thenewstack.io: Grafana 7.5: Controversial Pie Charts and Loki Alerts](https://thenewstack.io/grafana-7-5-controversial-pie-charts-and-loki-alerts)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the product enhancements shipped in Grafana 7.5, specifically focusing on native alert rule management inside Grafana Loki. It explains how these features simplified developer logging workflows and improved basic dashboard presentation elements.
#### Unified Alerting

  - **(2021)** [zdnet.com: Grafana 8.0 integrates with Prometheus alerting](https://www.zdnet.com/article/grafana-8-0-integrates-with-prometheus-alerting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the release of Grafana 8.0 and its significant consolidation of the platform's alerting architecture. The update introduces deep integration with Prometheus Alertmanager, allowing operators to construct complex multi-dimensional alert workflows directly.
  - **(2021)** [thenewstack.io: Grafana 8.0 Rethinks Alerts and Visualizations](https://thenewstack.io/grafana-8-0-rethinks-alerts-and-visualizations)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An technical review examining Grafana 8.0's visualization panel system and unified alerting engine. The article details how these visual rendering upgrades improved dashboard performance and standardized monitoring logic across multiple telemetry backends.
## Observability and Delivery

### Application Observability

#### Grafana Faro RUM

  - **(2022)** [grafana.com: Introducing Grafana Faro, an open source project for frontend application observability](https://grafana.com/blog/introducing-grafana-faro-oss-application-observability)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces Grafana Faro, an open-source JavaScript SDK designed to capture frontend Web-Vitals, console exceptions, and real-user-monitoring (RUM) metrics. Faro integrates client-side trace-contexts with backend services via OpenTelemetry, enabling end-to-end transaction transparency. A critical tool for aligning frontend application performance with deep backend container telemetries.
### Kubernetes Observability

#### Grafana Cloud

  - **(2021)** [grafana.com: A 3-step guide to troubleshooting and visualizing Kubernetes with Grafana Cloud](https://grafana.com/blog/a-3-step-guide-to-troubleshooting-and-visualizing-kubernetes-with-grafana-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Simplifies cluster-wide observability configurations down to three primary phases: installing the agent, collecting Prometheus metrics/Loki logs, and loading predefined cluster-health dashboards. Provides actionable advice to visually debug pod scheduling limits, node starvation, and OOM-Killed container cycles rapidly.
### Load Testing

#### k6 and OpenTelemetry

  - **(2022)** [grafana.com: Testing shift left observability with the Grafana Stack, OpenTelemetry, and k6](https://grafana.com/blog/testing-shift-left-observability-with-the-grafana-stack-opentelemetry-and-k6) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural validation of incorporating performance and observability telemetry early in the software lifecycle. Demonstrates using k6 for synthetic load generation while leveraging OpenTelemetry and the Grafana Stack to evaluate container bottlenecks during integration phases. This shift-left pattern prevents performance regressions before software hits live production environments.
### Metrics Querying

#### PromQL Basics

  - **(2021)** [grafana.com: Video: How to build a Prometheus query in Grafana](https://grafana.com/blog/video-how-to-build-a-prometheus-query-in-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Video breakdown demonstrating the assembly of PromQL (Prometheus Query Language) structures inside Grafana's query editor. Explores metric labels, functions like `rate()`, aggregation operations, and template variables. A foundational resource to help infrastructure engineers formulate robust alerting rules and visual dashboards.
### Network Monitoring

#### Advanced Prometheus

  - **(2021)** [grafana.com: An advanced guide to network monitoring with Grafana and Prometheus](https://grafana.com/blog/an-advanced-guide-to-network-monitoring-with-grafana-and-prometheus) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Builds on foundational network concepts to introduce complex PromQL configurations, high-density traffic visualizations, and multi-layered alert thresholds. Explores analyzing network interface errors, tracking packet drop trends, and integrating blackbox exporter synthetic probes to build a highly resilient multi-cluster tracking profile.
#### Prometheus snmp_exporter

  - **(2021)** [grafana.com: A beginner's guide to network monitoring with Grafana and Prometheus](https://grafana.com/blog/a-beginners-guide-to-network-monitoring-with-grafana-and-prometheus)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A foundational walkthrough on tracking physical and virtual networking infrastructure using Prometheus snmp_exporter. Focuses on gathering router/switch metrics, parsing bandwidth limits, and building clear Grafana interfaces to visualize network bottlenecks. An excellent baseline guide for administrators connecting traditional networks to cloud topologies.
### Platform Operations

#### Managed Observability

  - **(2021)** [grafana.com: Why companies choose Grafana Cloud over self-managed OSS stacks](https://grafana.com/blog/why-companies-choose-grafana-cloud-over-self-hosted-oss-stacks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the total cost of ownership (TCO) differences when operating self-hosted Prometheus/Loki/Tempo stacks versus utilizing Grafana Cloud. Evaluates scalability challenges, engineering maintenance resources, and the advantages of centralized enterprise licensing. Practical resource for decision makers evaluating managed telemetry platforms.
### Synthetic Monitoring

#### Grafana Alerting

  - **(2021)** [grafana.com: Top 5 user-requested synthetic monitoring alerts in Grafana Cloud](https://grafana.com/blog/top-5-user-requested-synthetic-monitoring-alerts-in-grafana-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Shares actionable configurations for the most prominent user-requested synthetic monitoring alerts in Grafana Cloud, including DNS failures, HTTP latency spikes, SSL certificate expirations, and global availability drops. Facilitates preemptive identification of microservice edge-network connectivity failures before user impact occurs.
### Visualization (2)

#### Dashboard Design

  - **(2021)** [grafana.com: Grafana dashboards: A complete guide to all the different types you can build](https://grafana.com/blog/grafana-dashboards-a-complete-guide-to-all-the-different-types-you-can-build)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Detailed directory detailing Grafana dashboard templates designed for infrastructure health, application profiling, alerting states, and executive summaries. Illustrates best practices for using colors, mapping dynamic parameters, and structuring queries to minimize browser rendering lag. Excellent primer for SRE and platform teams establishing visualization frameworks.
#### Grafana Cloud (1)

  - **(2021)** [grafana.com: What's new in Grafana Cloud for July 2021: Traces, live streaming, Kubernetes and Docker integrations, and more](https://grafana.com/blog/whats-new-in-grafana-cloud-for-july-2021-traces-live-streaming-kubernetes-and-docker-integrations-and-more)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines major feature enhancements in Grafana Cloud, highlighting integrations for distributed tracing with Tempo, real-time live streaming visualization, and streamlined onboarding for Kubernetes environments. This release accelerated the telemetry unification workflow, offering single-pane views across isolated environments.
#### Grafana Cloud Integration

  - **(2021)** [grafana.com: Introducing the AWS CloudWatch integration, Grafana Cloud's first fully managed integration](https://grafana.com/blog)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Focuses on Grafana Cloud's fully managed integration for AWS CloudWatch. Automates connection configurations, IAM policy templates, and out-of-the-box system dashboards to rapidly pull metrics from EC2, RDS, and ECS without setting up complex collectors. This SaaS integration reduces initial ingestion setups down to minutes.
#### Grafana Plugins

  - **(2021)** [grafana.com: Introducing the new and improved New Relic plugin for Grafana](https://grafana.com/blog/introducing-the-new-and-improved-new-relic-plugin-for-grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the upgraded New Relic integration for Grafana dashboards, permitting operations teams to query NRQL data blocks directly. It enables telemetry unification by blending APM, infrastructure metrics, and custom log searches within a single visual canvas. This integration mitigates team operational silos during incident triage cycles.
  - **(2021)** [Popular community plugins that can improve your Grafana dashboards 🌟](https://grafana.com/blog/popular-community-plugins-that-can-improve-your-grafana-dashboards)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights top community-created visualization plugins extending the native capabilities of Grafana dashboards, including specialized charting tools, flow diagrams, and advanced geographic mappings. Helps dashboard authors enrich analytics panels and improve observability interfaces across operations groups.
#### Grafana Releases

  - **(2021)** [grafana.com: Grafana 8.1 released: New Geomap and Annotations panels, updated plugin management, and more](https://grafana.com/oss/grafana)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical announcement detailing the new capabilities in Grafana 8.1, including the rewritten unified Geomap panel, automated annotations query integrations, and an upgraded interface for local plugin management. These features enhance geographical spatial data analysis and speed up event correlation during active incident mitigation.
## Observability and Monitoring

### Data Collection

#### Telemetry Agents

  - **(2024)** [==grafana/agent: Grafana Agent==](https://github.com/grafana/agent) <span class='md-tag md-tag--info'>⭐ 1709</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-dcd09096" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 8 L 20 5 L 30 2 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-dcd09096)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An agent for metrics, logs, and trace collection. Live grounding confirms Grafana Agent is now deprecated and succeeded by Grafana Alloy, the vendor's unified telemetry collector for OpenTelemetry and Prometheus.
### Grafana Ecosystem

#### AIOps and AI Observability

  - **(2023)** [devops.com: Grafana Labs Acquires Asserts.ai to Bring AI to Observability](https://devops.com/grafana-labs-acquires-assert-ai-to-bring-ai-to-observability) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the strategic acquisition of Asserts.ai by Grafana Labs. Live grounding highlights the integration of semantic graphs, relationship maps, and automated root-cause discovery directly into Grafana's UI stack.
#### Cloud and Enterprise Partnerships

  - **(2021)** [thenewstack.io: Grafana Is Not Worried About AWS Commercialization](https://thenewstack.io/grafana-is-not-worried-about-aws-commercialization)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes the strategic relationship between Grafana Labs and AWS regarding the Managed Grafana service. Live grounding verifies that despite initial fears of commercial erosion, AWS partnership validated Grafana's cloud-native dominance and expanded its enterprise reach, establishing a co-existence model.
  - **(2021)** [grafana.com: Grafana Labs and Microsoft partner to deliver new first party Microsoft Azure service](https://grafana.com/press/2021/11/10/grafana-labs-and-microsoft-partner-to-deliver-new-first-party-microsoft-azure-service)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official announcement of the partnership between Microsoft and Grafana Labs, launching Azure Managed Grafana. Details native Azure security, directory integrations, and SaaS SLA support.
#### Cloud Integrations

  - **(2022)** [devblogs.microsoft.com:Monitoring Azure by using Grafana dashboards 🌟](https://devblogs.microsoft.com/devops/monitoring-azure-by-using-grafana-dashboards)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Technical guide on visualizing Azure metrics using native Azure Monitor integrations and Azure Managed Grafana. Explores cross-tenant security and centralized dashboard architectures in public cloud environments.
#### Community Dashboards

  - **(2022)** [==github.com/onzack/grafana-dashboards==](https://github.com/onzack/grafana-dashboards) <span class='md-tag md-tag--info'>⭐ 145</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-833788aa" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 6 L 20 7 L 30 12 L 40 13 L 50 10" fill="none" stroke="url(#spark-grad-833788aa)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="10" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Collection of bespoke dashboards for infrastructure monitoring. Covers edge network routers, Ceph clusters, and hardware diagnostics via Prometheus exporters.
  - **(2021)** [==github.com/DevOps-Nirvana/Grafana-Dashboards==](https://github.com/DevOps-Nirvana/Grafana-Dashboards) <span class='md-tag md-tag--info'>⭐ 314</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b1d29198" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 8 L 20 6 L 30 6 L 40 4 L 50 2" fill="none" stroke="url(#spark-grad-b1d29198)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Community-maintained dashboard library specialized for common DevOps infrastructure. Includes optimization configurations for Nginx, PHP-FPM, MySQL, Redis, and Linux host monitoring.
  - **(2020)** [github.com/mlabouardy: Grafana Dashboards](https://github.com/mlabouardy/grafana-dashboards) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — Archived repository containing early Grafana dashboard iterations. Shows fundamental layout compositions for visualizing container workloads, though highly outdated compared to current standards.
#### Dashboard-as-Code

  - **(2021)** [prskavec.net: Grafana dashboards and Jsonnet](https://www.prskavec.net/post/grafana-jsonnet) <span class='md-tag md-tag--warning'>[JSONNET CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introduction to programmatic dashboard development utilizing Jsonnet. Explores Dashboard-as-Code (DaC) practices to manage, version, and scale large volumes of dashboard definitions in production.
#### Dashboards

  - **(2021)** [Grafana Dashboards](https://grafana.com/grafana/dashboards) <span class='md-tag md-tag--warning'>[JSON CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official ecosystem library hosting thousands of pre-configured dashboard JSON definitions. Enables fast deployment of visual layouts for standard tools like databases, networks, and virtualizers.
#### Database Monitoring

  - **(2023)** [==Percona Grafana dashboards for MySQL and MongoDB monitoring using Prometheus 🌟==](https://github.com/percona/grafana-dashboards) <span class='md-tag md-tag--info'>⭐ 2902</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-98bb75fb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 8 L 20 11 L 30 2 L 40 2 L 50 5" fill="none" stroke="url(#spark-grad-98bb75fb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Enterprise-grade dashboards by Percona designed for MySQL, PostgreSQL, and MongoDB monitoring. Delivers deep, low-level metrics on query throughput, memory pool utilization, and thread contention.
#### Incident Management

  - **(2022)** [infoq.com: Grafana Cloud Adds Incident and On-Call Management Solutions](https://www.infoq.com/news/2022/02/grafana-incident-oncall)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the integration of 'Grafana Incident' and 'Grafana OnCall' into the Grafana Cloud platform. Transitions Grafana from passive telemetry visualization to active, multi-channel incident response coordination.
#### Network Observability

  - **(2021)** [CISCO DNA Center with Grafana Dashboard](https://hawar.no/2021/05/cisco-dna-center-with-grafana-dashboard) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Operational guide detailing integration workflows between Cisco DNA Center APIs and Grafana. Translates enterprise network controller metrics into visual graphs for performance auditing.
#### Platform Evolution

  - **(2021)** [thenewstack.io: Grafana 8.2 Wants to ‘Democratize’ Cloud Native Metrics](https://thenewstack.io/grafana-wants-to-democratize-cloud-native-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Overview of Grafana 8.2’s features aiming to democratize access to metrics modeling. Focuses on integrated Prometheus alerting logic and simplification of visual dashboards for standard dev teams.
  - **(2020)** [Open source observability, meet data transformation: Grafana 7.0 promises to connect, unify, and visualize all your data](https://www.zdnet.com/article/open-source-observability-meet-data-transformation-grafana-7-0-promises-to-connect-unify-and-visualize-all-your-data)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Historical analysis of Grafana 7.0, detailing its paradigm shift to UI-driven data transformation pipelines. Underpins the core design framework that allows combining disjointed backend datasources.
#### Security and Access Control

  - **(2022)** [grafana.com: Grafana 9.3 feature: Grafana OAuth token improvements](https://grafana.com/oss/grafana/?mdm=social) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural breakdown of OAuth credentials handling enhancements in Grafana 9.3. Focuses on downstream token propagation, background credential refreshes, and access token security constraints.
#### UX Best Practices

  - **(2022)** [percona.com: Tips for Designing Grafana Dashboards](https://www.percona.com/blog/designing-grafana-dashboards)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents design methodologies for high-performance Grafana dashboards. Recommends reducing cognitive overhead, using proper query intervals, and structuring query transformations to optimize render times.
#### User Experience and Usability

  - **(2022)** [thenewstack.io: Will Grafana Become Easier to Use in 2022?](https://thenewstack.io/will-grafana-become-easier-to-use-in-2022)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines Grafana's platform roadmap toward simplifying visual dashboarding, query building, and exploration. Focuses on low-barrier UI paradigms to democratize data analytics without reducing technical expressiveness.
### Kubernetes Deployment

#### Core Infrastructure Dashboards

  - **(2024)** [==github.com/dotdc/grafana-dashboards-kubernetes 🌟==](https://github.com/dotdc/grafana-dashboards-kubernetes) <span class='md-tag md-tag--info'>⭐ 3599</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a471185e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 8 L 20 2 L 30 12 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-a471185e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Production-grade, community-approved Kubernetes dashboards. Delivers deep, clean observability of APIServer, node memory, CPU scheduling, storage, and pod ingress configurations.
#### Grafana Ecosystem (1)

  - **(2023)** [devopscube.com: How To Setup Grafana On Kubernetes](https://devopscube.com/setup-grafana-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Technical blueprint for deploying Grafana on a Kubernetes cluster. Details setup architectures using Helm charts, Persistent Volume Claims (PVCs) for persistence, and ConfigMaps to configure programmatic dashboards.
#### Virtualization Monitoring

  - **(2023)** [==github.com/kubevirt/monitoring==](https://github.com/kubevirt/monitoring) <span class='md-tag md-tag--info'>⭐ 28</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-e8edfa54" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 9 L 20 9 L 30 8 L 40 3 L 50 6" fill="none" stroke="url(#spark-grad-e8edfa54)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Defines monitoring instrumentation targets for KubeVirt resources. Provides Prometheus alerting rules and Grafana dashboard templates specifically optimized to monitor VM workloads running in Kubernetes.
### Log Management (1)

#### Kubernetes Logging

  - **(2022)** [itnext.io: Logging in Kubernetes with Loki and the PLG Stack](https://itnext.io/logging-in-kubernetes-with-loki-and-the-plg-stack-93b27c90ec34) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Detailed implementation guide for deploying the PLG (Prometheus, Loki, Grafana) stack on Kubernetes. Illustrates logging agent configurations that offer a lightweight alternative to EFK.
#### Log Aggregation

  - **(2024)** [==Grafana Loki==](https://grafana.com/oss/loki) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Grafana Loki is a highly available, multi-tenant log aggregation engine designed to index metadata labels instead of log contents. Minimizes overhead and simplifies Kubernetes-native log parsing.
### Metrics Storage

#### Scalable TSDB

  - **(2022)** [==github.com/grafana/mimir==](https://github.com/grafana/mimir) <span class='md-tag md-tag--info'>⭐ 5124</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3dca7ec9" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 8 L 20 10 L 30 2 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-3dca7ec9)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Grafana Mimir is a highly scalable, multi-tenant database for long-term Prometheus metrics storage. Engineered to easily process billions of active series with fast query performance and operational isolation.
### User Experience Monitoring

#### Frontend Observability

  - **(2023)** [==Grafana Faro 🌟==](https://grafana.com/oss/faro) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Introduction to Grafana Faro, an open-source web SDK designed for Frontend Application Observability. Collects real-time core web vitals, user logs, console errors, and session metrics.

---
💡 **Explore Related:** [Demos](./demos.md) | [Kubernetes](./kubernetes.md) | [Cloud Arch Diagrams](./cloud-arch-diagrams.md)

