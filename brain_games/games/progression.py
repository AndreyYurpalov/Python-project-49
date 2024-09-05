# ---   The goal of the game is to answer the question   ---
# ---     What number is missing in the progression?     ---


import random


QUESTION_OF_GAME = 'What number is missing in the progression?'


def get_progression_whit_missing_number_and_answer():
    start_sp = random.randint(1, 100)
    kof_prog = random.randint(2, 4)
    len_prog = 10
    progression = [i * kof_prog for i in range(start_sp, len_prog + start_sp)]
    i = random.randint(0, 9)
    correct_answer = progression[i]
    progression[i] = '..'
    question = ' '.join(str(arg) for arg in progression)
    return str(question), str(correct_answer)
