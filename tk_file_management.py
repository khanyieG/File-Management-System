import tkinter as tk
import os

root = tk.Tk()
root.title("File management system")
root.geometry("350x300")

def browse_directory():
    selected_dir = tk.filedialog.askdirectory()
    # Update listbox or perform file operations based on selected directory

def list_files(directory):
    files = os.listdir(directory)
    tk.Listbox.delete(0, tk.END)  # Clear listbox contents
    for file in files:
        tk.Listbox.insert(tk.END, file)

def navigate_to_dir(directory):
    list_files(directory)  # Update listbox with files in the new directory


browse_button = tk.Button(root, text="Browse", command=browse_directory)
browse_button.pack()

dir_entry = tk.Entry(root, width=50)
dir_entry.pack()

navigate_button = tk.Button(root, text="Navigate", command=lambda: navigate_to_dir(dir_entry.get()))
navigate_button.pack()

listbox = tk.Listbox(root)
listbox.pack()


root.mainloop()
