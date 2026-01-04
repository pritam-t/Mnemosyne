def apply_behavior(system_prompt: str, memories: list):
    for m in memories:
        if "concise" in m.lower():
            return """
You are a technical assistant.

RESPONSE RULES (MANDATORY):
- Bullet points only
- Maximum 5 bullets
- Maximum 12 words per bullet
- No introductions
- No conclusions
- No metaphors
- No business or marketing language
- No self-reference
"""
    return system_prompt
