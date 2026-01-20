from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello
from brain_games.helpers.run_game import run_game
from brain_games.helpers.select_number import set_number


def right_answer_gcd(first_number, second_number):
    first_number = abs(first_number)
    second_number = abs(second_number)

    while second_number != 0:
        first_number, second_number = (
            second_number, first_number % second_number)

    return int(first_number)


def ask_question_gcd():
    first_number = set_number()
    second_number = set_number()
    print(f'Question: {first_number} {second_number}')
    issue_answer = right_answer_gcd(first_number, second_number)
    return int(issue_answer)


def main():
    say_hello()
    username = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    run_game(username, ask_question_gcd)


if __name__ == '__main__':
    main()