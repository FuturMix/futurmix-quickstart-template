/**
 * FuturMix Streaming Example (Node.js)
 * ======================================
 * Stream chat completions token-by-token using the OpenAI SDK.
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
  const stream = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [
      { role: "system", content: "You are a helpful assistant." },
      { role: "user", content: "Write a short poem about multi-model AI." },
    ],
    max_tokens: 256,
    stream: true,
  });

  console.log("Streaming response:\n");

  for await (const chunk of stream) {
    const content = chunk.choices?.[0]?.delta?.content;
    if (content) {
      process.stdout.write(content);
    }
  }

  console.log("\n\nDone!");
}

main().catch(console.error);
