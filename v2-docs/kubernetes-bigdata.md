# Big Data and Kubernetes Big Data

!!! info "Architectural Context"
    Detailed reference for Big Data and Kubernetes Big Data in the context of The Container Stack.

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [tomlous.medium.com: CI/CD for Data Engineers. Reliably Deploying Scala Spark' containers for Kubernetes with Github Actions](https://tomlous.medium.com/ci-cd-for-data-engineers-68b0fd915545)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering tomlous.medium.com: CI/CD for Data Engineers. Reliably Deploying Scala Spark' containers for Kubernetes with Github Actions in the Kubernetes Tools ecosystem.
  - [dzone: Run and Scale an Apache Spark Application on Kubernetes](https://dzone.com/articles/run-and-scale-an-apache-spark-application-on-kuber)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Run and Scale an Apache Spark Application on Kubernetes in the Kubernetes Tools ecosystem.
  - [dzone: Running Apache Spark on Kubernetes](https://dzone.com/articles/running-apache-spark-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Running Apache Spark on Kubernetes in the Kubernetes Tools ecosystem.
  - [medium: Running Apache Spark on Kubernetes](https://medium.com/empathyco/running-apache-spark-on-kubernetes-2e64c73d0bb2)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering medium: Running Apache Spark on Kubernetes in the Kubernetes Tools ecosystem.
  - [levelup.gitconnected.com: Master SparkML: Practical Guide for Machine Learning](https://levelup.gitconnected.com/master-sparkml-practical-guide-for-machine-learning-1efe1bd9cdce)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering levelup.gitconnected.com: Master SparkML: Practical Guide for Machine Learning in the Kubernetes Tools ecosystem.
## Data and AI

### Apache Spark

#### Cloud Migration

  - **(2021)** [**itnext.io: Migrating Apache Spark workloads from AWS EMR to Kubernetes**](https://itnext.io/migrating-apache-spark-workloads-from-aws-emr-to-kubernetes-463742b49fda) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly granular migration case study describing the engineering process of moving Apache Spark analytical jobs from AWS EMR to Amazon EKS. Addresses key architectural trade-offs such as node grouping, instance types, spot instance lifecycle management, and driver/executor scheduling. Live Grounding underscores that moving Spark workloads to Kubernetes optimizes compute utilization and reduces vendor lock-in.
#### Cost Optimization

  - **(2023)** [spot.io: Setting up, Managing & Monitoring Spark on Kubernetes](https://www.flexera.com/products/flexera-one/container-optimization) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the financial and operational mechanics of running Spark executor pods on heterogeneous Kubernetes clusters. Emphasizes automated cost optimization, spot instance utilization, and intelligent scaling practices. Live Grounding shows that dynamically shifting Spark executor tasks to spot instances under strict fallback rules is essential for scaling modern, cost-sensitive big data pipelines.
#### OpenShift

  - **(2022)** [cloud.redhat.com: Getting Started running Spark workloads on OpenShift](https://www.redhat.com/en/blog/getting-started-running-spark-workloads-on-openshift) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Provides an enterprise guide to running containerized Apache Spark workloads within Red Hat OpenShift, highlighting security-first practices and security context constraints (SCCs). Illustrates leveraging OpenShift's cluster monitoring and dynamic storage classes for big data analytics. Live Grounding confirms OpenShift remains a preferred, secure platform for regulated enterprises executing large-scale analytical tasks.
#### Performance and Tuning

  - **(2022)** [==coderstan.com: Apache Spark on Kubernetes—Lessons Learned from Launching Millions of Spark Executors (Databricks Data+AI Summit 2022)==](https://coderstan.com/2022/07/15/spark-on-kubernetes-launching-millions-of-spark-executors) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Shares high-scale operational insights and hard-earned engineering lessons from managing millions of Spark executors on Kubernetes clusters. Details scheduling bottlenecks, DNS limits, local SSD configurations, and executor startup latency optimizations. Live Grounding highlights these exact tuning principles as standard operating procedures for operating hyperscale, cost-efficient data platforms today.
#### Streaming and Scheduling

  - **(2023)** [**docs.databricks.com: Use scheduler pools for multiple streaming workloads**](https://docs.databricks.com/aws/en/structured-streaming/production) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — Deep dives into configuring Spark scheduler pools to enforce Fair Scheduling (FAIR) when running multiple concurrent Structured Streaming queries in a shared production workspace. Prevents heavy resource queries from starving lightweight streaming jobs. Live Grounding verifies that proper allocation of pool weights remains a mandatory configuration practice for robust multi-tenant streaming pipelines.
### Cloud Platforms

#### Databricks

  - **(2022)** [aprenderbigdata.com: Databricks: Introducción a Spark en la nube](https://aprenderbigdata.com/databricks) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Offers a clear Spanish-language introduction to Databricks, highlighting its managed Apache Spark ecosystem across AWS and Azure. Demystifies collaborative notebooks, workspace management, and optimized runtimes. Live Grounding shows that Databricks continues to expand its lakehouse dominance, abstracting underlying infrastructure away from data engineers while offering native cloud integrations.
### Data Pipelines

#### Apache Spark (1)

  - **(2022)** [hevodata.com: Building Apache Spark Data Pipeline? Made Easy 101 🌟](https://hevodata.com/learn/spark-data-pipeline) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An introductory primer outlining the core concepts of building end-to-end data processing pipelines with Apache Spark. Focuses on data ingestion, transformations, and loading into modern target data warehouses. Live Grounding confirms that while Spark remains a foundational ETL standard, contemporary architectures increasingly wrap these pipelines inside orchestrated dbt-on-Kubernetes or SparkOperator setups.
### Databricks (1)

#### Governance

  - **(2024)** [**github.com/databrickslabs/ucx: Databricks Labs UCX**](https://github.com/databrickslabs/ucx) <span class='md-tag md-tag--info'>⭐ 308</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — The Databricks Labs UCX project provides a specialized framework designed to upgrade legacy Databricks workspaces to Unity Catalog governance standards. Simplifies catalog and privilege migrations automatically. Live Grounding confirms UCX is standard for enterprise organizations establishing secure, centralized data governance, metadata isolation, and unified access controls.
### Market Analysis

#### Adoption Trends

  - **(2021)** [opensourceforu.com: Kubernetes Adoption Widespread for Big Data: Survey](https://www.opensourceforu.com/2021/12/kubernetes-adoption-widespread-for-big-data-survey/?amp) <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details industry survey results illustrating the widespread migration of Big Data and stateful analytics workloads onto Kubernetes. Shows the transition from static, dedicated bare-metal clusters to dynamic, container-orchestrated platforms. Live Grounding confirms this historical trajectory has culminated in 2026, where cloud-native orchestration is the unquestioned standard for running Spark, Flink, and ML training pipelines.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Openshift](./openshift.md) | [Serverless](./serverless.md)

