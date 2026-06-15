print("Welcome to the secret auction program.")
import subprocess
from art import logo


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    max(bidding_dictionary.values())

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


should_continue = "yes"
bidders = {}

while should_continue == "yes":
    logo
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    subprocess.run("cls || clear", shell=True)
    if should_continue == "no":
        find_highest_bidder(bidders)

# highest_bid = 0
# winners = []

# for bidder, bid in bidders.items():
#     if bid > highest_bid:
#         highest_bid = bid
#         winners = [bidder]
#     elif bid == highest_bid:
#         winners.append(bidder)

# print(winners)

# if len(winners) == 1:
#     print(f"The winner is {winners[0]} with a bid of ${highest_bid}.")
# else:
#     print(
#         f"There is a tie between {', '.join(winners)} "
#         f"with a bid of ${highest_bid}."
#     )




