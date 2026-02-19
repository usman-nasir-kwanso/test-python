"""Basic prompting with system instructions using the OpenAI API."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_MESSAGE = (
    "You are a helpful fitness coach. "
    "You give short, practical workout advice. "
    "If a question is not about fitness, politely decline."
)
USER_MESSAGE = "I only have 15 minutes in the morning. What's a good quick workout?"

response = client.responses.create(
    model="gpt-5.2",
    instructions=SYSTEM_MESSAGE,
    input=USER_MESSAGE,
)

print(response.output_text)
