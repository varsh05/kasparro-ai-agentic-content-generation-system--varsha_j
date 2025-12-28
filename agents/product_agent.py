from agents.base import BaseAgent
from graph.state import GraphState
from utils.json_parser import extract_json


class ProductPageAgent(BaseAgent):
    """
    Generates structured product page content using LLM reasoning.
    Output is STRICT JSON.
    """

    def run(self, state: GraphState) -> GraphState:
        prompt = f"""
You are a product page generation agent.

Your task:
- Generate a complete product page using the product context
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include headings or explanations

Required JSON format:
{{
  "name": "string",
  "description": "string",
  "skin_type": ["string"],
  "key_ingredients": ["string"],
  "benefits": ["string"],
  "how_to_use": "string",
  "safety_information": "string",
  "price": number
}}

Product context:
{state.product_context}
"""

        response = self.safe_invoke(prompt)


        try:
            parsed = extract_json(response.content)

            # Basic validation
            required_fields = [
                "name",
                "description",
                "skin_type",
                "key_ingredients",
                "benefits",
                "how_to_use",
                "safety_information",
                "price",
            ]

            for field in required_fields:
                if field not in parsed:
                    raise ValueError(f"Missing field: {field}")

            state.product_page = parsed

        except Exception as e:
            state.errors.append(f"ProductPageAgent failed: {str(e)}")
            raise RuntimeError("Invalid ProductPageAgent output")

        return {
            "product_page": parsed
        }
