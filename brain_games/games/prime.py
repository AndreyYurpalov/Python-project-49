# ---   The goal of the game is to answer the question   ---
# ---                 Is the number prime?               ---


import random


QUESTION_OF_GAME = ('Answer "yes" if given number is prime. '
                    'Otherwise answer "no".')


def is_number_prime(number):
    divisions = [i for i in range(2, number - 1) if number % i == 0]
    return len(divisions) < 1


def get_number_and_answer():
    len_sp = 100
    question = random.randint(2, len_sp)
    correct_answer = 'yes' if is_number_prime(question) else 'no'
    return question, str(correct_answer)
