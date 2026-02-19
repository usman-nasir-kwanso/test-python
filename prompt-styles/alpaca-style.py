"""Alpaca-style prompting: Instruction + Input = Response."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

INSTRUCTION = "Summarize the following email in one sentence."
INPUT_TEXT = (
    "Hi team, just a reminder that the office will be closed "
    "next Friday for maintenance. Please take your laptops home "
    "on Thursday evening. Thanks!"
)

ALPACA_TEMPLATE = """### Instruction:
{instruction}

### Input:
{input_text}

### Response:"""

prompt = ALPACA_TEMPLATE.format(instruction=INSTRUCTION, input_text=INPUT_TEXT)

response = client.responses.create(
    model="gpt-5.2",
    instructions=(
        "You follow the Alpaca format: read the Instruction, "
        "analyze the Input, and write a clear Response."
    ),
    input=prompt,
)

print(response.output_text)
