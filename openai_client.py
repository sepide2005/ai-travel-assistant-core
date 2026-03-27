import os

OPENAI_CHAT_MODEL = "gpt-4o-mini"

def get_system_prompt():
    return """
You are a travel assistant.

Rules:
- Provide helpful travel suggestions
- Keep answers structured and clear
"""
