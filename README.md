# Agentic AI Lab

## Overview

This repository contains implementations of different types of AI agents as part of the **Agentic AI Systems Lab**.
The lab focuses on building agents that can reason, plan, and use tools to perform tasks autonomously.

## Objectives

* Understand AI agent architecture
* Implement rule-based and tool-using agents
* Integrate LLM-based decision making
* Design multi-step planning agents
* Build modular and reusable AI components

---

## Repository Structure

agentic-ai-lab/
│
├── day1/   # Rule-Based Agent
├── day2/   # Tool-Using Agent
├── day3/   # LLM-Based Agent
├── day4/   # Multi-Step Planning Agent
│
└── README.md

## Assignments

### Day 1: Rule-Based AI Agent

* Implements a simple agent using keyword-based logic
* Follows Input → Decision → Action pipeline
* Handles:

  * Greeting
  * Date retrieval
  * Basic calculations

### Day 2: Tool-Using Agent

* Introduces external tools
* Tools implemented:

  * Calculator
  * Weather (mock)
  * Text summarizer
* Agent selects and executes tools based on input

### Day 3: LLM-Based Agent

* Replaces rule-based decision logic with LLM-style reasoning
* Simulated LLM used due to API constraints
* Features:

  * Tool selection using intelligent logic
  * Logging of:

    * Input
    * Selected tool
    * Output

### Day 4: Multi-Step Planning Agent

* Implements planning-based execution
* Breaks tasks into multiple steps
* Supports:

  * Number extraction
  * Average calculation
  * Multiplication
  * Division
  * Result summarization
* Displays intermediate outputs for transparency

## Technologies Used

* Python 3
* Basic NLP techniques (keyword matching, regex)
* Modular programming
* Simulated LLM reasoning

## How to Run

1. Clone the repository:

git clone <https://github.com/Prajwal323-lang/agentic-ai-lab>
cd agentic-ai-lab

2. Run any assignment:
cd day1
python agent.py

(Repeat for day2, day3, day4)

## Key Concepts Demonstrated

* Agent architecture (Input → Decision → Action)
* Tool abstraction and function calling
* LLM-based decision making (simulated)
* Task decomposition and planning
* Sequential execution

## Note

Due to API limitations, LLM behavior in Day 3 is simulated using structured logic. The system is designed such that it can be easily extended with real LLM APIs.



