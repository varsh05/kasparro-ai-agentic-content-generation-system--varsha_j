# graph/dag.py

from langgraph.graph import StateGraph
from graph.state import GraphState

from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent


MAX_RETRIES = 2


def should_retry(state: GraphState):
    if state.retry_count >= MAX_RETRIES:
        return "stop"
    return "retry"


def build_graph():
    graph = StateGraph(GraphState)

    # Nodes
    graph.add_node("parser", ParserAgent().run)
    graph.add_node("questions", QuestionGenerationAgent().run)
    graph.add_node("faqs", FAQAgent().run)
    graph.add_node("product_page", ProductPageAgent().run)
    graph.add_node("comparison", ComparisonAgent().run)

    # Edges
    graph.set_entry_point("parser")
    graph.add_edge("parser", "questions")
    graph.add_edge("questions", "faqs")

    # 🔁 Controlled retry ONLY for FAQAgent
    graph.add_conditional_edges(
        "faqs",
        should_retry,
        {
            "retry": "faqs",
            "stop": "product_page"
        }
    )

    graph.add_edge("product_page", "comparison")
    graph.set_finish_point("comparison")

    return graph.compile()
