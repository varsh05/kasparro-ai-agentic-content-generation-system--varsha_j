from agents.base import BaseAgent
from graph.state import GraphState
from utils.json_parser import extract_json


class QuestionGenerationAgent(BaseAgent):
    """
    Generates FAQ questions as a strict JSON list using LLM reasoning.
    """

    def run(self, state: GraphState) -> GraphState:
        prompt = f"""
You are an FAQ question generation agent.

Your task:
- Generate AT LEAST 15 distinct, user-focused FAQ questions
- Return ONLY valid JSON
- Do NOT include explanations
- Do NOT include markdown

Required JSON format:
{{
  "questions": [
    "question 1",
    "question 2",
    "... at least 15 total"
  ]
}}

Product context:
{state.product_context}
"""

        response = self.llm.invoke(prompt)

        try:
            parsed = extract_json(response.content)

            questions = parsed.get("questions")
            if not isinstance(questions, list) or len(questions) < 15:
                raise ValueError("Less than 15 FAQ questions generated")

            state.faq_questions = questions

        except Exception as e:
            state.errors.append(f"QuestionGenerationAgent failed: {str(e)}")
            raise RuntimeError("Invalid FAQ questions output")

        return state
