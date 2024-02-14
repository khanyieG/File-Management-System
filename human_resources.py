import os

def human_resources(path):
    human_resources_path = path / "Human resources"  # Use pathlib for concise path joining
    human_resources_path.mkdir(parents=True, exist_ok=True)

    