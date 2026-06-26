import random
from subprocess import run
from art import logo


def deal_card():
    """Retorna uma carta aleatória do baralho."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Calcula a pontuação da mão."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Empate 🤷‍♂️"
    elif c_score == 0:
        return "Perdeu, o PC tem Blackjack! 🫣"
    elif u_score == 0:
        return "Você GANHOU com Blackjack! 😎"
    elif u_score > 21:
        return "Estouro! Você Perdeu! 😭"
    elif c_score > 21:
        return "PC estourou! Você ganhou! 😂"
    elif u_score > c_score:
        return "Você ganhou! 😁"
    else:
        return "Você perdeu! 😣"


def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Suas cartas: {user_cards}, pontuação atual: {user_score}")
        print(f"Primeira carta do computador: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Deseja comprar outra carta? Digite 's' para sim ou 'n' para não: ")
            if user_should_deal == 's':
                user_cards.append(deal_card())
            else:
                is_game_over = True
            
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Sua mão final: {user_cards} | Pontos: {user_score}")
    print(f"Mão final PC : {computer_cards} | Pontos: {computer_score}")
    print(compare(user_score, computer_score))

while input("Você quer jogar Blackjack? 's' ou 'n': ") == "s":
    run("cls || clear", shell=True)
    print(logo)
    play_game()