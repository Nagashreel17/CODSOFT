import tkinter as tk
from tkinter import messagebox, simpledialog


class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(root, text="Add Task", command=self.add_task)
        add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        update_button = tk.Button(root, text="Update Task", command=self.update_task)
        update_button.pack()

        delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        delete_button.pack()

        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.pack()
    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = simpledialog.askstring("Update Task", "Enter the updated task:")
            if updated_task:
                self.tasks[selected_index[0]] = updated_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task)
        else:
            messagebox.showwarning("Warning", "Please select a task to update.")
    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_to_delete = self.task_listbox.get(selected_index)
            confirm = messagebox.askokcancel("Confirm Deletion", f"Do you want to delete the task: {task_to_delete}?")
            if confirm:
                self.tasks.pop(selected_index[0])
                self.task_listbox.delete(selected_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()