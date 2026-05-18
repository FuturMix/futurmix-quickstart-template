"""
FuturMix Basic Chat Example (Python)
=====================================
Simple chat completion using the OpenAI SDK with FuturMix.

Setup:
    pip install openai
    export FUTURMIX_API_KEY="your-futurmix-api-key"
"""

import os
from openai import OpenAI

# Initialize the client -- points to FuturMix API
client = OpenAI(
    api_key=os.environ.get("FUTURMIX_API_KEY", os.environ.get("OPENAI_API_KEY")),
    base_url=os.environ.get("OPENAI_BASE_URL", "https://futurmix.ai/v1"),
)

# Send a chat completion request
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is FuturMix and how does it help developers?"},
    ],
    max_tokens=512,
)

# Print the response
print("Model:", response.model)
print("Usage:", response.usage)
print()
print(response.choices[0].message.content)
