from storage import load_contacts
from main_menu import show_menu



def main():
    print("Welcome to Contact Book CLI")

    contacts = load_contacts()
    if len(contacts) > 0:
        print(f"Loaded {len(contacts)} contacts.\n")
    else:
        print(f"No Contact in Contact book. Please Add a contact \n")
    
    while True:
        selected_option  = show_menu()
        if selected_option == "1":
            pass
        elif selected_option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid input! Please enter 1-5.\n")



if __name__ == "__main__":
    main()

