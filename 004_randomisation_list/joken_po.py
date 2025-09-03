import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options_list = [rock, paper, scissors]

player_one = input("Choose Rock, Paper or Scissors: R, P or S: ")
player_pc = random.randint(0, 2)


if player_one.upper() == "R":
    player_one = 0
elif player_one.upper() == "P":
    player_one = 1
elif player_one.upper() == "S":
    player_one = 2


if player_one == 0 and player_pc == 1:
    print(f"PC Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
elif player_one == 0 and player_pc == 2:
    print(f"P1 Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
elif player_one == 1 and player_pc == 0:
    print(f"P1 Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
elif player_one == 1 and player_pc == 2:
    print(f"PC Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
elif player_one == 2 and player_pc == 0:
    print(f"PC Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
elif player_one == 2 and player_pc == 1:
    print(f"P1 Wins! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
else:
    print(f"Draw Game! \nPlayer 1: {options_list[player_one]} \nPlayer PC: {options_list[player_pc]}")
