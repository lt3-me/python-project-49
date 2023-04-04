#!/usr/bin/env python3
from random import randint
import prompt
from brain_games.game import start_game

MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99
DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    start_game(DESC, ask_question_even)


def ask_question_even():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_number)
    return (answer.lower(), correct_answer)


def get_correct_answer(num):
    is_even = num % 2 == 0
    if is_even:
        return 'yes'
    else:
        return 'no'


if __name__ == '__main__':
    main()
