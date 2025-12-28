🧠 Agentic Content Generation System (Kasparro Assignment)
This repository contains a production-oriented agentic AI system built as part of the Kasparro Applied AI / Agentic Systems assignment.
The system uses LangGraph for explicit orchestration and a real LLM (Groq) to generate structured, machine-readable product content.
The focus of this project is engineering quality, not prompt hacking — emphasizing modular agents, deterministic execution, robustness, and validated JSON outputs.


🚀 Key Highlights
✅ Framework-based agentic architecture (LangGraph DAG)
✅ Real LLM integration using Groq (llama-3.1-8b-instant)
✅ Clearly defined, single-responsibility agents
✅ Retry limits and deterministic fallback handling
✅ Strictly JSON outputs (no free-text pages)
✅ Output schema validation using jsonschema
✅ Execution metadata for traceability and observability
✅ Production-style logging and artifact generation


🧩 System Architecture
The system is orchestrated as a Directed Acyclic Graph (DAG) where each agent performs a specific task and passes structured data to the next stage.
Execution Flow:
Raw Product Input
       ↓
ParserAgent
       ↓
QuestionGenerationAgent
       ↓
FAQAgent (retry + fallback)
       ↓
ProductPageAgent
       ↓
ComparisonAgent
       ↓
Validated JSON Output

LangGraph ensures:
  Explicit execution order
  Controlled retries
  No hidden global state
  Deterministic termination


🤖 Agent Overview
ParserAgent: Normalizes raw product input into a structured product_context.
QuestionGenerationAgent: Uses the LLM to generate 15+ relevant product questions.
FAQAgen: Generates structured FAQs (question–answer pairs).
  Key behaviors:
  Validates LLM output as JSON
  Retries on malformed output
  Uses deterministic fallback when needed
  Always returns valid structured data
ProductPageAgent: Builds a structured product page object using generated content.
ComparisonAgent: Produces a structured comparison between the main product and a competing product.


🔄 Orchestration & State Management
  Implemented using LangGraph StateGraph
  Explicit nodes and edges
  Conditional retry logic with capped attempts
  Shared graph state for all agents
  Guaranteed graph termination


🛡 Robustness & Failure Handling
The system is designed for real-world LLM behavior, including:
  Malformed JSON responses
  Rate limiting
  Partial failures
Safeguards include:
  JSON extraction & validation
  Retry limits
  Graceful fallback logic
  Deterministic completion with valid output
Fallback behavior is treated as a successful terminal state, not a crash.


📦 Output Format
The final output is written as a machine-readable JSON artifact:
D:\Agentic_AI\output\final_output.json

Output includes:
  raw_product_data
  product_context
  faq_questions
  faq
  product_page
  comparison_page
  metadata (execution trace)


🧪 Schema Validation
Before writing the output, the system validates the final state against a JSON Schema using jsonschema, ensuring:
  Structural correctness
  Contract-driven design
  Safe downstream consumption


📊 Execution Metadata
Each run appends a metadata block containing:
  Unique run ID
  Execution timestamp
  LLM model used
  Retry & fallback awareness
  Agents executed
This improves observability and auditability.


🛠 Tech Stack
  Python 3
  LangGraph – agent orchestration
  LangChain
  Groq LLM (llama-3.1-8b-instant)
  jsonschema – output validation
All dependencies are explicitly listed in requirements.txt.


▶️ How to Run
1️⃣ Set environment variable
setx GROQ_API_KEY "your_groq_api_key"
Restart the terminal after setting.

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the system
py main.py


📄 Documentation
Detailed architectural and design explanations are available in:
docs/projectdocumentation.md


🧠 Design Philosophy
This project prioritizes:
  Explicit orchestration over sequential scripts
  Failure-aware LLM integration
  Structured outputs over free text
  Production readiness over demo behavior
The result is a real agentic system, not a deterministic transformation script.

🏁 Summary
This repository demonstrates a framework-backed, production-grade agentic content system with real LLM integration, robust orchestration, and validated machine-readable outputs — aligned with modern applied AI engineering standards.
