# 🌦️ Weather Agent with Gemini & OpenWeatherMap

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Made with UV](https://img.shields.io/badge/Package%20Manager-uv-orange)](https://github.com/astral-sh/uv)
[![OpenWeatherMap API](https://img.shields.io/badge/API-OpenWeatherMap-lightgrey)](https://openweathermap.org/)
[![Gemini API](https://img.shields.io/badge/API-Gemini-blueviolet)](https://ai.google.dev/)

A simple weather assistant powered by a Gemini 2.0 model and OpenWeatherMap API, designed with the `agents` framework and asynchronous OpenAI client. This tool retrieves real-time weather information using city names and provides a natural-language interface.

---

## 🚀 Features

- 🔍 Ask for weather in any city
- 🤖 Powered by Google's Gemini 2.0 (Flash variant)
- 🌐 Uses OpenWeatherMap API
- 🛠 Built with `agents`, `uv`, `requests`, and `openai`

---

## 🧰 Requirements

- Python 3.10+
- API Keys for:
  - OpenWeatherMap
  - Gemini (via Google Generative Language API)

---

## 📦 Installation

This project uses [uv](https://github.com/astral-sh/uv) for package management. To get started:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone this repository
git clone https://github.com/HarrisMuhammad/learning-agentic-ai.git
cd  learning-agentic-ai/gemini_api/weather-update



# Install dependencies
uv pip install -r requirements.txt
```

## 🔐 Environment Setup

Create a .env file in the root directory:

```bash
gemini_api=your_google_generative_ai_api_key
open_weather_api=your_openweathermap_api_key
```

## 🧪 Usage

Run the script with:

```bash
python main.py
```

## Expected output (example):
```pqsql
The current weather in Peshawar is 29°C with clear sky.
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋‍♂️ Acknowledgements

    OpenAI

    OpenWeatherMap

    Google AI

    astral-sh/uv
