# OCP 3

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ocp3/).

!!! info "Architectural Context"
    Detailed reference for OCP 3 in the context of The Container Stack.

## Table of Contents

1. [Observability](#observability)
  - [Application Monitoring](#application-monitoring)
    - [Java JMX](#java-jmx)
1. [Platform Architecture](#platform-architecture)
  - [High Availability](#high-availability)
    - [Disaster Recovery](#disaster-recovery)
1. [Security](#security)
  - [Encryption](#encryption)
    - [.NET Core](#net-core)

## Observability

### Application Monitoring

#### Java JMX

  - **(2017)** [developers.redhat.com: Troubleshooting java applications on openshift (Jolokia)](https://developers.redhat.com/blog/2017/08/16/troubleshooting-java-applications-on-openshift) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Guides developers on using Jolokia, an HTTP/JSON bridge for JMX, to securely query and troubleshoot Java microservices deployed inside Red Hat OpenShift pods.
## Platform Architecture

### High Availability

#### Disaster Recovery

  - **(2019)** [blog.openshift.com/: Stateful Workloads and the Two Data Center Conundrum](https://www.redhat.com/en/blog/stateful-workloads-and-the-two-data-center-conundrum) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Analyzes the persistence challenges associated with stateful microservices running across multi-site cluster architectures. Evaluates split-brain hazards and suggests synchronous storage configurations to guarantee data integrity.
## Security

### Encryption

#### .NET Core

  - **(2018)** [developers.redhat.com: Securing .NET Core on OpenShift using HTTPS](https://developers.redhat.com/blog/2018/10/12/securing-net-core-on-openshift-using-https) <span class='md-tag md-tag--warning'>[C# CONTENT]</span>  <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Guides engineers through configuring ASP.NET Core microservices with end-to-end TLS encryption on OpenShift. Discusses dynamic integration of local server certificates using OpenShift's service serving certificates feature.

---
💡 **Explore Related:** [OCP 4](./ocp4.md) | [Serverless](./serverless.md) | [Kubectl Commands](./kubectl-commands.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

