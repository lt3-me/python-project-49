#!/usr/bin/env python3
from brain_games.games.game import start_game
from brain_games.games.prime_game import DESC, ask_question_prime


def main():
    start_game(DESC, ask_question_prime)


if __name__ == '__main__':
    main()
