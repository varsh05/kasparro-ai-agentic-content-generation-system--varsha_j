class QuestionGenerationAgent:
    """
    Agent responsible for generating categorized
    user questions from product data.
    """

    def generate(self, product: dict) -> dict:
        return {
            "informational": [
                f"What is {product['name']}?",
                "What are the key ingredients?",
                "What are the benefits of this product?"
            ],
            "usage": [
                "How should this serum be applied?",
                "When is the best time to use it?",
                "Can it be used daily?"
            ],
            "safety": [
                "Are there any side effects?",
                "Is it suitable for sensitive skin?",
                "Can it cause irritation?"
            ],
            "purchase": [
                "What is the price of the product?",
                "Is this product affordable?",
                "Where can I buy it?"
            ],
            "comparison": [
                "How is this different from other Vitamin C serums?",
                "Is it better than similar products?",
                "How does it compare in price?"
            ]
        }