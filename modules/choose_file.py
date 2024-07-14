import tkinter as tk
from tkinter import filedialog
import json

def choose_json_file():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open file dialog to choose a JSON file
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        title="Choose a JSON file"
    )

    # Return the selected file path
    return file_path