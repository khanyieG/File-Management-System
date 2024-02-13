import os
from pathlib import Path

path = "C:/Users/User1/Documents/Pre-Production"

# try:
#     os.mkdir(path)
#     print(f"folder {path}created.")
# except FileExistsError:
#     print(f"folder {path} already exits.")

os.mkdir(os.path.join(path, "Idea", "Research"))
os.mkdir(os.path.join(path, "Scripts" ,"Scenario Production"))
os.mkdir(os.path.join(path, "Storyboarding"))
os.mkdir(os.path.join(path, "Animatic"))
os.mkdir(os.path.join(path, "Characters development"))
os.mkdir(os.path.join(path, "Style framing"))


