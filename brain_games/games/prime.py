import random
from brain_games.games_engine import engine, QUESTION_PRIME


def game_cycle_prime():
    len_sp = 100
    question = random.randint(2, len_sp)
    list_div = [i for i in range(2, question - 1) if question % i == 0]
    correct_answer = 'yes' if len(list_div) < 1 else 'no'
    return question, str(correct_answer)


def start_game_prime():
    engine(game_cycle_prime, QUESTION_PRIME)
