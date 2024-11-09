import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def read_file_list(file_list_path):
    """
    Reads a list of files from a text file. Each line in the file is assumed to be a file name.
    """
    with open(file_list_path, 'r') as file_list:
        files = {line.strip() for line in file_list.readlines()}
    return files

def copy_files_with_list(source_dir, target_dir, files_to_copy):
    """
    Copies files listed in files_to_copy from source_dir to target_dir while maintaining directory structure.
    """
    missing_files = []
    for root, dirs, files in os.walk(source_dir):
        matching_files = [f for f in files if f in files_to_copy]
        for file in matching_files:
            source_file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, source_dir)
            target_path = os.path.join(target_dir, relative_path)
            os.makedirs(target_path, exist_ok=True)
            target_file_path = os.path.join(target_path, file)
            try:
                shutil.copy2(source_file_path, target_file_path)
                print(f"Copied {source_file_path} to {target_file_path}")
            except FileNotFoundError:
                missing_files.append(file)
                print(f"Warning: {file} not found in {root}")
    if missing_files:
        print("\nFiles not found in source directory:")
        for missing_file in missing_files:
            print(missing_file)

def select_source_dir():
    source_directory = filedialog.askdirectory(title="Select Source Directory")
    source_dir_var.set(source_directory)

def select_target_dir():
    target_directory = filedialog.askdirectory(title="Select Target Directory")
    target_dir_var.set(target_directory)

def select_file_list():
    file_list_path = filedialog.askopenfilename(
        title="Select File List", filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    file_list_var.set(file_list_path)

def start_copying():
    source_dir = source_dir_var.get()
    target_dir = target_dir_var.get()
    file_list_path = file_list_var.get()

    if not os.path.exists(source_dir):
        messagebox.showerror("Error", "Source directory does not exist.")
        return
    if not os.path.exists(target_dir):
        messagebox.showerror("Error", "Target directory does not exist.")
        return
    if not os.path.isfile(file_list_path):
        messagebox.showerror("Error", "File list not found.")
        return

    files_to_copy = read_file_list(file_list_path)
    copy_files_with_list(source_dir, target_dir, files_to_copy)
    messagebox.showinfo("Success", "Files copied successfully.")

def show_about():
    messagebox.showinfo("About", "File Copier\nDeveloped by Mirza Hasnain Baig\nUsed Chat GPT")

# Initialize the main GUI window
root = tk.Tk()
root.title("YTD File Copier by Mirza Hasnain Baig")
root.geometry("500x300")

# Variables to hold directory paths
source_dir_var = tk.StringVar()
target_dir_var = tk.StringVar()
file_list_var = tk.StringVar()

# GUI layout
tk.Label(root, text="Source Directory:").grid(row=0, column=0, sticky='e', padx=10, pady=10)
tk.Entry(root, textvariable=source_dir_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_source_dir).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Target Directory:").grid(row=1, column=0, sticky='e', padx=10, pady=10)
tk.Entry(root, textvariable=target_dir_var, width=40).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_target_dir).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="File List (TXT):").grid(row=2, column=0, sticky='e', padx=10, pady=10)
tk.Entry(root, textvariable=file_list_var, width=40).grid(row=2, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file_list).grid(row=2, column=2, padx=10, pady=10)

tk.Button(root, text="Start Copying", command=start_copying, width=15).grid(row=3, column=1, pady=20)

# Add the "About" button after initializing the root window
tk.Button(root, text="About", command=show_about).grid(row=4, column=1, pady=10)

# Run the application
root.mainloop()
