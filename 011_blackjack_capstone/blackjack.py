from random import choice
from art import logo
from subprocess import run

CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def display_logo():
    """Exibe a logo e mensagem de boas-vindas."""
    run("cls || clear", shell=True)
    print(logo)
    print("Bem-vindo ao Blackjack!\n")


def deal_card():
    """Retorna uma carta aleatória."""
    return choice(CARDS)


def calculate_score(cards):
    """
    Calcula a pontuação da mão.

    Retorna:
    - 0 se for Blackjack (Ás + 10)
    - Soma das cartas ajustando o Ás (11 → 1) quando necessário.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack

    score = sum(cards)

    # Ajusta o valor do Ás
    while 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


def compare_scores(player_score, computer_score):
    """Determina o vencedor da partida."""
    if player_score == computer_score:
        return "Empate! 🙃"

    if computer_score == 0:
        return "Você perdeu. O computador tem Blackjack! 😱"

    if player_score == 0:
        return "Blackjack! Você venceu! 😎"

    if player_score > 21:
        return "Você estourou. Você perdeu 😭"

    if computer_score > 21:
        return "O computador estourou. Você venceu 😁"

    if player_score > computer_score:
        return "Você venceu 😃"

    return "Você perdeu 😤"


def display_game_state(player_cards, computer_cards, reveal_computer=False):
    """Exibe o estado atual do jogo."""
    player_score = calculate_score(player_cards)

    print(f"\nSuas cartas: {player_cards}, " f"pontuação atual: {player_score}")

    if reveal_computer:
        computer_score = calculate_score(computer_cards)

        if computer_score == 0:
            computer_score_display = 21
        else:
            computer_score_display = computer_score

        print(
            f"Cartas do computador: {computer_cards}, "
            f"pontuação: {computer_score_display}"
        )
    else:
        print(f"Primeira carta do computador: " f"{computer_cards[0]}")


def player_turn(player_cards, computer_cards):
    """Gerencia a vez do jogador."""
    while True:
        player_score = calculate_score(player_cards)

        if player_score == 0:
            print("Blackjack! 🎉")
            break

        if player_score > 21:
            break

        display_game_state(player_cards, computer_cards, reveal_computer=False)

        choice_option = input(
            "\nDigite 'y' para comprar outra carta " "ou 'n' para parar: "
        ).lower()

        if choice_option == "y":
            player_cards.append(deal_card())
        else:
            break


def computer_turn(computer_cards):
    """Gerencia a vez do computador."""
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())


def play_game():
    """Executa uma partida completa de Blackjack."""
    display_logo()

    player_cards = []
    computer_cards = []

    # Distribui as cartas iniciais
    for _ in range(2):
        player_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Turno do jogador
    player_turn(player_cards, computer_cards)

    player_score = calculate_score(player_cards)

    # Turno do computador
    if player_score <= 21:
        computer_turn(computer_cards)

    # Resultado final
    display_game_state(player_cards, computer_cards, reveal_computer=True)

    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)

    print()
    print(compare_scores(player_score, computer_score))


def main():
    """Controla o fluxo principal do jogo."""
    while True:
        play = input(
            "Deseja jogar Blackjack? " "Digite 'y' para sim ou 'n' para não: "
        ).lower()

        if play != "y":
            print("Obrigado por jogar!")
            break

        print("\n" * 20)
        play_game()


if __name__ == "__main__":
    main()
