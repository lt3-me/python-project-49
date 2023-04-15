from random import randint

DESC = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question():
    random_number = randint(1, 99)
    is_even = random_number % 2 == 0
    if is_even:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return (random_number, correct_answer)
