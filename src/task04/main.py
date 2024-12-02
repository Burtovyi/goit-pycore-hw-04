def parse_input(user_input):
    user_input = user_input.strip()
    if not user_input:
        return '', []
    parts = user_input.strip().split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for add command."
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid number of arguments for change command."
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid number of arguments for phone command."
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()