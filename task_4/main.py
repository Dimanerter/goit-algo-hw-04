import re
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def handler(args, contacts, func_name):
    try:
        if func_name in ["add", "change", "phone"]:
            if re.search(r"\d", args[0]):
                print("The arguments are not correct")
                return False

            if func_name in ["add", "change"]:
                if re.search(r"\D", args[1]):
                    print("The arguments are not correct")
                    return False
                
            if func_name == "phone" and len(args) > 1:
                print("The arguments are not correct")
                return False
            
        if func_name in ["add"]:
            if args[0] in contacts:
                print("This contact already exists")
                return False
        
        if len(args) > 0 and func_name == "all":
            print("This contact already exists")
            return False
        
        return True
            
    except ValueError:
        print("The arguments are not correct")
    except IndexError:
        print("The arguments are not correctr")
        

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        name, phone = args
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found"
    
def show_phone(arg, contacts):
    if arg[0] in contacts:
        return f"[{contacts[arg[0]]}]"
    else:
        return "Contact not found"
    
def show_all(contacts):
    return f"Усі контакти:\n {contacts}"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                if handler(args, contacts, command):
                    print(add_contact(args, contacts))
            case "change":
                if handler(args, contacts, command):
                    print(change_contact(args, contacts))
            case "phone":
                if handler(args, contacts, command):
                    print(show_phone(args, contacts))
            case "all":
                if handler(args, contacts, command):
                    print(show_all(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
