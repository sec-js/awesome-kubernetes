# Server Vendors Providing Java EE/Jakarta EE and MicroProfile Runtimes

!!! info "Architectural Context"
    Detailed reference for Server Vendors Providing Java EE/Jakarta EE and MicroProfile Runtimes in the context of Developer Ecosystem.

## Standard Reference

  - [About WebSphere Liberty](https://developer.ibm.com/wasdev/websphere-liberty)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [wikipedia: Jakarta EE](https://en.wikipedia.org/wiki/Jakarta_EE)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Wikipedia: Payara Server](https://en.wikipedia.org/wiki/Payara_Server)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Getting Started With Java EE 8, Payara 5 and Eclipse Oxygen](https://dzone.com/articles/getting-started-with-java-ee-8-payara-5-and-eclips)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Red Hat JBoss Enterprise Application Platform (JBoss EAP)](https://developers.redhat.com/products/eap/overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [Dzone: Jakarta EE & Wildfly Running on Kubernetes](https://dzone.com/articles/jakarta-ee-amp-wildfly-running-on-kubernetes)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## Cloud-Native Java

### Runtimes

#### Payara Micro

##### Docker

  - **(2026)** [**Payara Micro**](https://hub.docker.com/r/payara/micro) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The official Docker image for Payara Micro, a lightweight, cloud-optimized container runtime designed specifically for MicroProfile applications. Live Grounding shows Payara Micro is extensively used in dynamic, auto-scaling Kubernetes microservice pods due to its rapid startup and low configuration overhead.
#### Payara Server

##### Docker (1)

  - **(2026)** [Payara](https://hub.docker.com/r/payara/server-full) 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> — The official Docker Hub repository for Payara Server Full, providing ready-made container images for complete Jakarta EE runtime capabilities. Live Grounding shows its primary use in legacy system migration, allowing enterprise operations to orchestrate monolithic workloads with modern container tooling.
#### WildFly

##### Developer Workflow

  - **(2021)** [opensource.com: Get started with WildFly for Java web development](https://opensource.com/article/21/7/wildfly) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An introductory guide on using WildFly for web application development, demonstrating fast setup and deploy loops. Live Grounding indicates its practical value for developers looking to run traditional web-profiles on modular container frameworks without heavy J2EE runtime friction.
  - **(2026)** [**WildFly**](https://www.wildfly.org) 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — The project homepage for WildFly, Red Hat's open-source application server executing modern Jakarta EE specifications. Live Grounding highlights WildFly as a high-performance, modular system featuring fast startup and low memory usage, heavily favored for container deployments.
## Enterprise Java

### Runtimes (1)

#### Apache TomEE

  - **(2026)** [TomEE from Tomitribe](http://tomee.apache.org) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Apache TomEE is a lightweight, certified Jakarta EE and MicroProfile implementation built on Apache Tomcat. It merges Tomcat's speed and small footprint with full Java Enterprise capabilities, including CDI, JTA, and JPA, making it ideal for microservice deployments requiring standardized API layers.
#### KumuluzEE

  - **(2026)** [KumuluzEE](https://ee.kumuluz.com) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An award-winning, lightweight microservice framework that enables standard Java EE APIs to run as independent, containerized applications. It focuses on modular, plug-and-play architecture, bypassing heavy runtime components to achieve fast startup times and minimal cloud resource utilization.
#### Payara Server (1)

  - **(2026)** [Payara](https://payara.fish) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Payara Server and Payara Micro provide high-performance, container-friendly environments for running Jakarta EE and MicroProfile workloads. Designed for critical production architectures, it supports built-in clustering, hazelcast-powered data grids, and auto-tuning capabilities inside Kubernetes deployments.

---
💡 **Explore Related:** [Chromedevtools](./ChromeDevTools.md) | [Angular](./angular.md) | [API](./api.md)

