from agents import Agent
from agents import Runner
from dotenv import load_dotenv
import os
from agents import GuardrailFunctionOutput
from pydantic import BaseModel
import asyncio


load_dotenv()
key = os.getenv("new_api")

class HomeworkOutput(BaseModel):
    is_homework : bool
    reasoning : str
    

guardrail_agent = Agent(
    name = "Guardrail Check",
    instructions="Check if the user is asking about the homework.",
    output_type=HomeworkOutput
)

async def function_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent,input_data, context=ctx.context)
    final_output = 

math_agent = Agent(
    name="Math Tutor",
    handoff_description="Math Tutor is an agent that helps users with math problems.",
    instructions="You proivide help to the user with math problems.",
)

history_agent = Agent(
    name="History Tutor",
    handoff_description="History Tutor is an agent that helps users with history problems.",
    instructions="You provide help to the user with history problems.",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent is best suited to help the user based on their request. If the request is about math, hand it off to Math Tutor. If it's about history, hand it off to History Tutor. If it's about something else, inform the user that you cannot help them.",
    handoffs=[history_agent, math_agent],
)


async def main():
    result = await Runner.run(triage_agent, "Can you help me with a math problem?")
    print(result.final_output)
