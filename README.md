# LLM-Agent_Insuranc_Workflow
LLM Agents for Insurance Workflows Project (LangChain + LangGraph)

### Architecture Overview

```
User Query → Supervisor Agent (router)
                ├── Claims Triage Agent (extract claim details, assess urgency, recommend next steps)
                ├── Policy Issuance Agent (collect risk data, underwrite, generate policy PDF)
                ├── Customer Onboarding Agent (KYC checks, data collection, risk profile)
                └── Document Processing Agent (classify & extract info from insurance documents)
```

Each agent is a LangGraph node that can call insurance-specific tools. State is shared across agents using a typed InsuranceState. The supervisor uses an LLM to route to the correct agent, then the agent executes its workflow and returns results.


### Project Structure

```
insurance_llm_agents/
├── requirements.txt
├── main.py                 # Entry point: CLI or interactive demo
├── state.py                # Pydantic state models
├── tools.py                # Mock insurance tools (OCR, risk, KYC, etc.)
├── agents.py               # Agent nodes (LangGraph functions)
├── workflow.py             # LangGraph workflow assembly
└── README.md
```
