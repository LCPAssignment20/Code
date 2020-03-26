import Program1
import random

Brandlist = []

for x in range(0, 25):
    with open("Bingo.txt", "r") as radm:
        Randbrand = random.choice(Program1.lst)
        print(Randbrand)
        Brandlist.append(Randbrand)

print(Brandlist)