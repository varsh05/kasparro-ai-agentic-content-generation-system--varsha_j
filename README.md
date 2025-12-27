Kasparro AI – Agentic Content Generation System

This repository contains a modular, agentic automation system built as part of the Kasparro Applied AI Engineer challenge.  
The system transforms structured product data into multiple machine-readable JSON content pages using clearly defined agents, reusable logic blocks, a DAG-style orchestration pipeline, and a custom template engine.

---

🎯 Objective

Design and implement a production-style multi-agent content generation system that demonstrates:
- Clear agent boundaries
- Automation flow / orchestration graph (DAG-style pipeline)
- Reusable content logic blocks
- Template-based content generation
- Structured, machine-readable JSON output

The focus of this project is system design and automation engineering, not UI or content writing.

---

🏗️ System Architecture Overview

The system follows an orchestrator → worker agent pattern with a Directed Acyclic Graph (DAG) style execution flow.

High-Level Flow
Raw Product Data
|
v
ProductParserAgent
|
v
QuestionGenerationAgent
|
v
Orchestrator (DAG Pipeline)
|
v
Logic Blocks + Templates
|
v
JSON Output Pages

---

🤖 Agents

Each agent:
- Has a single responsibility
- Uses explicit input/output contracts
- Maintains no hidden global state
- Implements a common run(input_data) interface

Implemented Agents:
- ProductParserAgent
  Parses raw product data into a normalized internal model.
- QuestionGenerationAgent 
  Generates categorized user questions from structured product data.

---

🔄 Orchestration Flow (DAG)

The automation pipeline is implemented as a step-based DAG, executed by a central orchestrator.

Execution order:
1. Parse product data
2. Generate categorized user questions
3. Assemble Product Description page
4. Assemble FAQ page
5. Assemble Comparison page

This ensures deterministic execution with clear data dependencies and no cyclic flow.

---

🧩 Reusable Logic Blocks

Reusable logic blocks apply deterministic rules to structured data and are independent of agents and templates.

Examples:
- Benefits extraction
- Usage instruction extraction
- Safety information extraction
- Product comparison logic

These blocks can be reused across multiple templates and page types.

---

📐 Template Engine

The system includes a custom template engine where each template defines:
- Output fields
- Formatting rules
- Explicit dependencies on logic blocks or agent outputs

Templates are free of business logic and focus only on structure and assembly.

Implemented Templates
- Product Description Page
- FAQ Page
- Comparison Page

---

📄 Output Files

The system generates the following **machine-readable JSON files**:

- product_page.json
- faq.json
- comparison_page.json

All outputs are deterministic and suitable for downstream system consumption.

---

🚀 How to Run

Prerequisites
- Python 3.8+

Steps

bash
py main.py

---

📘 Documentation
docs/projectdocumentation.md






