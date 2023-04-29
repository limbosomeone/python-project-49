import prompt
from random import random
from ..cli import welcome_user


def user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    counter = 0
    questions_count = 3
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(questions_count):
        number_for_question = int(random() * 100)
        print(f'Question: {number_for_question}')
        answer = user_answer()
        if number_for_question % 2 == 0:
            correct_answer = 'yes'
            if answer == correct_answer:
                print('Correct!')
                counter += 1
            else:
                print(f"'{answer}' is wrong answer ;(. Correct answer was "
                      f"'{correct_answer}'.\nLet's try again, {name}!")
                break
        else:
            correct_answer = 'no'
            if answer == correct_answer:
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
