from random import randint

MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    is_even = random_number % 2 == 0
    if is_even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (random_number, correct_answer)
