# OpenAI-Compatible Endpoint Troubleshooting

Common issues when connecting Claude Code, Codex, Aider, Cursor,
or other AI coding tools to a custom API endpoint.

> **Scope**: This checklist is for debugging endpoint compatibility, not for bypassing provider terms or rate limits.

---

## 1. Auth header mismatch

**Symptom**: 401 / "invalid API key" / "unauthorized"

**Checklist**:
- Anthropic-native endpoints expect `x-api-key: <key>` header
- OpenAI-compatible endpoints expect `Authorization: Bearer <key>` header
- Some proxies strip or rewrite auth headers during format conversion
- Confirm which header format your endpoint expects, then verify with a minimal request:
  ```bash
  curl -H "Authorization: Bearer $KEY" https://your-endpoint/v1/models
  ```
- If you get a 401, try the alternative header format or check your proxy's auth rewriting rules

## 2. Model name resolution

**Symptom**: "model not found" / 404 / "does not exist"

**Checklist**:
- Does your endpoint expect `claude-sonnet-4-6` or a provider-prefixed name like `anthropic/claude-sonnet-4-6`?
- Check environment variables that control model selection (exact names differ by tool/version — confirm with the target tool's docs):
  - `ANTHROPIC_MODEL`
  - `ANTHROPIC_DEFAULT_SONNET_MODEL`
  - `ANTHROPIC_DEFAULT_OPUS_MODEL`
  - `ANTHROPIC_DEFAULT_HAIKU_MODEL`
- Some tools automatically prepend a provider prefix — check request logs for the actual model string sent
- If using model mapping/aliasing, verify both the input name and the mapped output name are correct

## 3. max_tokens overflow

**Symptom**: 400 / "max_tokens out of range" / "Range of max_tokens should be [1, N]"

**Checklist**:
- The requesting tool may send a `max_tokens` value higher than the target provider supports
- Check the target provider's documentation for the specific model's output token limit
- If using a proxy/routing layer, clamp `max_tokens` before forwarding:
  ```
  request.max_tokens = min(request.max_tokens, provider_limit)
  ```
- Also clamp `thinking.budget_tokens` if present — it must be less than the final `max_tokens`
- Leave a safety margin (e.g., 1024 tokens) between `budget_tokens` and `max_tokens`

## 4. Thinking / reasoning_content passthrough

**Symptom**: 400 / "reasoning_content must be passed back to the API" / "content[].thinking in the thinking mode must be passed back"

**Checklist**:
- Some providers (e.g., those supporting thinking/reasoning mode) require the `reasoning_content` field to be round-tripped in multi-turn conversations
- If your proxy converts between Anthropic and OpenAI formats, it must preserve `reasoning_content` during the conversion
- Check if the proxy recognizes the target provider and enables reasoning content preservation
- If your tool/version supports disabling thinking/reasoning beta flags, test that as a temporary isolation step to confirm the issue is in reasoning passthrough
- Longer-term: ensure the proxy's format converter handles the `thinking` ↔ `reasoning_content` mapping for each provider

## 5. Session / provider namespace isolation

**Symptom**: Previous sessions disappear after switching providers / "session not found"

**Checklist**:
- Some tools store sessions per provider namespace (e.g., `model_provider` field)
- Switching the provider identifier mid-session can make previous sessions inaccessible
- If switching between OpenAI-compatible endpoints, keep the provider identifier consistent
- Start a fresh session after changing provider configuration rather than resuming

## 6. Streaming format differences

**Symptom**: Partial responses, hanging connections, garbled output, or abrupt disconnections

**Checklist**:
- Anthropic streaming uses `data: {"type":"content_block_delta"...}` events
- OpenAI-compatible streaming uses `data: {"choices":[{"delta":...}]}` events
- Verify your proxy correctly translates between these formats if protocol conversion is needed
- Test with non-streaming first to isolate whether the issue is in streaming translation:
  - Add `"stream": false` to the request body, or check tool settings for a non-streaming option
- Check for connection timeout settings — long-running agentic requests may exceed default timeouts

## 7. Billing / cost verification

**Symptom**: Unexpected charges, quota consumption higher than expected

**Checklist**:
- Log per-request token counts from API responses — capture all four classes separately:
  - `input_tokens`
  - `output_tokens`
  - `cache_creation_input_tokens`
  - `cache_read_input_tokens`
- Compare against your provider's usage dashboard for the same time window
- If using a proxy or routing layer, check its request logs for token breakdowns
- Calculate expected cost using provider's published per-token rates for each token class
- When filing a support ticket, include: request IDs, timestamps, the four token classes separately, and before/after quota percentages

---

## General debugging tips

- **Check request logs**: Most proxies and routing layers have request/response logging. Enable verbose logging during debugging.
- **Test the simplest case first**: Try a single, non-streaming request with a short prompt before debugging complex agentic workflows.
- **Verify the endpoint independently**: Use `curl` to send a test request directly to the endpoint, bypassing the tool, to isolate whether the issue is in the tool or the endpoint.
- **Check provider status pages**: Transient 500/503 errors may be provider-side outages, not configuration issues.
