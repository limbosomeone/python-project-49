from random import random
from brain_games.engine import start_brain_game
from brain_games.cli import welcome_user


task = 'Find the greatest common divisor of given numbers.'


def ask_gcd_question():
    question = (int(random()*100), int(random()*10))
    correct_answer = question
    return (question, correct_answer)


def get_gcd_correct_answer(question_result):
    a, b = question_result
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def start_gcd_game(name):
    start_brain_game(task, ask_gcd_question, get_gcd_correct_answer, name)


def main():
    name = welcome_user()
    start_gcd_game(name)


if __name__ == '__main__':
    main()
