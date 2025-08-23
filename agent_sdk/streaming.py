from agents import Agent, Runner
from agents import function_tool
from agents import RunContextWrapper
from agents import handoff
from agents import ItemHelpers
from dotenv import load_dotenv
import asyncio
from pydantic import BaseModel
import os
import time
import random



async def main():

    load_dotenv()
    api_key = os.getenv("API_KEY")

    class ManagerEscalation(BaseModel):
        issue: str  # the issue being escalated
        reason: str  # the reason for escalation


    @function_tool
    def create_ticket(issue: str):
        """Create a ticket for the escalated issue"""
        # Simulate ticket creation
        print(f"Ticket created for issue: {issue}")
        return f"Ticket created successfully ID {random.randint(10000, 99999)}"


    manager_agent = Agent(
        name="Manager Agent",
        handoff_description="Handles Escalated Issues that requires managerial oversight",
        instructions="""
        you handle escalated customer issues that the initial customer service agent could not resolve.
        you will recieve the issue and the reason for escalation if the issue could not be resolved for the 
        customer create a ticket and inform the customer.
        """,
        tools=[create_ticket],
        model="gpt-4o-mini",
    )


    def on_manager_handoff(ctx: RunContextWrapper[None], input: ManagerEscalation):
        print("Escalating to the Manager Agent : \t", input.issue)
        print("Reason For Escalation : \t", input.reason)


    customer_service_agent = Agent(
        name="Customer Service Agent",
        handoff_description="Handles initial customer inquiries and issues",
        instructions="""
        you are the first point of contact for customer inquiries.
        if you cannot resolve the issue, escalate it to the manager agent.
        """,
        model="gpt-4o-mini",
        handoffs=[
            handoff(
                manager_agent,
                input_type=ManagerEscalation,
                on_handoff=on_manager_handoff,
            )
        ],
    )

    result = Runner.run_streamed(
        customer_service_agent, "I need a refund but the website is blank"
    )

    print("___Streaming_ON____\n")

    async for event in result.stream_events():
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            print(f"Current Agent : {event.new_agent.name} \n")
            continue
        elif event.type == "run_item_stream_event":
            event = event.item
            
            if event.type == "tool_call_item":
                print(f"Tool Called  \n")
            if event.type == "tool_call_output_item":
                print(f" -Tool Output {event.output}\n")
            if event.type == "handoff_call_item":
                print(f"handoff initiating from {event.agent.name}\n")
            if event.type == "handoff_output_item":
                time.sleep(0.5)
                print(f"Handoff initiated from: {event.agent.name} \n")
            if event.type == "message_output_item":
                print(f"-- Message Output : {ItemHelpers.text_message_output(event)}\n")
            else:
                pass
    print("____Streaming_OFF____")


asyncio.run(main())