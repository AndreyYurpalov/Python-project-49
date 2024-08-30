import random


dic_res = dict()
dic_res['question'] = ('Answer "yes" if the number is even, '
                       'otherwise answer "no".')


def game_cycle():
    number = random.randint(1, 100)
    control = number % 2
    if control == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    dic_res['correct_answer'] = str(correct_answer)
    dic_res['number1'] = number
    return dic_res
