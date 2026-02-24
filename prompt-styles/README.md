# Prompt Styles

Compares different prompt formatting styles used across LLM ecosystems. Each file shows the same idea — sending a message to a model — but structured differently.

## Files

| File | Style | Origin |
|---|---|---|
| `chatml-style.py` | **ChatML** | OpenAI (GPT models) |
| `alpaca-style.py` | **Alpaca** | Stanford Alpaca |
| `llama2-inst-style.py` | **[INST]** | Meta LLaMA-2 |

## Styles Explained

### ChatML (Chat Markup Language)
Role-based messages: `system`, `user`, `assistant`. Supports multi-turn conversations naturally. This is the format OpenAI's API uses natively.

```
system: You are a travel guide.
user: What should I see in Paris?
assistant: Day 1: Eiffel Tower...
user: What food should I try?
```

### Alpaca (Instruction-Input-Response)
A text template with three sections. Originally created for Stanford's Alpaca fine-tuning dataset. Best for single-turn tasks.

```
### Instruction:
Summarize the following email.

### Input:
Hi team, the office will be closed...

### Response:
```

### LLaMA-2 [INST]
Uses special tokens `[INST]`, `[/INST]`, `<<SYS>>`, `<</SYS>>` to mark roles. Everything is packed into a single string instead of separate message objects.

```
[INST] <<SYS>>
You are a cooking assistant.
<</SYS>>

How do I make an omelette? [/INST]
```

## When to Use Which

| Style | Best For |
|---|---|
| ChatML | Multi-turn conversations, OpenAI API |
| Alpaca | Single-turn tasks, fine-tuning datasets |
| LLaMA-2 [INST] | Working with LLaMA-2 family models |

## Run

```bash
source venv/bin/activate
python prompt-styles/chatml-style.py
python prompt-styles/alpaca-style.py
python prompt-styles/llama2-inst-style.py
```
