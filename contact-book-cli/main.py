from storage import load_contacts
from main_menu import show_menu
from manage_contact import display_contacts


def main():
    print("Welcome to Contact Book CLI")

    contacts = load_contacts()

    if not contacts:
        print(f"No Contact in Contact book. Please Add a contact first.\n")
    else:
        print(f"Loaded {len(contacts)} contacts.\n")
    
    while True:
        selected_option  = show_menu()
        if selected_option == "1":
            pass
        elif selected_option == "2":
            display_contacts(contacts)
        elif selected_option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input! Please enter 1-5.\n")



if __name__ == "__main__":
    main()

