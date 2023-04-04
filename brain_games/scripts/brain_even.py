#!/usr/bin/env python3
from brain_games.games.game import start_game
from brain_games.games.even_game import DESC, ask_question_even

def main():
    start_game(DESC, ask_question_even)

if __name__ == '__main__':
    main()
