from random import randint

MIN_RAND_NUM_VALUE = 1
MAX_RAND_NUM_VALUE = 99

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_question():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    print(f'Question: {random_number}')
    correct_answer = get_correct_answer(random_number)

    return correct_answer


def get_correct_answer(num):
    is_even = num % 2 == 0
    if is_even:
        return 'yes'
    else:
        return 'no'
