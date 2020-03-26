import Program2

random_draw_list = Program2.Brandlist

def generate_card():

    card = {
        "B": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for letter in card:
        card[letter] = Program2.Brandlist
        min += 1
        max += 2
        if letter == "N":
            card[letter][2] = "X" # free space!
    return card

def print_card(card):
    """
    Prints the bingo card.

    Arguments:
        card (dictionary): The card to be printed out.
    """
    for letter in card:
        print(letter, end="\t")
        for number in card[letter]:
            print(number, end="\t")
        print("\n")
    print("\n")

def draw(card, list):
    """
    Pops a number off a list of random numbers. Using the pop method ensures no duplicate
    numbers will be drawn.

    Arguments:
        card (dictionary): The card to to check for the number that was drawn.
        list (list): The list of random numbers to be drawn from.
    """
    number_drawn = random_draw_list.pop()
    for letter in card:
        i = 0
        for number in card[letter]:
            if number == number_drawn:
                card[letter][i] = "X"
            i += 1
    return number_drawn

def check_win(card):
    """
    First checks for diagonal wins, then four-corner, then horizontal, and finally, vertical.

    Arguments:
        card (dictionary): The card to check for a win.
    """
    win = False
    if card["B"][0] == "X" and card["I"][1] == "X" and card["N"][2] == "X" and card["G"][3] == "X" and card["O"][4] == "X":
        win = True
    elif card["O"][0] == "X" and card["G"][1] == "X" and card["N"][2] == "X" and card["I"][3] == "X" and card["B"][4] == "X":
        win = True
    elif card["B"][0] == "X" and card["O"][4] == "X" and card["B"][4] == "X" and card["O"][0] == "X":
        win = True
    for letter in card:
        if(len(set(card[letter]))==1):
            win = True
    for i in range(5):
        cnt = 0
        for letter in card:
            if card[letter][i] == "X":
                cnt += 1
        print(cnt)
        if cnt == 5:
            win = True
            break
    return win

def main():
    """
    Main method for the program. Generates a card, prints it, and loops through drawing
    and printing until the check_win method returns True or the user enters "quit".
    """
    print("Let's play bingo!")
    card = generate_card()

    print("\nHere is your card:\n")
    print_card(card)

    print("\nKeep pressing enter to continue or type quit to exit.\n")
    user_input = input()
    win = check_win(card)
    balls_till_win = 0

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