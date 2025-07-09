contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    
    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.\n")
        return
    
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    print("\n--- Search Contact ---")
    query = input("Enter name or phone number to search: ").lower()
    found = False

    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True

    if not found:
        print("No matching contact found.\n")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ").lower()
    
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave a field blank to keep it unchanged.")
            new_name = input("New Name: ")
            new_phone = input("New Phone Number: ")
            new_email = input("New Email: ")
            new_address = input("New Address: ")

            if new_name:
                contact['name'] = new_name
            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated successfully!\n")
            return
    
    print("Contact not found.\n")

def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    
    print("Contact not found.\n")

def display_menu():
    print("======= Contact Management System =======")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

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
            print("Thank you for using the Contact Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

# Run the program
main()