from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool
from openai import AsyncOpenAI
import requests
from dotenv import get_key, find_dotenv


gemini_api_key = get_key(find_dotenv(), "gemini_api")
openweather_key = get_key(find_dotenv(), "open_weather_api")


client = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api_key,
)


@function_tool
def get_weather(city: str) -> str:
    """Gets the current weather for a city using OpenWeatherMap."""
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_key}&units=metric"
    )

    if response.status_code != 200:
        return f"Failed to get weather data for {city}. Error: {response.status_code}"

    data = response.json()

    temp_c = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The current weather in {city} is {temp_c}°C with {description}."


model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client)


agent = Agent(
    name="Weather Agent",
    instructions="You are helpful weather assitant",
    model=model,
    tools=[get_weather],
)

result = Runner.run_sync(agent, "What is the weather like in peshawar,kpk")
print(result.final_output)
