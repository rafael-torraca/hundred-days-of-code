from game import HigherLowerGame
from game_data import data


def main():
    game = HigherLowerGame(data)
    game.play()


if __name__ == "__main__":
    main()