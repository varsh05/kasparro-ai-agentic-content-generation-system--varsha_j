import json
import re


def extract_json(text: str) -> dict:
    """
    Extract and parse JSON from LLM output.

    Handles:
    - Raw JSON
    - ```json fenced blocks
    - Extra text before/after JSON

    Raises:
    - ValueError if valid JSON cannot be extracted
    """

    if not isinstance(text, str):
        raise ValueError("LLM output is not a string")

    # Remove markdown fences if present
    cleaned = re.sub(r"```json|```", "", text, flags=re.IGNORECASE).strip()

    # Try direct JSON parsing
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        pass

    # Try extracting JSON object using regex
    json_match = re.search(r"\{[\s\S]*\}", cleaned)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON structure: {e}")

    raise ValueError("No valid JSON found in LLM output")
