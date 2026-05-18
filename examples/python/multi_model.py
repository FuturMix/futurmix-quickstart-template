"""
FuturMix Multi-Model Comparison (Python)
==========================================
Send the same prompt to multiple models and compare their responses.
This is one of the biggest advantages of FuturMix -- one API key,
many models.

Setup:
    pip install openai
    export FUTURMIX_API_KEY="your-futurmix-api-key"
"""

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("FUTURMIX_API_KEY", os.environ.get("OPENAI_API_KEY")),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://futurmix.ai/v1"),
)

# Models to compare -- all accessible through the same API key
models = [
    "claude-sonnet-4-6",   # Anthropic  (10% off)
    "gpt-4o-mini",          # OpenAI     (30% off)
    "gemini-2.5-flash",     # Google     (20% off)
    "deepseek-chat",        # DeepSeek
]

prompt = "Explain quantum computing in exactly two sentences."

print("=" * 60)
print("FuturMix Multi-Model Comparison")
print("=" * 60)
print(f"\nPrompt: {prompt}\n")

for model in models:
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=256,
        )
        answer = response.choices[0].message.content
        tokens = response.usage.total_tokens if response.usage else "N/A"

        print(f"--- {model} (tokens: {tokens}) ---")
        print(answer)
        print()

    except Exception as e:
        print(f"--- {model} ---")
        print(f"Error: {e}")
        print()

print("=" * 60)
print("All models accessed with one API key via FuturMix!")
