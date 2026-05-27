# 🎥 Cloud Native Core

Welcome to the **Cloud Native Core** section of the V2 Video Hub. Explore curated high-density videos with architectural summaries.

## Table of Contents

1. [Kubernetes](#kubernetes)
2. [Red Hat OpenShift](#red-hat-openshift)
3. [Platform Engineering](#platform-engineering)
4. [Ruby on Rails](#ruby-on-rails)
5. [Ruby on Rails Hotwire](#ruby-on-rails-hotwire)
6. [Portworx](#portworx)
7. [HashiCorp Stack Terraform Vault Consul Boundary](#hashicorp-stack-terraform-vault-consul-boundary)
8. [Modular Monoliths](#modular-monoliths)
9. [Git](#git)
10. [Distributed Systems Strategy](#distributed-systems-strategy)
11. [FinOps](#finops)
12. [GitOps](#gitops)
13. [Hosted Control Planes](#hosted-control-planes)
14. [Azure Verified Modules AVM](#azure-verified-modules-avm)
15. [OpenShift](#openshift)
16. [VS Code](#vs-code)

## Kubernetes

??? note "🎬 Kubernetes for SysAdmins | Kelsey Hightower at PuppetConf | Talk & Demo"
    !!! info "Architectural Summary"
        This seminal presentation outlines the paradigm shift from traditional imperative configuration management to declarative, container-orchestrated infrastructure by redefining the operating contract between applications and underlying systems. Viewed from a 2026 cloud-native perspective, Kelsey Hightower's early demonstrations of self-healing workloads, automated bin-packing, and custom controllers for automated TLS provisioning serve as the foundational blueprint for modern platform engineering. The architectural concepts covered—specifically decoupling stateful storage and leveraging native service discovery—remain highly relevant for engineers transitioning from static sysadmin practices to dynamic API-driven control loops.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/HlAXp0-M6SY?clip=UgkxWpu3QFPEDZBuMgy_Xq4mBR--uLA-3CSZ&amp;clipt=EMSoKxiG3C4" title="Kubernetes for SysAdmins | Kelsey Hightower at PuppetConf | Talk & Demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Keynote: 7 Years of Running Kubernetes for Mercedes-Benz"
    !!! info "Architectural Summary"
        This architectural retrospective outlines Mercedes-Benz's transformation from legacy, manual infrastructure management to an on-premises, self-service cloud platform managing nearly 1,000 clusters via Cluster API (CAPI). In a 2026 cloud-native context, it demonstrates the vital patterns for scaling declarative cluster lifecycle management and shifting traditional enterprise operations toward platform engineering model. The session highlights how organizational resilience, open-source alignment, and robust automation topologies can successfully modernize highly regulated corporate data centers.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/UmbjwSK9b3I?clip=UgkxRGuBMDAVDqKckQ1lhk-9U2jLBhBIBI5l&amp;clipt=EP2dHhjd8iE" title="Keynote: 7 Years of Running Kubernetes for Mercedes-Benz" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Red Hat OpenShift

??? note "🎬 Thursday morning general session - May 9 - Red Hat Summit 2019"
    !!! info "Architectural Summary"
        This session outlines the architectural deployment of Red Hat OpenShift as a unified hybrid cloud platform, demonstrating how enterprise Kubernetes orchestrates complex workloads across multi-cloud and edge environments. It highlights critical integrations with GPU acceleration and AI/ML pipelines, establishing a robust blueprint for modern MLOps and scalable cloud-native operations.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/FUu4kMc0PL8?clip=UgkxFMdlFKBQze7NVVd7q2nIwBYWkeaKeoX8&amp;clipt=EIzBzwIY1fnSAg" title="Thursday morning general session - May 9 - Red Hat Summit 2019" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Red Hat OpenShift Platform Plus - Overview"
    !!! info "Architectural Summary"
        Red Hat OpenShift Platform Plus provides an enterprise-grade, multi-cluster Kubernetes foundation integrating advanced cluster management, declarative DevSecOps security, and a global container registry. In a 2026 cloud-native landscape, it delivers a unified platform engineering control plane that simplifies multi-cloud operations while enforcing consistent governance and security policies from core to edge. This suite accelerates secure software delivery pipelines by embedding automated compliance and threat protection directly into the application lifecycle.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/V7PSnH8YnTk?si=6Mq4wjpipTLwUvYe" title="Red Hat OpenShift Platform Plus - Overview" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Platform Engineering

??? note "🎬 What is Platform Engineering and how it fits into DevOps and Cloud world"
    !!! info "Architectural Summary"
        This video details the evolution of cloud operations into Platform Engineering, focusing on the architecture and implementation of Internal Developer Platforms (IDPs) to mitigate developer cognitive load. By establishing standardized 'golden paths' through Infrastructure as Code (IaC) and self-service APIs, organizations can balance developer autonomy with rigorous governance, security, and compliance. This paradigm shift optimizes resource provisioning and modernizes DevOps workflows for highly scalable, cloud-native environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/ghzsBm8vOms" title="What is Platform Engineering and how it fits into DevOps and Cloud world" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Ruby on Rails

??? note "🎬 David Heinemeier Hansson: Microservices vs. Monolith"
    !!! info "Architectural Summary"
        In this discussion, David Heinemeier Hansson critiques the dogmatic adoption of microservices, highlighting how they introduce substantial operational complexity, network latency, and cognitive load compared to a well-structured monolith. He champions the 'Majestic Monolith' as a pattern that maximizes developer velocity and reduces organizational overhead by keeping the deployment domain unified. For modern cloud-native architectures, this perspective serves as a crucial counterweight to microservice fatigue, driving the industry toward highly-optimized modular monoliths that simplify infrastructure and cut cloud spend.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/rkXGSLf-rVQ?si=Ho8Zzxbrecn7Yncb" title="David Heinemeier Hansson: Microservices vs. Monolith" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Ruby on Rails Hotwire

??? note "🎬 The creator of Rails on JavaScript FE vs. Classic Server-side Rendering"
    !!! info "Architectural Summary"
        David Heinemeier Hansson critiques the complexity of modern Single Page Application (SPA) architectures, advocating instead for the 'Majestic Monolith' and HTML-over-the-wire (Hotwire) to keep application logic unified on the server. In a 2026 cloud-native context, this paradigm challenges the overhead of decoupled micro-frontends by proving that server-side rendering (SSR) combined with lightweight HTML streaming dramatically simplifies deployment pipelines, reduces client-side resource consumption, and lowers data egress costs. This architectural approach optimizes for operational efficiency, enabling smaller engineering teams to build highly responsive, production-grade applications without managing complex API contract synchronizations.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/IFUPG9KCJ4E?si=KMEXeVlcKTp87-Ja" title="The creator of Rails on JavaScript FE vs. Classic Server-side Rendering" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Portworx

??? note "🎬 Murli Thirumale | KubeCon CloudNativeCon EU 2023"
    !!! info "Architectural Summary"
        This discussion outlines how enterprise platform engineering teams leverage Portworx to deliver automated, resilient Database-as-a-Service (DBaaS) capabilities directly on Kubernetes. By abstracting multi-cloud storage, disaster recovery, and data security, it highlights architectural strategies essential for scaling stateful cloud-native workloads. For a 2026 cloud-native landscape, these unified data management planes are critical for mitigating multi-cloud lock-in, controlling cloud spend, and accelerating application delivery.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/I8Qh-TafMvQ?si=1A2-kmq6mV-S-03c" title="Murli Thirumale | KubeCon CloudNativeCon EU 2023" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## HashiCorp Stack Terraform Vault Consul Boundary

??? note "🎬 Building a developer platform? Ask these questions."
    !!! info "Architectural Summary"
        This session details how to build secure, scalable developer platforms by defining 'golden paths' using HashiCorp's suite of automation tools, including Terraform, Vault, Consul, and Boundary. It provides a strategic framework for resolving key platform engineering challenges such as Day 2 operations, infrastructure dependency mapping, secure access control, and seamless local-to-remote environment transitions. By abstracting cloud complexity, the session demonstrates how to deliver high-velocity self-service capabilities to development teams while ensuring governance and security compliance.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/1Fl25dR01pw?si=bJlQozIfT3J4rhN3" title="Building a developer platform? Ask these questions." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Modular Monoliths

??? note "🎬 ¿De verdad son necesarios los microservicios? [SPANISH CONTENT]"
    !!! info "Architectural Summary"
        This video critically evaluates the over-engineering of distributed systems, examining whether the operational overhead, network latency, and complexity of microservices are justified for most projects. In a 2026 cloud-native landscape focusing heavily on cost optimization and developer velocity, it advocates for a pragmatic, domain-driven approach, highlighting modular monoliths as a powerful alternative before prematurely adopting microservices.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/L8eJh1sfc1U?si=y546MyZpRe-thoad" title="¿De verdad son necesarios los microservicios?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Git

??? note "🎬 Branching Strategies Explained"
    !!! info "Architectural Summary"
        This guide provides a comprehensive architectural evaluation of various Git branching strategies, including Trunk-Based Development, Feature Branches, Git Flow, and Environment Branches, weighing their impacts on delivery velocity. For a 2026 cloud-native landscape, it emphasizes how moving toward trunk-based development or short-lived feature branches is essential for optimizing continuous integration (CI) pipelines, minimizing integration debt, and enabling rapid, automated deployments to Kubernetes and cloud environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/U_IFGpJDbeU?si=XzHSGU9dTH-1_0EW" title="Branching Strategies Explained" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Distributed Systems Strategy

??? note "🎬 Elon Musk talks Twitter, Tesla and how his brain works — live at TED2022"
    !!! info "Architectural Summary"
        This systemic interview highlights architectural principles around open-sourcing core algorithms to enforce platform transparency and trust, directly paralleling modern GitOps, policy-as-code, and zero-trust verification frameworks in Cloud Native environments. Additionally, the insights on extreme manufacturing automation offer critical design lessons for 2026 edge computing, emphasizing the necessity of closed-loop automation, event-driven orchestration, and radical simplification of complex distributed infrastructures.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/cdZZpaB2kDM?clip=UgkxWAPHZbVaNZzk9pi0lMu6k5ABLuMHBtRL&amp;clipt=EK2rfRjW9YAB" title="Elon Musk talks Twitter, Tesla and how his brain works — live at TED2022" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## FinOps

??? note "🎬 The Brutal Truth Behind Tech Layoffs"
    !!! info "Architectural Summary"
        This analysis dissects the macroeconomic shift from hyper-growth talent hoarding to hyper-efficiency, highlighting the systemic collapse of bloated engineering teams in favor of lean, automated operations. For a 2026 cloud-native landscape, this underscores the critical role of platform engineering and robust FinOps architectures designed to maximize resource utilization while minimizing human-in-the-loop operational overhead. Architects must leverage these insights to build self-healing, highly automated platforms that successfully decouple organizational scale from headcount.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/hAwtrJlBVJY?si=bnyptzNFx4jzOiEj" title="The Brutal Truth Behind Tech Layoffs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## GitOps

??? note "🎬 GitOps Guide to the Galaxy"
    !!! info "Architectural Summary"
        Every other Thursday at 3pm ET hosts Hilliary Lipsig and Jonathan Rickard dive into everything in the GitOps universe, from solutions to common problems in end-to-end CICD pipelines, to creating Git workflows. This series explores how GitOps enhances modern application delivery and discusses the latest news around best practices and Cloud Native architecture.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/videoseries?si=zdATyq_E2wXN7AC6&amp;list=PLbMP1JcGBmSGKO8UreWpOBOhCqilejhtd" title="GitOps Guide to the Galaxy" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Hosted Control Planes

??? note "🎬 GitOps Guide to the Galaxy: Hosted Control Planes (HyperShift)"
    !!! info "Architectural Summary"
        This session from the GitOps Guide to the Galaxy deconstructs the architecture of Hosted Control Planes (HCP), also known as HyperShift. It explores how HCP decouples the Kubernetes control plane from worker nodes, hosting it as a scalable workload on a management cluster to drastically reduce operational overhead, improve provisioning speed, and optimize resource utilization. For 2026 platform engineering, mastering this pattern is essential for managing large-scale, multi-tenant Kubernetes fleets with high-density efficiency and strong isolation.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/LiSb82Lug7M" title="GitOps Guide to the Galaxy: Hosted Control Planes (HyperShift)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## Azure Verified Modules AVM

??? note "🎬 Building Secure, Well‑Architected Azure Workloads with Azure Verified Modules and GitHub Copilot"
    !!! info "Architectural Summary"
        Azure Verified Modules (AVM) is the official Microsoft infrastructure-as-code module library for both Bicep and Terraform. This session explores how AVM standardizes deployments according to the Azure Well-Architected Framework by default, shipping with high-impact security defaults like zone redundancy and disabled public IPs. It introduces Spec-Driven Development with GitHub Copilot using the "Spec Kit" (an 8-step framework from constitution to implementation). By turning non-deterministic AI prompts into reliable, repeatable builds, architects can leverage AI as a trusted foundation for secure and compliant Azure workload orchestration.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/QBqRAMVTmwE" title="Building Secure, Well‑Architected Azure Workloads with Azure Verified Modules and GitHub Copilot" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## OpenShift

??? note "🎬 Fran Heeran, Red Hat | Red Hat Summit 2026"
    !!! info "Architectural Summary"
        In this Red Hat Summit 2026 interview, Fran Heeran details how telecommunications providers are shifting from heavily siloed infrastructure to unified cloud-native architectures. By leveraging OpenShift Virtualization, telcos can centrally manage both legacy virtual machines and modern containers across core networks and the far edge, accelerating deployments up to 50%. This unified architecture additionally enables sovereign cloud offerings and closed-loop network automation by feeding AI outputs directly into Ansible-driven remediation workflows.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/Tr4onEST70I" title="Fran Heeran, Red Hat | Red Hat Summit 2026" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

## VS Code

??? note "🎬 Remote VS Code with Dev Tunnels: access the editor from your browser [SPANISH CONTENT]"
    !!! info "Architectural Summary"
        In this tutorial, Gisela Torres explains the architecture and application of VS Code Dev Tunnels to enable secure remote access to local development environments. Dev Tunnels establish a secure, encrypted connection to VS Code without requiring complex VPNs or firewall modifications, allowing developers to connect from any web browser or secondary editor instance. For 2026 developer productivity, this simplifies remote workspace orchestration and collaborative debugging in cloud-native platforms. [SPANISH CONTENT]

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/embed/niuJpAKyb7c" title="Remote VS Code with Dev Tunnels: access the editor from your browser" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>
