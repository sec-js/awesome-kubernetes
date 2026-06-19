# API Marketplaces. API Management with API Gateways and Developer Portals

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/developerportals/).

!!! info "Architectural Context"
    Detailed reference for API Marketplaces. API Management with API Gateways and Developer Portals in the context of Platform & Site Reliability.

## Architecture

### API Management

#### API Economy

  - **(2023)** [chakray.com: API Strategy. How to create an API Marketplace](https://chakray.com/api-strategy-how-to-create-an-api-marketplace)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Discusses the technical and business requirements for architecting an API Marketplace, which facilitates resource monetization, secure tenant isolation, and developer onboarding. Emphasizes the integration of central API gateways with developer portals to streamline access control.
#### API Governance

  - **(2023)** [chakray.com: Why API Lifecycle Management is a MUST for Your Organisation APIs](https://chakray.com/why-api-lifecycle-management-is-must-organisation-apis)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Argues the necessity of complete lifecycle governance—from design and prototyping to retirement—for managing systemic API environments. Details risk minimization and development streamlining benefits.
  - **(2023)** [chakray.com: 11 Steps to achieving a successful API Management Strategy](https://chakray.com/11-steps-achieving-successful-api-management-strategy)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Synthesizes an eleven-step action plan to define and execute a scalable API strategy, detailing critical factors such as architectural pattern choices, SLA setups, and metric tracing.
  - **(2023)** [chakray.com: Por qué API LIFECYCLE MANAGEMENT es imprescindible para la organización de APIs](https://chakray.com/es/por-que-api-lifecycle-management-imprescindible-api-organizacion) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spanish language deep dive exploring why complete lifecycle governance is crucial for modern enterprise IT systems, mapping stages from deployment to clean deprecation.
  - **(2023)** [chakray.com: 11 Pasos para lograr una estrategia API Management exitosa](https://chakray.com/es/11-pasos-lograr-estrategia-api-management-exitosa) <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Spanish version outlines the eleven key steps for drafting and deploying an enterprise API Management structure, securing internal services, and setting up clean billing paths.
#### Case Studies

  - **(2022)** [konghq.com: Kong and Red Hat: Delivering Seamless Customer Experience](https://konghq.com/blog/news/kong-and-red-hat-collaboration)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights corporate collaboration structures between Kong and Red Hat. Evaluates unified cloud-native operator setups to quickly provision API boundaries within complex enterprise networks.
#### Cloud Services

  - **(2026)** [Google Apigee API Manager](https://cloud.google.com/apigee) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google Cloud's premier enterprise API management platform designed to build, secure, and monitor APIs globally. Provides integrated developer portals, advanced machine learning-driven threat detection, and seamless serverless hosting layers.
#### Gateway Engines

  - **(2026)** [Kong API Manager](https://konghq.com/products/kong-gateway) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kong Gateway is the world's most popular lightweight, fast, and highly customizable open-source API gateway. Powered by Nginx and Lua/Go, it offers sub-millisecond request latencies alongside dynamic routing and robust plugin ecosystems.
  - **(2026)** [Tyk API Manager](https://tyk.io) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A powerful, lightweight, open-source API Gateway and Management Platform written entirely in Go. Possesses stellar clustering configurations, multi-data-center capabilities, and dynamic rate limiting without external dependencies.
#### Infrastructure Patterns

  - **(2022)** [API Marketplace vs API Gateway (What’s the Difference?)](https://rapidapi.com/blog/api-marketplace-vs-api-gateway-whats-the-difference)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Clarifies the architectural differences between an API Gateway (acting as a reverse proxy for traffic control, authentication, and routing) and an API Marketplace (providing a discovery platform, billing infrastructure, and developer portal). Helps architects choose correct patterns for internal vs. external exposure.
  - **(2022)** [moesif.com: How to choose the right API Gateway for your platform: Comparison of Kong, Tyk, Apigee, and alternatives](https://www.moesif.com/blog/technical/api-gateways/How-to-Choose-The-Right-API-Gateway-For-Your-Platform-Comparison-Of-Kong-Tyk-Apigee-And-Alternatives) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Compares core enterprise-grade API Gateways, including Kong, Tyk, Apigee, and cloud-native solutions. Delves into benchmarks, execution models (e.g., Lua-based vs. Go-based plugins), licensing, and performance overheads under high-throughput microservice configurations.
  - **(2021)** [developers.redhat.com: Simplify load balancing for API gateways using Red Hat 3scale API Management](https://developers.redhat.com/articles/2021/08/11/simplify-load-balancing-api-gateways-using-red-hat-3scale-api-management) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Evaluates traffic management policies and network topologies designed to optimize high-performance load balancing in front of 3scale API gateways. Focuses on minimizing round-trip times and preventing traffic hotspots.
#### Kubernetes Orchestration

  - **(2022)** [openshift.com: Modern Application Development With Kong Konnect Enterprise and Red Hat OpenShift](https://www.redhat.com/en/blog/modern-application-development-with-kong-konnect-enterprise-and-red-hat-openshift) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores structural benefits of running Kong Konnect's control-and-data-plane models inside Red Hat OpenShift clusters. Streamlines decentralized routing while maintaining strong tenant access restrictions.
  - **(2020)** [OpenShift Ecosystem: API Management on Red Hat OpenShift with 3scale](https://www.redhat.com/en/blog/openshift-ecosystem-api-management-on-red-hat-openshift-with-3scale) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights deep deployment patterns of running Red Hat 3scale inside OpenShift clusters. Analyzes operator-based management, auto-scaling characteristics, and native Kubernetes Custom Resource Definitions (CRDs) used to define API policies declaratively.
#### Observability Platforms

  - **(2021)** [API Management vs API Gateway and where does API Analytics and Monitoring fit?](https://dev.to/moesif/api-management-vs-api-gateway-and-where-does-api-analytics-and-monitoring-fit-4g75)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores the delineation between routing runtime proxies (Gateways) and higher-level API lifecycle portals (Management), while explaining how analytics software fits in. Investigates the collection of telemetry metrics to track user behavior and API health without injecting latency.
#### Operations and Deployment

  - **(2020)** [developers.redhat.com: New custom metrics and air gapped (restricted networks) installation in Red Hat 3scale API Management 2.9](https://developers.redhat.com/blog/2020/10/29/new-custom-metrics-and-air-gapped-installation-in-red-hat-3scale-api-management-2-9) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explores deep administrative patterns introduced in 3scale 2.9, highlighting secure installation procedures on air-gapped systems and restricted enterprise networks. Evaluates custom telemetry collection pipelines for specialized monitoring.
  - **(2019)** [Install Red Hat 3scale and configure tenants with 7 simple commands](https://developers.redhat.com/blog/2019/09/09/install-3scale-multitenant-in-7-commands)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A practical administrative guide demonstrating rapid scripting mechanisms to install and configure multi-tenant structures in 3scale. Promotes standardized deployment setups on container platforms with minimum operational footprint.
#### Persistent Connections

  - **(2021)** [developers.redhat.com: How to expose a WebSocket endpoint using Red Hat 3scale API Management](https://developers.redhat.com/articles/2021/07/01/how-expose-websocket-endpoint-using-red-hat-3scale-api-management) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A highly technical guide demonstrating gateway configurations needed to establish persistent WebSocket connections through the 3scale API gateway. Discusses protocol upgrading, timeout values, and scaling metrics.
#### Red Hat Ecosystem

  - **(2026)** [Red Hat 3scale API Management](https://www.redhat.com/en/technologies/jboss-middleware/3scale) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Identical platform reference focusing on Red Hat 3scale API Gateway configurations. Delivers a cloud-native, operator-driven API management framework optimized for scaling microservices on OpenShift clusters with declarative security controls.
  - **(2018)** [Adding API Gateway Policies Now Easier With Red Hat 3scale API Management](https://developers.redhat.com/blog/2018/05/30/3scale-api-gateway-policies)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Outlines the declarative system for defining gateway routing rules and header manipulation schemas inside 3scale API Management without updating custom Lua scripts. Details deployment configurations for standard enterprise security controls.
#### Security and Protocols

  - **(2021)** [developers.redhat.com: Enhance application security by rotating 3scale access tokens](https://developers.redhat.com/blog/2021/04/29/enhance-application-security-by-rotating-3scale-access-tokens)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Explains robust administrative paradigms for managing secrets through programmatic, seamless rotation of 3scale access tokens. Mitigates exposure risk and integrates directly into CI/CD secrets management flows.
#### Video Walkthroughs

  - **(2026)** [Apigee @Youtube](https://www.youtube.com/user/apigee)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official video reference library for Google Cloud's Apigee, covering security policies, proxy design, billing implementation, and hybrid runtime cluster orchestration.
  - **(2026)** [WSO2 @Youtube](https://www.youtube.com/user/WSO2TechFlicks)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official visual channel for WSO2. Highlights integration capabilities, open-source API gateway patterns, and customer identity access management (CIAM) setups on Kubernetes-centric topologies.
  - **(2026)** [Kong API Platform @Youtube](https://www.youtube.com/channel/UCJfQURxlI_pQdeJUGXtA_zw)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Visual resources from KongHQ covering distributed gateway topologies, Konnect control planes, service mesh patterns, and complex custom plugin developments.
  - **(2026)** [Tyk @Youtube](https://www.youtube.com/channel/UCe3VG8wgz03u73xiomGeQzQ)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official visual guides highlighting Go plugin development, portal styling, API deprecation workflows, and analytics pipeline setups on Tyk's cloud-native infrastructure.
### Design Patterns

#### Microservices Patterns

  - **(2022)** [cloudtechtwitter.com: Pattern: API Gateway / Backends for Frontends](https://www.cloudtechtwitter.com/2022/05/pattern-api-gateway-backends-for.html) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An architectural review of the Backend-for-Frontend (BFF) and API Gateway patterns. It details how tailoring dedicated backend gateways to specific user interfaces (web, mobile, IoT) minimizes payload size, decouples frontend release cycles, and limits over-fetching.
### Microservices

#### API Gateways

  - **(2021)** [Layering domains and microservices using API Gateways](https://kislayverma.com/software-architecture/layering-domains-and-microservices-using-api-gateways) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes architectural design patterns for structuring enterprise APIs by layering domain services behind a unified API Gateway layer. Discusses decoupling strategies, cross-cutting concerns (auth, rate-limiting), and how to avoid anti-patterns when decomposing monoliths into distributed microservice topologies.
## Domain APIs

### IoT

#### Smart Cities

  - **(2026)** [Telefonica Thinking Cities](https://thinking-cities.readthedocs.io/en/latest) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive documentation portal explaining Telefónica's IoT architecture and FIWARE-based 'Thinking Cities' platform. It provides guidelines for streaming, mapping, and aggregating sensors telemetry to build urban monitoring environments.
## Infrastructure

### API Gateway

#### Cloud Native

  - **(2026)** [==apisix==](https://github.com/apache/apisix) <span class='md-tag md-tag--info'>⭐ 16724</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-182e8c75" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 13 L 10 13 L 20 9 L 30 10 L 40 5 L 50 5" fill="none" stroke="url(#spark-grad-182e8c75)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[LUA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Apache APISIX is a high-performance, dynamic cloud-native API gateway built on Nginx and OpenResty. It provides dynamic routing, active health checking, security protection, and telemetry integration, utilizing etcd for state storage to achieve ultra-low latency configurations.
#### Go Engines

  - **(2026)** [==KrakenD: The fastest API gateway comes with true linear scalability 🌟==](https://www.krakend.io) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — KrakenD is an enterprise-ready, open-source API Gateway engineered for linear scalability and ultra-high performance. By utilizing a stateless execution model, it avoids the overhead of internal database lookups, delivering sub-millisecond routing, data transformation, and endpoint aggregation.
  - **(2026)** [**Lura 🌟**](https://luraproject.org) <span class='md-tag md-tag--warning'>[GO CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Lura (formerly KrakenD framework) is an ultra-performant, stateless API Gateway engine written in Go. It allows developers to construct high-throughput microservice aggregations, protocol translations, and response manipulations using declarative configurations with zero state.
#### Industry News

  - **(2021)** [thenewstack.io - APISIX: An Open Source API Gateway for Microservices](https://thenewstack.io/apisix-an-open-source-api-gateway-for-microservices) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An editorial piece analyzing the microservices-centric architectural benefits of Apache APISIX. The article highlights its pluggable architecture, dynamic configuration sync via etcd, and its comparative advantages in speed and extensibility against traditional Java or Go gateways.
#### Java Spring Ecosystem

  - **(2026)** [==Spring Cloud Gateway==](https://spring.io/projects/spring-cloud-gateway) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Spring Cloud Gateway provides an API routing mechanism built on Spring WebFlux and Project Reactor. Ideal for Java and Spring Boot microservice architectures, it facilitates non-blocking, reactive traffic routing, security filtering, and resilience patterns like circuit breaking.
#### Open Source Governance

  - **(2021)** [krakend.io: KrakenD framework becomes a Linux Foundation project](https://www.krakend.io/blog/krakend-framework-joins-the-linux-foundation) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Official announcement outlining the donation of the KrakenD framework (now Lura) to the Linux Foundation. This strategic move ensures vendor-neutral governance and fosters open-source community collaboration for next-generation, high-performance API gateways.
## Platform Engineering

### Developer Portal

#### Internal Developer Platforms

  - **(2026)** [==Backstage Developer Portal:==](https://backstage.io) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Created by Spotify and donated to the CNCF, Backstage is an open-source framework for building internal developer portals. It unifies infrastructure tooling, services, and documentation under a single, centralized Software Catalog to streamline development workflows and reduce cognitive load.
  - **(2026)** [Backstage @Youtube](https://www.youtube.com/channel/UCHBvqSwbfAf5Vx1jrwkG43Q) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official CNCF Backstage YouTube channel, featuring community meetups, architecture reviews, plugin development tutorials, and adoption case studies. It serves as an essential visual learning reference for Platform Engineering teams designing internal developer platforms (IDPs).
#### Kubernetes Deployment

  - **(2024)** [piotrminkowski.com: Backstage on Kubernetes](https://piotrminkowski.com/2024/06/28/backstage-on-kubernetes) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — This guide details the production deployment steps for running Backstage on Kubernetes. It covers containerization, Helm chart configuration, database state persistence, and securing identity management integration for scalable developer portal deployments.
#### Tutorials

  - **(2024)** [piotrminkowski.com: Getting Started with Backstage](https://piotrminkowski.com/2024/06/13/getting-started-with-backstage) 🌟🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive technical guide to bootstrapping Backstage, configuring the software catalog, and writing custom templates. The resource outlines practical steps to integrate local tooling with the developer portal, enabling swift adoption of self-service developer templates.

---
💡 **Explore Related:** [DevOps](./devops.md) | [Test Automation Frameworks](./test-automation-frameworks.md) | [SRE](./sre.md)

🔗 **See Also:** [About](./about.md) | [Postman](./postman.md)

