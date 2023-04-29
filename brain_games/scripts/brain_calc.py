import operator
import prompt
from random import random, uniform
from ..cli import welcome_user


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


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
    print('Welcome to the Brain Games!')
    name = welcome_user()
    counter = 0
    questions_count = 3
    print('What is the result of the expression?')
    for i in range(questions_count):
        expresion = random_exprection()
        correct_answer = expresion[1]
        print(f'Question: {expresion[0]}')
        answer = user_answer()
        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
            f"'{correct_answer}'.\nLet's try again, {name}!")
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()