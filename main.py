# main.py

import json
from data import PRODUCT_DATA
from orchestrator.pipeline import Orchestrator

orchestrator = Orchestrator()
result = orchestrator.run(PRODUCT_DATA)

with open("output/product_page.json", "w") as f:
    json.dump(result["product_page"], f, indent=2)

with open("output/faq.json", "w") as f:
    json.dump(result["faq_page"], f, indent=2)

with open("output/comparison_page.json", "w") as f:
    json.dump(result["comparison_page"], f, indent=2)

print("Agentic content generation completed successfully.")
