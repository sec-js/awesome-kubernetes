# 🎥 DevOps, IaC, and SRE

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/).

Welcome to the **DevOps, IaC, and SRE** section of the V2 Video Hub. Explore curated high-density videos with architectural summaries.

## Table of Contents

1. [Prometheus](#prometheus)
2. [Terraform Enterprise](#terraform-enterprise)
3. [HashiCorp Stack Terraform Vault Consul Boundary](#hashicorp-stack-terraform-vault-consul-boundary)
4. [Azure DevOps and GitHub Actions](#azure-devops-and-github-actions)
5. [DevSecOps](#devsecops)
6. [FinOps](#finops)
7. [GitOps](#gitops)
8. [Jenkins](#jenkins)
9. [NetBox](#netbox)

## Prometheus

??? note "🎬 Prometheus: The Documentary"
    !!! info "Architectural Summary"
        This documentary explores the architectural genesis of Prometheus at SoundCloud, detailing how the shift to microservices necessitated a fundamental pivot from host-based monitoring to a pull-based, multi-dimensional metric data model. In a 2026 cloud-native context, understanding these foundational design decisions—specifically the trade-offs of localized TSDB storage, HTTP pull mechanics, and PromQL—is vital for architecting self-healing, high-cardinality observability pipelines across distributed, edge, and hybrid-cloud environments.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="rT4fJNbfe14" data-video-url="https://www.youtube.com/embed/rT4fJNbfe14" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/rT4fJNbfe14/hqdefault.jpg" alt="Prometheus: The Documentary" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Terraform Enterprise

??? note "🎬 Standardizing infrastructure automation with Terraform Enterprise"
    !!! info "Architectural Summary"
        This presentation details AXA Group's cloud migration strategy (ATLAS) utilizing Terraform Enterprise as the cornerstone of their multi-cloud and private IaaS migration factory. It highlights how a highly regulated financial enterprise standardizes infrastructure-as-code (IaC) practices across multiple global subsidiaries to accelerate cloud adoption while maintaining governance. For a 2026 cloud-native landscape, this case study provides key insights into scaling self-service provisioning, implementing policy-as-code, and automating multi-tenant enterprise architectures at massive scale.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="PxyyY7TsCqs" data-video-url="https://www.youtube.com/embed/PxyyY7TsCqs?si=kzCRojDteESqork1" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/PxyyY7TsCqs/hqdefault.jpg" alt="Standardizing infrastructure automation with Terraform Enterprise" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## HashiCorp Stack Terraform Vault Consul Boundary

??? note "🎬 Building a developer platform? Ask these questions."
    !!! info "Architectural Summary"
        This session details how to build secure, scalable developer platforms by defining 'golden paths' using HashiCorp's suite of automation tools, including Terraform, Vault, Consul, and Boundary. It provides a strategic framework for resolving key platform engineering challenges such as Day 2 operations, infrastructure dependency mapping, secure access control, and seamless local-to-remote environment transitions. By abstracting cloud complexity, the session demonstrates how to deliver high-velocity self-service capabilities to development teams while ensuring governance and security compliance.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="1Fl25dR01pw" data-video-url="https://www.youtube.com/embed/1Fl25dR01pw?si=bJlQozIfT3J4rhN3" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/1Fl25dR01pw/hqdefault.jpg" alt="Building a developer platform? Ask these questions." class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## Azure DevOps and GitHub Actions

??? note "🎬 Panel: Azure DevOps vs. GitHub Actions"
    !!! info "Architectural Summary"
        This panel discussion provides a comprehensive architectural comparison between Azure DevOps and GitHub Actions, focusing on enterprise governance, extensibility, and CI/CD workflow migration strategies. It outlines decision frameworks for hybrid platform setups, highlighting how organizations can leverage GitHub Actions for modern cloud-native developer velocity while maintaining Azure DevOps for mature project management, test plans, and strict regulatory compliance. Essential for cloud architects planning long-term toolchain evolution, this session clarifies integration pathways and future-proof migration strategies.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="8g4qLzkpjeE" data-video-url="https://www.youtube.com/embed/8g4qLzkpjeE?si=xcfl3ugsMGZ8Kthg" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/8g4qLzkpjeE/hqdefault.jpg" alt="Panel: Azure DevOps vs. GitHub Actions" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## DevSecOps

??? note "🎬 What is DevSecOps? DevSecOps explained in 8 Mins"
    !!! info "Architectural Summary"
        This video details the transition from traditional, late-stage security audits to DevSecOps, explaining how shifting security left eliminates deployment bottlenecks in fast-paced delivery pipelines. It covers the automation of static analysis (SAST), software composition analysis (SCA), and container scanning directly within CI/CD workflows. In a 2026 cloud-native context, this paradigm is critical for securing ephemeral microservices and maintaining continuous compliance without sacrificing deployment velocity.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="nrhxNNH5lt0" data-video-url="https://www.youtube.com/embed/nrhxNNH5lt0?si=U5h1mbkbF6ZEOvlj" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/nrhxNNH5lt0/hqdefault.jpg" alt="What is DevSecOps? DevSecOps explained in 8 Mins" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## FinOps

??? note "🎬 The Brutal Truth Behind Tech Layoffs"
    !!! info "Architectural Summary"
        This analysis dissects the macroeconomic shift from hyper-growth talent hoarding to hyper-efficiency, highlighting the systemic collapse of bloated engineering teams in favor of lean, automated operations. For a 2026 cloud-native landscape, this underscores the critical role of platform engineering and robust FinOps architectures designed to maximize resource utilization while minimizing human-in-the-loop operational overhead. Architects must leverage these insights to build self-healing, highly automated platforms that successfully decouple organizational scale from headcount.

    <center markdown="1">

    <div class="video-lazy-container" data-video-id="hAwtrJlBVJY" data-video-url="https://www.youtube.com/embed/hAwtrJlBVJY?si=bnyptzNFx4jzOiEj" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">
      <img src="https://img.youtube.com/vi/hAwtrJlBVJY/hqdefault.jpg" alt="The Brutal Truth Behind Tech Layoffs" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">
      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">
        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>
      </div>
    </div>

    </center>

## GitOps

??? note "🎬 GitOps Guide to the Galaxy"
    !!! info "Architectural Summary"
        Every other Thursday at 3pm ET hosts Hilliary Lipsig and Jonathan Rickard dive into everything in the GitOps universe, from solutions to common problems in end-to-end CICD pipelines, to creating Git workflows. This series explores how GitOps enhances modern application delivery and discusses the latest news around best practices and Cloud Native architecture.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=zdATyq_E2wXN7AC6&amp;list=PLbMP1JcGBmSGKO8UreWpOBOhCqilejhtd" title="GitOps Guide to the Galaxy" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Jenkins

??? note "🎬 Jenkins Tutorials"
    !!! info "Architectural Summary"
        This comprehensive video series details core Jenkins CI/CD automation techniques, including Pipeline-as-Code implementations and system management best practices. In a 2026 cloud-native context, mastering Jenkins remains critical for orchestrating complex build pipelines, bridging the gap between legacy infrastructure and modern Kubernetes deployment targets. The tutorials provide foundational architectural patterns for establishing scalable, automated, and reproducible continuous integration workflows across distributed enterprise environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=GBJtqv36O8bslj9z&amp;list=PLvBBnHmZuNQJeznYL2F-MpZYBUeLIXYEe" title="Jenkins Tutorials" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## NetBox

??? note "🎬 NetBox Zero To Hero"
    !!! info "Architectural Summary"
        NetBox serves as the foundational source of truth for modern network automation by integrating IP Address Management (IPAM) and Data Center Infrastructure Management (DCIM) into a unified database. In a 2026 Cloud Native ecosystem, it empowers Infrastructure as Code (IaC) pipelines to dynamically query and enforce intended network state via robust APIs, effectively eliminating configuration drift. This architectural approach bridges the gap between physical hardware tracking and automated, declarative network orchestration across complex hybrid environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=fJvBV63-mjQ6S-Ht&amp;list=PL7sEPiUbBLo_iTds-NV-9Tu05Gg2Aj8N7" title="NetBox Zero To Hero" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>
