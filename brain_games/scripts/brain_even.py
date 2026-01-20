from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello
from brain_games.helpers.run_game import run_game
from brain_games.helpers.select_number import set_number


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


def main():
    say_hello()
    username = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    run_game(username, ask_question_even)


if __name__ == '__main__':
    main()
