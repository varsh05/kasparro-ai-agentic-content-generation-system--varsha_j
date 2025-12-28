Kasparro Agentic Content Generation System

1. Project Overview

This project implements a production-oriented agentic content generation system using LangGraph for orchestration and a real Large Language Model (Groq) for intelligent content generation.
The system is designed to generate structured, machine-readable product content (FAQs, product pages, and comparisons) through a modular multi-agent architecture, with built-in robustness against LLM failures such as malformed outputs or rate limits.
This implementation emphasizes:
        Clear agent responsibilities
        Explicit orchestration (DAG)
        Reusable logic blocks
        Deterministic termination
        JSON-only outputs suitable for downstream systems

-------------------------------------------------------

2. High-Level Architecture
The system follows an agent-oriented DAG (Directed Acyclic Graph) pattern.
Execution Flow:
        Raw Product Input
        ↓
        ParserAgent
        ↓
        QuestionGenerationAgent
        ↓
        FAQAgent (with retry + fallback)
        ↓
        ProductPageAgent
        ↓
        ComparisonAgent
        ↓
        Validated JSON Output

The workflow is orchestrated using LangGraph, ensuring:
        Explicit control over execution order
        Controlled retries
        No hidden global state
        Deterministic termination

-------------------------------------------------------

3. Agent Responsibilities
Each agent has a single responsibility, defined inputs, and structured outputs.

3.1 ParserAgent
Responsibility:
        Normalizes raw product input into a structured product_context.
Input:
        raw_product_data
Output:
        product_context

3.2 QuestionGenerationAgent
Responsibility:
        Generates a list of 15+ product-relevant questions using the LLM.
Input:
        product_context
Output:
        faq_questions (List of strings)

3.3 FAQAgent
Responsibility:
        Generates structured FAQs (question–answer pairs) using the LLM.
Key Features:
        JSON validation of LLM output
        Retry mechanism
        Deterministic fallback if JSON is invalid
        Retry limit enforcement
Input:
        faq_questions
        product_context
Output:
        faqs (List of {question, answer} objects)

3.4 ProductPageAgent
Responsibility:
        Composes a structured product page using extracted and generated content.
Input:
        product_context
        faqs
Output:
        product_page (Structured JSON object)

3.5 ComparisonAgent
Responsibility:
        Generates a structured comparison between the primary product and a competing product.
Input:
        product_page
Output:
        comparison_page (Structured JSON object)

-------------------------------------------------------

4. Orchestration & State Management
4.1 LangGraph DAG
The system uses LangGraph’s StateGraph to define:
        Entry points
        Agent nodes
        Conditional edges for retries
        Explicit termination
Retries are capped, and fallback outputs are treated as successful terminal states, preventing infinite loops.

4.2 Shared Graph State
The shared state (GraphState) carries all intermediate and final outputs, including:
        Product data
        Generated questions
        FAQ
        Product page
        Comparison page
        Retry metadata
No agent mutates global state outside the DAG.

-------------------------------------------------------

5. Robustness & Failure Handling
The system is explicitly designed to handle real-world LLM failures:
Implemented Safeguards
        JSON extraction & validation for all LLM outputs
        Retry limits to avoid infinite loops
        Graceful fallback for malformed LLM responses
        Rate-limit awareness
        Deterministic graph termination
Fallback behavior ensures that the system always produces valid JSON output, even under degraded LLM conditions.

-------------------------------------------------------

6. Output Structure & Validation
6.1 Machine-Readable Output
The final output is written to: D:\Agentic_AI\output\final_output.json
The output is strictly JSON, containing:
        raw_product_data
        product_context
        faq_questions
        faqs
        product_page
        comparison_page
        metadata

6.2 Schema Validation
Before writing the output, the system validates the final state against a JSON schema using jsonschema.
This ensures:
        Structural correctness
        Contract-driven output
        Safe downstream consumption

-------------------------------------------------------

7. Execution Metadata & Observability
Each run appends a metadata block to the output, including:
        Unique run ID
        Execution timestamp
        LLM model use
        Retry information
        Fallback awareness
        Agents executed
This improves:
        Traceability
        Debuggability
        Auditability

-------------------------------------------------------

8. Technology Stack
        Python 3
        LangGraph – Agent orchestration (DAG)
        LangChain
        Groq LLM (llama-3.1-8b-instant)
        jsonschema – Output validation
All dependencies are explicitly declared in requirements.txt.

-------------------------------------------------------

9. Design Principles
This system was designed with the following principles:
        Single-responsibility agents
        Explicit orchestration over implicit control flow
        Failure-aware LLM integratio
        Machine-readable outputs over free text
        Production-style logging and artifacts

-------------------------------------------------------

10. Summary
This project demonstrates a real, framework-based agentic content system, not a sequential script. It integrates a live LLM, handles failures gracefully, and produces validated JSON outputs suitable for real-world applications.
The design emphasizes clarity, robustness, and extensibility — aligning with industry expectations for applied AI systems.