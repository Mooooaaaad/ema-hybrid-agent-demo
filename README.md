# EMA Hybrid Agent Workflow Demo

This project demonstrates a hybrid AI workflow using:

- Azure Functions
- Azure OpenAI
- deterministic tools
- an LLM-based decision agent
- Microsoft Agent Framework (MAF)

The demo simulates an entity resolution process for organizations.

---

## Workflow

HTTP request  
↓  
MAF Workflow Orchestration  
↓  
NormalizeAddressExecutor (deterministic tool)  
↓  
RegistryLookupExecutor (deterministic tool)  
↓  
ResolutionExecutor (Azure OpenAI)  
↓  
Decision (MATCH / REVIEW / NEW_RECORD)

---

## Example result

The system can resolve an organization against a registry of candidates.

Example:

Input:
- Organization: Pfizer SA  
- Address: Boulevard de la Plaine 17  

Output:
- MATCH → org-001  

---

## Tech stack

- Python
- Azure Functions
- Azure OpenAI
- Microsoft Agent Framework (MAF)
- LLM reasoning
- Hybrid workflow architecture

---

## Run locally

```bash
pip install -r requirements.txt
func start