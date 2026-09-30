from art import logo, vs
from game_data import data
import random

print(logo)

def format_data(account):
    """Takes account data and returns the printable format."""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


# def check_answer(user_guess, a_followers, b_followers):
#     if user_guess == 'a' and a_followers > b_followers:
#         return True
#     elif user_guess == 'b' and b_followers > a_followers:
#         return True
#     return False


def check_answer(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    return user_guess == "b"

def start_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_b = random.choice(data)

    while game_should_continue:
        # generate random account
        account_a = account_b
        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)

        account_a_data = format_data(account_a)
        account_b_data = format_data(account_b)

        print()
        print(f"Compare A: {account_a_data}.")
        print(vs)
        print(f"Compare B: {account_b_data}.")
        print()

        guess = input("Who has more followers? Type 'a' or 'b': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! {score:.2f}")
        else:
            print("Sorry, that's wrong. Final score: {:02d}".format(score))
            game_should_continue = False

is_new_game = True

while is_new_game:
    start_game()
    option = input("New game? (Y/N): ").lower()
    if option == 'n':
        is_new_game = False
