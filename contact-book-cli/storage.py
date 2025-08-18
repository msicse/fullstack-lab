import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    return []

def save_contact(contacts):
    print("\n=== Add New Contact ===")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

