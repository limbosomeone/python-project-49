from random import uniform
from brain_games.engine import start_brain_game
from brain_games.cli import welcome_user


task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def ask_prime_question():
    question = int(uniform(1, 100))
    for_correct_answer = question
    return (question, for_correct_answer)


def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def get_prime_correct_answer(question_result):
    answer = isPrime(question_result)
    if answer:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def start_prime_game(name):
    start_brain_game(task, ask_prime_question, get_prime_correct_answer, name)


def main():
    name = welcome_user()
    start_prime_game(name)


if __name__ == '__main__':
    main()
