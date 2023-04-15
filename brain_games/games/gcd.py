from random import randint

DESC = 'Find the greatest common divisor of given numbers.'


def generate_question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    correct_gcd = gcd(first_number, second_number)
    question = f"{first_number} {second_number}"
    correct_gcd = str(correct_gcd)

    return (question, correct_gcd)


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1
