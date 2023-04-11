from random import randint
import prompt


OPERATIONS = ['+', '-', '*']
DESC = 'What is the result of the expression?'


def ask_question():
    random_operator = OPERATIONS[randint(0, len(OPERATIONS) - 1)]
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
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
