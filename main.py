```python
from workflow import insurance_workflow
from state import InsuranceState

def run_insurance_agent(user_input: str):
    state = InsuranceState(messages=[{"role": "user", "content": user_input}])
    result = insurance_workflow.invoke(state)
    print("\n🤖 Agent Response:\n")
    print(result.get("final_output", "No output generated."))
    # Optionally print structured data
    if result.get("claims"):
        print("\n📋 Claim Details:", result["claims"].json(indent=2))
    if result.get("policy"):
        print("\n📄 Policy Details:", result["policy"].json(indent=2))
    if result.get("onboarding"):
        print("\n👤 Onboarding:", result["onboarding"].json(indent=2))
    if result.get("document"):
        print("\n📑 Document Result:", result["document"].json(indent=2))
    print("-" * 50)

if __name__ == "__main__":
    print("🏦 Insurance LLM Agent System (mock tools)")
    print("Type 'quit' to exit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break
        run_insurance_agent(user_input)
```
