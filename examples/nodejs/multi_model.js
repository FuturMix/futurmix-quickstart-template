/**
 * FuturMix Multi-Model Comparison (Node.js)
 * ===========================================
 * Send the same prompt to multiple models and compare responses.
 * One API key, many models -- that's the FuturMix advantage.
 *
 * Setup:
 *   npm install openai
 *   export FUTURMIX_API_KEY="your-futurmix-api-key"
 */

import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.FUTURMIX_API_KEY || process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL || "https://futurmix.ai/v1",
});

// Models to compare -- all accessible through the same API key
const models = [
  "claude-sonnet-4-6", // Anthropic  (10% off)
  "gpt-4o-mini", // OpenAI     (30% off)
  "gemini-2.5-flash", // Google     (20% off)
  "deepseek-chat", // DeepSeek
];

const prompt = "Explain quantum computing in exactly two sentences.";

async function main() {
  console.log("=".repeat(60));
  console.log("FuturMix Multi-Model Comparison");
  console.log("=".repeat(60));
  console.log(`\nPrompt: ${prompt}\n`);

  for (const model of models) {
    try {
      const response = await client.chat.completions.create({
        model,
        messages: [{ role: "user", content: prompt }],
        max_tokens: 256,
      });

      const answer = response.choices[0].message.content;
      const tokens = response.usage?.total_tokens ?? "N/A";

      console.log(`--- ${model} (tokens: ${tokens}) ---`);
      console.log(answer);
      console.log();
    } catch (error) {
      console.log(`--- ${model} ---`);
      console.log(`Error: ${error.message}`);
      console.log();
    }
  }

  console.log("=".repeat(60));
  console.log("All models accessed with one API key via FuturMix!");
}

main().catch(console.error);
