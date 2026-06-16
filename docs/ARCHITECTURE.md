# Architecture

## Workflow
1. Job Discovery (src/job_discovery.py)
2. Tailoring (src/resume_tailor.py + LLM)
3. Tracking (src/tracker.py)
4. Application (future: Playwright)

Extend with CrewAI/LangGraph for agents.