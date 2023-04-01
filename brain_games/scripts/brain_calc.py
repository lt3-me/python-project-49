#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli
from brain_games.game import start_game

MIN_RAND_NUM_VALUE = 2
MAX_RAND_NUM_VALUE = 99
MAX_MULT_RES_VALUE = 225


OPERATIONS = ['+', '-', '*']
DESC = 'What is the result of the expression?'


def main():
    username = cli.welcome_user()
    start_game(username, DESC, ask_question_even)


def ask_question_even():
    random_operator = OPERATIONS[randint(0, len(OPERATIONS)-1)]
    random_number1 = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    random_number2 = generate_second_operand(random_number1, random_operator)
    print(f'Question: {random_number1} {random_operator} {random_number2}')
    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_number1,
                                        random_number2,
                                        random_operator)
    try:
        answer = int(answer)
    except Exception:
        pass

    return (answer, correct_answer)


def get_correct_answer(num1, num2, operation):
    match operation:
        case '+':
            corr_answer = num1 + num2
        case '-':
            corr_answer = num1 - num2
        case '*':
            corr_answer = num1 * num2
        case _:
            corr_answer = None
    return corr_answer


def generate_second_operand(num1, operation):
    match operation:
        case '+':
            num2 = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
        case '-':
            num2 = randint(MIN_RAND_NUM_VALUE, num1)
        case '*':
            num2 = randint(MIN_RAND_NUM_VALUE, MAX_MULT_RES_VALUE // num1)
        case _:
            num2 = 0
    return num2


if __name__ == '__main__':
    main()
