from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class GraphState(BaseModel):
    """
    Central state object passed between LangGraph nodes.
    This state enables memory, validation, retries, and orchestration.
    """

    # Input
    raw_product_data: Dict

    # Normalized product data (LLM-assisted)
    product_context: Optional[Dict] = None

    # FAQ generation
    faq_questions: Optional[List[str]] = None
    faqs: Optional[List[Dict]] = None

    # Generated pages
    product_page: Optional[Dict] = None
    comparison_page: Optional[Dict] = None

    # Control & robustness
    retry_count: int = 0
    max_retries: int = 2
    errors: List[str] = Field(default_factory=list)
