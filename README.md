# FuturMix Quickstart -- Multi-Model AI API

[![Try Free](https://img.shields.io/badge/Try%20Free-FuturMix.ai-blue?style=for-the-badge)](https://futurmix.ai/register?utm_source=github&utm_medium=quickstart)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![OpenAI Compatible](https://img.shields.io/badge/OpenAI-Compatible-black?logo=openai)](https://futurmix.ai)

**One API, 22+ models, built-in discounts.** Access Claude, GPT, Gemini, and DeepSeek through a single OpenAI-compatible endpoint at [futurmix.ai](https://futurmix.ai).

---

## Quick Setup (3 Steps)

### 1. Sign Up

Create your free account at [futurmix.ai/register](https://futurmix.ai/register?utm_source=github&utm_medium=quickstart) and grab your API key from the dashboard.

### 2. Set Environment Variables

```bash
export FUTURMIX_API_KEY="your-futurmix-api-key"

# OpenAI-compatible (works with any OpenAI SDK)
export OPENAI_API_KEY="$FUTURMIX_API_KEY"
export OPENAI_BASE_URL="https://futurmix.ai/v1"

# Anthropic-native (works with Claude Code, Claude Desktop, Anthropic SDK)
export ANTHROPIC_API_KEY="$FUTURMIX_API_KEY"
export ANTHROPIC_BASE_URL="https://futurmix.ai"
```

### 3. Run an Example

```bash
# Python
pip install openai
python examples/python/basic_chat.py

# Node.js
cd examples/nodejs && npm install && node basic_chat.js

# cURL
bash examples/curl/basic_chat.sh
```

---

## Code Examples

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-futurmix-api-key",
    base_url="https://futurmix.ai/v1",
)

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello from FuturMix!"}],
)
print(response.choices[0].message.content)
```

### Node.js (OpenAI SDK)

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: "your-futurmix-api-key",
  baseURL: "https://futurmix.ai/v1",
});

const response = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [{ role: "user", content: "Hello from FuturMix!" }],
});
console.log(response.choices[0].message.content);
```

### cURL

```bash
curl https://futurmix.ai/v1/chat/completions \
  -H "Authorization: Bearer your-futurmix-api-key" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "Hello from FuturMix!"}]
  }'
```

---

## Anthropic-Native Format (Claude Code / Claude Desktop)

FuturMix also supports the **native Anthropic API format**, so you can use it directly with Claude Code, Claude Desktop, and the Anthropic Python/JS SDKs.

### Claude Code Setup

```bash
# Set these environment variables, then launch Claude Code as normal
export ANTHROPIC_API_KEY="your-futurmix-api-key"
export ANTHROPIC_BASE_URL="https://futurmix.ai"
```

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "apiKey": "your-futurmix-api-key",
  "apiBaseUrl": "https://futurmix.ai"
}
```

### Anthropic Python SDK

```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-futurmix-api-key",
    base_url="https://futurmix.ai",
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello from FuturMix!"}],
)
print(message.content[0].text)
```

See [`examples/anthropic/`](examples/anthropic/) for complete working examples.

---

## Supported Models & Pricing

| Provider | Model | FuturMix Price | Discount |
|----------|-------|---------------|----------|
| **Anthropic** | `claude-sonnet-4-6` | 10% off | :star: |
| **Anthropic** | `claude-opus-4-6` | 10% off | :star: |
| **Anthropic** | `claude-haiku-3-5` | 10% off | :star: |
| **OpenAI** | `gpt-4o` | 30% off | :star::star::star: |
| **OpenAI** | `gpt-4o-mini` | 30% off | :star::star::star: |
| **OpenAI** | `gpt-4.1` | 30% off | :star::star::star: |
| **OpenAI** | `gpt-4.1-mini` | 30% off | :star::star::star: |
| **OpenAI** | `gpt-4.1-nano` | 30% off | :star::star::star: |
| **OpenAI** | `o3` | 30% off | :star::star::star: |
| **OpenAI** | `o3-mini` | 30% off | :star::star::star: |
| **OpenAI** | `o4-mini` | 30% off | :star::star::star: |
| **Google** | `gemini-2.5-pro` | 20% off | :star::star: |
| **Google** | `gemini-2.5-flash` | 20% off | :star::star: |
| **Google** | `gemini-2.0-flash` | 20% off | :star::star: |
| **DeepSeek** | `deepseek-chat` | Market rate | |
| **DeepSeek** | `deepseek-reasoner` | Market rate | |

> **22+ models available.** See the full list at [futurmix.ai/models](https://futurmix.ai/models).

---

## Example Files

| File | Description |
|------|-------------|
| [`examples/python/basic_chat.py`](examples/python/basic_chat.py) | Simple chat completion |
| [`examples/python/streaming.py`](examples/python/streaming.py) | Streaming response |
| [`examples/python/multi_model.py`](examples/python/multi_model.py) | Compare responses across models |
| [`examples/nodejs/basic_chat.js`](examples/nodejs/basic_chat.js) | Simple chat completion |
| [`examples/nodejs/streaming.js`](examples/nodejs/streaming.js) | Streaming response |
| [`examples/nodejs/multi_model.js`](examples/nodejs/multi_model.js) | Compare responses across models |
| [`examples/curl/basic_chat.sh`](examples/curl/basic_chat.sh) | cURL chat completion |
| [`examples/curl/streaming.sh`](examples/curl/streaming.sh) | cURL streaming |
| [`examples/anthropic/claude_code_setup.sh`](examples/anthropic/claude_code_setup.sh) | Claude Code / Claude Desktop setup |
| [`examples/anthropic/python_native.py`](examples/anthropic/python_native.py) | Anthropic Python SDK example |

---

## Deploy Your Own

Use FuturMix as the AI backend for your own apps. Works anywhere:

- **Vercel** -- Set `OPENAI_BASE_URL=https://futurmix.ai/v1` in your project environment variables
- **Railway** -- Add your `FUTURMIX_API_KEY` as a service variable
- **Docker** -- Pass `-e OPENAI_API_KEY=your-key -e OPENAI_BASE_URL=https://futurmix.ai/v1`
- **Any OpenAI-compatible app** -- Just change the base URL to `https://futurmix.ai/v1`

```bash
# Docker example
docker run -e OPENAI_API_KEY=$FUTURMIX_API_KEY \
           -e OPENAI_BASE_URL=https://futurmix.ai/v1 \
           your-app
```

---

## Why FuturMix?

- **One API key** for Claude, GPT, Gemini, and DeepSeek
- **OpenAI-compatible** -- works with any existing OpenAI SDK or tool
- **Anthropic-native** -- also supports the Anthropic API format for Claude Code
- **Built-in discounts** -- up to 30% off vs. going direct
- **No vendor lock-in** -- switch models with one line of code
- **22+ models** and growing

---

## Links

- [FuturMix Dashboard](https://futurmix.ai?utm_source=github&utm_medium=quickstart)
- [Sign Up (Free)](https://futurmix.ai/register?utm_source=github&utm_medium=quickstart)
- [API Documentation](https://futurmix.ai/docs)
- [Model List](https://futurmix.ai/models)

---

## License

MIT -- see [LICENSE](LICENSE).
