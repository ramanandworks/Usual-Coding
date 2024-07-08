import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

CONTACTS_FILE = 'contacts.json'
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)
class ContactBookApp:
    def __init__(self, root):
        self.contacts = load_contacts()
        self.root = root
        self.root.title("Contact Book")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=0, column=0, padx=5, pady=5)

        self.view_button = tk.Button(self.frame, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = tk.Button(self.frame, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.update_button = tk.Button(self.frame, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=0, column=3, padx=5, pady=5)

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=0, column=4, padx=5, pady=5)

        self.contacts_listbox = tk.Listbox(self.frame, width=80, height=20)
        self.contacts_listbox.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
        self.refresh_contacts_list()
    def refresh_contacts_list(self):
        self.contacts_listbox.delete(0, tk.END)
        for name, details in self.contacts.items():
            self.contacts_listbox.insert(tk.END, f"Name: {name}, Phone: {details['phone']}")
    def add_contact(self):
        name = simpledialog.askstring("Add Contact", "Enter name:")
        phone = simpledialog.askstring("Add Contact", "Enter phone number:")
        email = simpledialog.askstring("Add Contact", "Enter email:")
        address = simpledialog.askstring("Add Contact", "Enter address:")

        if name and phone and email and address:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            save_contacts(self.contacts)
            self.refresh_contacts_list()
            messagebox.showinfo("Success", f"Contact {name} added.")
        else:
            messagebox.showwarning("Error", "All fields are required.")
    def view_contacts(self):
        self.refresh_contacts_list()
    def search_contact(self):
        search = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        found = False
        for name, details in self.contacts.items():
            if search.lower() in name.lower() or search in details['phone']:
                messagebox.showinfo("Contact Found",
                                    f"Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}")
                found = True
                break
        if not found:
            messagebox.showwarning("Not Found", "Contact not found.")
    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:")
        if name in self.contacts:
            phone = simpledialog.askstring("Update Contact", "Enter new phone number (leave blank to keep current):")
            email = simpledialog.askstring("Update Contact", "Enter new email (leave blank to keep current):")
            address = simpledialog.askstring("Update Contact", "Enter new address (leave blank to keep current):")

            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
            if address:
                self.contacts[name]['address'] = address

            save_contacts(self.contacts)
            self.refresh_contacts_list()
            messagebox.showinfo("Success", f"Contact {name} updated.")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")
    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:")
        if name in self.contacts:
            del self.contacts[name]
            save_contacts(self.contacts)
            self.refresh_contacts_list()
            messagebox.showinfo("Success", f"Contact {name} deleted.")
        else:
            messagebox.showwarning("Not Found", "Contact not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()