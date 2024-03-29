from random import randint

OPERATIONS = ['+', '-', '*']
DESC = 'What is the result of the expression?'


def generate_question_and_answer():
    random_operator = OPERATIONS[randint(0, len(OPERATIONS) - 1)]
    random_number1 = randint(1, 10)
    random_number2 = randint(1, 10)
    correct_answer = calculate(random_number1,
                               random_number2,
                               random_operator)

    question = f'{random_number1} {random_operator} {random_number2}'
    correct_answer = str(correct_answer)

    return (question, correct_answer)


def calculate(num1, num2, operation):
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
