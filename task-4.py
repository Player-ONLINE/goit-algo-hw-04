def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    
    if len(args) != 2:
        return "Error: Use format 'add <name> <phone>'"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    
    if len(args) != 2:
        return "Error: Use format 'change <name> <new_phone>'"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for {name} updated."
    return f"Error: Contact '{name}' not found."

def show_all(contacts):
    
    if not contacts:
        return "No contacts saved."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def get_phone(args, contacts):
    
    if len(args) != 1:
        return "Error: Use format 'phone <name>'"
    name = args[0]
    return contacts.get(name, f"Error: Contact '{name}' not found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye", "-"]:
            print("Good bye!")
            break
        elif command in ["hello", "+"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

