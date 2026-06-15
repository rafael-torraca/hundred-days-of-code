import random


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

user_cards = []
computer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)
print(f"Suas cartas: {user_cards}, pontuação atual: {user_score}")
print(f"Primeira carta do computador: {computer_cards[0]}")

if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True
