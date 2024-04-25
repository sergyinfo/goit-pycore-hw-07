"""
This module contains the main function of the assistant bot.

The main function reads user input, parses it, and calls the appropriate command handler function.

The assistant bot can perform the following commands:
- hello: Display a greeting message.
- add: Add a contact to the contacts dictionary.
- change: Change the name of an existing contact.
- remove: Remove a contact from the contacts dictionary.
- phone-add: Add a phone number to a contact.
- phone-edit: Edit a phone number of a contact.
- phone-remove: Remove a phone number from a contact.
- phone: Show the phone number of a contact.
- all: Show all contacts in the contacts dictionary.
- close or exit: Close the assistant bot.
"""
from assistant_bot.command_handlers import add_contact, change_contact, remove_contact, \
                                            add_birthday, show_birthday, birthdays, add_phone, \
                                            edit_phone, remove_phone, show_phone, show_all
from assistant_bot.address_book.repositories.AddressBook import AddressBook

def parse_input(user_input):
    """
    Parse the user input into a command and arguments.

    Args:
    user_input (str): The user input string.

    Returns:
    tuple: A tuple containing the command (str) and arguments (list).
    """
    parts = user_input.strip().split()
    command = parts[0].lower() if parts else None
    args = parts[1:]
    return command, args

def main():
    """
    The main function of the assistant bot.
    """
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                break
            case "hello":
                # display a greeting and all possible commands
                print("Hello! Here are the available commands:")
                print("add <name> <phone>: Add a contact")
                print("add-birthday <name> <birthday>: Add a birthday to a contact")
                print("change <name> <new_name>: Change the name of a contact")
                print("remove <name>: Remove a contact")
                print("phone-add <name> <phone>: Add a phone number to a contact")
                print("phone-edit <name> <old_phone> <new_phone>: Edit a phone number of a contact")
                print("phone-remove <name> <phone>: Remove a phone number from a contact")
                print("phone <name>: Show the phone number of a contact")
                print("all: Show all contacts")
                print("close or exit: Close the assistant bot")
            case "add":
                print(add_contact(args, book))
            case "change":
                print(change_contact(args, book))
            case "remove":
                print(remove_contact(args, book))
            case "phone-add":
                print(add_phone(args, book))
            case "phone-edit":
                print(edit_phone(args, book))
            case "phone-remove":
                print(remove_phone(args, book))
            case "phone":
                print(show_phone(args, book))
            case "all":
                print(show_all(book))
            case 'add-birthday':
                print(add_birthday(args, book))
            case 'show-birthday':
                print(show_birthday(args, book))
            case 'birthdays':
                print(birthdays(book))
            case None:
                print("Please enter a command.")
            case _:
                print("Invalid command.")

if __name__ == "__main__":
    main()
