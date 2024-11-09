import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_file():
    """Open a file dialog to select the text file with folder names."""
    file_path = filedialog.askopenfilename(
        title="Select Text File with Folder Names",
        filetypes=[("Text Files", "*.txt")]
    )
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def select_directory():
    """Open a directory dialog to select the parent directory for folder creation."""
    directory_path = filedialog.askdirectory(title="Select Parent Directory")
    folder_entry.delete(0, tk.END)
    folder_entry.insert(0, directory_path)

def create_folders():
    """Read folder names from file and create them in the specified directory."""
    file_path = file_entry.get()
    parent_directory = folder_entry.get()

    # Check if paths are provided
    if not file_path or not parent_directory:
        messagebox.showwarning("Warning", "Please select both file and directory.")
        return

    # Try to read the file and create folders
    try:
        with open(file_path, 'r') as file:
            folder_names = [line.strip() for line in file.readlines()]

        created_folders = []
        existing_folders = []

        for folder_name in folder_names:
            folder_path = os.path.join(parent_directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                created_folders.append(folder_name)
            else:
                existing_folders.append(folder_name)

        # Show results
        result_message = (
            f"Created Folders:\n" + "\n".join(created_folders) +
            "\n\nExisting Folders:\n" + "\n".join(existing_folders)
        )
        messagebox.showinfo("Result", result_message)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_about():
    """Show an 'About' popup with information about the tool."""
    messagebox.showinfo("About", "Folder Creator Tool\nBy Mirza Hasnain Baig\nBuilt by ChatGPT\n"
                                 "This tool reads a list of folder names from a text file "
                                 "and creates folders in a selected parent directory.")

# Setup GUI
app = tk.Tk()
app.title("Folder Creator Tool By Mirza Hasnain Baig")

# Title label
title_label = tk.Label(app, text="Folder Creator Tool", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=(10, 20))

# File selection section
file_label = tk.Label(app, text="Text File with Folder Names:")
file_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
file_entry = tk.Entry(app, width=40)
file_entry.grid(row=1, column=1, padx=10, pady=5)
file_button = tk.Button(app, text="Browse", command=select_file)
file_button.grid(row=1, column=2, padx=10, pady=5)

# Folder selection section
folder_label = tk.Label(app, text="Parent Directory:")
folder_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
folder_entry = tk.Entry(app, width=40)
folder_entry.grid(row=2, column=1, padx=10, pady=5)
folder_button = tk.Button(app, text="Browse", command=select_directory)
folder_button.grid(row=2, column=2, padx=10, pady=5)

# Create button
create_button = tk.Button(app, text="Create Folders", command=create_folders, bg="lightgreen")
create_button.grid(row=3, column=1, padx=10, pady=(15, 10))

# About button
about_button = tk.Button(app, text="About", command=show_about)
about_button.grid(row=4, column=1, padx=10, pady=(5, 15))

# Start the GUI event loop
app.mainloop()
