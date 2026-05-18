/**
 * FuturMix Basic Chat Example (Node.js)
 * =======================================
 * Simple chat completion using the OpenAI SDK with FuturMix.
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

async function main() {
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      {
        role: "user",
        content: "What is FuturMix and how does it help developers?",
      },
    ],
    max_tokens: 512,
  });

  console.log("Model:", response.model);
  console.log("Usage:", response.usage);
  console.log();
  console.log(response.choices[0].message.content);
}

main().catch(console.error);
