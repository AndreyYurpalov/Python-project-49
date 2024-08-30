import random


dic_res = dict()
dic_res['question'] = 'Answer "yes" if given number is prime.'
'Otherwise answer "no".'


def game_cycle():
    len_sp = 100
    number = random.randint(2, len_sp)
    list_div = [i for i in range(2, number - 1) if number % i == 0]
    if len(list_div) >= 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    dic_res['correct_answer'] = str(correct_answer)
    dic_res['number1'] = number
    return dic_res
