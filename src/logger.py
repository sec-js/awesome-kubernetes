import os
import sys
from datetime import datetime

# Ruta por defecto para el log local (fuera del repo)
DEFAULT_LOG_PATH = "/home/inafev/.gemini/tmp/awesome-kubernetes/curation_progress.log"

def log_event(message: str, section_break: bool = False):
    """
    Logs an event to both console (STDOUT) and local log file if it exists.
    In GitHub Actions, this will appear in the workflow logs.
    """
    timestamp = datetime.now().strftime('%H:%M:%S')
    formatted_msg = f"[{timestamp}] {message}"
    
    if section_break:
        separator = "=" * 60
        print(f"\n{separator}\n{formatted_msg}\n{separator}", flush=True)
        _write_to_file(f"\n{separator}\n{formatted_msg}\n{separator}")
    else:
        print(formatted_msg, flush=True)
        _write_to_file(formatted_msg)
    
    # Mandate 13: Ensure immediate visibility and prevent GHA agent stuttering
    sys.stdout.flush()

def _write_to_file(message: str):
    # Only try to write to file if not in GitHub Actions
    if not os.getenv("GITHUB_ACTIONS"):
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(DEFAULT_LOG_PATH), exist_ok=True)
            with open(DEFAULT_LOG_PATH, "a") as f:
                f.write(message + "\n")
        except Exception as e:
            print(f"[WARN] write to log file: {str(e)[:100]}")
