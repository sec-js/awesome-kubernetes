# AI Agents and Model Context Protocol (MCP) for Kubernetes

!!! info "Architectural Context"
    Detailed reference for AI Agents and Model Context Protocol (MCP) for Kubernetes in the context of AI.

## Standard Reference

  - [IBM IAM for AI Agents](https://t.co/EKsVgKA4xn)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>
  - [PulseMCP](https://pulsemcp.com)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span>

## AI Engineering

### AI Agents

#### Web Automation

  - **(2025)** [==Skyvern==](https://github.com/Skyvern-ai/Skyvern) <span class='md-tag md-tag--info'>⭐ 21899</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: An AI-powered web browser automation agent designed to extract data and execute workflows on complex interfaces. Live Grounding: Translates plain-text instructions into resilient selenium-style interactions, dynamically adapting to DOM mutations and bypassing rigid selector patterns.
### Model Context Protocol

#### Architecture

  - **(2024)** [anthropic.com: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Anthropic's release document introducing the Model Context Protocol (MCP), an open-standard protocol enabling LLM agents to securely interact with external tools and data sources. MCP standardizes the JSON-RPC interface between hosts and servers, resolving the integration fragmentation that previously plagued generative AI integrations and agentic workflows.
#### Awesome Lists

  - **(2025)** [==Awesome MCP Servers==](https://github.com/punkpeye/awesome-mcp-servers) <span class='md-tag md-tag--info'>⭐ 89112</span> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: A community-curated collection of servers implementing the Model Context Protocol. Live Grounding: Aggregates verified integrations linking AI models to tools like relational databases, enterprise APIs, version control providers, and local execution runtimes.
#### Developer Experience

  - **(2025)** [MCPBundles](https://www.mcpbundles.com) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — MCPBundles is a discovery and packaging platform designed to bundle various Model Context Protocol servers for rapid deployment. It simplifies agentic application building by providing curated, pre-configured groupings of tools (e.g., database drivers, git utilities, API endpoints) that can be integrated into AI hosts in a single setup operation.
#### Google Cloud

  - **(2025)** [Google Cloud Managed MCP](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-managed-mcp-for-gemini) <span class='md-tag md-tag--warning'>[NONE CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Google Cloud's managed solution for Model Context Protocol, allowing enterprise Gemini models to safely interact with local data sources and external enterprise systems. By hosting and scaling MCP servers inside Google's managed environment, it minimizes operational overhead while securing transactional agentic workflows with native cloud IAM.
#### Official Servers

  - **(2025)** [==GitHub MCP Server==](https://github.com/modelcontextprotocol/servers) <span class='md-tag md-tag--info'>⭐ 87194</span> <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Primary collection of production-grade Model Context Protocol (MCP) servers. Live Grounding: Establishes development standards for JSON-RPC 2.0 based message exchange between host agents and enterprise backend systems.
#### Specifications

  - **(2025)** [modelcontextprotocol.io: MCP Official Documentation](https://modelcontextprotocol.io/docs/getting-started/intro) <span class='md-tag md-tag--warning'>[TYPESCRIPT CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — The official technical documentation and specifications for the Model Context Protocol (MCP). It provides comprehensive blueprints for implementing client-server architectures, defining standard JSON-RPC 2.0 schemas for prompt execution, resource exploration, and tool binding. Serves as the authoritative source for developers building LLM integrations.
## AI Infrastructure

### Distributed Computing

#### Kube-Ray

  - **(2025)** [Kube-Ray](https://github.com/ray-project/kuberay) <span class='md-tag md-tag--info'>⭐ 2541</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An open-source Kubernetes Operator enabling the deployment and management of Ray clusters. Live Grounding: Serves as the backbone for distributed machine learning workloads on Kubernetes, abstracting compute node scaling, memory configuration, and actor scheduling.
### Hardware Orchestration

#### NVIDIA Operators

  - **(2025)** [NVIDIA GPU Operator](https://github.com/NVIDIA/gpu-operator) <span class='md-tag md-tag--info'>⭐ 2739</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: Kubernetes operator designed to automate the management of NVIDIA software components on nodes. Live Grounding: Provisions GPU drivers, container runtimes, device plug-ins, and monitoring tools automatically, ensuring consistent access to hardware acceleration.
### LLM Serving

#### LocalAI

  - **(2025)** [**LocalAI**](https://github.com/mudler/LocalAI) <span class='md-tag md-tag--info'>⭐ 46845</span> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: A self-hosted, community-first OpenAI-compatible API gateway running on local hardware. Live Grounding: Allows developers to host LLMs, audio-to-text, and image generation services inside Kubernetes without external data dependencies, optimized for consumer-grade and enterprise hardware.
#### vLLM

  - **(2025)** [==vLLM on Kubernetes==](https://github.com/vllm-project/vllm) <span class='md-tag md-tag--info'>⭐ 82816</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Integration guides and deployment schemas for hosting vLLM on Kubernetes clusters. Live Grounding: Standardizes memory-efficient LLM serving using PagedAttention. Features rapid integration with Kubernetes HPA (Horizontal Pod Autoscaler) and native Prometheus performance scraping.
## Cloud Native Operations

### AI AIOps

#### Kubernetes Troubleshooting

  - **(2025)** [HolmesGPT (Robusta)](https://github.com/HolmesGPT/holmesgpt) <span class='md-tag md-tag--info'>⭐ 2623</span> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An AI-driven troubleshooting assistant for Kubernetes clusters by Robusta. Live Grounding: Utilizes LLM agents to autonomously parse Prometheus alerts, collect pod logs, inspect live status, and deliver actionable remediation steps for infrastructure incidents.
## Developer Experience (1)

### AI-Assisted Coding

#### Claude Code

  - **(2025)** [==Claude Code Best Practice==](https://github.com/shanraisshan/claude-code-best-practice) <span class='md-tag md-tag--info'>⭐ 57660</span> <span class='md-tag md-tag--warning'>[MARKDOWN CONTENT]</span> <span class='md-tag md-tag--primary'>[GUIDE]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Curator Insight: Curated collection of best practices, system prompts, and architecture layouts for Claude Code. Live Grounding: Explores advanced CLI-driven agent workflows, highlighting configuration optimizations, shell integration strategies, and secure execution configurations in local and remote environments.
## Software Engineering

### AI Tools

#### Claude Code (1)

  - **(2025)** [youtube: The 6 Levels of Claude Code Explained](https://www.youtube.com/watch?v=TUKYbUIXLOE)  <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A deep-dive video breakdown analyzing the capabilities of Anthropic's Claude Code interface. Evaluates the progression from basic code generation and syntax correction to advanced multi-file refactoring and semi-autonomous agentic software engineering tasks.

---
💡 **Explore Related:** [AI](./ai.md) | [MLOps](./mlops.md) | [ChatGPT](./chatgpt.md)

