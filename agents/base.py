from abc import ABC, abstractmethod
from langchain_groq import ChatGroq
from graph.state import GraphState


class BaseAgent(ABC):
    """
    Abstract base class for all AI agents.
    Each agent must:
    - Use an LLM
    - Read from shared state
    - Write back to shared state
    """

    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.3):
        self.llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=temperature
        )

    @abstractmethod
    def run(self, state: GraphState) -> GraphState:
        """
        Execute agent logic using LLM and update shared state.
        """
        pass
