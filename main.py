import sys
import os
import json

# Ensure project root is in Python path (Windows-safe)
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from graph.dag import build_graph
from graph.state import GraphState


def main():
    """
    Entry point for the Kasparro Agentic Content Generation System.
    Executes the LangGraph DAG and writes final JSON output.
    """

    # Simulated upstream product input
    raw_product_data = {
        "name": "GlowBoost Vitamin C Serum",
        "ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "skin_type": ["Oily", "Combination"],
        "price": 699
    }

    # Build LangGraph DAG
    graph = build_graph()

    # Initialize shared graph state
    initial_state = GraphState(
        raw_product_data=raw_product_data
    )

    # Execute the agentic workflow
    final_state = graph.invoke(initial_state)

    # Ensure output directory exists
    output_dir = os.path.join(PROJECT_ROOT, "output")
    os.makedirs(output_dir, exist_ok=True)

    # Write final machine-readable JSON output
    output_path = os.path.join(output_dir, "final_output.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_state, f, indent=2)

    # Console output (for verification)
    print("\n===== FINAL GRAPH STATE =====\n")
    print(json.dumps(final_state, indent=2))
    print(f"\n✅ Output written to: {"D:\Agentic_AI\output\final_output.json"}\n")


if __name__ == "__main__":
    main()
