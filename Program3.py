import random
import Program2
import Program1

with open("Bingo.txt", "r") as radm:
    brand_drawn = random.choice(Program1.lst)

    letterB = Program2.Brandlist[0], Program2.Brandlist[1], Program2.Brandlist[2], Program2.Brandlist[3], Program2.Brandlist[4]
    letterI = Program2.Brandlist[5], Program2.Brandlist[6], Program2.Brandlist[7], Program2.Brandlist[8], Program2.Brandlist[9]
    letterN = Program2.Brandlist[10], Program2.Brandlist[11], Program2.Brandlist[12], Program2.Brandlist[13], Program2.Brandlist[14]
    letterG = Program2.Brandlist[15], Program2.Brandlist[16], Program2.Brandlist[17], Program2.Brandlist[18], Program2.Brandlist[19]
    letterO = Program2.Brandlist[20], Program2.Brandlist[21], Program2.Brandlist[22], Program2.Brandlist[23], Program2.Brandlist[24]

def generate_card():
    for letter in (letterB, letterI, letterN, letterG, letterO):
        print(letter, end="\n")
    print(generate_card())

def draw():
    for word in Program2.Brandlist:
        i = 0
        if word == brand_drawn:
            Program2.Brandlist[i] = "X"
            i += 1
    return brand_drawn

def main():
    print(generate_card())

    print("\nKeep pressing enter to continue or type quit to exit.\n")
    #user_input = input()
    #win = check_win(card)
    #balls_till_win = 0

while win == False and user_input != "quit":
        number_drawn = draw(card, random_draw_list)
        balls_till_win += 1

        print(f"\nNumber drawn: {number_drawn}.")
        print(f"Total balls drawn: {balls_till_win}.\n")
        print_card(card)

        win = check_win(card)

        user_input = input()
    if win == True:
        print(f"\nBingo! Total balls to win: {balls_till_win}.")
    else:
        print("Goodbye! Thanks for playing!")

main()