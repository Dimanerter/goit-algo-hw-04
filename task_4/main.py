# Декоратор для обработки ошибок
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "The arguments are not correct."
        except IndexError:
            return "The arguments are not correct."
    return wrapper

# Парсинг ввода
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функция для добавления контакта
@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "This contact already exists."
    contacts[name] = phone
    return "Contact added."

# Функция для изменения контакта
@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

# Функция для отображения телефона по имени
@input_error
def show_phone(args, contacts):
    return f"[{contacts[args[0]]}]"

# Функция для отображения всех контактов
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return f"All contacts:\n {contacts}"

# Основная функция
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
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
