---
description: "Top AI Agents MCP resources for 2026, AI-ranked: vLLM on Kubernetes, LocalAI and more — curated Cloud Native tools, guides and references."
---
# AI Agents and Model Context Protocol (MCP) for Kubernetes

!!! tip "Nubenetes V2 Elite Portal"
    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/ai-agents-mcp/).

!!! info "Architectural Context"
    Detailed reference for AI Agents and Model Context Protocol (MCP) for Kubernetes in the context of AI.

## AI Infrastructure

### Distributed Computing

#### Kube-Ray

  - **(2025)** [Kube-Ray](https://github.com/ray-project/kuberay) <span class='md-tag md-tag--info'>⭐ 2541</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-2471d9c8" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 12 L 10 11 L 20 3 L 30 12 L 40 5 L 50 4" fill="none" stroke="url(#spark-grad-2471d9c8)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="4" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An open-source Kubernetes Operator enabling the deployment and management of Ray clusters. Live Grounding: Serves as the backbone for distributed machine learning workloads on Kubernetes, abstracting compute node scaling, memory configuration, and actor scheduling.
### LLM Serving

#### LocalAI

  - **(2025)** [**LocalAI**](https://github.com/mudler/LocalAI) <span class='md-tag md-tag--info'>⭐ 46845</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-ea9eeb00" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 7 L 10 3 L 20 12 L 30 7 L 40 12 L 50 5" fill="none" stroke="url(#spark-grad-ea9eeb00)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[GO CONTENT]</span> 🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: A self-hosted, community-first OpenAI-compatible API gateway running on local hardware. Live Grounding: Allows developers to host LLMs, audio-to-text, and image generation services inside Kubernetes without external data dependencies, optimized for consumer-grade and enterprise hardware.
#### vLLM

  - **(2025)** [==vLLM on Kubernetes==](https://github.com/vllm-project/vllm) <span class='md-tag md-tag--info'>⭐ 82816</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-6caed060" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 9 L 10 7 L 20 6 L 30 7 L 40 10 L 50 5" fill="none" stroke="url(#spark-grad-6caed060)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> 🌟🌟🌟🌟🌟 <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Curator Insight: Integration guides and deployment schemas for hosting vLLM on Kubernetes clusters. Live Grounding: Standardizes memory-efficient LLM serving using PagedAttention. Features rapid integration with Kubernetes HPA (Horizontal Pod Autoscaler) and native Prometheus performance scraping.
## Cloud Native Operations

### AI AIOps

#### Kubernetes Troubleshooting

  - **(2025)** [HolmesGPT (Robusta)](https://github.com/HolmesGPT/holmesgpt) <span class='md-tag md-tag--info'>⭐ 2623</span> <svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend"><defs><linearGradient id="spark-grad-892577ed" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" /><stop offset="100%" stop-color="var(--md-accent-fg-color)" /></linearGradient></defs><path class="v2-sparkline-path" d="M 0 5 L 10 5 L 20 6 L 30 13 L 40 13 L 50 5" fill="none" stroke="url(#spark-grad-892577ed)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /><circle cx="50" cy="5" r="2" fill="var(--md-accent-fg-color)" /></svg> <span class='md-tag md-tag--warning'>[PYTHON CONTENT]</span> <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span> 🌟🌟 <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Curator Insight: An AI-driven troubleshooting assistant for Kubernetes clusters by Robusta. Live Grounding: Utilizes LLM agents to autonomously parse Prometheus alerts, collect pod logs, inspect live status, and deliver actionable remediation steps for infrastructure incidents.

---
💡 **Explore Related:** [MLOps](./mlops.md) | [AI](./ai.md) | [ChatGPT](./chatgpt.md)

🔗 **See Also:** [Kubernetes Backup Migrations](./kubernetes-backup-migrations.md) | [OCP 4](./ocp4.md)

