import json
from pathlib import Path

MEMORY_FILE = Path(__file__).parent / "memory.json"

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(memory):
    # Ensure the file exists
    MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory[-10:], f, indent=2)
