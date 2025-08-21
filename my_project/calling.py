import asyncio
import os
from typing import Any
from pydantic import BaseModel
from agents import Agent, Runner, FunctionTool, InputGuardrail

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "new_api"


# Define data models
class CustomerQuery(BaseModel):
    query_type: str
    details: str
    customer_id: str


class EscalationData(BaseModel):
    issue: str
    customer_id: str
    urgency: str


class QueryResponse(BaseModel):
    response: str
    action_taken: str
    escalation_needed: bool


class InputValidation(BaseModel):
    is_valid: bool
    reason: str


# Tool 1: Fetch customer information
def get_customer_info(customer_id: str) -> dict:
    return {
        "customer_id": customer_id,
        "name": "Sample Customer",
        "location": "Karachi, Pakistan",
        "account_status": "Active",
    }


get_customer_info_tool = FunctionTool(
    name="get_customer_info",
    description="Fetch customer details based on customer ID.",
    params_json_schema={
        "type": "object",
        "properties": {"customer_id": {"type": "string"}},
        "required": ["customer_id"],
    },
    on_invoke_tool=get_customer_info,
)


# Tool 2: Log interaction to CRM
def log_interaction(customer_id: str, query: str, response: str) -> str:
    return f"Interaction logged for customer {customer_id}: Query - {query}, Response - {response}"


log_interaction_tool = FunctionTool(
    name="log_interaction",
    description="Log customer interaction to CRM system.",
    params_json_schema={
        "type": "object",
        "properties": {
            "customer_id": {"type": "string"},
            "query": {"type": "string"},
            "response": {"type": "string"},
        },
        "required": ["customer_id", "query", "response"],
    },
    on_invoke_tool=log_interaction,
)


# Tool 3: Escalate issue to supervisor
def escalate_issue(issue: str, customer_id: str, urgency: str) -> str:
    return (
        f"Issue '{issue}' escalated for customer {customer_id} with {urgency} urgency."
    )


escalate_issue_tool = FunctionTool(
    name="escalate_issue",
    description="Escalate complex issue to supervisor.",
    params_json_schema={
        "type": "object",
        "properties": {
            "issue": {"type": "string"},
            "customer_id": {"type": "string"},
            "urgency": {"type": "string"},
        },
        "required": ["issue", "customer_id", "urgency"],
    },
    on_invoke_tool=escalate_issue,
)


# Guardrail to validate input
async def validate_input(ctx: Any, input_text: str) -> InputValidation:
    if len(input_text.strip()) < 5:
        return InputValidation(is_valid=False, reason="Input too short.")
    if any(word in input_text.lower() for word in ["abuse", "threat"]):
        return InputValidation(
            is_valid=False, reason="Inappropriate language detected."
        )
    return InputValidation(is_valid=True, reason="Input valid.")


# Define agents
query_handler_agent = Agent(
    name="QueryHandler",
    instructions="Handle customer queries politely for a BPO in Pakistan. Fetch customer data, log interactions, and escalate complex issues. Use culturally appropriate language (e.g., 'Assalamualaikum' for greetings).",
    tools=[get_customer_info_tool, log_interaction_tool, escalate_issue_tool],
    output_type=QueryResponse,
)

guardrail_agent = Agent(
    name="GuardrailAgent",
    instructions="Validate incoming customer queries for appropriateness.",
    output_type=InputValidation,
    # guardrails=[InputGuardrail(validate_input)],
)

triage_agent = Agent(
    name="TriageAgent",
    instructions="Route customer queries to the query handler after validation. If invalid, respond with the reason.",
    handoffs=[query_handler_agent],
    # guardrails=[guardrail_agent],
)


# Main execution
async def main():
    customer_input = "Assalamualaikum, my order #12345 hasn't arrived. Can you check?"
    result = await Runner.run(triage_agent, input=customer_input)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
