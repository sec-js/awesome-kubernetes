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
17. [Cloud Native](#cloud-native)

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

## Cloud Native

??? note "🎬 Agent-first workflows from prompt to production"
    !!! info "Architectural Summary"
        A deep dive into the operationalization of AI agents and agentic application lifecycles on Google Cloud. Focuses on orchestrating multi-agent systems, integrating Model Context Protocol (MCP) standards, and automating secure CI/CD pipelines directly from developer environments to managed serverless backends.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=QtXBAz6TU2g&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=4&pp=iAQB" title="Agent-first workflows from prompt to production" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 What's new in Android development tools"
    !!! info "Architectural Summary"
        A deep dive into the 2026 features of Android Studio and its accompanying tool suite. Focuses on native AI diagnostics, code refactoring optimizations, layout rendering acceleration, and debugging frameworks aimed at building resilient applications targetting Android 17.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=iyc69njNYOw&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=9&pp=iAQB" title="What's new in Android development tools" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Google I/O 2026: Dialogues"
    !!! info "Architectural Summary"
        A highly strategic collection of panels from Google I/O 2026 focused on industrial technology shifts. Covers critical conversations with scientific leaders, including DeepMind and Boston Dynamics executives, analyzing the crossover between quantum computing, physical embodiment robotics, and proactive multi-agent orchestration. Essential viewing for enterprise architects assessing the trajectory of next-generation physical and logical agentic applications.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/playlist?list=PLOU2XLYxmsIJuxYe1znksQlhLJ4w8GKCu" title="Google I/O 2026: Dialogues" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 AI at Google I/O 2026"
    !!! info "Architectural Summary"
        An elite collection of developer technical sessions from Google I/O 2026. Delves deep into the architectural implementations of Google Antigravity 2.0, multi-agent frameworks, on-device AI deployments using Gemma 4, and developer-centric orchestration layers. Provides practical engineering blueprints for cloud and mobile platform engineers building autonomous, secure, and resilient agentic workflows.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/playlist?list=PLOU2XLYxmsIJp39MsvkeWYYNwMso-HeNT" title="AI at Google I/O 2026" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Integrating ComfyUI & Avid: Google AI's Big Move"
    !!! info "Architectural Summary"
        An expert architectural discussion detailing the integration of Google Cloud's generative AI frameworks with professional media editors like Avid Media Composer and ComfyUI. Demonstrates how multimodal search APIs powered by Gemini automate indexing, while generative models streamline localized edits. Illustrates a paradigm shift toward production-scale agentic video editing, reducing technical friction within traditional filmmaking toolchains.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=ppMWxjsmk2k&linkId=61897585" title="Integrating ComfyUI & Avid: Google AI's Big Move" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Integrating ComfyUI & Avid: Google AI's Big Move"
    !!! info "Architectural Summary"
        An expert architectural discussion detailing the integration of Google Cloud's generative AI frameworks with professional media editors like Avid Media Composer and ComfyUI. Demonstrates how multimodal search APIs powered by Gemini automate indexing, while generative models streamline localized edits. Illustrates a paradigm shift toward production-scale agentic video editing, reducing technical friction within traditional filmmaking toolchains.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=BtgZLw8hYiU&feature=youtu.be" title="Integrating ComfyUI & Avid: Google AI's Big Move" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation"
    !!! info "Architectural Summary"
        * **Curator Insight:** Ensuring clean code review, architectural cohesion, and governance across thousands of global developers is fundamental to the long-term sustainability of the CNCF core.
        * **Live Grounding (MCP):** The April 2026 orientation walk-through presents SIG architectures, environment installation steps, coding standards, and repository PR policies, establishing a standard learning curve for platform engineers.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=DjBBV7oZxm8" title="Kubernetes New Contributor Orientation" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation"
    !!! info "Architectural Summary"
        * **Curator Insight:** Ensuring clean code review, architectural cohesion, and governance across thousands of global developers is fundamental to the long-term sustainability of the CNCF core.
        * **Live Grounding (MCP):** The April 2026 orientation walk-through presents SIG architectures, environment installation steps, coding standards, and repository PR policies, establishing a standard learning curve for platform engineers.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=aqmpZocmR8o&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=3&pp=iAQB" title="Kubernetes New Contributor Orientation" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 The Shift Podcast by Microsoft Azure—Agentic Edition"
    !!! info "Architectural Summary"
        An authoritative, engineering-focused video podcast playlist from Microsoft Azure that deep-dives into the architecture of agentic systems. Across several unscripted episodes, industry leads and Core AI research scientists explore multi-agent orchestration, context engineering vs. RAG, the evolution of relational and open-source databases (Postgres) to support context retrieval, and the role of unified data fabrics like Microsoft OneLake. It serves as an essential architectural design guide for software engineers and systems architects building context-aware, autonomous enterprise workloads.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/playlist?list=PLLasX02E8BPBCP7KdYsjKKFFQUmNEUmE9" title="The Shift Podcast by Microsoft Azure—Agentic Edition" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2026-02-17"
    !!! info "Architectural Summary"
        Curator Insight: Structured community onboarding plays a vital role in sustaining core open-source infrastructure velocity.
        
        Live Grounding: This SIG Contributor Experience recording guides developers through the CNCF ecosystem, detailing SIG structures, GitHub PR triaging via Prow bot commands, and the technical requirements for official Kubernetes org membership.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=F3al0HP0MNo" title="Kubernetes New Contributor Orientation for 2026-02-17" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2026-03-17"
    !!! info "Architectural Summary"
        Curator Insight: Standardized onboarding tutorials are indispensable for reducing the barrier of entry into massive microservice orchestration codebases.
        
        Live Grounding: This community briefing walks new contributors through the Kubernetes architecture, mentoring programs, the SIG CLI subset, and operational steps for setting up local test beds and submitting code.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=gkcZEXqkmZM" title="Kubernetes New Contributor Orientation for 2026-03-17" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2026-04-21"
    !!! info "Architectural Summary"
        Curator Insight: Target-specific SIG orientations are highly valuable for engineers developing specialized client tooling or control plane extensions.
        
        Live Grounding: This April 2026 recording explicitly zeroes in on SIG CLI and kubectl architectures, walking contributors through local build pipelines, command validation, and the technical lifecycle of CLI contributions.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=B_8vYxurU4k" title="Kubernetes New Contributor Orientation for 2026-04-21" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2026-03-17"
    !!! info "Architectural Summary"
        Curator Insight: Sustaining massive open-source systems like Kubernetes relies on structured mentoring and clear contribution pathways.
        
        Live Grounding: This official session recorded in March 2026 provides a guided overview of the community governance under the SIG ContribEx mentoring subproject.
        
        Technical Relevance:
        - Demystifies the roles of special interest groups (SIGs) and working groups in core development.
        - Educates cloud-native engineers on contribution guidelines, code review, and pull request mechanics.
        - Offers direct community onboarding without hands-on coding requirements to prioritize structural understanding.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=Frje5KfNrxE" title="Kubernetes New Contributor Orientation for 2026-03-17" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19"
    !!! info "Architectural Summary"
        **Curator Insight:** This episode deconstructs the shift in image generation architectures from early pixel-diffusion to highly coherent multi-modal reasoning models.
        **Live Grounding:** Product and research leads at OpenAI detail ChatGPT's Images 2.0 capabilities, demonstrating breakthroughs in spatial photorealism, multilingual typography rendering, and high-fidelity aspect ratio adaptability.
        *   **Architectural Significance:** Provides critical engineering context on how model training breakthroughs enhance character and scene consistency across iterative generative pipelines.
        *   **Key Features Covered:** Real-time prompt evaluation, multilingual world knowledge injection, and the integration of image generators with agentic coding environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=bH2nP-aCFjk&feature=youtu.be" title="Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19"
    !!! info "Architectural Summary"
        **Curator Insight:** This episode deconstructs the shift in image generation architectures from early pixel-diffusion to highly coherent multi-modal reasoning models.
        **Live Grounding:** Product and research leads at OpenAI detail ChatGPT's Images 2.0 capabilities, demonstrating breakthroughs in spatial photorealism, multilingual typography rendering, and high-fidelity aspect ratio adaptability.
        *   **Architectural Significance:** Provides critical engineering context on how model training breakthroughs enhance character and scene consistency across iterative generative pipelines.
        *   **Key Features Covered:** Real-time prompt evaluation, multilingual world knowledge injection, and the integration of image generators with agentic coding environments.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=sig3n7XyaaA&list=PLOU2XLYxmsIKL_eEgkKJWDRhYUEvS9eYz&index=2" title="Inside image generation’s Renaissance moment — the OpenAI Podcast Ep. 19" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-08-19"
    !!! info "Architectural Summary"
        An official onboarding session for aspiring Kubernetes project contributors, detailing the governance framework of the CNCF ecosystem. Explains the structural organization across Special Interest Groups (SIGs) and Working Groups, org membership criteria, and GitHub automation tools like Probot. Ideal for software engineers and site reliability engineers looking to contribute to upstream Kubernetes repositories.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=V3Sq0Fgy3ds" title="Kubernetes New Contributor Orientation for 2025-08-19" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-08-19 (Alternative Link)"
    !!! info "Architectural Summary"
        Alternative upload or session recording of the Kubernetes 2025 contributor orientation. Outlines the CNCF governance models, organization of Special Interest Groups (SIGs), and GitHub-driven developer workflows utilizing tools like Probot. Provides key foundational insights for engineers aiming to secure organizational membership and contribute code to upstream repositories.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=3B41u33BS2E" title="Kubernetes New Contributor Orientation for 2025-08-19 (Alternative Link)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-07-15"
    !!! info "Architectural Summary"
        An official video recording of the Kubernetes New Contributor Orientation, managed by the CNCF. It outlines upstream development workflows, Special Interest Group (SIG) engagement models, and the testing/CI pipelines (Prow) necessary for successfully contributing code and documentation to the Kubernetes repository.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=l2HpdgRFtN0" title="Kubernetes New Contributor Orientation for 2025-07-15" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-09-16"
    !!! info "Architectural Summary"
        This video records the official monthly onboarding session organized by SIG-ContribEx for aspiring Kubernetes project developers. It breaks down the vast governance structure of the CNCF ecosystem, outlining the roles of Special Interest Groups (SIGs), the mailing lists, and how to navigate core repositories like kubernetes/community and kubernetes/enhancements. It serves as an essential stepping stone for engineers looking to actively participate in upstream cloud-native development.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=36aGHlsxlow" title="Kubernetes New Contributor Orientation for 2025-09-16" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-08-18"
    !!! info "Architectural Summary"
        An official community onboarding video detailing the core processes of contributing to the Kubernetes codebase and ecosystem. It outlines the logical SIG structure, repository layouts, contribution workflows, and development workflows (such as Prow). This recording acts as a practical handbook for cloud engineers intending to navigate CNCF governance models.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=XAOqUU5Xh1c" title="Kubernetes New Contributor Orientation for 2025-08-18" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation for 2025-09-16"
    !!! info "Architectural Summary"
        The September 2025 edition of the official Kubernetes contributor orientation. This session focuses on guiding engineers through repository structures, the Slack channels, mailing lists, and governance mechanisms. Essential guidance for individuals aiming to commit upstream code, join SIGs, or collaborate on documentation within CNCF frameworks.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=J7R-T9Y1x3Y" title="Kubernetes New Contributor Orientation for 2025-09-16" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 Kubernetes New Contributor Orientation Playlist"
    !!! info "Architectural Summary"
        This official, continuously updated YouTube playlist collects previous orientation sessions for new Kubernetes contributors. Organized by the Kubernetes Contributor Experience group, the videos outline technical governance structures, toolsets, and workflow patterns. It serves as an authoritative learning pathway for organizations deploying and contributing to upstream Kubernetes projects.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/playlist?list=PLA6Ht2dJt3SId7vE9P5mppWdj65_l6hl7" title="Kubernetes New Contributor Orientation Playlist" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>

??? note "🎬 What is New in Google AI"
    !!! info "Architectural Summary"
        Recorded at Google I/O 2026, Google developer advocates and product leads present a comprehensive overview of the company's end-to-end AI stack. The session details advanced multimodal capabilities, media generation models, and robotics integration, while explaining how to leverage Google's infrastructure for agent development, vibe-coding workflows, and open-source model tuning and serving.

    <center markdown="1">

    <iframe width="720" height="405" src="https://www.youtube.com/watch?v=SSe1VmVrtw0&feature=youtu.be" title="What is New in Google AI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>

    </center>
