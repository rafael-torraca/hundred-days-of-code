from art import logo
from random import randint

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def show_welcome():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")


def choose_level():
    while True:
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if level == "easy":
            return EASY_ATTEMPTS
        if level == "hard":
            return HARD_ATTEMPTS
        print("Only 'easy' or 'hard'!")


def generate_number():
    return randint(1, 100)


def guess_number():
    while True:
        try:
            return int(input("Make a guess: "))
        except ValueError:
            print("Only numbers allowed!")


def compare_answer(player_number, secret_number):
    if player_number == secret_number:
        return True, "You Win!"
    if player_number < secret_number:
        return False, "Too Low!"
    return False, "Too High!"


def play_game(attempts, secret_number):
    list_attempts = []
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        print(f"Already tried: {list_attempts}")
        player_number = guess_number()
        list_attempts.append(player_number)
        won, message = compare_answer(player_number, secret_number)
        print(message)
        if won:
            return True
        attempts -= 1
    return False


def show_result(won, secret_number):
    if won:
        print("Congratulations!")
    else:
        print(f"You Lose! The number was {secret_number}.")


def play_again():
    while True:
        answer = input("\nPlay again? (y/n): ").lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Only 'y' or 'n'!")


def game():
    show_welcome()
    attempts = choose_level()
    secret_number = generate_number()
    won = play_game(attempts, secret_number)
    show_result(won, secret_number)

while True:
    game()

    if not play_again():
        print("Thanks for playing!")
        break