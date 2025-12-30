import random

import prompt

from brain_games.cli import welcome_user


RIGHT_ANSWER_COUNTER = 3


def set_number():
    random_number = random.randint(1, 20)
    return random_number


def is_correct(number, user_answer):
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return user_answer == correct_answer


def change_answer(user_answer):
    if user_answer == 'yes':
        return 'no'
    else:
        return 'yes'


def answers_counter(username):
    counter = 0
    while counter < RIGHT_ANSWER_COUNTER:
        number = set_number()
        print(f'Question: {number}')
        user_text = prompt.string('Your answer: ')
        if is_correct(number, user_text):
            print('Correct!')
        else:
            print(f"'{user_text}' is wrong answer ;(. Correct answer was "
                  f"'{change_answer(user_text)}'.")
            print(f'Let,s try again, {username}')
            break
        counter += 1
    else:
        print(f'Congratulations, {username}')


def main():
    print("Welcome to Brain Games!")
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    answers_counter(username)


if __name__ == '__main__':
    main()
