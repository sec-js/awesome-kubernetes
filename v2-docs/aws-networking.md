# AWS Networking

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/aws-networking/).

!!! info "Architectural Context"
    Detailed reference for AWS Networking in the context of Cloud Providers (Hyperscalers).

## Table of Contents

1. [Cloud Infrastructure](#cloud-infrastructure)
  - [AWS](#aws)
    - [API Gateway](#api-gateway)
      - [Architecture](#architecture)
      - [Cross-Account Patterns](#cross-account-patterns)
    - [CDN](#cdn)
      - [CloudFront](#cloudfront)
      - [Edge Security](#edge-security)
    - [Kubernetes Networking](#kubernetes-networking)
      - [Controllers](#controllers)
    - [Load Balancing](#load-balancing)
      - [Announcements](#announcements)
      - [Application Load Balancer](#application-load-balancer)
      - [Configuration Updates](#configuration-updates)
      - [Serverless Integration](#serverless-integration)
    - [Reverse Proxy](#reverse-proxy)
      - [NGINX Plus](#nginx-plus)
    - [Security](#security)
      - [WAF](#waf)
1. [Software Engineering](#software-engineering)
  - [Deployment Patterns](#deployment-patterns)
    - [Blue-Green](#blue-green)
      - [ALB](#alb)

## Cloud Infrastructure

### AWS

#### API Gateway

##### Architecture

  - **(2020)** [alexdebrie.com: A Detailed Overview of AWS API Gateway](https://www.alexdebrie.com/posts/api-gateway-elements)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — An extensive architectural analysis of AWS API Gateway, deconstructing HTTP APIs, REST APIs, and WebSockets. Provides deep insights into routing, request validation, and authorization strategies that underpin serverless microservices architectures.
##### Cross-Account Patterns

  - **(2021)** [aws.amazon.com: Architecture patterns for consuming private APIs cross-account](https://aws.amazon.com/blogs/compute/architecture-patterns-for-consuming-private-apis-cross-account) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Examines security and network topology blueprints for consuming private APIs across different AWS accounts. Highlights the interaction of VPC endpoints, API Gateway resource policies, and Route 53 resolver rules to secure enterprise SaaS products.
#### CDN

##### CloudFront

  - **(2016)** [Amazon CloudFront now supports HTTP/2](https://aws.amazon.com/about-aws/whats-new/2016/09/amazon-cloudfront-now-supports-http2) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Announces native HTTP/2 support in CloudFront, highlighting performance gains from request multiplexing and header compression. A major historical milestone for fast content delivery networks, paving the way for modern responsive web applications.
##### Edge Security

  - **(2021)** [aws.amazon.com: Authorization@Edge using cookies: Protect your Amazon CloudFront content from being downloaded by unauthenticated users](https://aws.amazon.com/de/blogs/networking-and-content-delivery/authorizationedge-using-cookies-protect-your-amazon-cloudfront-content-from-being-downloaded-by-unauthenticated-users) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Presents edge security patterns leveraging Lambda@Edge or CloudFront Functions to validate cookies and JWTs. This approach prevents unauthorized downloads of static content directly at the CDN tier, dramatically reducing backend origin load.
#### Kubernetes Networking

##### Controllers

  - **(2020)** [Introducing the AWS Load Balancer Controller](https://aws.amazon.com/blogs/containers/introducing-aws-load-balancer-controller) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Introduces the Kubernetes-native controller that provisions ALBs and NLBs directly from EKS Ingress and Service objects. A de facto standard in EKS architectures, replacing generic reverse proxies with tightly integrated AWS-managed application delivery controllers.
#### Load Balancing

##### Announcements

  - **(2016)** [aws blogs - New – AWS Application Load Balancer](https://aws.amazon.com/blogs/aws/new-aws-application-load-balancer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The foundational blog post introducing AWS ALB in 2016, revolutionizing container and microservices ingress on AWS. Contrasts CLB's limitations with ALB's ability to host multiple target groups on a single instance port, enabling dense ECS/EKS hosting.
##### Application Load Balancer

  - **(2020)** [Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The authoritative landing page for AWS ALB, highlighting its Layer 7 request routing capabilities, HTTP/2 support, and WAF integrations. Modern microservices rely on ALB's path-based and host-based routing to expose APIs dynamically.
##### Configuration Updates

  - **(2024)** [aws.amazon.com/about-aws: Application Load Balancer enables configuring HTTP client keepalive duration](https://aws.amazon.com/about-aws/whats-new/2024/03/application-load-balancer-http-keepalive-duration) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the 2024 update enabling custom HTTP keep-alive duration configurations on ALB. Architects use this feature to align load balancer timeouts with backend server timeouts, effectively eliminating random 502 Bad Gateway errors in microservices.
##### Serverless Integration

  - **(2020)** [dashbird.io: AWS Elastic Load Balancing from a Serverless perspective](https://dashbird.io/blog/aws-application-load-balancer)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Analyzes Application Load Balancer configurations when integrated with serverless backends like AWS Lambda. Details pricing, cold-starts, and architectural trade-offs compared to API Gateway. Live systems often choose ALB for cost-effective, high-volume HTTP routing.
#### Reverse Proxy

##### NGINX Plus

  - **(2016)** [NGINX Plus on the AWS Cloud: Quick Start Reference Deployment](https://aws.amazon.com/about-aws/whats-new/2016/09/nginx-plus-on-the-aws-cloud-quick-start-reference-deployment) <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--critical'>[LEGACY]</span> — A legacy but highly informative deployment blueprint for configuring high-availability NGINX Plus instances on AWS. Explains load-balancing patterns, session persistence, and active health checks that bridge standard EC2 architectures with NGINX's enterprise proxy features.
#### Security

##### WAF

  - **(2024)** [AWS WAF enhances rate-based rules to support lower rate limits](https://aws.amazon.com/about-aws/whats-new/2024/08/aws-waf-rate-based-rules-lower-rate-limits) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Highlights the critical update reducing AWS WAF rate-based rule limits to protect low-traffic APIs and login endpoints from brute-force attacks. Provides developers with more granular rate-limiting controls to prevent application abuse at the edge.
## Software Engineering

### Deployment Patterns

#### Blue-Green

##### ALB

  - **(2021)** [Fine-tuning blue/green deployments on application load balancer](https://aws.amazon.com/blogs/devops/blue-green-deployments-with-application-load-balancer) <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Focuses on ALB's advanced routing capabilities to orchestrate safe blue/green deployments by shifting traffic percentages between target groups. A crucial operational pattern for continuous delivery pipelines, minimizing deployment blast radius.

---
💡 **Explore Related:** [Googlecloudplatform](./GoogleCloudPlatform.md) | [Edge Computing](./edge-computing.md) | [Oraclecloud](./oraclecloud.md)

🔗 **See Also:** [Postman](./postman.md) | [Cloudflare](./cloudflare.md)

