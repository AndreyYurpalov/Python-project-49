import random
from brain_games.games_engine import engine, QUESTION_PROGRESSION


def game_cycle_progression():
    start_sp = random.randint(1, 100)
    kof_prog = random.randint(2, 4)
    len_prog = 10
    progression = [i * kof_prog for i in range(start_sp, len_prog + start_sp)]
    i = random.randint(0, 9)
    correct_answer = progression[i]
    progression[i] = '..'
    question = ' '.join(str(arg) for arg in progression)
    return str(question), str(correct_answer)


def start_game_progression():
    engine(game_cycle_progression, QUESTION_PROGRESSION)
