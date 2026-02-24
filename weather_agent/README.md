# Weather Agent (Function Calling)

An AI agent that fetches **real** weather data by deciding on its own when to call a function.

## What is Function Calling?

The model can't access the internet or run code. But you can give it a **menu of functions** it can ask you to call. The model decides *when* and *with what arguments* — you execute it.

```
You: "What's the weather in Lahore?"
         |
         v
┌─────────────────────────────────────┐
│  Model thinks:                      │
│  "I need real weather data.         │
│   I'll call get_weather(Lahore)"    │
└─────────────────────────────────────┘
         |
         v
   Your code runs get_weather("Lahore")
   Gets: "Clear +32°C"
         |
         v
┌─────────────────────────────────────┐
│  Model receives the data and says:  │
│  "Today in Lahore it's 32°C..."     │
└─────────────────────────────────────┘
```

The model **never** calls the function itself. It only says "please call this function with these arguments." Your code does the rest.

## File

| File | Purpose |
|---|---|
| `main.py` | The complete agent — tool definition, function, and agent loop |

## How It Works (3 Steps in Code)

### Step 1: Define the Tool
Tell the model what functions exist, what they do, and what parameters they accept (JSON Schema).

### Step 2: Write the Function
A regular Python function that fetches weather from `wttr.in` — runs on your machine, no API key needed.

### Step 3: The Agent Loop
1. Send user's question + tool definitions to the model
2. If the model wants to call a function → extract arguments → run it → send result back
3. Model writes the final human-readable answer

## Run

```bash
source venv/bin/activate
python weather_agent/main.py
```

You'll see the full flow printed:

```
Ask about the weather: What's the weather in Tokyo?

You: What's the weather in Tokyo?

Model wants to call: get_weather(city="Tokyo")
Function returned: The weather in Tokyo is Partly cloudy +18°C

Agent: Today (Wednesday, February 19, 2026) in Tokyo, the weather is
partly cloudy with a temperature of 18°C (64°F).
```

## Key Concepts

| Concept | What It Means |
|---|---|
| **Function Calling** | Model requests a function call — you execute it |
| **Tool Definition** | JSON schema describing your function's name, description, and parameters |
| **Agent Loop** | The cycle: ask model → call tool → feed result → get final answer |
| **`function_call` output** | Model's response saying "call this function with these args" |
| **`function_call_output`** | Your response sending the function's return value back to the model |
