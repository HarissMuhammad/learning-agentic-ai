# Streaming Demo For OpenAI Agents

This demo showcases the streaming capabilities of OpenAI agents using the `agent_sdk` library, built with [Streamlit](https://streamlit.io/). It allows you to interact with an OpenAI-powered agent and see real-time streamed responses.

## Features

- **Live Streaming**: See agent responses as they are generated.
- **Customizable Agent**: Set agent name, instructions, and select from multiple models.
- **Prompt Selection**: Choose from demo prompts or enter your own.
- **Easy UI**: Built with Streamlit for a simple, interactive experience.

## Setup

1. **Clone the repository** 
    ```bash
    git clone https://github.com/HarissMuhammad/learning-agentic-ai.git 
    ```
2. **create Virtual Environment**

    ```bash
        uv venv
        #to activate on linux
        source .venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    uv pip install -e .
    ```

3. **Set your OpenAI API key**:
    - Create a `.env` file in the project root:
      ```
      OPENAI_API_KEY=your_openai_api_key_here
      ```

4. **Run the app using uv**:
    ```bash
    uv run python run streamlit run streaming_demo.py
    ```

## Usage

- Configure the agent in the sidebar (name, instructions, model).
- Select a demo prompt or enter your own.
- Click **Send** to generate a streamed response.
- Use the **Clear** button to reset.

## File Structure

- `streaming_demo.py` — Main Streamlit app for the demo.

## Requirements

- Python 3.8+
- `streamlit`
- `python-dotenv`
- `agent_sdk` (custom library)
- `openai`

## Screenshot

![Streaming Demo Screenshot](screenshot.png)

## License

MIT License

---

Made with AI 🤖