# ---   The goal of the game is to answer the question   ---
# ---         What is the result of the expression?'     ---


import random


QUESTION_OF_GAME = 'What is the result of the expression?'


def get_question_and_correct_answer():
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    actions = ('+', '-', '*')
    action = random.choice(actions)
    if action == '+':
        correct_answer = num1 + num2
    elif action == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    question = f'{num1} {action} {num2}'
    return question, str(correct_answer)
