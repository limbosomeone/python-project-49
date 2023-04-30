from random import random
from brain_games.cli import welcome_user
from brain_games.engine import start_brain_game


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def ask_even_question():
    return int(random() * 100)


def get_even_correct_answer(question_result):
    if question_result % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def start_even_game(name):
    start_brain_game(task, ask_even_question, get_even_correct_answer, name)


def main():
    name = welcome_user()
    start_even_game(name)


if __name__ == '__main__':
    main()
