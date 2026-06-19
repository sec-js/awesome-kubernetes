# Prometheus

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/prometheus/).

!!! info "Architectural Context"
    Detailed reference for Prometheus in the context of Architectural Foundations.

## Table of Contents

1. [Cloud Native Infrastructure](#cloud-native-infrastructure)
  - [Observability](#observability)
    - [Prometheus](#prometheus-1)
      - [AWS Integration](#aws-integration)
      - [Client Libraries](#client-libraries)
      - [Pushgateway](#pushgateway)
      - [Query Tools](#query-tools)
1. [Cloud Native Platforms](#cloud-native-platforms)
  - [Azure](#azure)
    - [Azure Monitor Integration](#azure-monitor-integration)
  - [Kubernetes](#kubernetes)
    - [Multi-Arch Telemetry](#multi-arch-telemetry)
1. [Observability](#observability-1)
  - [Distributed Storage](#distributed-storage)
    - [Cortex Engine](#cortex-engine)
    - [InfluxDB](#influxdb)
    - [M3 Engine](#m3-engine)
    - [Thanos Engine](#thanos-engine)
  - [Monitoring](#monitoring)
    - [Prometheus Meta-Monitoring](#prometheus-meta-monitoring)
  - [OpenTelemetry](#opentelemetry)
    - [Collector Infrastructure](#collector-infrastructure)
  - [Prometheus](#prometheus-2)
    - [Core Platform](#core-platform)

## Cloud Native Infrastructure

### Observability

#### Prometheus (1)

##### AWS Integration

  - **(2020)** [itnext.io - Prometheus: yet-another-cloudwatch-exporter — collecting AWS CloudWatch metrics](https://itnext.io/prometheus-yet-another-cloudwatch-exporter-collecting-aws-cloudwatch-metrics-806bd34818a8) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This article introduces 'YACE' (Yet Another CloudWatch Exporter), a high-performance Go-based exporter designed to retrieve AWS CloudWatch metrics. By utilizing AWS API calls optimally, YACE reduces AWS API transactional costs compared to the official Java-based CloudWatch exporter.
##### Client Libraries

  - **(2020)** [gabrieltanner.org: Golang Application monitoring using Prometheus](https://gabrieltanner.org/blog/collecting-prometheus-metrics-in-golang) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A practical walk-through detailing how to instrument a Go application with custom Prometheus metrics using the official client library. Demonstrates defining, registering, and incrementing Counters and Gauges, and exposes them over an HTTP handler endpoint.
##### Pushgateway

  - **(2026)** [==Pushgateway==](https://github.com/prometheus/pushgateway) <span class='md-tag md-tag--info'>⭐ 3334</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-af13d2fb" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 4 L 20 9 L 30 9 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-af13d2fb)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official GitHub repository for Prometheus Pushgateway. Designed to allow ephemeral, short-lived, or batch jobs to push metrics to an intermediate gateway, which Prometheus then scrapes. Note that official guidelines advise against using Pushgateway for standard applications due to structural state issues.
##### Query Tools

  - **(2021)** [promlens.com 🌟](https://promlens.com) <span class='md-tag md-tag--warning'>[GO CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — PromLens is an advanced query builder and analyzer for PromQL. Created to help developers write, visualize, and debug complex PromQL expressions, it provides syntactic parsing, inline documentation, and tree-based diagnostic tools. Now integrated as an official Prometheus community project.
## Cloud Native Platforms

### Azure

#### Azure Monitor Integration

  - **(2025)** [Promitor 🌟](https://promitor.io) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An Azure Monitor collector that translates native Microsoft cloud diagnostics into a standard Prometheus-compatible API format, linking closed-source telemetry with open tools.
### Kubernetes

#### Multi-Arch Telemetry

  - **(2025)** [==Cluster Monitoring stack for ARM / X86-64 platforms==](https://github.com/carlosedp/cluster-monitoring) <span class='md-tag md-tag--info'>⭐ 754</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-c7b3de5e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 6 L 10 2 L 20 11 L 30 2 L 40 12 L 50 6" fill="none" stroke="url(#spark-grad-c7b3de5e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="6" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSONNET CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A specialized telemetry suite crafted for physical, edge, and multi-architecture Kubernetes clusters running on ARM or x86 systems. Extends modern operators to resource-constrained environments.
## Observability (1)

### Distributed Storage

#### Cortex Engine

  - **(2024)** [==github.com/cortexproject/cortex==](https://github.com/cortexproject/cortex) <span class='md-tag md-tag--info'>⭐ 5811</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-9287ae06" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 8 L 20 8 L 30 9 L 40 2 L 50 4" fill="none" stroke="url(#spark-grad-9287ae06)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Open-source repository for Cortex. Implements Prometheus as a service, allowing isolated multi-tenancy, long-term metric durability in object storage (S3/GCS), and horizontally scalable querying.
  - **(2024)** [**Cortex**:](https://cortexmetrics.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural landing page of Cortex, an enterprise-grade, horizontally scalable, multi-tenant TSDB. Note: Since 2024-2025, many users have migrated toward Thanos or VictoriaMetrics, yet Cortex remains a highly resilient classic for long-term storage.
#### InfluxDB

  - **(2021)** [influxdata.com: Building a Metrics & Alerts as a Service (MaaS) Monitoring Solution Using the InfluxDB Stack](https://www.influxdata.com/blog/building-a-metrics-alerts-as-a-service-maas-monitoring-solution-using-the-influxdb-stack) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores an architecture for metrics and alerting as a service (MaaS) built on the InfluxDB stack. Highlights utilizing multi-tenancy, dynamic bucket allocations, and custom push metric pipelines.
#### M3 Engine

  - **(2023)** [**M3**:](https://m3db.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural homepage of M3, Uber’s highly scalable, distributed TSDB engine. Highly custom-built to support massive data ingestion volumes and dynamic metric downsampling with optimized storage layouts.
#### Thanos Engine

  - **(2024)** [**Thanos**:](https://thanos.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official landing page for Thanos, a CNCF graduated project providing highly available, infinitely scalable Prometheus monitoring. Known for sidecar-based object storage offloading and cost-effective downsampling.
  - **(2022)** [Highly Available Prometheus Metrics for Distributed SQL with Thanos on GKE](https://blog.yugabyte.com/highly-available-prometheus-metrics-for-distributed-sql-with-thanos-on-gke) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates deploying Thanos alongside Prometheus Operator on Google Kubernetes Engine (GKE) to collect metrics for YugabyteDB. Highlights the implementation of Multi-Cluster and Multi-Tenant metric architectures using Thanos Receiver and Store gateways.
  - **(2021)** [github.com/ruanbekker: Thanos Cluster Setup](https://github.com/ruanbekker/thanos-cluster-setup) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Developer guide outlining the architectural deployment of a highly available Thanos cluster with Docker Compose. Demonstrates configuring Thanos Sidecar, Querier, Store Gateway, and S3 object storage targets.
### Monitoring

#### Prometheus Meta-Monitoring

  - **(2023)** [grafana.com: How we use metamonitoring Prometheus servers to monitor all other Prometheus servers at Grafana Labs](https://grafana.com/blog/how-we-use-metamonitoring-prometheus-servers-to-monitor-all-other-prometheus-servers-at-grafana-labs) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A high-performance monitoring case study from Grafana Labs. Illustrates the architectural pattern of metamonitoring, utilizing dedicated Prometheus servers to watch, query, and alert on larger global telemetry networks.
### OpenTelemetry

#### Collector Infrastructure

  - **(2026)** [==OpenTelemetry Collector==](https://github.com/open-telemetry/opentelemetry-collector) <span class='md-tag md-tag--info'>⭐ 7132</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-02095d03" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 10 L 10 9 L 20 2 L 30 3 L 40 6 L 50 5" fill="none" stroke="url(#spark-grad-02095d03)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A high-performance processing engine capable of receiving, parsing, filtering, and routing traces, metrics, and logs across vendor-agnostic infrastructure. Serves as the central data pipeline component in modern cloud-native observability stacks.
### Prometheus (2)

#### Core Platform

  - **(2026)** [==github.com/prometheus/prometheus==](https://github.com/prometheus/prometheus) <span class='md-tag md-tag--info'>⭐ 64493</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-95404ed3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 4 L 10 13 L 20 5 L 30 9 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-95404ed3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Source codebase for Prometheus, the benchmark cloud-native telemetry engine. Employs active scraping mechanics over HTTP alongside a custom-built local TSDB to deliver sub-second querying speeds and powerful alerting capabilities.

---
💡 **Explore Related:** [About](./about.md) | [Demos](./demos.md) | [Kubernetes](./kubernetes.md)

🔗 **See Also:** [Postman](./postman.md) | [Cloudflare](./cloudflare.md)

