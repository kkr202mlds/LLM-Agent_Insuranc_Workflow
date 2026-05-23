# LLM-Agent_Insuranc_Workflow
LLM Agents for Insurance Workflows Project (LangChain + LangGraph)

Architecture Overview

```
User Query → Supervisor Agent (router)
                ├── Claims Triage Agent (extract claim details, assess urgency, recommend next steps)
                ├── Policy Issuance Agent (collect risk data, underwrite, generate policy PDF)
                ├── Customer Onboarding Agent (KYC checks, data collection, risk profile)
                └── Document Processing Agent (classify & extract info from insurance documents)
```
