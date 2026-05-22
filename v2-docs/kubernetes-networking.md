# Kubernetes Networking

!!! info "Architectural Context"
    Detailed reference for Kubernetes Networking in the context of Networking & Service Mesh.

## Cloud Infrastructure

### Kubernetes

#### Networking

  - **(2026)** [==cilium.io==](https://cilium.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An eBPF-powered open-source project that provides high-performance, secure, and observable networking, load balancing, and network security for Kubernetes workloads. Cilium is widely adopted by enterprise platforms due to its scale capabilities and granular L3-L7 policy controls.
## Cloud Native Infrastructure

### Networking (1)

#### Egress Traffic Control

##### Case Studies

  - **(2020)** [**Controlling outbound traffic from Kubernetes**](https://monzo.com/blog/controlling-outbound-traffic-from-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[CASE STUDY]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> — A highly regarded engineering case study by Monzo bank detailing how they designed and operated egress gateways to control and audit outbound traffic. Explains compliance benefits, custom proxy layers, and high-availability engineering patterns.
## Cloud Native Security

### Network Security

#### Network Policies

  - **(2020)** [blog.nody.cc: Verify your Kubernetes Cluster Network Policies: From Faith to Proof](https://blog.nody.cc/posts/2020-06-kubernetes-network-policy-verification) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines a methodology to empirically test and verify active Kubernetes Network Policies. Details the usage of programmatic probes to transition network security evaluation from abstract policy syntax configurations to verifiable network boundaries.

---
💡 **Explore Related:** [Servicemesh](./servicemesh.md) | [Istio](./istio.md) | [Networking](./networking.md)

