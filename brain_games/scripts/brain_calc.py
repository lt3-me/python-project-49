#!/usr/bin/env python3
from brain_games.games.game import start_game
from brain_games.games.calc_game import DESC, ask_question_calc


def main():
    start_game(DESC, ask_question_calc)


if __name__ == '__main__':
    main()
