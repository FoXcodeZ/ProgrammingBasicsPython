from termcolor import colored


def show_menu():
    print(f"{colored('[1]', 'yellow')} First Option")
    print(f"{colored('[2]', 'yellow')} Second Option")
    print(f"{colored('[Q]', 'yellow')} Quit")


def ask_user():
    user_option = input("Your option: ")
    return user_option


while True:
    show_menu()
    option = ask_user()
    if option == "1":
        print(f"You selected option {colored('[1]', 'yellow')}")
        break
    elif option == "2":
        print(f"You selected option {colored('[2]', 'yellow')}")
        break
    elif option == "Q" or option == "q":
        print(f"You selected option {colored('[Q]', 'yellow')}")
        exit(0)
    else:
        print("Nothing selected, try again")