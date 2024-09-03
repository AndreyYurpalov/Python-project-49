import random
from brain_games.games_engine import engine, QUESTION_CALC


def game_cycle_calc():
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


def start_game_calc():
    engine(game_cycle_calc, QUESTION_CALC)
