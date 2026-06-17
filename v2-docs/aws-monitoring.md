# AWS Monitoring and Logging

!!! info "Architectural Context"
    Detailed reference for AWS Monitoring and Logging in the context of Cloud Providers (Hyperscalers).

## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [logz.io: What are AWS EC2 Instances? A Tutorial for EC2 Metrics Shipping' with Logz.io](https://logz.io/blog/aws-ec2-metrics)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering logz.io: What are AWS EC2 Instances? A Tutorial for EC2 Metrics Shipping' with Logz.io in the Kubernetes Tools ecosystem.
  - [logz.io: A Guide to Monitoring AWS Lambda Metrics with Prometheus & Logz.io](https://logz.io/blog/aws-lambda-metrics-monitoring-guide)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering logz.io: A Guide to Monitoring AWS Lambda Metrics with Prometheus & Logz.io in the Kubernetes Tools ecosystem.
  - [dzone: Optimize AWS Costs With CloudWatch's Advanced Metrics, Dashboards,' and Alerts](https://dzone.com/articles/optimize-aws-costs-with-cloudwatchs-advanced-metri)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering dzone: Optimize AWS Costs With CloudWatch's Advanced Metrics, Dashboards,' and Alerts in the Kubernetes Tools ecosystem.
## Cloud Native Platforms

### AWS

#### Managed Observability

  - **(2026)** [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — AWS fully-managed metric service designed around open-source Cortex core architecture. Automatically scales telemetry storage, ingestion, and query resources in secure enterprise environments.
## Observability and Monitoring

### Case Studies

#### Enterprise Scale

  - **(2021)** [How BT uses Amazon CloudWatch to monitor millions of devices](https://aws.amazon.com/blogs/mt/how-bt-uses-amazon-cloudwatch-to-monitor-millions-of-devices) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span>  <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Deep-dives into an enterprise architecture deployed by BT utilizing Amazon CloudWatch to ingest, structure, and analyze telemetry streams originating from millions of physical client network units globally.
### CloudWatch

#### Alerting Systems

  - **(2021)** [Extending and exploring alarm history in Amazon CloudWatch – part 2](https://aws.amazon.com/blogs/mt/extending-and-exploring-alarm-history-in-amazon-cloudwatch-part-2) <span class='md-tag md-tag--warning'>[SQL CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Investigates strategies to maintain and analyze deep historical records of CloudWatch alarm states over multi-year thresholds using Kinesis Firehose, S3 object storage targets, and Athena SQL queries.
#### Dashboards

  - **(2020)** [Amazon CloudWatch Dashboards now supports sharing](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-dashboards-supports-sharing) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces external sharing support for AWS CloudWatch Dashboards, permitting secure read-only console visualizations to key stakeholders outside the immediate AWS organization footprint.
#### Guides Collection

  - **(2021)** [threatstack.com: 50 Best AWS CloudWatch Tutorials](https://www.f5.com/company/blog) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive directory linking to performance tuning guides, log group configurations, and real-time dashboard design patterns inside Amazon CloudWatch. Evaluates fundamental metric generation techniques.
#### Prometheus Integration

  - **(2020)** [Amazon CloudWatch now monitors Prometheus metrics from Container environments](https://aws.amazon.com/about-aws/whats-new/2020/09/amazon-cloudwatch-monitors-prometheus-metrics-container-environments) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Documents Amazon CloudWatch Container Insights' ability to ingest, index, and visualize standard Prometheus application metrics directly from Elastic Kubernetes Service (EKS) cluster deployments.
### Enterprise Observability

#### Elastic Stack

  - **(2022)** [elastic.co: Elastic and AWS: Accelerating the cloud migration journey](https://www.elastic.co/blog/elastic-and-aws-accelerate-your-cloud-migration-journey) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores integrations between Elastic Cloud and AWS native logging solutions. Facilitates high-velocity log ingest, distributed tracing across container environments, and simplified security event monitoring across cloud instances.
### Legacy Systems

#### Self-Hosted

  - **(2018)** [==github: Steps I used to install Nagios in the cloud==](https://github.com/andrewpuch/nagios_setup) <span class='md-tag md-tag--warning'>[SHELL CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--info'>[LEGACY]</span> — A historical walkthrough illustrating legacy installations of the Nagios monitoring framework inside static virtual instances. Outlines core process definitions, alerting rules, and manual configuration management.
### Managed Services

#### Announcements

  - **(2021)** [infoq.com: AWS Introduces Amazon Managed Service for Grafana and Amazon Managed Service for Prometheus](https://www.infoq.com/news/2021/01/aws-grafana-prometheus) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Architectural breakdown of AWS's entry into cloud-native managed open-source telemetry tools. Reviews integration advantages, storage strategies, and price efficiencies compared to self-hosted instances on EC2.
#### Grafana

  - **(2024)** [Amazon Managed Service for Grafana](https://aws.amazon.com/grafana) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Managed visualization console offering direct enterprise integrations with SSO and IAM setups. Allows telemetry aggregation from diverse cloud datasources (S3, Prometheus, CloudWatch, Opensearch) under unified dynamic views.
## Security and Governance

### Cloud Governance

#### Compliance and Audit

  - **(2022)** [How to use AWS Config and CloudTrail to find who made changes to a resource](https://aws.amazon.com/blogs/mt/how-to-use-aws-config-and-cloudtrail-to-find-who-made-changes-to-a-resource) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Demonstrates how to correlate events from AWS Config history with CloudTrail api audit logs. Provides an audit mechanism to pinpoint precise user identities, timestamps, and parameters related to unauthorized resource alterations.
### Cloud Security Posture

#### Automated Auditing

  - **(2024)** [==github: ElectricEye==](https://github.com/jonrau1/ElectricEye/blob/master/README.md) <span class='md-tag md-tag--info'>⭐ 1043</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An automated cloud security assessment framework designed to continually monitor AWS environments for configuration drift, vulnerabilities, and deviations from industry standards. Outputs findings directly to AWS Security Hub.
## Service Discovery

### AWS Cloud Map

#### Health Checks

  - **(2022)** [Custom Health Check: HealthCheckCustomConfig](https://docs.aws.amazon.com/cloud-map/latest/api/API_HealthCheckCustomConfig.html) <span class='md-tag md-tag--warning'>[N/A CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official reference guide for Cloud Map API's custom health checks. Explains dynamic service discovery patterns for serverless workloads where traditional load balancer health checks are inapplicable.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [AWS Backup](./aws-backup.md) | [AWS Containers](./aws-containers.md)

