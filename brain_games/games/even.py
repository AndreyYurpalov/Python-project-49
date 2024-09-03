import random
from brain_games.games_engine import engine, QUESTION_EVEN


def is_even(num):
    return num % 2 == 0


def game_cycle_even():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), str(correct_answer)


def start_game_even():
    engine(game_cycle_even, QUESTION_EVEN)
