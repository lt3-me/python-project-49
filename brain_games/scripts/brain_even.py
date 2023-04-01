#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli

QUESTIONS_COUNT = 3
MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99


def main():
    username = cli.welcome_user()
    start_game(username)


def start_game(username):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(QUESTIONS_COUNT):
        random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        correct_answer = get_correct_answer(random_number)
        if answer.lower() == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return None
    print(f'Congratulations, {username}!')


def get_correct_answer(num):
    is_even = num % 2 == 0
    if is_even:
        corr_answer = 'yes'
    else:
        corr_answer = 'no'
    return corr_answer


if __name__ == '__main__':
    main()
