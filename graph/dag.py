from langgraph.graph import StateGraph, END
from graph.state import GraphState

from agents.parser_agent import ParserAgent
from agents.question_agent import QuestionGenerationAgent
from agents.faq_agent import FAQAgent
from agents.product_agent import ProductPageAgent
from agents.comparison_agent import ComparisonAgent


def build_graph():
    """
    Builds a LangGraph DAG with stateful AI agents.
    """

    graph = StateGraph(GraphState)

    # Instantiate agents
    parser = ParserAgent()
    question_agent = QuestionGenerationAgent()
    faq_agent = FAQAgent()
    product_agent = ProductPageAgent()
    comparison_agent = ComparisonAgent()

    # Register nodes
    graph.add_node("parse_product", parser.run)
    graph.add_node("generate_questions", question_agent.run)
    graph.add_node("generate_faqs", faq_agent.run)
    graph.add_node("generate_product_page", product_agent.run)
    graph.add_node("generate_comparison", comparison_agent.run)

    # Define execution flow (DAG)
    graph.set_entry_point("parse_product")

    graph.add_edge("parse_product", "generate_questions")
    graph.add_edge("generate_questions", "generate_faqs")
    graph.add_edge("generate_faqs", "generate_product_page")
    graph.add_edge("generate_product_page", "generate_comparison")

    graph.add_edge("generate_comparison", END)

    return graph.compile()
