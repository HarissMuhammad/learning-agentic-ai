from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
import streamlit as st
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

st.set_page_config(
    page_title="Streaming Demo For OpenAI Agents",
    page_icon=":guardsman:",  # Add a page icon (optional)
    layout="wide",  # Choose the layout (wide or centered)
)

st.title("Streaming Demo For OpenAI Agents")
st.write(
    "This demo showcases the streaming capabilities of OpenAI agents using the `agent_sdk` library."
)

with st.sidebar:
    st.header("Agent Configuration")
    Agent_name = st.text_input("Enter Agent Name", "Thoughtful Agent")
    Agent_instructions = st.text_area(
        "Enter Agent Instructions", "You are a helpful agent with thoughtful responses."
    )

    models = ["gpt-3.5-mini", "gpt-4o-mini", "gpt-o3-mini"]

    selected_model = st.selectbox("Model", models, index=1)

    demo_options = [
        "Give me 5 quotes regarding existence with purpose",
        "what is a lofty spirit?",
        "What is the source of drive for a persons life? ",
        "Give me 5 verses of Quran that speak against pragmatism",
    ]

demo_prompts = st.selectbox("Select a Demo Prompt", demo_options)

st.markdown("---")
st.markdown("Made with AI")

user_input = st.text_area("Enter your prompt here:", value=demo_prompts, height=100)
send_button = st.button("Send", type="primary")

response_container = st.container()


async def stream_response(agent: Agent, user_input: str) -> None:
    response_parts = ""
    try:
        result = Runner.run_streamed(agent, input=user_input)
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(
                event.data, ResponseTextDeltaEvent
            ):
                print(event.data.delta)
                response_parts += event.data.delta
            message_placeholder.markdown(response_parts + "▌")
            message_placeholder.markdown(response_parts)
    except Exception as e:
        st.error(f"An Error occurred {e}")


if send_button and user_input:
    agent = Agent(Agent_name, Agent_instructions, model=selected_model)

    with response_container:
        message_placeholder = st.empty()

        with st.spinner("Generating response..."):
            asyncio.run(stream_response(agent, user_input))

        if st.button("clear"):
            st.rerun()

if not send_button:
    with response_container:
        st.info("Please enter a prompt and click 'Send' to generate a response.")
        st.markdown(
            """  ### Tips:
        - Choose from the quick prompts or enter your own
        - Try complex prompts to see how the agent responds in real-time
        """
        )
