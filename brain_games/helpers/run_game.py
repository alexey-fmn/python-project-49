from brain_games.helpers.chat import (
    ask_user_answer,
    congratulation,
    wrong_answer,
)
from brain_games.helpers.compare_results import is_right_answer
from brain_games.settings import RIGHT_ANSWER_COUNTER


def run_game(username, game):
    counter = 0
    while counter < RIGHT_ANSWER_COUNTER:
        issue_answer = game()
        user_answer = ask_user_answer()
        if is_right_answer(issue_answer, user_answer):
            print('Correct!')
            counter += 1
        else:
            wrong_answer(user_answer, issue_answer, username)
            break
    else:
        congratulation(username)