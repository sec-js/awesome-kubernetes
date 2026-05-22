# Prometheus

!!! info "Architectural Context"
    Detailed reference for Prometheus in the context of Architectural Foundations.

## Observability

### Metrics

#### Prometheus (1)

  - **(2022)** [**Setup Prometheus Using Helm Chart on Kubernetes**](https://devopscube.com/setup-prometheus-helm-chart) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A direct, production-ready tutorial demonstrating how to install and configure Prometheus using official Helm charts. Explains default values overrides, persistent volume configurations, and custom alertmanager integration for instant operational visibility.

</div></details>
### Monitoring Stack

#### Helm Charts

##### kube-prometheus-stack

  - **(2026)** [==prometheus-community/kube-prometheus-stack 🌟🌟==](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The de facto standard Helm chart for deploying Prometheus and Grafana on Kubernetes. It manages the custom resource definitions (CRDs), handles scraper configurations, and provides out-of-the-box system alerting rules.

</div></details>

***
💡 **Explore Related:** [Mkdocs](./mkdocs.md) | [Cheatsheets](./cheatsheets.md) | [Linux](./linux.md)

