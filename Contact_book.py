contacts = {}

def add_contact():
    name = input("Enter full name: ").strip().title()
    if name in contacts:
        print(f"Contact for '{name}' already exists.")
        return
    phone = input("Phone number: ").strip()
    email = input("Email address: ").strip()
    address = input("Home address: ").strip()
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print(f"Contact for '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("\nYour contact list is empty.")
        return
    print("\nAll Saved Contacts:")
    for name, details in contacts.items():
        print(f"- {name}: {details['phone']}")

def search_contact():
    name = input("Enter the name to search for: ").strip().title()
    contact = contacts.get(name)
    if contact:
        print(f"\n Contact Details for {name}:")
        for field, value in contact.items():
            print(f"{field.capitalize()}: {value}")
    else:
        print(" No contact found with that name.")

def update_contact():
    name = input("Enter the name of the contact to update: ").strip().title()
    if name in contacts:
        print("Press Enter without typing to keep the current value.")
        phone = input(f"New phone (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"New address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Contact for '{name}' updated.")
    else:
        print("That contact does not exist.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().title()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print(f"🗑️ Contact for '{name}' deleted.")
        else:
            print("Deletion canceled.")
    else:
        print("Contact not found.")

def main_menu():
    while True:
        print("\n====== Contact Book Menu ======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("What would you like to do? (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print(" Exiting Contact Book. See you next time!")
            break
        else:
            print(" Please choose a valid option (1-6).")

main_menu()