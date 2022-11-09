import random


def deal_card():
    """Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


user_cards = []
computer_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Your cards: {user_cards}, current score: {user_score}")
print(f"Computer first card: {computer_cards[0]}")

if user_cards == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True


# my first trial
"""
import os
b_j = input("Do you want to play Blackjack? Type 'y' to play or 'no' to exit.")
if b_j == "y":
    os.system('clear')
else:
    print("Goodbye")


print("Welcome to the Blackjack!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, ]

gamer = []
computer = []


def black_game():
    game_round = 0
    game_round_3 = True
    while game_round_3:
        gamer.append(random.choice(cards))
        computer.append(random.choice(cards))
        game_round += 1
        print(f"Your total score is: {sum(gamer)}")
        print(f"Your cards: {gamer} \nComputer card: {computer}")

        if sum(gamer) > 21:
            game_round_3 = False
            print("you lose")

        if game_round == 3:
            game_round_3 = False
            if sum(gamer) > sum(computer) and sum(gamer) <= 21:
                print("The winner is: YOU!")
            elif sum(gamer) < sum(computer) <= 21:
                print("The winner is: the computer")

        game_continue = input("Hit 'y' to continue or 'n' to stop!")
        if game_continue == "n":
            game_round_3 = False
            if sum(gamer) > sum(computer) or sum(gamer) <= 21 and sum(computer) > 21:
                print("The winner is: YOU!")
            elif sum(gamer) < sum(computer) <= 21:
                print("The winner is: the computer")


black_game()
"""
