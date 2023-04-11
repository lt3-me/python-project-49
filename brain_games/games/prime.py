from random import randint

MIN_RAND_NUM_VALUE = 0
MAX_RAND_NUM_VALUE = 230

DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_question():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    correct_answer = 'yes' if is_prime(random_number) else 'no'

    return (random_number, correct_answer)


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
