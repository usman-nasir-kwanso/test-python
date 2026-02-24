# Prompting Techniques

Explores different prompting techniques using the OpenAI API. Each file demonstrates a technique with a simple, everyday example.

## Files

| File | Technique | Example |
|---|---|---|
| `main.py` | **Basic prompting** | Fitness coach giving workout advice |
| `few-shot-prompting.py` | **Few-shot prompting** | Sentiment classifier (positive/negative/neutral) |
| `chain-of-thought.py` | **Chain-of-thought** | Math tutor solving a word problem step by step |
| `persona-prompting.py` | **Persona prompting** | Same question answered by a nutritionist, chef, or budget advisor |

## Techniques Explained

### Basic Prompting
Set a system message (persona + rules) and send a user message. The simplest way to use an LLM.

### Few-Shot Prompting
Show the model 2-3 examples of input/output pairs before asking the real question. The model learns the pattern and follows it.

### Chain-of-Thought (CoT)
Ask the model to "think step by step." Uses `o3-mini` with `reasoning.effort = "high"` for deeper thinking.

### Persona Prompting
Change the system message to adopt different expert perspectives. Same question, completely different answers depending on the persona.

## Run

```bash
source venv/bin/activate
python prompting/main.py
python prompting/few-shot-prompting.py
python prompting/chain-of-thought.py
python prompting/persona-prompting.py
```
