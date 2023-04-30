import operator
from random import random, uniform
from brain_games.engine import start_brain_game
from brain_games.cli import welcome_user


task = 'What is the result of the expression?'
get_operator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}.get


def random_exprection():
    x = int(random() * 100)
    y = int(random() * 10)
    operator_index = int(uniform(0, 3))
    operator_list = ['+', '*', '-']
    random_operator = operator_list[operator_index]
    expresion = f'{x} {random_operator} {y}'
    return expresion


def ask_calc_question():
    expression = random_exprection()
    return expression


def get_calc_correct_answer(question_result):
    x, op, y = question_result.split()
    expresion_result = get_operator(op)(int(x), int(y))
    return expresion_result


def start_calc_game(name):
    start_brain_game(task, ask_calc_question, get_calc_correct_answer, name)


def main():
    name = welcome_user()
    start_calc_game(name)


if __name__ == '__main__':
    main()
