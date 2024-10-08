import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
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

        try:
            match command:
                case "close" | "exit":
                    print("Good bye!")
                    break
                case "hello":
                    print("How can I help you?")
                case "add":
                    if re.search(r"\d", args[0]) or re.search(r"\D", args[1]):
                        print("The arguments are not correct")
                    else:
                        if args[0] in contacts:
                            print("This contact already exists")
                        else:
                            print(add_contact(args, contacts))
                case "change":
                    if re.search(r"\d", args[0]) or re.search(r"\D", args[1]):
                        print("The arguments are not correct")
                    else:
                        print(change_contact(args, contacts))
                case "phone":
                    if re.search(r"\d", args[0]):
                        print("The arguments are not correct")
                    else:
                        print(show_phone(args, contacts))
                case "all":
                    if not args:
                        print(show_all(contacts))
                    else:
                        print('The "all" command must be without arguments.')
                case _:
                    print("Invalid command.")
        except ValueError:
            print("The arguments are not correct")
        except IndexError:
            print("The arguments are not correct")

if __name__ == "__main__":
    main()
