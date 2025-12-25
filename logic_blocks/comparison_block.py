def compare_products(product_a: dict, product_b: dict) -> dict:
    """
    Compares two products and returns structured differences.
    """
    return {
        "price_difference": product_a["price"] - product_b["price"],
        "ingredients": {
            "product_a": product_a["ingredients"],
            "product_b": product_b["ingredients"]
        }
    }