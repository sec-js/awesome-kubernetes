# Kubectl Commands

!!! info "Architectural Context"
    Detailed reference for Kubectl Commands in the context of The Container Stack.

## Continuous Integration

### CI Tools

#### Jenkins

  - [**Jenkins Kubernetes Plugin**](https://plugins.jenkins.io/kubernetes) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The critical Kubernetes integration for Jenkins, executing dynamic agents directly inside cluster pods. Solves pipeline scale issues by tearing down runner instances upon build completion.

</div></details>
  - [Kubernetes Continuous Deploy](https://plugins.jenkins.io/kubernetes-cd) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A traditional Jenkins plugin for deploying build outputs to Kubernetes. Note: Has fallen out of favor in modern GitOps-centric continuous delivery pipelines.

</div></details>

***
💡 **Explore Related:** [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md) | [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md)

