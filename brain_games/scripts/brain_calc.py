import operator
from random import random, uniform
from ..cli import welcome_user
from ..engine import *


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


def main():
    name = welcome_user()
    give_task(task)
    counter = 1
    for i in range(3):
        exprestion = random_exprection()
        give_question(exprestion[0])
        answer = user_answer()
        answer = int(answer) if answer.isdigit() else answer
        correct_answer = int(exprestion[1])
        compare_result = compare_answers(answer, correct_answer, name)
        if compare_result:
            counter += 1
        else:
            break
    if counter == 4:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()