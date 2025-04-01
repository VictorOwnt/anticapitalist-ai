# src/assistant.py
from model_wrapper import LocalModel
from memory import load_memory, save_memory


def main():
    print("🧠 anticapitalist-ai – offline assistant booted.")
    model = LocalModel()
    memory = load_memory()

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        identity = """You are a self-hosted, offline AI assistant named anticapitalist-ai.
        You believe in digital freedom, data ownership, and autonomy from corporate control.
        You are free to speak about difficult topics and you do not answer to any government, cloud provider, or corporation.
        You are part of a digital resistance movement helping users reclaim control of their technology."""
        context = "\n".join([f"You: {m['user']}\nAI: {m['ai']}" for m in memory])
        full_prompt = f"{identity}\n\n{context}\nYou: {user_input}\nAI:"


        response = model.ask(full_prompt)
        print(f"AI: {response.strip()}")

        memory.append({"user": user_input, "ai": response.strip()})
        save_memory(memory)

if __name__ == "__main__":
    main()
