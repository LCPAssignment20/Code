#creating a list
lst = []

n = input("Welcome to Buzzword Bingo! You will now be asked for 30 words that fit a theme:")

#opening file and writing in it
with open("Bingo.txt", "w") as myfile:
#loop that asks for 30 words that are appended to the list
    for i in range(0, 30):
        word = (input())

        lst.append(word)

lst = list(dict.fromkeys(lst))

