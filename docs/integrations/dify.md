# Use FuturMix in Dify

Access Claude, GPT, and Gemini models in your Dify workflows through the FuturMix plugin.

## Install the Plugin

### From Dify Marketplace

1. Go to **Plugins** → **Marketplace**
2. Search for **FuturMix**
3. Click **Install**

### From Source

Download `futurmix.difypkg` from [dify-plugins/FuturMix](https://github.com/langgenius/dify-plugins/tree/main/FuturMix/futurmix) and install via **Plugins** → **Install from file**.

## Configure the Provider

After installation:

1. Go to **Settings** → **Model Provider**
2. Find **FuturMix** in the provider list
3. Enter your credentials:

| Field | Value |
|-------|-------|
| API Key | `sk-your-key-here` |
| API Base | `https://futurmix.ai/v1` |

4. Click **Save**

## Add Models

In the FuturMix provider settings, add the models you want to use:

| Model ID | Use case |
|----------|----------|
| `gpt-5.4-mini` | Fast, low cost — routing, summarization |
| `gpt-5.5` | GPT flagship — complex reasoning |
| `claude-sonnet-4-6` | Claude Sonnet — coding, analysis |
| `gemini-2.5-pro` | Gemini flagship — long context, multimodal |

The plugin supports both predefined models and custom model configurations. To add a model not in the predefined list, use **Add Custom Model** and enter the exact model identifier from [futurmix.ai/pricing](https://futurmix.ai/pricing).

## Use in Workflows

Once configured, FuturMix models appear in the model selector for:

- **Chat / Completion** nodes
- **LLM** nodes in workflows
- **Agent** assistants

Select any FuturMix model from the dropdown, same as any other provider.

Full model list and live pricing: [futurmix.ai/pricing](https://futurmix.ai/pricing)

## Get Started

1. **Register** at [futurmix.ai/register](https://futurmix.ai/register)
2. **Top up your balance** — new accounts start with $0 balance. API calls return `insufficient_user_quota` until you add funds.
3. **Create an API key** in your [dashboard](https://futurmix.ai/console), then paste it into Dify's provider settings.

## Troubleshooting

**Plugin not showing in Marketplace**: Search for "FuturMix" (case-sensitive). If running Dify Community Edition, make sure your Dify version supports plugins and Marketplace.

**`insufficient_user_quota` error in workflow**: Your balance is $0. Top up at [futurmix.ai/console/topup](https://futurmix.ai/console/topup).

**`model_not_available` error**: The model ID doesn't match an available model. Check [futurmix.ai/pricing](https://futurmix.ai/pricing) for exact identifiers.

**Connection timeout**: Ensure API Base is `https://futurmix.ai/v1` (with `/v1` suffix). Dify's plugin handles the rest of the path.

---

*FuturMix provides OpenAI-compatible endpoint access to multiple leading models with model routing and cost control for teams.*
