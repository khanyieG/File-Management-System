import os

def gaming(path):
    gaming_path = path / "Gaming"  # Use pathlib for concise path joining
    gaming_path.mkdir(parents=True, exist_ok=True)