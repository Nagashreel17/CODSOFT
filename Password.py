import tkinter as tk
from tkinter import StringVar
import random
import string
class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.length_label = tk.Label(root, text="Password Length:")
        self.length_label.pack()

        self.length_var = StringVar()
        self.length_entry = tk.Entry(root, textvariable=self.length_var)
        self.length_entry.pack()

        self.complexity_label = tk.Label(root, text="Password Complexity:")
        self.complexity_label.pack()

        self.complexity_var = StringVar()
        self.complexity_var.set("Medium")

        self.complexity_options = ["Low", "Medium", "High"]
        self.complexity_menu = tk.OptionMenu(root, self.complexity_var, *self.complexity_options)
        self.complexity_menu.pack()

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.pack()

        self.result_var = StringVar()
        self.password_entry = tk.Entry(root, textvariable=self.result_var, state='readonly', width=50)
        self.password_entry.pack()
    def generate_password(self):
        length = int(self.length_var.get())
        complexity = self.complexity_var.get()

        if complexity == "Low":
            characters = string.ascii_letters + string.digits
        elif complexity == "Medium":
            characters = string.ascii_letters + string.digits + string.punctuation
        elif complexity == "High":
            characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_var.set(password)

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
