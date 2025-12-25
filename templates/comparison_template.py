def comparison_template(product_a, product_b, comparison_data):
    """
    Template for product comparison page
    """
    return {
        "product_a": {
            "name": product_a["name"],
            "price": product_a["price"],
            "ingredients": product_a["ingredients"]
        },
        "product_b": {
            "name": product_b["name"],
            "price": product_b["price"],
            "ingredients": product_b["ingredients"]
        },
        "comparison_summary": comparison_data
    }