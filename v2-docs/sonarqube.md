# Sonarqube

!!! info "Architectural Context"
    Detailed reference for Sonarqube in the context of Engineering Pipeline.

## DevSecOps

### Continuous Inspection

#### Static Code Analysis

##### Execution

  - **(2021)** [thenewstack.io: How to Analyze Code and Find Vulnerabilities with SonarQube](https://thenewstack.io/how-to-analyze-code-and-find-vulnerabilities-with-sonarqube) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Hands-on guide to running static analyzers against real codebases using SonarQube scanners, configuring quality gates, and reviewing vulnerability alerts.

</div></details>
##### Installation

  - **(2021)** [thenewstack.io: How to Install the SonarQube Security Analysis Platform](https://thenewstack.io/how-to-install-the-sonarqube-security-analysis-platform) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Step-by-step deployment guide detailing how to host SonarQube locally or on dedicated infrastructure, including database dependencies and JVM configurations.

</div></details>
##### SonarQube

  - **(2026)** [==Sonarqube.org==](https://www.sonarsource.com/products/sonarqube) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The leading platform for continuous inspection of code quality, executing automatic reviews with static analysis of code to detect bugs, security vulnerabilities, and code smells across 30+ programming languages.

</div></details>
##### SonarQube Scanner

  - **(2026)** [**SonarQube Scanner Overview**](https://docs.sonarsource.com/sonarqube-server/analyzing-source-code/overview) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Core index for the official SonarQube scanner integrations, providing detailed configurations for popular build tools and continuous integration platforms like Gradle, MSBuild, Maven, Jenkins, and Azure DevOps.

</div></details>
### Continuous Integration

#### Jenkins Pipelines

##### Dockerized Scans

  - **(2020)** [**itnext.io: SonarQube: running tests from Jenkins Pipeline in Docker**](https://itnext.io/sonarqube-running-tests-from-jenkins-pipeline-from-docker-7740702b6f42) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Deep technical guide showing how to architect a Jenkins pipeline that runs unit tests and executes SonarQube code coverage scans natively inside transient Docker containers.

</div></details>
### Kubernetes Native

#### Google Cloud Platform

##### Blueprints

  - **(2023)** [click-to-deploy/sonarqube](https://github.com/GoogleCloudPlatform/click-to-deploy/tree/master/k8s/sonarqube) <span class='md-tag md-tag--info'>⭐ 771</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

A Google Cloud Platform blueprint repository designed to ease the deployment of SonarQube on Google Kubernetes Engine (GKE) via highly standardized manifest suites.

</div></details>
#### Helm Deployments

##### SonarQube (1)

  - **(2024)** [hub.helm.sh/charts/oteemo/sonarqube](https://artifacthub.io/packages/helm/oteemo/sonarqube) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Helm chart repository listing for deploying SonarQube on Kubernetes, complete with configurations for persistence, ingress routing, and integrated database deployments.

</div></details>
#### Local Environments

##### Video Tutorials

  - **(2021)** [youtube: Installation of Sonarqube on Kubernetes/Minikube](https://www.youtube.com/watch?v=_cT-kkvw3NQ) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Video guide demonstrating how to spin up a SonarQube server inside Minikube, configured for localized developer playground environments.

</div></details>

***
💡 **Explore Related:** [Registries](./registries.md) | [Jenkins Alternatives](./jenkins-alternatives.md) | [Argo](./argo.md)

