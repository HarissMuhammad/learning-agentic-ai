# 💬 Gemini CLI Chatbot

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![API: Gemini 2.0 Flash](https://img.shields.io/badge/API-Gemini--2.0--Flash-blueviolet)](https://ai.google.dev/)

An interactive command-line chatbot built using **Google Gemini 2.0 Flash**, capable of generating rich, philosophical, and poetic responses. This tool allows users to chat with the model and outputs both the conversation history and additional creative content.

---

## 🧠 Features

- Chat with the Gemini 2.0 Flash model in real-time
- Configurable generation temperature and max output
- Automatically loads API keys from `.env`
- Prints:
  - Model's response
  - Chat history
  - Thought-provoking philosophical insights and poetry

---

## 📥 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name
```

### 🧰 Requirements

    Python 3.10+

    Google Generative AI API Key

    Python packages:

        google-generativeai

        python-dotenv

### 📦 Installation
```bash
pip install google-generativeai python-dotenv
```

### 🔐 Setup

Create a .env file in the project root:
```bash
gemini_api=your_gemini_api_key
```
### 🧪 Usage
    Open the notebook (e.g., Gemini_Chatbot.ipynb) in Jupyter.

    Ensure the environment variable is loaded from .env.

    Execute each cell step by step.

    In the input prompt, type your message and receive a model response.

    Enjoy the included philosophical and poetic responses.

### 🧾 Sample Outputs
💡 Philosophical Insight

    Liberalism's emphasis on individual rights can erode social cohesion...

✨ Poetic Reflection

    The lines on maps, drawn sharp and bold,
    A story whispered, bought and sold...
    Let’s see the human, not the flag,
    And tear the pages of the brag.

### 🛡 License

MIT © HarrisMuhammad

### 🙏 Acknowledgements

    Google Generative AI

    Pillow

    python-dotenv
