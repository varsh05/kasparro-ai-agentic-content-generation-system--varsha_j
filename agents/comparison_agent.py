from agents.base import BaseAgent
from graph.state import GraphState
from utils.json_parser import extract_json


class ComparisonAgent(BaseAgent):
    """
    Generates structured product comparison using LLM reasoning.
    Output is STRICT JSON.
    """

    def run(self, state: GraphState) -> GraphState:
        prompt = f"""
You are a product comparison agent.

Your task:
- Compare the main product with a competing product
- Return ONLY valid JSON
- Do NOT include markdown or formatting
- Do NOT include explanations outside JSON

Required JSON format:
{{
  "product_a": {{
    "name": "string",
    "price": number,
    "key_ingredients": ["string"],
    "benefits": ["string"]
  }},
  "product_b": {{
    "name": "string",
    "price": number,
    "key_ingredients": ["string"],
    "benefits": ["string"]
  }},
  "differences": {{
    "ingredients": "string",
    "pricing": "string",
    "benefits": "string"
  }},
  "recommendation": "string"
}}

Product context:
{state.product_context}
"""

        response = self.llm.invoke(prompt)

        try:
            parsed = extract_json(response.content)

            required_keys = [
                "product_a",
                "product_b",
                "differences",
                "recommendation"
            ]

            for key in required_keys:
                if key not in parsed:
                    raise ValueError(f"Missing key in comparison_page: {key}")

            state.comparison_page = parsed

        except Exception as e:
            state.errors.append(f"ComparisonAgent failed: {str(e)}")
            raise RuntimeError("Invalid ComparisonAgent output")

        return state
