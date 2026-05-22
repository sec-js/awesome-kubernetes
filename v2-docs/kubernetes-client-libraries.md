# Kubernetes Client Libraries

!!! info "Architectural Context"
    Detailed reference for Kubernetes Client Libraries in the context of The Container Stack.

## Cloud-Native

### Kubernetes Native

#### Java Build Plugins

##### Eclipse JKube

  - **(2020)** [developers.redhat.com: Cloud-native Java applications made easy: Eclipse JKube 1.0.0 now available](https://developers.redhat.com/blog/2020/09/09/cloud-native-java-applications-made-easy-eclipse-jkube-1-0-0-now-available) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Launch announcement of Eclipse JKube 1.0.0 detailing its design philosophy, architectural decoupling from old Fabric8 dependencies, and its seamless integration with modern cloud-native standards.

</div></details>
  - **(2020)** [developers.redhat.com: Java development on top of Kubernetes using Eclipse JKube](https://developers.redhat.com/blog/2020/08/24/java-development-on-top-of-kubernetes-using-eclipse-jkube) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Exploring developer loop workflows utilizing Eclipse JKube to build, deploy, and debug Java applications in real-time inside a local or remote Kubernetes cluster environment.

</div></details>
#### Migration Guides

##### Eclipse JKube (1)

  - **(2026)** [**eclipse.org: Migration Guide for projects using Fabric8 Maven Plugin to Eclipse JKube 🌟**](https://eclipse.dev/jkube/docs/migration-guide) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Official technical reference outlining the exact property conversions, API transformations, and plugin changes needed to move builds from `fabric8-maven-plugin` to `jkube-maven-plugin`.

</div></details>
  - **(2020)** [developers.redhat.com: Migrating from Fabric8 Maven Plugin to Eclipse JKube 1.0.0](https://developers.redhat.com/blog/2020/09/21/migrating-from-fabric8-maven-plugin-to-eclipse-jkube-1-0-0) 🌟🌟🌟 <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Step-by-step technical guide highlighting the namespace transitions, configuration changes, and structural refactoring required when migrating legacy Fabric8 Maven build files to the modernized Eclipse JKube.

</div></details>
#### Quarkus Integration

##### Video Tutorials

  - **(2021)** [youtube: Deploying a Quarkus application into Kubernetes using JKube | Cloud Tool Time | Marc Nuri 🌟](https://www.youtube.com/watch?v=HDDfdZqwM1E&ab_channel=EclipseFoundation) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Video session detailing the integration of Quarkus with Eclipse JKube to deploy highly optimized, native-compiled Java microservices directly to Kubernetes.

</div></details>
## Red Hat OpenShift

### Developer Experience

#### Java Integrations

  - **(2020)** [developers.redhat.com: Getting started with the fabric8 Kubernetes Java client](https://developers.redhat.com/blog/2020/05/20/getting-started-with-the-fabric8-kubernetes-java-client) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Technical introduction to utilizing the Fabric8 Kubernetes Java Client SDK. Details how to perform CRUD operations on Kubernetes APIs, deploy custom controllers, and stream container logs inside Java runtimes.

</div></details>
  - **(2019)** [Fabric8](https://fabric8.io) <span class='md-tag md-tag--warning'>[EN CONTENT]</span>  <span class='md-tag md-tag--info'>[LEGACY]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

Historically significant platform offering tools, microservices, and management mechanisms for Java environments on Kubernetes and OpenShift. Now deprecated, but set foundations for contemporary Java developer abstractions.

</div></details>
#### Maven Plugins

  - **(2025)** [Eclipse JKube 🌟](https://eclipse.dev/jkube) <span class='md-tag md-tag--warning'>[EN CONTENT]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <details class='v2-inline-summary'><summary class='md-tag md-tag--info'>Deep-Dive</summary><div class='v2-summary-wrapper' markdown='1'>

The central documentation portal for Eclipse JKube, an open-source suite of tooling designed to facilitate the rapid containerization, deployment, and management of Java applications across Kubernetes and Red Hat OpenShift infrastructures.

</div></details>

***
💡 **Explore Related:** [Kubernetes Troubleshooting](./kubernetes-troubleshooting.md) | [Ocp4](./ocp4.md) | [Kubernetes Based Devel](./kubernetes-based-devel.md)

