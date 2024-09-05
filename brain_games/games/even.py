# ---   The goal of the game is to answer the question   ---
# ---                  Is the number even?               ---


import random


QUESTION_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_random_num_and_answer():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return str(question), str(correct_answer)
