class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print("Contact already exists!")
        else:
            self.contacts[name] = {
                'phone': phone,
                'email': email,
                'address': address
            }
            print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")

    def search_contact(self, keyword):
        found = False
        for name, details in self.contacts.items():
            if keyword.lower() in name.lower() or keyword in details['phone']:
                print(f"\nFound Contact:")
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
                found = True
        if not found:
            print("No matching contacts found.")

    def update_contact(self, name):
        if name in self.contacts:
            print("Enter new details (leave blank to keep unchanged):")
            phone = input("Phone: ") or self.contacts[name]['phone']
            email = input("Email: ") or self.contacts[name]['email']
            address = input("Address: ") or self.contacts[name]['address']
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            contact_book.add_contact(name, phone, email, address)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            contact_book.search_contact(keyword)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
