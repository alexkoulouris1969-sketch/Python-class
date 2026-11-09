def phone_numbers():
    contacts = {}

    while True:
        print("(1) Add contact")
        print("(2) Find phone number")
        print("(3) Change phone number")
        print("(0) Exit")
        choice = input("Enter your choice (0-3): ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            contacts[name] = phone
            print(f"Contact {name} added with phone number {phone}.")
        elif choice == "2":
            name = input("Enter name to find: ")
            if name in contacts:
                print(f"Phone number for {name} is {contacts[name]}.")
            else:
                print(f"No contact found for {name}.")
        elif choice == "3":
            name = input("Enter name to change phone number: ")
            if name in contacts:
                new_phone = input("Enter new phone number: ")
                contacts[name] = new_phone
                print(f"Phone number for {name} updated to {new_phone}.")
            else:
                print(f"No contact found for {name}.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please enter a number from 0 to 3.")


if __name__ == "__main__":
    phone_numbers()
            