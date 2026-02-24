# Tokenization

Demonstrates how LLMs break text into tokens using OpenAI's `tiktoken` library.

## What is Tokenization?

Tokenization is the process of converting text into smaller units called **tokens**. LLMs don't read words — they read tokens. A token can be a word, part of a word, or even a single character.

For example, `"Hello, world!"` becomes `[13225, 11, 2375, 0]` — four tokens.

## File

- **`main.py`** — Encodes text into tokens using the `gpt-4o` model's tokenizer (`o200k_base`), then decodes them back to text.

## Key Concepts

| Concept | Description |
|---|---|
| `encoding_for_model()` | Looks up the correct tokenizer for a given model name |
| `encode()` | Converts a string into a list of token IDs |
| `decode()` | Converts token IDs back into a string |

## Run

```bash
source venv/bin/activate
python tokenization/main.py
```
