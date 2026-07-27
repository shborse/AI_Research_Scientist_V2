import os

os.makedirs("reports", exist_ok=True)

def save_markdown(filename, content):
    with open(f"reports/{filename}", "w", encoding="utf-8") as f:
        f.write(content)