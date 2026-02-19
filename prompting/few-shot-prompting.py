"""Few-shot prompting: teach the model by showing examples first."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_MESSAGE = "You classify the sentiment of a message as positive, negative, or neutral."

EXAMPLE_1_USER = "I love this weather, it's perfect for a walk!"
EXAMPLE_1_ASSISTANT = "Positive"

EXAMPLE_2_USER = "The flight got cancelled and I'm stuck at the airport."
EXAMPLE_2_ASSISTANT = "Negative"

EXAMPLE_3_USER = "The meeting is at 3pm tomorrow."
EXAMPLE_3_ASSISTANT = "Neutral"

USER_MESSAGE = "My friend surprised me with concert tickets for my birthday!"

response = client.responses.create(
    model="gpt-5.2",
    instructions=SYSTEM_MESSAGE,
    input=[
        {"role": "user", "content": EXAMPLE_1_USER},
        {"role": "assistant", "content": EXAMPLE_1_ASSISTANT},
        {"role": "user", "content": EXAMPLE_2_USER},
        {"role": "assistant", "content": EXAMPLE_2_ASSISTANT},
        {"role": "user", "content": EXAMPLE_3_USER},
        {"role": "assistant", "content": EXAMPLE_3_ASSISTANT},
        {"role": "user", "content": USER_MESSAGE},
    ],
)

print(response.output_text)
