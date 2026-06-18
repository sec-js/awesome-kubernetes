import os
import sys

# Add the project root to python path to resolve imports correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.pr_guardian import auto_format_file

def format_all_files():
    print("[*] Starting global formatting pass on all markdown files...")
    count = 0
    for folder in ["docs", "v2-docs"]:
        if not os.path.exists(folder):
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    auto_format_file(filepath)
                    count += 1
    print(f"[+] Formatting complete. Processed {count} Markdown files.")

if __name__ == "__main__":
    format_all_files()
