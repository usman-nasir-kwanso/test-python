# Hugging Face Basic

Demonstrates using Hugging Face's `transformers` pipeline for multimodal inference (image + text).

## How It Works

Uses Google's **MedGemma** model (`google/medgemma-1.5-4b-it`) with an `image-text-to-text` pipeline. You provide an image and a question, and the model answers based on what it sees.

## File

- **`main.py`** — Sends an image of candy to the model and asks "What animal is on the candy?"

## Prerequisites

- `transformers` library installed
- Sufficient GPU/RAM for the 4B parameter model
- Hugging Face access token (if model is gated)

## Run

```bash
source venv/bin/activate
python hf-basic/main.py
```
