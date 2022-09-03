import random

list = [
    "Eren Jagger",
    "Mr. Bean",
    "Ala Makota",
    "Jett Steel",
    "Henry Ford"
    "Mike Mouse",
]

presence = {}

while len(list) != 0:
    winner = random.choice(list)
    list.remove(winner)
    presence[winner] = input(f"Czy {winner} jest obecny? [Y/N]")


for key in presence:
    print(f"{key} :y {presence[key]}")