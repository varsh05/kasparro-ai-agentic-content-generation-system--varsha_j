def faq_template(questions: dict) -> list:
    """
    Template for FAQ page
    """
    faq_list = []

    for category, qs in questions.items():
        for q in qs[:1]:  # take at least one question per category
            faq_list.append({
                "category": category,
                "question": q,
                "answer": "This answer is generated based on the product information."
            })

    return faq_list