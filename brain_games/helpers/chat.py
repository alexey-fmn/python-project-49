import prompt


def say_hello():
    print("Welcome to the Brain Games!")


def wrong_answer(user_text, expression, name):
    print(f'\'{user_text}\' is wrong answer ;(. '
          f'Correct answer: \'{expression}\'.')
    print(f'Let\'s try again, {name}!')


def ask_user_answer():
    return prompt.string('Your answer: ')


def congratulation(name):
    print(f'Congratulations, {name}!')