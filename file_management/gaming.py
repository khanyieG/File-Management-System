import os


def gaming(path):
    gaming_path = path / "Gaming"  # Use pathlib for concise path joining
    gaming_path.mkdir(parents=True, exist_ok=True)
    code_path= gaming_path / "Code"
    code_path.mkdir(parents=True, exist_ok=True)
    animation_path= gaming_path / "Animation"
    animation_path.mkdir(parents=True, exist_ok=True)
    animation_file = animation_path / "animation.txt"
    animation_file.touch()
    design_path= gaming_path / "Design"
    design_path.mkdir(parents=True, exist_ok=True)