#!/usr/bin/env bash
#
# FuturMix Basic Chat Example (cURL)
# ====================================
# Simple chat completion using cURL with the OpenAI-compatible API.
#
# Setup:
#   export FUTURMIX_API_KEY="your-futurmix-api-key"
#
# Usage:
#   bash basic_chat.sh

set -euo pipefail

API_KEY="${FUTURMIX_API_KEY:-${OPENAI_API_KEY:-your-futurmix-api-key}}"
BASE_URL="${OPENAI_BASE_URL:-https://futurmix.ai/v1}"

echo "Sending request to FuturMix (claude-sonnet-4-6)..."
echo

curl -s "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "What is FuturMix and how does it help developers?"}
    ],
    "max_tokens": 512
  }' | python3 -m json.tool

echo
echo "Done!"
