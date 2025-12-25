class ProductParserAgent:
    """
    Agent responsible for parsing raw product data
    into a clean internal product model.
    """

    def parse(self, raw_data: dict) -> dict:
        return {
            "name": raw_data["name"],
            "concentration": raw_data["concentration"],
            "skin_type": raw_data["skin_type"],
            "ingredients": raw_data["key_ingredients"],
            "benefits": raw_data["benefits"],
            "usage": raw_data["how_to_use"],
            "side_effects": raw_data["side_effects"],
            "price": raw_data["price"]
        }