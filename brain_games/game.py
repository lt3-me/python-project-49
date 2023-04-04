import brain_games.cli as cli


ROUNDS_NUMBER = 3


def start_game(game_desc: str, ask_question):
    username = cli.welcome_user()
    print(game_desc)
    for _ in range(ROUNDS_NUMBER):
        answer, correct_answer = ask_question()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return None
    print(f'Congratulations, {username}!')
