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


def three_rounds_loop(game_feature, name):
    counter = 1
    question_count = 3
    for i in range(question_count):
        answer, correct_answer = game_feature()
        compare_result = compare_answers(answer, correct_answer, name)
        if compare_result:
            counter += 1
        else:
            break
    if counter == 4:
        print(f'Congratulations, {name}!')
        