import subprocess

MODEL_NAME = "tinyllama"

def generate(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    output = result.stdout.strip()

    # HARD STOP — prevent documents, memos, etc.
    stop_markers = [
        "MEMO",
        "Title:",
        "Table of Contents",
        "Introduction",
        "Conclusion",
        "Date:",
        "Subject:"
    ]

    for marker in stop_markers:
        if marker in output:
            output = output.split(marker)[0].strip()

    return output
