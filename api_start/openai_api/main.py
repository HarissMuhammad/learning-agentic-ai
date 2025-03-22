import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("test")


client = openai.OpenAI(api_key=api_key)


def get_llm_response(prompt):
    response = client.chat.completions.create(  # Not "openai.chat.completions.create"
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content


print(get_llm_response("Hi!"))
