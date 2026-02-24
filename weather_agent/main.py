"""
Weather Agent — Function Calling Example

How it works (3 steps):

  1. You ask: "What's the weather in Lahore?"
  2. The model reads your question and decides:
     "I need to call get_weather with city=Lahore"
  3. We run get_weather("Lahore"), get real data,
     send it back to the model, and it writes a nice answer.

The model NEVER calls the function itself.
It only tells us WHICH function to call and WITH WHAT arguments.
We execute it and feed the result back.
"""

import json
from datetime import date

import requests
from openai import OpenAI
from openai.types.responses import FunctionToolParam
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

TODAY = date.today().strftime("%A, %B %d, %Y")

SYSTEM_MESSAGE = (
    f"You are a helpful weather assistant. Today's date is {TODAY}. "
    "Use the get_weather tool to fetch real weather data. "
    "Always include the exact temperature and today's date in your response."
)


# ---- STEP 1: Define the tool (tell the model what functions exist) ----

WEATHER_TOOL: FunctionToolParam = {
    "type": "function",
    "name": "get_weather",
    "strict": None,
    "description": "Get the current weather for a given city.",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city name, e.g. 'Lahore', 'Tokyo', 'London'",
            }
        },
        "required": ["city"],
    },
}


# ---- STEP 2: Write the actual function (this runs on YOUR machine) ----

def get_weather(city: str):
    """Fetch real weather data from wttr.in (no API key needed)."""
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url, timeout=10)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text.strip()}"

    return "Something went wrong!"


# ---- STEP 3: The agent loop ----

def run_agent(user_message: str):
    """
    Send user's question to the model along with available tools.

    The model will either:
      A) Answer directly (if it doesn't need a tool)
      B) Ask us to call a function (if it needs data)

    If B, we call the function, send the result back,
    and the model writes the final answer.
    """

    # First call: send the question + tell model about our tools
    print(f"You: {user_message}\n")
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=SYSTEM_MESSAGE,
        input=user_message,
        tools=[WEATHER_TOOL],
    )

    # Check if the model wants to call a function
    for item in response.output:
        if item.type == "function_call" and item.name == "get_weather":
            # Model said: "call get_weather with these arguments"
            args = json.loads(item.arguments)
            print(f"Model wants to call: get_weather(city=\"{args['city']}\")")

            # We run the function ourselves
            weather_data = get_weather(args["city"])
            print(f"Function returned: {weather_data}\n")

            # Send the result back to the model for a final answer
            tool_output: dict = {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": weather_data,
            }

            followup = client.responses.create(
                model="gpt-4o-mini",
                instructions=SYSTEM_MESSAGE,
                input=[
                    {"role": "user", "content": user_message},
                    item,  # type: ignore[list-item]
                    tool_output,
                ],
                tools=[WEATHER_TOOL],
            )

            return followup.output_text

    # Model answered directly without calling any function
    return response.output_text


# ---- Run it ----

USER_MESSAGE = input("Ask about the weather: ")
print(f"\nAgent: {run_agent(USER_MESSAGE)}")
