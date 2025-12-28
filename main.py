import sys
import os
import json
import uuid
from datetime import datetime

from jsonschema import validate, ValidationError

# Ensure project root is in Python path (Windows-safe)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from graph.dag import build_graph
from graph.state import GraphState
from schemas.final_output_schema import FINAL_OUTPUT_SCHEMA


def main():
    """
    Entry point for the Kasparro Agentic Content Generation System.
    Executes the LangGraph DAG, validates output, and writes final JSON artifact.
    """

    print("🔥 Kasparro Agentic System starting...")

    # -------------------------------
    # Simulated upstream product input
    # -------------------------------
    raw_product_data = {
        "name": "GlowBoost Vitamin C Serum",
        "ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "skin_type": ["Oily", "Combination"],
        "price": 699
    }

    # -------------------------------
    # Build and execute LangGraph DAG
    # -------------------------------
    graph = build_graph()
    initial_state = GraphState(raw_product_data=raw_product_data)

    print("🚀 Executing agentic workflow...")
    final_state = graph.invoke(initial_state)
    print("✅ Workflow completed successfully")

    # -------------------------------
    # Attach execution metadata
    # -------------------------------
    final_state["metadata"] = {
        "run_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat(),
        "model": "llama-3.1-8b-instant",
        "max_retries": final_state.get("max_retries"),
        "fallback_used": final_state.get("retry_count", 0) > 0,
        "agents_executed": [
            "ParserAgent",
            "QuestionGenerationAgent",
            "FAQAgent",
            "ProductPageAgent",
            "ComparisonAgent"
        ]
    }

    # -------------------------------
    # Validate final output structure
    # -------------------------------
    try:
        validate(instance=final_state, schema=FINAL_OUTPUT_SCHEMA)
        print("🧪 Output schema validation passed")
    except ValidationError as e:
        raise RuntimeError(f"Output schema validation failed: {e}")

    # -------------------------------
    # Write final JSON output (explicit path)
    # -------------------------------
    output_dir = r"D:\Agentic_AI\output"
    os.makedirs(output_dir, exist_ok=True)

    output_path = r"D:\Agentic_AI\output\final_output.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_state, f, indent=2)

    print(f"📄 Final output written to: {output_path}")
    print("🎯 System finished cleanly without errors")


if __name__ == "__main__":
    main()
