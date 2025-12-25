from agents.parser_agent import ProductParserAgent
from agents.question_agent import QuestionGenerationAgent

from logic_blocks.benefits_block import generate_benefits
from logic_blocks.usage_block import generate_usage
from logic_blocks.safety_block import generate_safety
from logic_blocks.comparison_block import compare_products

from templates.product_template import product_page_template
from templates.faq_template import faq_template
from templates.comparison_template import comparison_template


class Orchestrator:
    """
    Orchestrates the entire agentic content generation pipeline.
    """

    def run(self, raw_product_data: dict) -> dict:
        # Step 1: Parse product data
        parser = ProductParserAgent()
        product = parser.parse(raw_product_data)

        # Step 2: Generate user questions
        question_agent = QuestionGenerationAgent()
        questions = question_agent.generate(product)

        # Step 3: Generate Product Page
        product_page = product_page_template(
            product,
            generate_benefits(product),
            generate_usage(product),
            generate_safety(product)
        )

        # Step 4: Generate FAQ Page
        faq_page = faq_template(questions)

        # Step 5: Create fictional Product B (as required)
        product_b = {
            "name": "RadiantGlow Serum",
            "ingredients": ["Vitamin C", "Niacinamide"],
            "price": 799
        }

        # Step 6: Generate Comparison Page
        comparison_data = compare_products(product, product_b)
        comparison_page = comparison_template(product, product_b, comparison_data)

        return {
            "product_page": product_page,
            "faq_page": faq_page,
            "comparison_page": comparison_page
        }