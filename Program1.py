lst = []

n = input("Welcome to Buzzword Bingo! You will now be asked for 30 words that fit a theme:")

with open("Bingo.txt", "w") as myfile:
    for i in range(0, 30):
        word = (input())

        lst.append(word)

lst = list(dict.fromkeys(lst))

