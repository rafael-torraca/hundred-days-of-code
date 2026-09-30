from art import vs, logo
from subprocess import run
from game_data import data
from random import randint


def game_over():
    print(f"Sorry, that's wrong. Final score {score}")



print(len(data))
def generate_question(data):
    return data[randint(0,49)]


score = 0

game_on = True
while game_on:
    run("cls || clear", shell=True)
    question_a = generate_question(data)
    question_b = generate_question(data)
    while question_a == question_b:
        question_b = generate_question(data)
    print(f"\nCompare A: {question_a['name']}, {question_a['description']}, from {question_a['country']}")
    print(vs)
    print(f"Compare B: {question_b['name']}, {question_b['description']}, from {question_b['country']}")

    print(f"\n Score: {score}\n")

    user_answer = input("Who has more followers? Type 'a' or 'b': ")
    if question_a['follower_count'] > question_b['follower_count'] and user_answer == 'a':
        score += 1
    elif question_a['follower_count'] < question_b['follower_count'] and user_answer == 'b':
        score += 1
    else:
        game_on = False
        game_over()
