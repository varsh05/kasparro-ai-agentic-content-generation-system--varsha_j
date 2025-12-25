def product_page_template(product, benefits, usage, safety):
    """
    Template for product description page
    """
    return {
        "product_name": product["name"],
        "description": f"{product['name']} is a skincare serum with {product['concentration']}.",
        "skin_type": product["skin_type"],
        "key_ingredients": product["ingredients"],
        "benefits": benefits,
        "how_to_use": usage,
        "safety_information": safety,
        "price": product["price"]
    }