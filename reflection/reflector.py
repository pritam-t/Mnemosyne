from memory.store import store_memory

def reflect(user_input: str, response: str):
    text = user_input.lower()

    if "prefer" in text or "i like" in text:
        return f"User preference: {user_input}"

    return None
