from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello
from brain_games.helpers.run_game import run_game
from brain_games.helpers.select_number import set_number


def right_answer_prime(number):
    if number < 2:
        return 'no'
    if number == 2:
        return 'yes'
    if number % 2 == 0:
        return 'no'

    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return 'no'

    return 'yes'


def ask_question_prime():
    number = set_number()
    print(f'Question: {number}')
    issue_answer = right_answer_prime(number)
    return issue_answer


def main():
    say_hello()
    username = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    run_game(username, ask_question_prime)


if __name__ == '__main__':
    main()