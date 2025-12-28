from pydantic import BaseModel
from typing import Dict, List, Any, Optional
from typing_extensions import Annotated


class GraphState(BaseModel):
    """
    Shared state for the agentic system.

    IMPORTANT DESIGN NOTES:
    - raw_product_data is IMMUTABLE input (written once)
    - All other fields are updated incrementally by agents
    - Agents MUST return partial dict updates, not full state
    """

    # --------------------
    # Immutable input
    # --------------------
    raw_product_data: Annotated[Dict[str, Any], "input"]

    # --------------------
    # Agent-generated state
    # --------------------
    product_context: Optional[Dict[str, Any]] = None
    faq_questions: Optional[List[str]] = None
    faqs: Optional[List[Dict[str, str]]] = None
    product_page: Optional[Dict[str, Any]] = None
    comparison_page: Optional[Dict[str, Any]] = None

    # --------------------
    # System metadata
    # --------------------
    retry_count: int = 0
    max_retries: int = 2
    errors: List[str] = []
