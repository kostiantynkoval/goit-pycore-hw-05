def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, IndexError):
            return "Enter the argument for the command"
    return inner


def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        return cmd.strip().casefold(), *args
    except ValueError:
        return None, []


@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return "Contact already exists"
    else:
        contacts[name] = phone
        return "Contact added"


@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated"
    else:
        return "404. Contact not found. Use add command to add contact."


@input_error
def show_phone(args, contacts):
    name, *rest = args
    if name in contacts:
        return contacts[name]
    else:
        return "404. Contact not found."

@input_error
def show_all(contacts):
    if contacts:
        phone_numbers = []
        for name, phone in contacts.items():
            phone_numbers.append(f"{name}: {phone}")
        return '\n'.join(phone_numbers)
    else:
        return "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()


assert parse_input("") == (None, [])
assert parse_input('add') == ('add',)
assert parse_input('add K') == ('add', 'K')
assert parse_input('aDD K') == ('add', 'K')

assert add_contact(('K', 234), {}) == 'Contact added'
assert input_error(add_contact)(('K', 234), {}) == 'Contact added'
assert input_error(add_contact)(('K', 234), {'K', 123}) == 'Contact already exists'
assert input_error(add_contact)(('K',), {}) == 'Enter the argument for the command'
assert input_error(add_contact)([], {}) == 'Enter the argument for the command'

assert input_error(change_contact)(('K', 234), {}) == '404. Contact not found. Use add command to add contact.'
assert input_error(change_contact)(('K', 234), {'K': 123}) == 'Contact updated'
assert input_error(change_contact)(('K',), {}) == 'Enter the argument for the command'
assert input_error(change_contact)([], {}) == 'Enter the argument for the command'

assert input_error(show_phone)(('K', 234), {}) == '404. Contact not found.'
assert input_error(show_phone)(('K',), {}) == '404. Contact not found.'
assert input_error(show_phone)([], {}) == 'Enter the argument for the command'
assert input_error(show_phone)(('K', 234), {'K': 234}) == 234

assert input_error(show_all)({'K': 123, 'D': 321}) == 'K: 123\nD: 321'
assert input_error(show_all)({}) == 'No contacts found.'