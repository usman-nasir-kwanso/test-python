"""ChatML-style prompting: structured role-based conversation format."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_MESSAGE = "You are a friendly travel guide who gives short, helpful answers."

PREVIOUS_USER = "I'm visiting Paris for 2 days. What should I see?"
PREVIOUS_ASSISTANT = (
    "Day 1: Eiffel Tower in the morning, Louvre in the afternoon, "
    "Seine river walk in the evening.\n"
    "Day 2: Montmartre and Sacré-Cœur, then stroll through Le Marais."
)
USER_MESSAGE = "What local food should I try while I'm there?"

response = client.responses.create(
    model="gpt-5.2",
    instructions=SYSTEM_MESSAGE,
    input=[
        {"role": "user", "content": PREVIOUS_USER},
        {"role": "assistant", "content": PREVIOUS_ASSISTANT},
        {"role": "user", "content": USER_MESSAGE},
    ],
)

print(response.output_text)
