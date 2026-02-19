"""LLaMA-2 [INST] style prompting: system message + instruction tags."""

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

SYSTEM_MESSAGE = (
    "You are a helpful cooking assistant. Keep answers short and practical."
)
USER_MESSAGE = "How do I make a perfect omelette for beginners?"

LLAMA2_TEMPLATE = """[INST] <<SYS>>
{system}
<</SYS>>

{user_message} [/INST]"""

prompt = LLAMA2_TEMPLATE.format(system=SYSTEM_MESSAGE, user_message=USER_MESSAGE)

response = client.responses.create(
    model="gpt-5.2",
    input=prompt,
)

print(response.output_text)
