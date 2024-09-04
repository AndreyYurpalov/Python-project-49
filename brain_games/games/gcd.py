import random
import math
from brain_games.games_engine import engine, QUESTION_GCD


def game_cycle_gcd():
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    correct_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return question, str(correct_answer)


def start_game_gcd():
    engine(game_cycle_gcd, QUESTION_GCD)
