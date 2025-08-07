import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("320x460")
root.configure(bg="#f5f0e1")

display = tk.Entry(root, font=("Helvetica", 24), borderwidth=0, relief="flat", bg="#fff8dc", justify="right")
display.pack(pady=20, padx=10, fill="x")

keys = [['7', '8', '9', '/'],
        ['4', '5', '6', '*'],
        ['1', '2', '3', '-'],
        ['C', '0', '=', '+']]

def tap(e):
    k = e.widget.cget("text")
    if k == "=":
        try:
            r = str(eval(display.get()))
            display.delete(0, tk.END)
            display.insert(tk.END, r)
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif k == "C":
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, k)

pad = tk.Frame(root, bg="#f5f0e1")
pad.pack()

for row in keys:
    r = tk.Frame(pad, bg="#f5f0e1")
    r.pack(pady=5)
    for ch in row:
        b = tk.Button(r, text=ch, font=("Helvetica", 18), width=5, height=2, bg="#deb887", fg="black", activebackground="#cd853f", relief="flat")
        b.pack(side="left", padx=5)
        b.bind("<Button-1>", tap)

root.mainloop()