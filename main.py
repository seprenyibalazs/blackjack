
import random
"""
import os
b_j = input("Do you want to play Blackjack? Type 'y' to play or 'no' to exit.")
if b_j == "y":
    os.system('clear')
else:
    print("Goodbye")"""


print("Welcome to the Blackjack!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]

gamer = 0
computer = 0


def black_game():
    game_round = 0
    game_round_3 = True
    while game_round_3:
        gamer = random.choice(cards)
        computer = random.choice(cards)
        game_round += 1
        print(f"Your cards: {gamer} \nComputer card: {computer}")
        game_continue = input("Hit 'y' to continue!")

        if game_round == 3:
            game_round_3 = False
            print("The winner is: ")


black_game()
