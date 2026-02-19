"""Persona prompting: same question, different expert perspectives."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

PERSONAS = {
    "nutritionist": (
        "You are a certified nutritionist. "
        "You focus on balanced meals, portion control, and whole foods. "
        "Keep advice practical and easy to follow."
    ),
    "chef": (
        "You are a professional chef. "
        "You focus on flavor, technique, and presentation. "
        "Keep tips fun and creative."
    ),
    "budget_advisor": (
        "You are a budget-savvy meal planner. "
        "You focus on saving money while eating well. "
        "Always suggest affordable alternatives."
    ),
}

PERSONA_KEY = "nutritionist"
USER_MESSAGE = "What should I eat for a healthy breakfast?"

response = client.responses.create(
    model="gpt-5.2",
    instructions=PERSONAS[PERSONA_KEY],
    input=USER_MESSAGE,
)

print(f"Persona: {PERSONA_KEY}")
print(f"\n{response.output_text}")
