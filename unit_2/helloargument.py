def get_user_name():
    return input("What's your name? ").capitalize()

def get_hello_message(name):
    if len(name) > 0:
        return f"Hello, {name}"
    else:
       return "Hello, World!"

def say_hello():
    userName = get_user_name()
    print(get_hello_message(userName))

say_hello()