import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Too Short", "Oops! Let’s aim for at least 4 characters for a safer password ")
            return
        all_chars = string.ascii_letters + string.digits + string.punctuation
        final_password = ''.join(random.choice(all_chars) for _ in range(length))
        result_var.set(final_password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number, my friend")

root = tk.Tk()
root.title(" Password Generator ")
root.geometry("450x280")
root.resizable(False, False)

canvas = tk.Canvas(root, width=450, height=280)
canvas.pack(fill="both", expand=True)
for i in range(0, 280):
    r = 210 - i//4
    g = 235 - i//5
    b = 215 - i//6
    color = f"#{r:02x}{g:02x}{b:02x}"
    canvas.create_line(0, i, 450, i, fill=color)

title_label = tk.Label(root, text="Password Generator", 
                       font=("Segoe UI", 14, "bold"), bg="#d2ead7", fg="#2d5a4e")
title_label.place(relx=0.5, rely=0.12, anchor="center")

prompt_label = tk.Label(root, text="How long should your password be?", 
                        font=("Segoe UI", 12), bg="#d2ead7", fg="#2d5a4e")
prompt_label.place(relx=0.5, rely=0.28, anchor="center")

length_entry = tk.Entry(root, font=("Segoe UI", 12), justify='center', bd=2, relief="ridge")
length_entry.place(relx=0.5, rely=0.38, anchor="center", width=120)

generate_btn = tk.Button(root, text=" Generate ", font=("Segoe UI", 12, "bold"), 
                         bg="#88c999", fg="white", activebackground="#6ab07d", 
                         relief="flat", command=generate_password, cursor="hand2")
generate_btn.place(relx=0.5, rely=0.5, anchor="center")

result_var = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result_var, font=("Segoe UI", 12, "bold"), 
                        justify='center', state='readonly', bd=2, relief="ridge")
result_entry.place(relx=0.5, rely=0.62, anchor="center", width=250)

root.mainloop()
