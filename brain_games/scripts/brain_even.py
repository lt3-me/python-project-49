#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli
from brain_games.game import start_game

QUESTIONS_COUNT = 3
MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99
DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    username = cli.welcome_user()
    start_game(username, DESC, QUESTIONS_COUNT, ask_question_even)


def ask_question_even():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    answer = answer.lower()
    correct_answer = get_correct_answer(random_number)
    return (answer, correct_answer)


def get_correct_answer(num):
    is_even = num % 2 == 0
    if is_even:
        corr_answer = 'yes'
    else:
        corr_answer = 'no'
    return corr_answer


if __name__ == '__main__':
    main()
