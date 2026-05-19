# Model Routing, Budget Limits & Key Isolation

For developers connecting AI coding tools to custom API endpoints
who need to manage multiple models, control costs, or isolate billing.

---

## Why this matters

AI coding tools send requests to a single API endpoint. When you need to:
- Use different models for different tasks (reasoning vs. bulk coding)
- Set hard spending limits per project or team
- Track costs per API key separately
- Fail over to a backup model when the primary is unavailable

...you need a routing layer between the tool and the model providers.

## Architecture overview

```
Tool (Claude Code / Aider / Cursor)
  │
  ▼
[Routing Layer]  ← model mapping, budget enforcement, key isolation
  │         │         │
  ▼         ▼         ▼
Provider A  Provider B  Provider C
(Claude)    (GPT)       (DeepSeek)
```

The tool only knows about one endpoint. The routing layer handles routing, logging, and policy enforcement.

---

## 1. Model routing

Map the tool's model name to the provider's actual model name.

**Environment variable approach** (no routing layer needed for simple cases):
```bash
export ANTHROPIC_BASE_URL=https://provider-endpoint/v1
export ANTHROPIC_MODEL=your-model-name
export ANTHROPIC_DEFAULT_SONNET_MODEL=model-for-sonnet-tasks
export ANTHROPIC_DEFAULT_OPUS_MODEL=model-for-opus-tasks
export ANTHROPIC_DEFAULT_HAIKU_MODEL=model-for-haiku-tasks
```

**Routing layer approach** (for complex multi-provider setups):
- Define model aliases in the routing layer config
- Tool sends `claude-sonnet-4-6`, routing layer maps to the target model
- Each provider can have different model names for the same capability tier

**Key consideration**: Different providers have different output token limits, context windows, and feature support (thinking mode, tool use, streaming). The routing layer should validate these constraints before forwarding.

## 2. Budget limits

Some provider-side spend limits may not behave like per-request hard stops in every tool workflow.

**Hard budget enforcement** at the routing layer:
- Set a per-key or per-project daily/monthly spending limit
- The routing layer tracks cumulative cost and rejects requests when the limit is reached
- This provides real-time enforcement, not delayed batch accounting

**Implementation pattern**:
```
Per-key config:
  - daily_budget: <amount>
  - monthly_budget: <amount>
  - alert_threshold: 80%  (notify at 80% consumed)
  - hard_stop: 100%       (reject requests at 100%)
```

**Token-based budgets** (alternative to dollar-based):
- Set limits in tokens rather than dollars
- Useful when you want consistent limits regardless of model pricing changes
- Track input, output, and cache tokens separately

## 3. Key isolation

One API key per project, team, or environment prevents:
- Silent cross-project billing contamination
- Difficulty attributing costs to the right team
- One runaway process consuming another project's budget

**Setup**:
- Generate separate API keys in your routing layer
- Assign each key to a project/team with its own budget and model access
- Log per-request: key ID, model, input tokens, output tokens, estimated cost
- Review per-key usage reports regularly

## 4. Failover & fallback

When a primary model or provider is unavailable:

**Automatic failover**:
- Primary model returns 5xx or timeout → route to secondary model
- Circuit breaker: if error rate exceeds threshold, skip the failing model for a cooldown period
- Latency-based routing: route to the fastest responding provider

**Graceful degradation**:
- Opus-tier task fails → fall back to Sonnet-tier model (cheaper, faster, but less capable)
- Log fallback events so you know when degradation is happening

**Configuration example**:
```
model_routing:
  claude-sonnet-4-6:
    primary: provider-a/claude-sonnet-4-6
    fallback: provider-b/claude-sonnet-4-6
    timeout: 30s
    circuit_breaker:
      error_threshold: 3
      cooldown: 60s
```

## 5. Common open-source tools for this

- **LiteLLM** — Python-based proxy with model routing, budget limits, and 100+ provider support
- **New-API / One-API** — Go-based API management with multi-provider support
- **Custom nginx + lua** — Lightweight option for simple routing and header rewriting
- **Cloudflare Workers / AWS Lambda** — Serverless option for simple routing without running infrastructure

## 6. Quick setup (env vars only)

For the simplest case — pointing your tool at a different endpoint:

```bash
# Point to your routing layer instead of the default API
export ANTHROPIC_BASE_URL=https://your-routing-layer/v1
export ANTHROPIC_API_KEY=your-routing-key

# That's it — the tool connects to your routing layer,
# which handles model mapping, budget enforcement, and provider selection
```

For tools that use OpenAI-compatible endpoints:
```bash
export OPENAI_BASE_URL=https://your-routing-layer/v1
export OPENAI_API_KEY=your-routing-key
```

---

## Further reading

- [Anthropic API documentation](https://docs.anthropic.com/)
- [OpenAI API compatibility guide](https://platform.openai.com/docs/guides/text)
- [LiteLLM documentation](https://docs.litellm.ai/)
