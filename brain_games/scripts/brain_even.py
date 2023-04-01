#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli

QUESTIONS_COUNT = 3
MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99


def main():
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(QUESTIONS_COUNT):
        random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        is_even = random_number % 2 == 0
        corr_answer = ''
        if is_even:
            corr_answer = 'yes'
        else:
            corr_answer = 'no'
        if answer.lower() == corr_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{corr_answer}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
