import asyncio
from datetime import datetime
import json
import os
import re
from typing import Dict, List, Tuple
from src.gemini_utils import call_gemini_with_retry, normalize_url
from src.logger import log_event
from src.mandate_ingestor import get_system_mandates

# Memory file to store resolved debates
DEBATE_MEMORY_FILE = "src/memory/health_learning.json"

async def run_debate_protocol(item: Dict, is_new_link: bool = False) -> Tuple[int, List[str], str, Dict]:
    """
    Executes a Multi-Agent Consensus & Debate Protocol for borderline resources.
    The panel of experts consists of:
    1. Security Architect (Vulnerabilities, Licensing, Supply-Chain)
    2. Cloud Native SRE (Production readiness, Scalability, Community activity)
    3. AI Platform Engineer (Developer experience, Agentic integrations)
    
    Returns:
        final_score: Resolved impact score (0-100)
        verified_tags: Consensus tags
        refined_summary: Refined high-density technical summary
        debate_data: Logs and details of the debate
    """
    url = item.get("url", "")
    title = item.get("title", "Unknown Resource")
    desc = item.get("description", item.get("ai_summary", ""))
    tags = item.get("tags", [])
    initial_score = item.get("impact_score", item.get("stars", 3) * 20) # Fallback mapping if stars is used
    
    log_event(f"  [⚖️] DEBATE TRIGGERED: '{title}' (Initial Score: {initial_score})", section_break=False)
    
    system_mandates = get_system_mandates()
    
    # 1. Independent Evaluation Round
    personas = {
        "Security Architect": "Focus on licensing (MIT/Apache vs BSL/SSPL), supply chain security, access control, vulnerabilities, and enterprise compliance.",
        "Cloud Native SRE": "Focus on high-availability, scalability, production maturity, operational complexity, community health, and performance metrics.",
        "AI Platform Engineer": "Focus on developer agility, tooling simplicity, AI stack integration (MCP, LLMs, agents), and 2026 architectural relevance."
    }
    
    scores = {}
    justifications = {}
    
    async def evaluate_persona(name: str, focus: str) -> Tuple[int, str]:
        prompt = (
            f"You are the Nubenetes {name}.\n"
            f"Your perspective: {focus}\n\n"
            f"{system_mandates}\n\n"
            f"Evaluate the following resource:\n"
            f"- Title: {title}\n"
            f"- URL: {url}\n"
            f"- Context: {desc}\n"
            f"- Proposed Tags: {tags}\n\n"
            "Assign an architectural impact score (0 to 100) and write a 1-2 sentence technical justification.\n"
            "Respond ONLY in valid JSON format: {\"score\": int, \"justification\": \"string\"}"
        )
        try:
            res = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role=f"Debater-{name.replace(' ', '')}")
            score = min(max(int(res.get("score", 50)), 0), 100)
            justification = res.get("justification", "No justification provided.")
            return score, justification
        except Exception as e:
            log_event(f"    [!] Persona {name} evaluation failed: {e}")
            return int(initial_score), "Failed to evaluate."

    # Run evaluations in parallel
    eval_tasks = [evaluate_persona(name, focus) for name, focus in personas.items()]
    eval_results = await asyncio.gather(*eval_tasks)
    
    for idx, (name, _) in enumerate(personas.items()):
        scores[name], justifications[name] = eval_results[idx]
        log_event(f"    [>] {name} rated: {scores[name]} (Justification: {justifications[name]})")
        
    # Check divergence: if max diff >= 15 points, run a debate round
    max_score = max(scores.values())
    min_score = min(scores.values())
    divergence = max_score - min_score
    
    debate_transcript = []
    
    if divergence >= 15:
        log_event(f"    [⚖️] Divergence detected ({divergence} points). Starting Debate Round...")
        
        async def run_rebuttal(name: str, focus: str) -> Tuple[int, str]:
            opponent_views = "\n".join([f"- {other}: Score {scores[other]} | Justification: {justifications[other]}" for other in personas if other != name])
            prompt = (
                f"You are the Nubenetes {name}.\n"
                f"Your perspective: {focus}\n\n"
                "The panel of experts disagrees on this resource. Here are the other views:\n"
                f"{opponent_views}\n\n"
                f"Resource details:\n"
                f"- Title: {title}\n"
                f"- URL: {url}\n"
                f"- Context: {desc}\n\n"
                "Reconsider your evaluation. You can either defend your initial score or adjust it.\n"
                "Respond ONLY in valid JSON format: {\"score\": int, \"rebuttal\": \"1-2 sentence response to other experts\"}"
            )
            try:
                res = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role=f"Debate-Rebuttal-{name.replace(' ', '')}")
                new_score = min(max(int(res.get("score", scores[name])), 0), 100)
                rebuttal = res.get("rebuttal", "No rebuttal provided.")
                return new_score, rebuttal
            except Exception as e:
                log_event(f"    [!] Persona {name} rebuttal failed: {e}")
                return scores[name], "No rebuttal provided."
        
        rebuttal_tasks = [run_rebuttal(name, focus) for name, focus in personas.items()]
        rebuttal_results = await asyncio.gather(*rebuttal_tasks)
        
        for idx, (name, _) in enumerate(personas.items()):
            scores[name], rebuttal = rebuttal_results[idx]
            debate_transcript.append(f"{name} (Score {scores[name]}): {rebuttal}")
            log_event(f"    [>] {name} revised rating to {scores[name]}. Rebuttal: {rebuttal}")
            
    # Compute Final Consensus
    final_score = int(sum(scores.values()) / len(scores))
    log_event(f"    [🏁] Consensus Score reached: {final_score}")
    
    # 2. Refined Curation/Tags Round
    refine_prompt = (
        "You are the Nubenetes Curation Synthesis Agent (2026).\n"
        f"Combine the following multi-agent expert reviews into a final technical decision.\n\n"
        f"Resource Title: {title}\n"
        f"URL: {url}\n"
        f"Consensus Score: {final_score}\n"
        f"Security Architect Score: {scores['Security Architect']} | Justification: {justifications['Security Architect']}\n"
        f"Cloud Native SRE Score: {scores['Cloud Native SRE']} | Justification: {justifications['Cloud Native SRE']}\n"
        f"AI Platform Engineer Score: {scores['AI Platform Engineer']} | Justification: {justifications['AI Platform Engineer']}\n\n"
        "Generate a final, high-density, professional technical summary (2-5 sentences, HSL-themed style, no generic statements).\n"
        "Select the appropriate subset of tags from: [DE FACTO STANDARD], [ENTERPRISE-STABLE], [EMERGING], [GUIDE], [CASE STUDY], [COMMUNITY-TOOL], [LEGACY].\n"
        "Respond ONLY in valid JSON format: {\"summary\": \"refined summary...\", \"tags\": [\"...\"]}"
    )
    
    refined_summary = desc
    final_tags = tags
    try:
        res = await call_gemini_with_retry(refine_prompt, prefer_flash=False, use_grounding=False, role="Debate-Synthesis")
        refined_summary = res.get("summary", desc)
        final_tags = res.get("tags", tags)
    except Exception as e:
        log_event(f"    [!] Error during debate synthesis: {e}")
        
    debate_data = {
        "url": url,
        "title": title,
        "initial_score": initial_score,
        "final_consensus_score": final_score,
        "scores": scores,
        "justifications": justifications,
        "rebuttals": debate_transcript,
        "timestamp": datetime.now().isoformat()
    }
    
    # Persist the resolved debate to memory log (Mandate 3.1)
    try:
        memory_data = {}
        if os.path.exists(DEBATE_MEMORY_FILE):
            try:
                memory_data = json.load(open(DEBATE_MEMORY_FILE, "r"))
            except: pass
        
        memory_data.setdefault("resolved_debates", {})[normalize_url(url)] = debate_data
        
        # Keep blacklist and other fields intact
        with open(DEBATE_MEMORY_FILE, "w") as f:
            json.dump(memory_data, f, indent=2)
    except Exception as e:
        log_event(f"    [!] Failed to persist debate memory: {e}")
        
    return final_score, final_tags, refined_summary, debate_data
