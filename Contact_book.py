import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

contacts = {}

# Add Contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Full Name:").strip().title()
    if not name:
        return
    if name in contacts:
        messagebox.showinfo("Duplicate", f"Contact for '{name}' already exists.")
        return
    phone = simpledialog.askstring("Add Contact", "Phone Number:").strip()
    email = simpledialog.askstring("Add Contact", "Email Address:").strip()
    address = simpledialog.askstring("Add Contact", "Home Address:").strip()
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    refresh_contacts()
    messagebox.showinfo("Success", f"Contact for '{name}' added successfully.")

# View Contacts in List
def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for name, details in contacts.items():
        contact_list.insert("", "end", values=(name, details['phone'], details['email'], details['address']))

# Search Contact
def search_contact():
    name = simpledialog.askstring("Search Contact", "Enter Name:").strip().title()
    if not name:
        return
    if name in contacts:
        details = contacts[name]
        messagebox.showinfo("Contact Found", f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
    else:
        messagebox.showinfo("Not Found", "No contact found with that name.")

# Update Contact
def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter Name:").strip().title()
    if name in contacts:
        current = contacts[name]
        phone = simpledialog.askstring("Update Contact", f"New phone (current: {current['phone']}):") or current['phone']
        email = simpledialog.askstring("Update Contact", f"New email (current: {current['email']}):") or current['email']
        address = simpledialog.askstring("Update Contact", f"New address (current: {current['address']}):") or current['address']
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        refresh_contacts()
        messagebox.showinfo("Updated", f"Contact for '{name}' updated successfully.")
    else:
        messagebox.showinfo("Not Found", "That contact does not exist.")

# Delete Contact
def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter Name:").strip().title()
    if name in contacts:
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{name}'?")
        if confirm:
            del contacts[name]
            refresh_contacts()
            messagebox.showinfo("Deleted", f"Contact for '{name}' deleted.")
    else:
        messagebox.showinfo("Not Found", "Contact not found.")

# GUI Setup
root = tk.Tk()
root.title("Premium Contact Book")
root.geometry("700x400")
root.configure(bg="#f9f9f9")

style = ttk.Style()
style.configure("Treeview", font=("Segoe UI", 11), rowheight=28)
style.configure("Treeview.Heading", font=("Segoe UI", 12, "bold"))

# Contact Table
columns = ("Name", "Phone", "Email", "Address")
contact_list = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    contact_list.heading(col, text=col)
    contact_list.column(col, width=150, anchor="center")
contact_list.pack(pady=20, fill="both", expand=True)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f9f9f9")
btn_frame.pack(pady=10)

buttons = [
    ("Add Contact", add_contact),
    ("Search Contact", search_contact),
    ("Update Contact", update_contact),
    ("Delete Contact", delete_contact)
]

for text, cmd in buttons:
    tk.Button(btn_frame, text=text, command=cmd, font=("Segoe UI", 11), bg="#1f4e79", fg="white", relief="flat", padx=10, pady=5).pack(side="left", padx=8)

root.mainloop()
