from random import randint

MIN_RAND_NUM_VALUE = 0
MAX_RAND_NUM_VALUE = 230

DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_question():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    print(f'Question: {random_number}')
    correct_answer = get_correct_answer(random_number)

    return correct_answer


def get_correct_answer(num):
    if num <= 1:
        return 'no'
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'
