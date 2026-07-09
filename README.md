# Project 1: Rule-Based AI Chatbot

## Overview

This project is the foundation phase of the DecodeLabs AI Internship. Before building systems that "learn" using machine learning, this project focuses on **control flow and logic** — the building blocks of any intelligent system.

The chatbot uses a dictionary-based rule system (instead of a long if-elif chain) to match user input to predefined responses, and runs in a continuous loop until the user exits.

## Features

- Continuous chat loop (`while True`)
- Input sanitization (handles case sensitivity and extra whitespace)
- Dictionary-based knowledge base with 10+ intents
- Fallback response for unrecognized input
- Clean exit commands (`bye`, `exit`, `quit`)

## Why a Dictionary Instead of If-Elif?

An if-elif ladder checks conditions one by one (O(n) complexity) and becomes hard to maintain as more rules are added. A dictionary lookup (`.get()`) is O(1) — constant time — regardless of how many rules exist, and keeps the code clean and scalable.

## How to Run

```bash
python chatbot.py
```

Then start chatting! Try inputs like:

- `hello`
- `how are you`
- `who is sabaoon`
- `your name`
- `bye` (to exit)

## Example Interaction

```
Chatbot: Hello Pookie! I'm a rule-based chatbot.Remember to type: 'bye' or 'exit' to end the chat.

You: hello
Chatbot: Hi there! How can I help you today?

You: who is sabaoon
Chatbot: Sabaoon is a BS Computer Science Graduate and She loves to explore new technologies!

You: bye
Chatbot: Goodbye! Have a nice day. 👋
```

## Key Concepts Practiced

- Control flow (loops, conditionals)
- Dictionaries / hash maps for fast lookups
- Input normalization and sanitization
- Designing a simple, deterministic ("white box") system — a foundation for understanding AI guardrails used in real-world LLM applications

## Tech Stack

- Python 3

---

Built as part of the DecodeLabs AI Internship.
