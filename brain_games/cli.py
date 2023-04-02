import prompt


username = "%username%"


def welcome_user():
    global username
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    username = name


def get_username():
    return username
