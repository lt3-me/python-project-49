from random import randint


#!/usr/bin/env python3
from random import randint
import prompt
import brain_games.cli as cli
from brain_games.game import start_game

MAX_RAND_START_VALUE = 100
MIN_RAND_COMMON_DIFF = 2
MAX_RAND_COMMON_DIFF = 20
NUMBER_OF_ELEMENTS = 10

DESC = 'What number is missing in the progression?'


def main():
    cli.welcome_user()
    start_game(cli.get_username(), DESC, ask_question_prog)


def ask_question_prog():
    common_difference = randint(MIN_RAND_COMMON_DIFF,
                                MAX_RAND_COMMON_DIFF)
    start_value = randint(0, MAX_RAND_START_VALUE)
    stop_value = start_value + \
        common_difference * NUMBER_OF_ELEMENTS
    progression = list(range(start_value, stop_value, 
                             common_difference))
    missing_element = randint(0, 9)
    progression_string = ''
    for id, elem in enumerate(progression):
        if id != missing_element:
            progression_string = progression_string + \
                str(elem) + ' '
        else:
            progression_string = progression_string + '.. '
    progression_string = progression_string.strip()
    print(f'Question: {progression_string}')
    answer = prompt.string('Your answer: ')
    correct_answer = progression[missing_element]
    try:
        answer = int(answer)
    except Exception:
        pass

    return (answer, correct_answer)