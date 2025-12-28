from agents.base import BaseAgent
from graph.state import GraphState
import json
import re


class QuestionGenerationAgent(BaseAgent):
    """
    Generates a fixed number of FAQ questions for a product.
    Responsible ONLY for `faq_questions` in the shared state.
    """

    def run(self, state: GraphState):
        product = state.product_context

        prompt = f"""
Generate EXACTLY 15 concise FAQ questions for the product below.

Product details:
{product}

Return STRICT JSON ONLY in the following format:
{{
  "questions": ["question 1", "question 2", "..."]
}}

Rules:
- Do NOT add explanations
- Do NOT add markdown
- Do NOT include anything outside JSON
- Keep questions short and clear
"""

        response = self.safe_invoke(prompt)

        questions = self._extract_questions(response.content)

        # LangGraph-safe partial update
        return {
            "faq_questions": questions
        }

    def _extract_questions(self, text: str):
        """
        Safely extract JSON from LLM output.
        """
        try:
            match = re.search(r"\{.*\}", text, re.DOTALL)
            if not match:
                raise ValueError("No JSON object found")

            data = json.loads(match.group())
            questions = data.get("questions", [])

            if not isinstance(questions, list):
                raise ValueError("Questions is not a list")

            # Enforce EXACTLY 15 questions
            return questions[:15]

        except Exception as e:
            print(f"⚠️ QuestionAgent parsing error: {e}")

            # Safe fallback (still machine-readable)
            return [
                f"What is {state.product_context.get('name')}?",
                "What are the key ingredients?",
                "Who should use this product?",
                "How is this product used?",
                "Is it suitable for sensitive skin?",
                "What are the benefits?",
                "How often should it be used?",
                "Can it be used daily?",
                "Does it cause side effects?",
                "Is it dermatologist tested?",
                "Is it safe for long-term use?",
                "What skin types is it suitable for?",
                "Does it contain harmful chemicals?",
                "How should it be stored?",
                "What makes this product different?"
            ]
