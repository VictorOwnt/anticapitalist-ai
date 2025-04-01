from gpt4all import GPT4All
from pathlib import Path

class LocalModel:
    def __init__(self):
        model_path = Path.home() / "Library" / "Application Support" / "nomic.ai" / "GPT4All" / "qwen2.5-coder-7b-instruct-q4_0.gguf"
        self.model = GPT4All(str(model_path))

    def ask(self, prompt: str) -> str:
        with self.model.chat_session():
            return self.model.generate(prompt)
