"""
FuturMix Anthropic-Native Example (Python)
============================================
Use the Anthropic Python SDK directly with FuturMix.
This works because FuturMix supports both OpenAI and Anthropic API formats.

Setup:
    pip install anthropic
    export ANTHROPIC_API_KEY="your-futurmix-api-key"
    export ANTHROPIC_BASE_URL="https://futurmix.ai"
"""

import os
import anthropic

# Initialize the Anthropic client -- points to FuturMix
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY", os.environ.get("FUTURMIX_API_KEY")),
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://futurmix.ai"),
)

# ── Basic message ──────────────────────────────────────────────

print("=== Basic Message ===\n")

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=512,
    messages=[
        {"role": "user", "content": "What is FuturMix and how does it help developers?"}
    ],
)

print(f"Model: {message.model}")
print(f"Stop reason: {message.stop_reason}")
print(f"Input tokens: {message.usage.input_tokens}")
print(f"Output tokens: {message.usage.output_tokens}")
print()
print(message.content[0].text)

# ── Streaming message ──────────────────────────────────────────

print("\n\n=== Streaming Message ===\n")

with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=256,
    messages=[
        {"role": "user", "content": "Write a haiku about API gateways."}
    ],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

print("\n\nDone!")
