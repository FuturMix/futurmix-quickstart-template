#!/usr/bin/env bash
#
# FuturMix -- Claude Code / Claude Desktop Setup
# =================================================
# Configure your environment to use FuturMix as the backend for
# Claude Code, Claude Desktop, and the Anthropic SDK.
#
# FuturMix supports the native Anthropic API format, so you can
# use Anthropic tools directly with a FuturMix API key.
#
# Usage:
#   source claude_code_setup.sh
#   # Then launch Claude Code as normal

set -euo pipefail

# ── Prompt for API key if not already set ──────────────────────
if [ -z "${FUTURMIX_API_KEY:-}" ]; then
    echo "Enter your FuturMix API key (from https://futurmix.ai/dashboard):"
    read -r FUTURMIX_API_KEY
fi

# ── Set Anthropic environment variables ────────────────────────
export ANTHROPIC_API_KEY="${FUTURMIX_API_KEY}"
export ANTHROPIC_BASE_URL="https://futurmix.ai"

# ── Also set OpenAI-compatible variables (for other tools) ─────
export OPENAI_API_KEY="${FUTURMIX_API_KEY}"
export OPENAI_BASE_URL="https://futurmix.ai/v1"

echo ""
echo "FuturMix environment configured:"
echo "  ANTHROPIC_API_KEY  = ${ANTHROPIC_API_KEY:0:12}..."
echo "  ANTHROPIC_BASE_URL = ${ANTHROPIC_BASE_URL}"
echo "  OPENAI_API_KEY     = ${OPENAI_API_KEY:0:12}..."
echo "  OPENAI_BASE_URL    = ${OPENAI_BASE_URL}"
echo ""
echo "You can now launch Claude Code or any Anthropic-compatible tool."
echo "All requests will be routed through FuturMix with built-in discounts."
