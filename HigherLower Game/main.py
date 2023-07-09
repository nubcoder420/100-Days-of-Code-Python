from art import logo, vs
from game_data import data
import random
import os


def clear_screen():
    os.system('cls')


def generate_account():
    account = random.choice(data)
    return account


def generate_item(from_generate_account):
    
    name = from_generate_account['name']
    follower_count = from_generate_account['follower_count']
    description = from_generate_account['description']
    country = from_generate_account['country']

    return f"{name}, a {description}, from {country}."


account_a = generate_account()
follower_count_a = account_a['follower_count']

account_b = generate_account()
follower_count_b = account_b['follower_count']

score = 0
is_game_over = False

while not is_game_over:

    clear_screen()

    print(logo)
    print(f"Current score: {score}")

    print()
    print(f"Compare A: {generate_item(account_a)}")
    print(f"HINT: Follower count: {follower_count_a}") # for testing code
    print(vs)
    print(f"Against B: {generate_item(account_b)}")
    print(f"HINT: Follower count: {follower_count_b}") # for testing code
    print()

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    if guess == 'a':

        if follower_count_a > follower_count_b:
            score += 1
            account_b = generate_account()
            follower_count_b = account_b['follower_count']
            clear_screen()
        else:
            clear_screen()
            print(logo)
            is_game_over = True
            print(f"Your final score is {score}\nGame Over!")

    elif guess == 'b':

        if follower_count_a < follower_count_b:
            score += 1
            account_a = account_b
            follower_count_a = follower_count_b
            account_b = generate_account()
            follower_count_b = account_b['follower_count']
            clear_screen()

        else:
            clear_screen()
            is_game_over = True
            print(logo)
            print(f"Your final score is {score}\nGame Over!")


# TODO : Improve the code
