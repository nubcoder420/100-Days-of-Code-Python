
# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


import random


def choose_difficulty():
    attempts = 0
    valid_difficulty = False
    while not valid_difficulty:

        difficulty = input("Choose a difficulty: 'Easy' or 'Hard': ").lower()

        if difficulty == 'easy':
            attempts = 10
            valid_difficulty = True
        elif difficulty == 'hard':
            attempts = 5
            valid_difficulty = True
        else:
            print("Invalid input. Choose between 'Easy' or 'Hard'.")
    return attempts

def choose_random_number():
    random_number = random.choice(range(1, 101))
    return random_number

def number_guessing_game():

    attempts = choose_difficulty() # saves the function choose_difficulty into the variable attempts
    random_number = choose_random_number() # saves the function choose_random_number() into the variable random_number

    # print(f"HINT: The number is: {random_number}") # for testing the code

    is_game_over = False

    while not is_game_over or attempts > 0:

        try:
            guess = int(input("Guess the number between 1 and 100: "))

            if guess == random_number:
                print(f'You guessed the number {random_number} correctly!')
                is_game_over = True
                break
            elif guess > random_number:
                attempts -= 1
                is_game_over = False
                print(f'Too high! You have {attempts} attempts remaining.')
            elif guess < random_number:
                attempts -= 1
                is_game_over = False
                print(f'Too low! You have {attempts} attempts remaining.')
        except ValueError:
            print('Invalid input. Please enter a number.')

        if attempts == 0:
            is_game_over = True
            print('Game over!')

number_guessing_game()
