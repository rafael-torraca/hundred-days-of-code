import os
import random

word_list = ["vaca", "danone", "camelo", "dinossauro", "cachorro", "sapato", "camiseta"]

word = random.choice(word_list)
word_to_guess = list(word)
user_guess_list = ["_"] * len(word)
user_choices = []

life = 6
while life:
    os.system("clear || cls")
    print(f"\nWord to guess:\n{' '.join(user_guess_list)}")
    print(f"\nLetters that have already been chosen:\n{' '.join(user_choices)}\n")
    print(f"Life: {life}")

    # Verifica se ganhou antes de pedir nova letra
    if word_to_guess == user_guess_list:
        print("\n🎉 Congratulations, you guessed it!")
        break

    input_letter = input("\nGuess a letter: ").lower()

    # Evita repetir letra
    if input_letter in user_choices:
        print("⚠️ You already chose that letter!")
        input("\nPress ENTER to continue...")
        continue

    user_choices.append(input_letter)

    right_guess = False
    for index, letter in enumerate(word_to_guess):
        if letter == input_letter:
            user_guess_list[index] = letter
            right_guess = True

    if not right_guess:
        life -= 1
        if life == 0:
            print(f"\n💀 GAME OVER!!!\nThe word was: {word}")
