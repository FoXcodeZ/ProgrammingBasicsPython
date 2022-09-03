def get_hello_message():
    userName = input("What's your name? ")
    if len(userName) > 0:
        return f"Hello, {userName}"
    else:
        return "Hello, World!"

def say_hello():
    print(get_hello_message())

say_hello()