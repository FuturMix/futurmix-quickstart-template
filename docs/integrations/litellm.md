# Use FuturMix with LiteLLM

Access Claude, GPT, and Gemini through an OpenAI-compatible endpoint for model routing and cost control in your LiteLLM proxy.

## Quick Setup (works now, any LiteLLM version)

Use the `openai/` prefix with a custom `api_base`:

```yaml
model_list:
  - model_name: claude-sonnet
    litellm_params:
      model: openai/claude-sonnet-4-6
      api_base: https://futurmix.ai/v1
      api_key: os.environ/FUTURMIX_API_KEY

  - model_name: gpt-5.4-mini
    litellm_params:
      model: openai/gpt-5.4-mini
      api_base: https://futurmix.ai/v1
      api_key: os.environ/FUTURMIX_API_KEY

  - model_name: gpt-5.5
    litellm_params:
      model: openai/gpt-5.5
      api_base: https://futurmix.ai/v1
      api_key: os.environ/FUTURMIX_API_KEY

  - model_name: gemini-2.5-pro
    litellm_params:
      model: openai/gemini-2.5-pro
      api_base: https://futurmix.ai/v1
      api_key: os.environ/FUTURMIX_API_KEY
```

Set the environment variable:

```bash
export FUTURMIX_API_KEY="sk-your-key-here"
```

### Python SDK

```python
import litellm

response = litellm.completion(
    model="openai/gpt-5.4-mini",
    api_base="https://futurmix.ai/v1",
    api_key="sk-your-key-here",
    messages=[{"role": "user", "content": "Hello!"}],
)

print(response.choices[0].message.content)
```

## After LiteLLM Merges FuturMix Support

Once [litellm#26769](https://github.com/BerriAI/litellm/pull/26769) is merged, FuturMix becomes a named provider. Until then, use the OpenAI-compatible setup above. After the merge, you can use the `futurmix/` prefix without specifying `api_base`:

```yaml
model_list:
  - model_name: claude-sonnet
    litellm_params:
      model: futurmix/claude-sonnet-4-6
      api_key: os.environ/FUTURMIX_API_KEY

  - model_name: gpt-5.4-mini
    litellm_params:
      model: futurmix/gpt-5.4-mini
      api_key: os.environ/FUTURMIX_API_KEY
```

```python
response = litellm.completion(
    model="futurmix/gpt-5.4-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

## Sample Models

| Model | Use case |
|-------|----------|
| `gpt-5.4-mini` | Fast, low cost — good for routing, summarization |
| `gpt-5.5` | GPT flagship — complex reasoning |
| `claude-sonnet-4-6` | Claude Sonnet — coding, analysis |
| `gemini-2.5-pro` | Gemini flagship — long context, multimodal |

Full model list and live pricing: [futurmix.ai/pricing](https://futurmix.ai/pricing)

## Get Started

1. **Register** at [futurmix.ai/register](https://futurmix.ai/register)
2. **Top up your balance** — new accounts start with $0 balance. API calls return `insufficient_user_quota` until you add funds.
3. **Create an API key** in your [dashboard](https://futurmix.ai/console), then set `FUTURMIX_API_KEY` and start your LiteLLM proxy.

## Troubleshooting

**`insufficient_user_quota` error**: Your balance is $0. Top up at [futurmix.ai/console/topup](https://futurmix.ai/console/topup).

**`model_not_available` error**: The model name doesn't match an available model. Check [futurmix.ai/pricing](https://futurmix.ai/pricing) for exact identifiers.

**Connection timeout**: FuturMix endpoint is `https://futurmix.ai/v1` (with `/v1` suffix). Make sure `api_base` includes the full path.

---

*FuturMix provides OpenAI-compatible endpoint access to multiple leading models with model routing and cost control for teams.*
