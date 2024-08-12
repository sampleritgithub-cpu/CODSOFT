import tkinter as tk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks from the list
def clear_tasks():
    listbox_tasks.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place the task entry field
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Create and place the add task button
button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(pady=5)

# Create and place the listbox to display tasks
listbox_tasks = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
listbox_tasks.pack(pady=10)

# Create and place the delete and clear buttons
button_delete_task = tk.Button(root, text="Delete Task", command=delete_task)
button_delete_task.pack(pady=5)

button_clear_tasks = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
button_clear_tasks.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()
