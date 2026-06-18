# OAuth2

!!! info "Architectural Context"
    Detailed reference for OAuth2 in the context of Hardened Infrastructure.

## Table of Contents

1. [Security](#security)
  - [IAM](#iam)
    - [Protocols](#protocols)
  - [Identity and Access](#identity-and-access)
    - [OAuth2](#oauth2-1)
    - [Spring Security](#spring-security)

## Security

### IAM

#### Protocols

  - **(2022)** [curity.io: OAuth 2.0 Overview](https://curity.io/resources/learn/oauth-overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An industrial-grade review of the OAuth 2.0 protocol specifications, flows, and grant types. Provides system architects with core design criteria to safely establish authorization states between microservice deployments. Underlines secure handling of access, refresh, and id tokens.
  - **(2022)** [curity.io: OpenID Connect Overview](https://curity.io/resources/learn/openid-connect-overview)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Provides a comprehensive architecture overview of OpenID Connect (OIDC) acting as the authentication layer on top of OAuth 2.0. Analyzes ID token syntax, discovery endpoints, and flows for multi-tenant systems. Essential background knowledge for implementing cloud-native federated identities.
### Identity and Access

#### OAuth2 (1)

  - **(2022)** [rapidapi.com:What is OAuth2.0?](https://rapidapi.com/guides/oath2-0)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A comprehensive foundational guide breaking down the OAuth 2.0 authorization framework. It delineates core concepts including authentication flows, grant types, token lifecycles, and security delegation mechanics.
#### Spring Security

  - **(2022)** [freecodecamp.org: How to Implement an OAuth2 Resource Server with Spring Security](https://www.freecodecamp.org/news/oauth2-resourceserver-with-spring-security) <span class='md-tag md-tag--warning'>[JAVA CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A hands-on implementation tutorial detailing the deployment of an OAuth2-compliant resource server using Spring Security. It guides through configuring middleware to parse and authenticate incoming JWT requests.

---
💡 **Explore Related:** [IaC](./iac.md) | [Terraform](./terraform.md) | [Ansible](./ansible.md)

