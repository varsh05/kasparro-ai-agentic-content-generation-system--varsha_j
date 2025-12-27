from agents.base import BaseAgent
from graph.state import GraphState
from utils.json_parser import extract_json


class FAQAgent(BaseAgent):
    """
    Generates FAQ answers for a list of questions using LLM reasoning.
    Output is a strict JSON list of {question, answer}.
    """

    def run(self, state: GraphState) -> GraphState:
        prompt = f"""
You are an FAQ answering agent.

Your task:
- Answer EACH question provided
- Use the product context accurately
- Return ONLY valid JSON
- Do NOT include markdown
- Do NOT include explanations

Required JSON format:
{{
  "faqs": [
    {{
      "question": "string",
      "answer": "string"
    }}
  ]
}}

Product context:
{state.product_context}

Questions:
{state.faq_questions}
"""

        response = self.llm.invoke(prompt)

        try:
            parsed = extract_json(response.content)

            faqs = parsed.get("faqs")
            if not isinstance(faqs, list) or len(faqs) < 15:
                raise ValueError("Invalid or insufficient FAQ answers")

            # Validate structure of each FAQ
            for item in faqs:
                if not isinstance(item, dict):
                    raise ValueError("FAQ item is not a dictionary")
                if "question" not in item or "answer" not in item:
                    raise ValueError("FAQ item missing required fields")

            state.faqs = faqs

        except Exception as e:
            state.errors.append(f"FAQAgent failed: {str(e)}")
            raise RuntimeError("Invalid FAQAgent output")

        return state
