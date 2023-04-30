from random import random
from brain_games.engine import *
from brain_games.cli import welcome_user


task = 'Find the greatest common divisor of given numbers.'

def gcd_correct_answer(question):
    a, b = question
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b
    

def get_gcd_feature():
    numbers_pair = (int(random()*100), int(random()*10))
    gcd_question = give_question(numbers_pair)
    answer = user_answer()
    answer = int(answer) if answer.isdigit() else answer
    correct_answer = gcd_correct_answer(gcd_question)
    return [answer, correct_answer]


def start_gcd_game(name):
    give_task(task)
    three_rounds_loop(get_gcd_feature, name)
    
    
def main():
    name = welcome_user()
    start_gcd_game(name)
    
    
if __name__ == '__main__':
    main()