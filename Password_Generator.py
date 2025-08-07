import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Go for at least 4 characters for a stronger password.")
            return

        all_chars = string.ascii_letters + string.digits + string.punctuation
        final_password = ''.join(random.choice(all_chars) for _ in range(length))
        result_var.set(final_password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

root = tk.Tk()
root.title("Human-style Password Maker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="How long do you want your password?", font=("Arial", 12)).pack(pady=10)

length_entry = tk.Entry(root, font=("Arial", 12), justify='center')
length_entry.pack()

tk.Button(root, text="Generate My Password", font=("Arial", 12), command=generate_password).pack(pady=10)

result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 12), justify='center', state='readonly').pack()

root.mainloop()