from agents.base import BaseAgent
from graph.state import GraphState
from utils.json_parser import extract_json


class ParserAgent(BaseAgent):
    """
    Parses and normalizes raw product input into structured product context
    using LLM reasoning.
    """

    def run(self, state: GraphState) -> GraphState:
        prompt = f"""
You are a product data normalization agent.

Your task:
- Read the raw product input
- Normalize it into a STRICT JSON object
- Do NOT include markdown
- Do NOT include explanations
- Return ONLY valid JSON

Required JSON schema:
{{
  "name": string,
  "description": string,
  "skin_type": list[string],
  "key_ingredients": list[string],
  "price": number
}}

Raw product input:
{state.raw_product_data}
"""

        response = self.safe_invoke(prompt)


        try:
            parsed_output = extract_json(response.content)
            state.product_context = parsed_output
        except Exception as e:
            state.errors.append(f"ParserAgent failed: {str(e)}")
            raise RuntimeError("ParserAgent returned invalid JSON")

        return {
            "product_context": parsed_output
        }