# 🧠 Gemini Image Analysis with Python

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow.svg)](LICENSE)
[![API: Google Generative AI](https://img.shields.io/badge/API-Gemini--2.0--Flash-blueviolet)](https://ai.google.dev/)

This project uses **Google Gemini 2.0 Flash** to analyze an image and generate a descriptive response in natural language. It downloads an image, passes it with a prompt to the Gemini API, and prints the response.

---

## 📸 Example Image Used

![Example Image](https://hips.hearstapps.com/hmg-prod/images/2022-ford-mustang-shelby-gt500-02-1636734552.jpg)

---

## 🚀 Features

- 🧠 Leverages Google's multimodal `gemini-2.0-flash` model
- 📷 Image + Text prompt input
- 💬 Text-based natural language description output

---
## 📥 Getting Started
1. Clone the Repository
```bash
git clone https://github.com/HarrisMuhammad/learning-agentic-ai.git
cd  learning-agentic-ai/gemini_api/usage/Image_Analyst

```

## 🧰 Requirements

- Python 3.10+
- Google Generative AI API key (Gemini)
- `google-generativeai`, `python-dotenv`, `Pillow` libraries

---

## 📦 Installation

```bash
# Install required libraries
pip install google-generativeai python-dotenv Pillow
```

## 🔐 Setup

Create a .env file in the project root:
```bash
gemini_api=your_google_generative_ai_api_key
```

## 🧪 Usage
Run the Script:
```bash
image.ipynb
```
## Expected output:

This image contains a high-performance sports car, specifically a 2022 Ford Mustang Shelby GT500...

## 🙌 Acknowledgements

    Google Generative AI

    Pillow

    dotenv
