
def display_contacts(contacts):
    if not contacts:
        print("No contacts found. Please add a contact first.")
        return
    print("\n=== All Contacts ===")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}")
        print(f"   Phone: {contact['phone']}")
        print(f"   Email: {contact['email']}")
        print(f"   Address: {contact['address']}\n")



