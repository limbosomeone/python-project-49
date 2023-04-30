from .cli import *
import prompt


"""
config_list = [
    task,
    question(),
    correct_answer(question),
    ]
"""


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def give_task(task):
    print(task)
    

def give_question(question):
    print(f'Question: {question}')
    return question


def compare_answers(answer, correct_answer, name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.\nLet's try again, {name}!")
        return False

        