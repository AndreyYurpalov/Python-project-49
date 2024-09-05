# ---   The goal of the game is to answer the question   ---
# ---  Find the greatest common divisor of given numbers. ---


import random
import math


QUESTION_OF_GAME = 'Find the greatest common divisor of given numbers.'


def get_numbers_and_answer():
    num1, num2 = random.randint(1, 20), random.randint(1, 20)
    correct_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return question, str(correct_answer)
