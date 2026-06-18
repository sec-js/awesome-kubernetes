# AI Agents and Model Context Protocol (MCP) for Kubernetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ai-agents-mcp/).

!!! info "Architectural Context"
    Detailed reference for AI Agents and Model Context Protocol (MCP) for Kubernetes in the context of AI.

## Table of Contents

1. [AI and Agents](#ai-and-agents)
  - [Environments](#environments)
    - [Claude](#claude)
  - [Frameworks](#frameworks)
    - [Google Cloud](#google-cloud)
1. [AI Engineering](#ai-engineering)
  - [AI Agents](#ai-agents)
    - [Web Automation](#web-automation)
  - [Agentic Frameworks](#agentic-frameworks)
    - [Developer Experience](#developer-experience)
  - [Model Context Protocol](#model-context-protocol)
    - [Architecture](#architecture)
    - [Awesome Lists](#awesome-lists)
    - [Developer Experience](#developer-experience-1)
    - [Google Cloud](#google-cloud-1)
    - [Official Servers](#official-servers)
    - [Specifications](#specifications)
1. [AI Infrastructure](#ai-infrastructure)
  - [Distributed Computing](#distributed-computing)
    - [Kube-Ray](#kube-ray)
  - [Hardware Orchestration](#hardware-orchestration)
    - [NVIDIA Operators](#nvidia-operators)
  - [LLM Serving](#llm-serving)
    - [LocalAI](#localai)
    - [vLLM](#vllm)
1. [Architectural Foundations](#architectural-foundations)
  - [Kubernetes Tools](#kubernetes-tools)
    - [General Reference](#general-reference)
1. [Automation](#automation)
  - [Agentic Systems](#agentic-systems)
    - [MCP Server](#mcp-server)
1. [Cloud Native Operations](#cloud-native-operations)
  - [AI AIOps](#ai-aiops)
    - [Kubernetes Troubleshooting](#kubernetes-troubleshooting)
1. [Developer Experience](#developer-experience-2)
  - [AI-Assisted Coding](#ai-assisted-coding)
    - [Claude Code](#claude-code)
    - [Cursor IDE](#cursor-ide)
1. [Software Engineering](#software-engineering)
  - [AI Tools](#ai-tools)
    - [Claude Code](#claude-code-1)

## AI and Agents

### Environments

#### Claude

  - **(2025)** [==docs.anthropic.com: Claude Code CLI==](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Anthropic's official command-line interface (CLI) tool designed for autonomous agentic software engineering.
Claude Code can read codebases, execute commands, run tests, and manage git workflows directly in terminal environments.
### Frameworks

#### Google Cloud

  - **(2026)** [==antigravity.google: Google Antigravity Agentic Platform==](https://antigravity.google) <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Google's unified development platform and SDK (google-antigravity) for building, evaluating, and deploying stateful AI agents.
Enables developers to transition from local prototype builds to secure GKE production environments and leverage the Gemini Enterprise Agent Platform.
## AI Engineering

### AI Agents

#### Web Automation

  - **(2025)** [==Skyvern==](https://github.com/Skyvern-ai/Skyvern) <span class='md-tag md-tag--info'>⭐ 21899</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-3038a3b2" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 12 L 20 13 L 30 3 L 40 11 L 50 5" fill="none" stroke="url(#spark-grad-3038a3b2)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: An AI-powered web browser automation agent designed to extract data and execute workflows on complex interfaces. Live Grounding: Translates plain-text instructions into resilient selenium-style interactions, dynamically adapting to DOM mutations and bypassing rigid selector patterns.
### Agentic Frameworks

#### Developer Experience

  - **(2025)** [Kiro: Engineering Rigor for Agentic Development](https://kiro.dev) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Kiro is a testing and engineering framework designed to bring traditional software discipline—such as regression testing, linting, and sandbox executing—to LLM agents and multi-agent workflows. It establishes strict validation steps to ensure agent behaviors remain deterministic, secure, and aligned with standard corporate software engineering guidelines.
### Model Context Protocol

#### Architecture

  - **(2024)** [anthropic.com: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Anthropic's release document introducing the Model Context Protocol (MCP), an open-standard protocol enabling LLM agents to securely interact with external tools and data sources. MCP standardizes the JSON-RPC interface between hosts and servers, resolving the integration fragmentation that previously plagued generative AI integrations and agentic workflows.
#### Awesome Lists

  - **(2025)** [==Awesome MCP Servers==](https://github.com/punkpeye/awesome-mcp-servers) <span class='md-tag md-tag--info'>⭐ 89112</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-396cb5e3" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 4 L 20 9 L 30 10 L 40 3 L 50 5" fill="none" stroke="url(#spark-grad-396cb5e3)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A community-curated collection of servers implementing the Model Context Protocol. Live Grounding: Aggregates verified integrations linking AI models to tools like relational databases, enterprise APIs, version control providers, and local execution runtimes.
#### Developer Experience (1)

  - **(2025)** [MCPBundles](https://www.mcpbundles.com) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — MCPBundles is a discovery and packaging platform designed to bundle various Model Context Protocol servers for rapid deployment. It simplifies agentic application building by providing curated, pre-configured groupings of tools (e.g., database drivers, git utilities, API endpoints) that can be integrated into AI hosts in a single setup operation.
#### Google Cloud (1)

  - **(2025)** [Google Cloud Managed MCP](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-managed-mcp-for-gemini) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google Cloud's managed solution for Model Context Protocol, allowing enterprise Gemini models to safely interact with local data sources and external enterprise systems. By hosting and scaling MCP servers inside Google's managed environment, it minimizes operational overhead while securing transactional agentic workflows with native cloud IAM.
#### Official Servers

  - **(2025)** [==GitHub MCP Server==](https://github.com/modelcontextprotocol/servers) <span class='md-tag md-tag--info'>⭐ 87194</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-b5025440" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 2 L 10 2 L 20 8 L 30 13 L 40 7 L 50 2" fill="none" stroke="url(#spark-grad-b5025440)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Primary collection of production-grade Model Context Protocol (MCP) servers. Live Grounding: Establishes development standards for JSON-RPC 2.0 based message exchange between host agents and enterprise backend systems.
#### Specifications

  - **(2025)** [modelcontextprotocol.io: MCP Official Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official technical documentation and specifications for the Model Context Protocol (MCP). It provides comprehensive blueprints for implementing client-server architectures, defining standard JSON-RPC 2.0 schemas for prompt execution, resource exploration, and tool binding. Serves as the authoritative source for developers building LLM integrations.
## AI Infrastructure

### Distributed Computing

#### Kube-Ray

  - **(2025)** [Kube-Ray](https://github.com/ray-project/kuberay) <span class='md-tag md-tag--info'>⭐ 2541</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2471d9c8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 11 L 20 3 L 30 12 L 40 5 L 50 4" fill="none" stroke="url(#spark-grad-2471d9c8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An open-source Kubernetes Operator enabling the deployment and management of Ray clusters. Live Grounding: Serves as the backbone for distributed machine learning workloads on Kubernetes, abstracting compute node scaling, memory configuration, and actor scheduling.
### Hardware Orchestration

#### NVIDIA Operators

  - **(2025)** [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator) <span class='md-tag md-tag--info'>⭐ 2739</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6c3bb734" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 6 L 20 4 L 30 8 L 40 4 L 50 5" fill="none" stroke="url(#spark-grad-6c3bb734)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Kubernetes operator designed to automate the management of NVIDIA software components on nodes. Live Grounding: Provisions GPU drivers, container runtimes, device plug-ins, and monitoring tools automatically, ensuring consistent access to hardware acceleration.
### LLM Serving

#### LocalAI

  - **(2025)** [**LocalAI**](https://github.com/mudler/LocalAI) <span class='md-tag md-tag--info'>⭐ 46845</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ea9eeb00" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 3 L 20 12 L 30 7 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-ea9eeb00)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: A self-hosted, community-first OpenAI-compatible API gateway running on local hardware. Live Grounding: Allows developers to host LLMs, audio-to-text, and image generation services inside Kubernetes without external data dependencies, optimized for consumer-grade and enterprise hardware.
#### vLLM

  - **(2025)** [==vLLM on Kubernetes==](https://github.com/vllm-project/vllm) <span class='md-tag md-tag--info'>⭐ 82816</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6caed060" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 7 L 20 6 L 30 7 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-6caed060)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Integration guides and deployment schemas for hosting vLLM on Kubernetes clusters. Live Grounding: Standardizes memory-efficient LLM serving using PagedAttention. Features rapid integration with Kubernetes HPA (Horizontal Pod Autoscaler) and native Prometheus performance scraping.
## Architectural Foundations

### Kubernetes Tools

#### General Reference

  - [IBM IAM for AI Agents](https://t.co/EKsVgKA4xn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering IBM IAM for AI Agents in the Kubernetes Tools ecosystem.
  - [PulseMCP](https://pulsemcp.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A curated technical resource and architectural guide covering PulseMCP in the Kubernetes Tools ecosystem.
## Automation

### Agentic Systems

#### MCP Server

  - **(2026)** [Announcing Azure MCP Server 2.0 Stable Release for Self-Hosted Agentic Cloud Automation](https://devblogs.microsoft.com/azure-sdk/announcing-azure-mcp-server-2-0-stable-release) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Details the stable release of Azure MCP (Model Context Protocol) Server 2.0, enabling secure, self-hosted agentic automation workflows. It provides architectural patterns for running local AI agents with direct, API-driven access to Azure resource management, optimizing operational automation via language model integrations.
## Cloud Native Operations

### AI AIOps

#### Kubernetes Troubleshooting

  - **(2025)** [HolmesGPT (Robusta)](https://github.com/HolmesGPT/holmesgpt) <span class='md-tag md-tag--info'>⭐ 2623</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-892577ed" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 5 L 20 6 L 30 13 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-892577ed)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An AI-driven troubleshooting assistant for Kubernetes clusters by Robusta. Live Grounding: Utilizes LLM agents to autonomously parse Prometheus alerts, collect pod logs, inspect live status, and deliver actionable remediation steps for infrastructure incidents.
## Developer Experience (2)

### AI-Assisted Coding

#### Claude Code

  - **(2025)** [==Claude Code Best Practice==](https://github.com/shanraisshan/claude-code-best-practice) <span class='md-tag md-tag--info'>⭐ 57660</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-26ea52d5" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 3 L 10 2 L 20 3 L 30 5 L 40 3 L 50 2" fill="none" stroke="url(#spark-grad-26ea52d5)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="2" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Curated collection of best practices, system prompts, and architecture layouts for Claude Code. Live Grounding: Explores advanced CLI-driven agent workflows, highlighting configuration optimizations, shell integration strategies, and secure execution configurations in local and remote environments.
  - **(2025)** [Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — An official hands-on tutorial and demonstration course by Anthropic showing the real-world utility of Claude Code. It covers basic terminal setups, interactive file refactoring, automated git commit orchestration, and contextual testing loops. Highly valuable for teams integrating terminal-based AI agents directly into daily engineering pipelines.
#### Cursor IDE

  - **(2025)** [Cursor AI Fundamentals Course](https://cursor.com/es/learn) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--secondary'>[GUIDE]</span> <span class='md-tag md-tag--critical'>[LEGACY]</span> — An educational program designed to train engineers on utilizing the Cursor AI code editor effectively. The curriculum covers foundational concepts of context inclusion, codebase indexing, and multi-file code transformations. It teaches developers how to write highly optimized prompts to synthesize software architecture and debug legacy systems directly inside the IDE.
## Software Engineering

### AI Tools

#### Claude Code (1)

  - **(2025)** [youtube: The 6 Levels of Claude Code Explained](https://www.youtube.com/watch?v=TUKYbUIXLOE)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive video breakdown analyzing the capabilities of Anthropic's Claude Code interface. Evaluates the progression from basic code generation and syntax correction to advanced multi-file refactoring and semi-autonomous agentic software engineering tasks.

---
💡 **Explore Related:** [AI](./ai.md) | [ChatGPT](./chatgpt.md) | [MLOps](./mlops.md)

