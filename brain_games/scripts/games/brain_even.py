from random import random
from brain_games.engine import *


task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_correct_answer(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def get_even_feature():
    even_question = give_question(int(random()*100))
    answer = user_answer()
    correct_answer = even_correct_answer(even_question)
    return [answer, correct_answer]


def start_even_game(name):
    give_task(task)
    three_rounds_loop(get_even_feature, name)
    


def main():
    name = welcome_user()
    start_even_game(name)
        
        
if __name__ == '__main__':
    main()
