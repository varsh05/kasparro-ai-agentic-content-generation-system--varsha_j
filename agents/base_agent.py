class BaseAgent:
    """
    Base interface for all agents in the system.

    Each agent must:
    - Have a single responsibility
    - Accept structured input
    - Return structured output
    - Contain no hidden global state
    """

    def run(self, input_data: dict) -> dict:
        raise NotImplementedError(
            "All agents must implement a run(input_data) method"
        )
