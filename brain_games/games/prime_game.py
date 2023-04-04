from random import randint
import prompt
from brain_games.games.game import start_game

MIN_RAND_NUM_VALUE = 0
MAX_RAND_NUM_VALUE = 230

DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def start_prime():
    start_game(DESC, ask_question_prime)


def ask_question_prime():
    random_number = randint(MIN_RAND_NUM_VALUE, MAX_RAND_NUM_VALUE)
    print(f'Question: {random_number}')
    answer = prompt.string('Your answer: ')
    correct_answer = get_correct_answer(random_number)
    return (answer.lower(), correct_answer)


def get_correct_answer(num):
    if num <= 1:
        return 'no'
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'
