from random import sample, choice
from subprocess import run

from art import logo, vs
from person import Person


class HigherLowerGame:
    def __init__(self, data):
        self.people = [Person(person) for person in data]
        self.score = 0

    def clear(self):
        run("cls || clear", shell=True)

    def generate_questions(self):
        return sample(self.people, 2)

    def generate_new_person(self, current_person):
        """
        Sorteia uma nova pessoa diferente da atual.
        """
        while True:
            person = choice(self.people)
            if person != current_person:
                return person

    def check_answer(self, answer, person_a, person_b):

        if answer == "a":
            return person_a.followers > person_b.followers

        elif answer == "b":
            return person_b.followers > person_a.followers

        return False

    def game_over(self):
        print("\nGame Over!")
        print(f"Final Score: {self.score}")

    def play_round(self):

        self.score = 0

        # Primeira rodada
        person_a, person_b = self.generate_questions()

        while True:
            self.clear()

            print(logo)

            print(f"Compare A: {person_a}")
            print(vs)
            print(f"Compare B: {person_b}")

            print(f"\nCurrent Score: {self.score}")

            answer = input("\nWho has more followers? (a/b): ").lower()

            if self.check_answer(answer, person_a, person_b):
                self.score += 1

                # A opção B vira a nova opção A
                person_a = person_b

                # Sorteia apenas uma nova opção B
                person_b = self.generate_new_person(person_a)

            else:
                self.game_over()
                return

    def play(self):

        while True:
            self.play_round()

            answer = input("\nDo you want to play again? (y/n): ").lower()

            if answer != "y":
                print("\nThanks for playing!")
                break
