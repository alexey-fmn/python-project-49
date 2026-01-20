from brain_games.cli import welcome_user
from brain_games.helpers.chat import say_hello


def main():
    say_hello()
    welcome_user()


if __name__ == "__main__":
    main()