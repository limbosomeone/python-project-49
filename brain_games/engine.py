import prompt


"""
config_list = [
    task,
    question(),
    correct_answer(),
    ]
"""


def give_task(task):
    print(task)


def give_question(game_question):
    print(f'Question: {game_question}')
    return game_question


def get_user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def compare_answers(answer, correct_answer, name):
    answer = int(answer) if answer.isdigit() else answer
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was "
              f"'{correct_answer}'.\nLet's try again, {name}!")
        return False


def three_rounds_loop(ask_game_question, get_game_correct_answer, name):
    counter = 0
    question_count = 3
    for i in range(question_count):
        question = ask_game_question()
        give_question(question)
        correct_answer = get_game_correct_answer(question)
        answer = get_user_answer()
        compare_result = compare_answers(answer, correct_answer, name)
        if compare_result:
            counter += 1
        else:
            break
    if counter == 3:
        print(f'Congratulations, {name}!')


def start_brain_game(task, ask_game_question, get_game_correct_answer, name):
    give_task(task)
    three_rounds_loop(ask_game_question, get_game_correct_answer, name)
