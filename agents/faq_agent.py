# agents/faq_agent.py

from agents.base import BaseAgent
from utils.json_parser import extract_json
import time


class FAQAgent(BaseAgent):
    def run(self, state):
        prompt = f"""
You are an AI assistant.

Generate at least 15 FAQs for the following product.
Return ONLY valid JSON in the format:

[
  {{ "question": "...", "answer": "..." }}
]

Product:
{state.product_context}
"""

        try:
            response = self.llm.invoke(prompt)
            parsed = extract_json(response.content)

            # Validate structure
            if not isinstance(parsed, list):
                raise ValueError("FAQ output is not a list")

            return {
                "faqs": parsed,
                "retry_count": state.retry_count
            }

        except Exception as e:
            print(f"⚠️ FAQAgent fallback triggered: {e}")

            # 🔒 HARD fallback — deterministic, safe, valid
            fallback_faqs = [
                {
                    "question": "What is this product?",
                    "answer": "This product is designed to improve skincare results."
                },
                {
                    "question": "Who can use this product?",
                    "answer": "It is suitable for most skin types."
                },
                {
                    "question": "How should this product be used?",
                    "answer": "Follow the usage instructions provided with the product."
                }
            ]

            return {
                "faqs": fallback_faqs,
                "retry_count": state.retry_count + 1
            }
