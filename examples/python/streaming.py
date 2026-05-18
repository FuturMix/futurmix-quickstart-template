"""
FuturMix Streaming Example (Python)
=====================================
Stream chat completions token-by-token using the OpenAI SDK.

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

# Create a streaming chat completion
stream = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Write a short poem about multi-model AI."},
    ],
    max_tokens=256,
    stream=True,
)

# Print tokens as they arrive
print("Streaming response:\n")
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

print("\n\nDone!")
