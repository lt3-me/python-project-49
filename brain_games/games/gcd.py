from random import randint

DESC = 'Find the greatest common divisor of given numbers.'


def generate_question():
    correct_gcd = randint(2, 25)
    random_multipliers = [randint(2,
                                  25 // correct_gcd)
                          for _ in range(2)]
    mult_gcd = gcd_list(random_multipliers)
    random_multipliers = [number // mult_gcd for number in random_multipliers]
    random_numbers = [number * correct_gcd for number in random_multipliers]

    question = " ".join(str(num) for num in random_numbers)
    correct_gcd = str(correct_gcd)

    return (question, correct_gcd)


def gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcd(result, numbers[i])
    return result
