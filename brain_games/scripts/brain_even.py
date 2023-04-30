from random import random
from ..engine import *


task = 'Answer "yes" if the number is even, otherwise answer "no".'
def even_correct_answer(question):
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def main():
    name = welcome_user()
    give_task(task)
    counter = 1
    for i in range(3):
        even_question = give_question(int(random()*100))
        answer = user_answer()
        correct_answer = even_correct_answer(even_question)
        compare_result = compare_answers(answer, correct_answer, name)
        if compare_result:
            counter += 1
        else:
            break
    if counter == 4:
        print(f'Congratulations, {name}!')
        
        
if __name__ == '__main__':
    main()
