from brain_games.cli import welcome_user
from brain_games.helpers.chat import (
    ask_user_answer,
    congratulation,
    say_hello,
    wrong_answer,
)
from brain_games.helpers.compare_results import is_right_answer
from brain_games.helpers.select_number import set_number
from brain_games.settings import RIGHT_ANSWER_COUNTER


def right_answer_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def ask_question_even():
    number = set_number()
    print(f'Question: {number}')
    issue_answer = right_answer_even(number)
    return issue_answer


def run_even_game(username):
    counter = 0
    while counter < RIGHT_ANSWER_COUNTER:
        issue_answer = ask_question_even()
        user_answer = ask_user_answer()
        if is_right_answer(issue_answer, user_answer):
            counter += 1
        else:
            wrong_answer(user_answer, issue_answer, username)
            break
    else:
        congratulation(username)


def main():
    say_hello()
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    run_even_game(username)


if __name__ == '__main__':
    main()
