#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli
from brain_games.game import start_game

MIN_RAND_GCD_VALUE = 2
MAX_RAND_GCD_VALUE = 25
MAX_RAND_NUM_VALUE = 162
DESC = 'Find the greatest common divisor of given numbers.'
NUMBER_OF_VALUES = 2


def main():
    cli.welcome_user()
    start_game(cli.get_username(), DESC, ask_question_gcd)


def ask_question_gcd():
    correct_gcd = randint(MIN_RAND_GCD_VALUE, MAX_RAND_GCD_VALUE)
    random_multipliers = [randint(MIN_RAND_GCD_VALUE,
                                  MAX_RAND_NUM_VALUE // correct_gcd)
                          for _ in range(NUMBER_OF_VALUES)]
    mult_gcd = gcd_list(random_multipliers)
    random_multipliers = [number // mult_gcd for number in random_multipliers]
    random_numbers = [number * correct_gcd for number in random_multipliers]
    print(f'Question: {" ".join(str(num) for num in random_numbers)}')
    answer = prompt.string('Your answer: ')
    try:
        answer = int(answer)
    except Exception:
        pass

    return (answer, correct_gcd)


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result


if __name__ == '__main__':
    main()
