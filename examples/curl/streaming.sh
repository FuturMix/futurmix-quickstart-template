#!/usr/bin/env bash
#
# FuturMix Streaming Example (cURL)
# ====================================
# Stream chat completions using cURL with server-sent events.
#
# Setup:
#   export FUTURMIX_API_KEY="your-futurmix-api-key"
#
# Usage:
#   bash streaming.sh

set -euo pipefail

API_KEY="${FUTURMIX_API_KEY:-${OPENAI_API_KEY:-your-futurmix-api-key}}"
BASE_URL="${OPENAI_BASE_URL:-https://futurmix.ai/v1}"

echo "Streaming response from FuturMix (claude-sonnet-4-6)..."
echo

curl -sN "${BASE_URL}/chat/completions" \
  -H "Authorization: Bearer ${API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Write a short poem about multi-model AI."}
    ],
    "max_tokens": 256,
    "stream": true
  }'

echo
echo
echo "Done!"
