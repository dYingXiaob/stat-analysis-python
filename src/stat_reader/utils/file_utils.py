from pathlib import Path

def get_extension(path):
    return Path(path).suffix.lower()