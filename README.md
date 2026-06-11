# Rule-Based AI Chatbot — Project 1

**DecodeLabs Industrial Training Kit | Batch 2026**

## Project Overview
A rule-based AI chatbot built using pure Python control flow and dictionary-based
intent matching. This is the foundation project demonstrating deterministic AI logic.

## Architecture: IPO Model
- **INPUT** — Raw user text, sanitized via `.lower().strip()`
- **PROCESS** — Intent matched via O(1) dictionary lookup (`.get()` method)
- **OUTPUT** — Response printed; loop continues until exit command

## Folder Structure

rule-based-chatbot/
── chatbot.py       # Main engine: loop, sanitization, response logic.
── responses.py     # Knowledge base: dictionary of 15+ intents.
── README.md        # Project documentation.
── .gitignore       # Files to exclude from Git.

## Author
Built as part of the DecodeLabs AI Industrial Training — Batch 2026.