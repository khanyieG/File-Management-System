
import tkinter as tk
from pathlib import Path
from animation import *
from gaming import *
from human_resources import *


def create_folder():
    new_folder = folder_entry.get()  # Retrieve input from entry widget
    new_dir = Path(new_folder)
    try:
        new_dir.mkdir(parents=True, exist_ok=True)
        select_project_type(new_dir)
        result_label.config(text=f"Folder created: {new_dir}")
    except FileExistsError:
        result_label.config(text=f"Folder {new_folder} already exists.")

def select_project_type(path):
    select_folder = project_type_var.get().lower()
    if select_folder == "animation":
        animation(path)
    elif select_folder == "gaming":
        gaming(path)

    elif select_folder == "human resources":
        human_resources(path)
    else:
        result_label.config(text="Incorrect input. Please choose the given options.")

root = tk.Tk()
root.title("Project Folder Creator")
root.geometry("200x200")

# Input for folder name
folder_label = tk.Label(root, text="Name of your new folder:")
folder_label.pack()
folder_entry = tk.Entry(root)
folder_entry.pack()

# Radio buttons for project types
project_type_var = tk.StringVar()
animation_button = tk.Radiobutton(root, text="Animation", variable=project_type_var, value="animation")
animation_button.pack()

gaming_button = tk.Radiobutton(root, text="Gaming", variable=project_type_var, value="gaming")
gaming_button.pack()

hr_button = tk.Radiobutton(root, text="Human Resources", variable=project_type_var, value="human resources")
hr_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Create folder button
create_button = tk.Button(root, text="Create Folder", command=create_folder)
create_button.pack()

root.mainloop()
