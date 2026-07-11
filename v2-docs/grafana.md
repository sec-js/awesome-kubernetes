---
description: "Curated, AI-ranked Grafana resources for the 2026 Cloud Native architect: top-tier tools, guides and references (Architectural Foundations)."
---
# Grafana

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/grafana/).

!!! info "Architectural Context"
    Detailed reference for Grafana in the context of Architectural Foundations.

## Observability

### Log Management

#### Deployment Guides

  - **(2021)** [youtube.com: Grafana Loki Promtail | Grafana Loki Setup And Configuration On CentOs](https://www.youtube.com/watch?v=iqpLXUdJ0Ro&ab_channel=Thetips4you)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A video deployment guide demonstrating how to install and configure Grafana Loki and Promtail on CentOS systems. It covers host-level systemd service configuration, log routing patterns, and connecting local log collectors to centralized Loki nodes.
#### Grafana Loki

  - **(2020)** [Log Monitoring and Alerting with Grafana Loki](https://www.infracloud.io/blogs/grafana-loki-log-monitoring-alerting)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A detailed deployment guide focusing on log monitoring and alerting integration using Grafana Loki and Promtail. Loki's design indexing only log metadata allows clusters to achieve cost-efficient, low-latency log collection compared to full-text indexing solutions.
## Observability and Delivery

### Kubernetes Observability

#### Grafana Cloud

  - **(2021)** [grafana.com: A 3-step guide to troubleshooting and visualizing Kubernetes with Grafana Cloud](https://grafana.com/blog/a-3-step-guide-to-troubleshooting-and-visualizing-kubernetes-with-grafana-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Simplifies cluster-wide observability configurations down to three primary phases: installing the agent, collecting Prometheus metrics/Loki logs, and loading predefined cluster-health dashboards. Provides actionable advice to visually debug pod scheduling limits, node starvation, and OOM-Killed container cycles rapidly.
### Synthetic Monitoring

#### Grafana Alerting

  - **(2021)** [grafana.com: Top 5 user-requested synthetic monitoring alerts in Grafana Cloud](https://grafana.com/blog/top-5-user-requested-synthetic-monitoring-alerts-in-grafana-cloud)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Shares actionable configurations for the most prominent user-requested synthetic monitoring alerts in Grafana Cloud, including DNS failures, HTTP latency spikes, SSL certificate expirations, and global availability drops. Facilitates preemptive identification of microservice edge-network connectivity failures before user impact occurs.
## Observability and Monitoring

### Data Collection

#### Telemetry Agents

  - **(2024)** [==grafana/agent: Grafana Agent==](https://github.com/grafana/agent) <span class='md-tag md-tag--info'>⭐ 1709</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-dcd09096" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 8 L 20 5 L 30 2 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-dcd09096)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An agent for metrics, logs, and trace collection. Live grounding confirms Grafana Agent is now deprecated and succeeded by Grafana Alloy, the vendor's unified telemetry collector for OpenTelemetry and Prometheus.
### Kubernetes Deployment

#### Core Infrastructure Dashboards

  - **(2024)** [==github.com/dotdc/grafana-dashboards-kubernetes 🌟==](https://github.com/dotdc/grafana-dashboards-kubernetes) <span class='md-tag md-tag--info'>⭐ 3599</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-a471185e" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 8 L 20 2 L 30 12 L 40 7 L 50 5" fill="none" stroke="url(#spark-grad-a471185e)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[JSON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Production-grade, community-approved Kubernetes dashboards. Delivers deep, clean observability of APIServer, node memory, CPU scheduling, storage, and pod ingress configurations.
#### Grafana Ecosystem

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

---
💡 **Explore Related:** [Git](./git.md) | [Other Awesome Lists](./other-awesome-lists.md) | [AWS Tools Scripts](./aws-tools-scripts.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

