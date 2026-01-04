from memory.retriever import retrieve
from memory.store import store_memory
from behavior.policy import apply_behavior
from llm.local_llm import generate
from reflection.reflector import reflect

USER_ID = "default_user"

SYSTEM_PROMPT = """
You are a technical AI assistant.
You do not describe yourself.
You do not use marketing language.
You follow formatting rules strictly.
"""

print("Agent ready. Type 'exit' to quit.\n")

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break

    # 1️⃣ Retrieve memory BEFORE generation
    memories = retrieve(USER_ID)

    # 🔍 DEBUG (keep this for now)
    print("Retrieved memories:", memories)

    # 2️⃣ Apply behavior rules based on memory
    system_prompt = apply_behavior(SYSTEM_PROMPT, memories)

    # 3️⃣ Build final prompt
    prompt = f"""
{system_prompt}

Relevant memory:
{chr(10).join(memories)}

User: {user_input}
Assistant:
"""

    # 4️⃣ Generate response
    response = generate(prompt)
    print(f"Agent: {response}")

    # 5️⃣ Reflect + store memory AFTER response
    insight = reflect(user_input, response)
    if insight:
        store_memory(USER_ID, insight)
