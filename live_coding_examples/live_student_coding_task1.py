number = float(input("Podaj liczbę z zakresu 0.0 do 1.0: "))

if number <= 1.0 and number <= 0.0:
    exit(1)

if number >= 0.9:
    print("Mark 5.0")
elif number >= 0.8:
    print("Mark 4.5")
elif number >= 0.7:
    print("Mark 4.0")
elif number >= 0.6:
    print("Mark 3.5")
elif number >= 0.5:
    print("Mark 3.0")
else:
    print("Mark 2.0")