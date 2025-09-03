from random import randint

user_choice = input("Heads(H) or Tails(T): ")
coin_random = randint(1,2)


def coin_string(coin_random: int) -> str:
    if coin_random == 1:
        return "Head"
    return "Tails"


def user_string(user_choice: str) -> str:
    if user_choice.upper() == "H":
        return "Head"
    return "Tails"


if user_choice.upper() == "H" and coin_random == 1:
    print(f"You Win! User: Head | Coin: Head")
elif user_choice.upper() == "T" and coin_random == 2:
    print(f"You Win! User: Tails | Coin: Tails")
else:
    print(f"You Lose! User: {user_string(user_choice)} | Coin: {coin_string(coin_random)}")
