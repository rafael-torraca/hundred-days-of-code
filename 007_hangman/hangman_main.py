import random
from hangman_arts import hang_body
from hangman_words import word_list

hang_body = hang_body[::-1]




chosen_word = random.choice(word_list)
print(chosen_word)
print(type(chosen_word))

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "


game_over = False
correct_letters = []

lives = 6
while not game_over:

    display = ""
    guess = input("\nGuess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")
        continue

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += " _ "

    print("\n************************************************\n")
    print(f"{display.strip()} ".center(30, "="))
    print(f" Lives: {lives} ".center(30, "="))
    print("\n************************************************\n")

    if guess not in chosen_word:
        if lives == 0:
            game_over = True
            print(f"{10*"*"} You Lose! {10*"*"}")
            print(f"The correct word was: {chosen_word}")
        lives -= 1

    if "_ " not in display:
        game_over = True
        print(f"{10*"*"} You Win! {10*"*"}")

    print(hang_body[lives])

