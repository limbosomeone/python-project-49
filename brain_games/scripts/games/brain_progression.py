from random import random, uniform
from brain_games.engine import start_brain_game
from brain_games.cli import welcome_user


task = 'What number is missing in the progression?'


def ask_progression_question():
    first_number = int(random() * 100) + 1
    progression_step = int(random() * 10) + 1
    progression_len = first_number + int(uniform(5, 15)) * progression_step
    progression_list = [str(x) for x in range(first_number,
                                              progression_len,
                                              progression_step)]
    progression_list
    i = int(uniform(0, len(progression_list)))
    for_correct_answer = int(progression_list[i])
    progression_list[i] = '..'
    question = ' '.join(progression_list)
    return (question, for_correct_answer)


def get_progression_correct_answer(question_result):
    correct_answer = question_result
    return correct_answer


def start_gcd_game(name):
    start_brain_game(task,
                     ask_progression_question,
                     get_progression_correct_answer,
                     name)


def main():
    name = welcome_user()
    start_gcd_game(name)
