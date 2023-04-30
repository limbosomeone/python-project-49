import operator
from random import random, uniform
from brain_games.engine import *


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
    expresion_result = get_operator(random_operator)(x, y)
    return (expresion, expresion_result)


def get_calc_feature():
    expression = random_exprection()
    calc_question = give_question(expression[0])
    answer = user_answer()
    answer = int(answer) if answer.isdigit() else answer
    correct_answer = expression[1]
    return [answer, correct_answer]


def start_calc_game(name):
    give_task(task)
    three_rounds_loop(get_calc_feature, name)
    

def main():
    name = welcome_user()
    start_calc_game(name)


if __name__ == '__main__':
    main()