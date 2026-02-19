"""Chain-of-thought prompting: let the model reason step by step."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_MESSAGE = (
    "You are a helpful math tutor. "
    "Think step by step before giving the final answer. "
    "Show your reasoning clearly."
)

USER_MESSAGE = (
    "A farmer has 3 fields. The first field has 12 cows, "
    "the second has twice as many, and the third has 5 fewer than the second. "
    "How many cows does the farmer have in total?"
)

response = client.responses.create(
    model="o3-mini",
    reasoning={"effort": "high"},
    instructions=SYSTEM_MESSAGE,
    input=USER_MESSAGE,
)

print(response.output_text)
