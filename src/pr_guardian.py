import os
import asyncio
from github import Github
from src.config import GH_TOKEN, TARGET_REPO
from src.gemini_utils import call_gemini_with_retry

async def analyze_pr_diff(diff_text: str) -> str:
    prompt = f"""
    You are the Nubenetes PR Guardian. Analyze this PR diff against the Nubenetes GEMINI.md mandates.
    Check for:
    1. Are new links added using the high-density description standard? (No generic clickbait)
    2. Are URLs normalized? (No tracking params)
    3. Are there emojis in H2/H3 titles? (Should be rejected)
    
    If the PR looks good, say '✅ PR Meets Nubenetes Standards.'
    If it violates mandates, list the violations clearly so the contributor can fix them.
    
    PR Diff:
    {diff_text}
    """
    try:
        response = await call_gemini_with_retry(prompt, prefer_flash=True)
        return str(response)
    except Exception as e:
        return f"⚠️ Guardian AI temporarily unavailable: {e}"

def main():
    pr_number = os.getenv("PR_NUMBER")
    if not pr_number:
        print("No PR_NUMBER provided.")
        return

    g = Github(GH_TOKEN)
    repo = g.get_repo(TARGET_REPO)
    pr = repo.get_pull(int(pr_number))

    # We don't want to comment repeatedly on the same commit
    # So we check if we already commented
    bot_signature = "<!-- PR_GUARDIAN_SIGNATURE -->"
    for comment in pr.get_issue_comments():
        if bot_signature in comment.body:
            print("Already commented on this PR.")
            # Optional: update the comment or just exit
            return

    # Get PR diff
    diff_url = pr.diff_url
    import httpx
    diff_text = httpx.get(diff_url).text

    # Skip if too huge or not markdown
    if len(diff_text) > 50000:
        return
        
    analysis = asyncio.run(analyze_pr_diff(diff_text))
    
    final_comment = f"{bot_signature}\n### 🛡️ Nubenetes PR Guardian\n\n{analysis}"
    pr.create_issue_comment(final_comment)
    print("Guardian comment posted.")

if __name__ == "__main__":
    main()
