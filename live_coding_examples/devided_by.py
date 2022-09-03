from termcolor import colored

user_number = int(input("Podaj liczbę: "))

dividing_range = range(3, 11)

for divisor in dividing_range:
    if user_number % divisor == 0:
        print(f"Podzielna przez {divisor}? {colored('TAK', 'green')}")
    else:
        print(f"Podzielna przez {divisor}? {colored('NIE', 'red')}")