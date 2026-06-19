# NoSQL Databases and NewSQL

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/nosql/).

!!! info "Architectural Context"
    Detailed reference for NoSQL Databases and NewSQL in the context of Data & Advanced Analytics.

## Data Architecture

### MongoDB Ecosystem

#### Kubernetes Networking

  - **(2022)** [**thenewstack.io: Deploy MongoDB in a Container, Access It Outside the Cluster**](https://thenewstack.io/deploy-mongodb-in-a-container-access-it-outside-the-cluster) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Addresses networking patterns required to expose in-cluster containerized MongoDB services to external application clients safely, discussing NodePorts, external LoadBalancers, and routing constraints.
#### Kubernetes Operators

  - **(2026)** [==MongoDB and Kubernetes 🌟==](https://www.mongodb.com/products/integrations/kubernetes) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official Kubernetes operator blueprint detailing integration procedures. Allows declarative scaling, self-healing, rolling updates, and TLS rotation of stateful MongoDB replica sets under container orchestrators.
  - **(2023)** [**adamtheautomator.com: How To Perform a MongoDB Kubernetes Installation 🌟**](https://adamtheautomator.com/mongodb-kubernetes) <span class='md-tag md-tag--warning'>[YAML CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Step-by-step tutorial for deploying MongoDB to Kubernetes clusters. Addresses StatefulSet configuration, persistent volume claim (PVC) templates, and replica-set discovery mechanisms.
### NoSQL Databases

#### Wide-Column Stores

  - **(2026)** [==Cassandra.apache.org==](https://cassandra.apache.org) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Highly scalable, distributed wide-column NoSQL database offering linear scalability and multi-datacenter active-active clustering. Managed via modern tooling like K8ssandra on top of cloud Kubernetes platforms.
## Observability

### Microservices Monitoring

#### Tracing Tools

  - **(2021)** [github.com/oslabs-beta: Odin's Eye](https://github.com/oslabs-beta/OdinsEye) <span class='md-tag md-tag--warning'>[JAVASCRIPT CONTENT]</span> 🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Open-source developer utility designed to monitor distributed microservices architecture patterns, tracking internal query metrics and communication flows. Primarily active within the community sandbox.

---
💡 **Explore Related:** [Yaml](./yaml.md) | [Databases](./databases.md) | [Crunchydata](./crunchydata.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

