import random

from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello
from brain_games.helpers.run_game import run_game
from brain_games.helpers.select_number import set_number
from brain_games.settings import EXPRESSIONS


def counted_result_calc(a, b, selected_expression):
    if selected_expression == '+':
        return a + b
    elif selected_expression == '*':
        return a * b
    elif selected_expression == '-':
        return a - b
    return None


def select_numbers_calc(random_expression):
    a = set_number()
    b = set_number()
    result = counted_result_calc(a, b, random_expression)
    string_expression = str(f'{a} {random_expression} {b}')
    count_expression = f'{result}'
    return [string_expression, count_expression]


def ask_question_calc():
    random_expression = random.choice(EXPRESSIONS)
    expression = select_numbers_calc(random_expression)
    question = expression[0]
    print(f'Question: {question}')
    return expression[1]


def main():
    say_hello()
    username = welcome_user()
    print('What is the result of the expression?')
    run_game(username, ask_question_calc)


if __name__ == '__main__':
    main()