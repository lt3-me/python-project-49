from random import randint

MAX_RAND_START_VALUE = 100
MIN_RAND_COMMON_DIFF = 2
MAX_RAND_COMMON_DIFF = 20
NUMBER_OF_ELEMENTS = 10

DESC = 'What number is missing in the progression?'


def ask_question():
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
    correct_answer = str(progression[missing_element])

    return correct_answer
