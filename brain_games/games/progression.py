from random import randint

NUMBER_OF_ELEMENTS = 10

DESC = 'What number is missing in the progression?'


def generate_question_and_answer():
    common_difference = randint(2, 20)
    start_value = randint(0, 100)
    stop_value = start_value + \
        common_difference * NUMBER_OF_ELEMENTS
    progression = list(range(start_value, stop_value,
                             common_difference))
    missing_element = randint(0, 9)

    correct_answer = str(progression[missing_element])
    progression[missing_element] = '..'

    progression = [str(x) for x in progression]
    progression_string = ' '.join(progression)

    return (progression_string, correct_answer)
