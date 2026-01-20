import random

from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello
from brain_games.helpers.run_game import run_game
from brain_games.helpers.select_number import set_number


def generate_progression():
    length = set_number(5, 15)
    step = set_number(1, 6)
    start = set_number(1, 50)

    progression = [start + i * step for i in range(length)]

    hidden_index = random.randrange(length)
    hide_number = progression[hidden_index]
    progression[hidden_index] = '..'
    map_progression = " ".join(map(str, progression))

    return [map_progression, hide_number]


def ask_question_progression():
    progression = generate_progression()
    print(f'Question: {progression[0]}')
    return progression[1]


def main():
    say_hello()
    username = welcome_user()
    print('What number is missing in the progression?')
    run_game(username, ask_question_progression)


if __name__ == '__main__':
    main()