############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 11 ,11 ,11 ,11 ,11, 11, 11, 11, 11, 11]


user_cards = []


def get_user_cards(user_cards):
    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_cards.append(user_card1)
    user_cards.append(user_card2)
    return user_cards


def get_user_total():
    user_total = 0
    for card in user_cards:
        user_total += card
        if 11 in user_cards and user_total > 21:
            user_cards[user_cards.index(11)] = 1
            user_total = sum(user_cards)
    return user_total


computer_cards = []


def get_computer_cards(computer_cards):
    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_cards.append(computer_card1)
    computer_cards.append(computer_card2)
    return computer_cards


def get_computer_total():
    computer_total = 0
    for card in computer_cards:
        computer_total += card
        if 11 in computer_cards and computer_total > 21:
            computer_cards[computer_cards.index(11)] = 1
            computer_total = sum(computer_cards)
    return computer_total


def is_blackjack(user, computer):
    if get_user_total() == 21:
        print('Blackjack! You have 21. You win!')
    elif get_computer_total() == 21:
        print('Blackjack! Computer has 21. You lose!')


def blackjack():

    clear_screen()
    print(logo)

    user = get_user_cards(user_cards)
    computer = get_computer_cards(computer_cards)

    user_total = get_user_total()
    computer_total = get_computer_total()

    print(f'Your cards: {user}')
    print(f'Your total: {user_total}')

    print(f'Computer cards: [{computer[0]}, hidden card]')
    print(f'Computer total: {computer[0]}')

    if user_total == 21:
        is_blackjack(user=user_total, computer=computer_total)
        return
    elif  computer_total == 21:
        is_blackjack(user=user_total, computer=computer_total)
        print(f'Computer cards: {computer}')
    
    while user_total < 21:
        draw_card = input("Do you want to draw another card?\n'Y' or 'N': ").lower()
        if draw_card == 'y':
            new_card = random.choice(cards)
            user_cards.append(new_card)
            user_total = get_user_total()

            print(f"You draw a card: {new_card}")
            print(f'Your cards: {user}')
            print(f'Your total: {user_total}')

        else:
            break

    print(f"Computer cards: {computer_cards}")
    print(f"Computer total: {computer_total}")

    while computer_total < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_total = get_computer_total()
        print(f"Computer draws card: {new_card}")
        print(f'Computer cards: {computer}')
        print(f'Computer total: {computer_total}')


    if user_total > 21:
        print('You went over 21. You lose!')
    elif computer_total > 21:
        print('Computer went over 21. You win!')
    elif user_total == computer_total:
        print("It's a draw!")
    elif user_total > computer_total:
        print(f'You have {user_total} and computer has {computer_total}. You win!')
    else:
        print('You lose!')


def lets_play_blackjack():

    play_again = True
    while play_again:
        user_cards.clear()
        computer_cards.clear()
        blackjack()

        new_game = input("Do you want to play again? Type 'y' for Yes or 'n' for No: ")
        if new_game.lower() == 'y':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing BLACKJACK!')

def main():
    play_blackjack = input("Do you want to play a game of BLACKJACK? Type 'y' for Yes or 'n' for No: ")
    if play_blackjack.lower() == 'y':
        lets_play_blackjack()
    else:
        return
    
main()
