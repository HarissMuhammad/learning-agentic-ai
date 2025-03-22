import os
import google.generativeai as genai
from dotenv import load_dotenv


def main():
    """Load the .env file"""
    load_dotenv()

    """retrieve the api key in a variable"""
    api_key = os.getenv("gemini_api")

    """cofigure"""
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Hi")

    """print the response"""
    print(response.text)


if __name__ == "__main__":
    main()
