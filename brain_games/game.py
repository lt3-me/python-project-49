def start_game(username: str, game_desc: str,
               questions_count: int, ask_question):
    print(game_desc)
    for _ in range(questions_count):
        answer, correct_answer = ask_question()
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {username}!")
            return None
    print(f'Congratulations, {username}!')