# EMA Hybrid Agent Workflow Demo

This project demonstrates a hybrid AI workflow using:

- Azure Functions
- Azure OpenAI
- deterministic tools
- an LLM-based decision agent

The demo simulates an entity resolution process for organizations.

## Workflow

HTTP request
↓
normalize_address (deterministic tool)
↓
registry_lookup (deterministic tool)
↓
resolution_agent (Azure OpenAI)
↓
decision (MATCH / REVIEW / NEW_RECORD)

## Example result

The system can resolve an organization against a registry of candidates.

Example:

Input:
- Organization: Pfizer SA
- Address: Boulevard de la Plaine 17

Output:
- MATCH → org-001

## Tech stack

- Python
- Azure Functions
- Azure OpenAI
- LLM reasoning
- hybrid workflow architecture

## Run locally

```bash
pip install -r requirements.txt
func start

Current Status

The current implementation demonstrates the hybrid workflow logic with deterministic tools and an LLM-based resolution agent.

For now, the workflow orchestration is implemented using a simple Python orchestrator.

HTTP Trigger
↓
Entity Extraction Agent
↓
normalize_address (tool)
↓
registry_lookup (tool)
↓
resolution_agent (LLM)
↓
decision

