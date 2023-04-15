import prompt

ROUNDS_NUMBER = 3


def start(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    print(game.DESC)
    for _ in range(ROUNDS_NUMBER):
        question, correct_answer = game.generate_question()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        answer = answer.strip()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            break
    else:
        print(f'Congratulations, {username}!')
