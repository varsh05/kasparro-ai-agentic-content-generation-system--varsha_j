import os
import time
from langchain_groq import ChatGroq
from groq import RateLimitError


class BaseAgent:
    def __init__(self, temperature: float = 0.2):
        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            raise RuntimeError(
                "GROQ_API_KEY not found. Set it before running the program."
            )

        self.llm = ChatGroq(
            api_key=api_key,              # 🔥 EXPLICITLY PASSED
            model="llama-3.1-8b-instant",
            temperature=temperature,
            max_tokens=300
        )

    def safe_invoke(self, prompt: str):
        for attempt in range(3):
            try:
                return self.llm.invoke(prompt)
            except RateLimitError:
                wait = 2 ** attempt
                print(f"⏳ Rate limit hit, retrying in {wait}s...")
                time.sleep(wait)

        raise RuntimeError("Groq retries exhausted")
