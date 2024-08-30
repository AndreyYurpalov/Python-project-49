import random


dic_res = dict()
dic_res['question'] = 'What number is missing in the progression?'


def game_cycle():
    start_sp = random.randint(1, 100)
    kof_prog = random.randint(2, 4)
    len_prog = 10
    progression = [i * kof_prog for i in range(start_sp, len_prog + start_sp)]
    i = random.randint(0, 9)
    correct_answer = progression[i]
    progression[i] = '..'
    dic_res['correct_answer'] = str(correct_answer)
    number = ' '.join(str(arg) for arg in progression)
    dic_res['number1'] = number
    return dic_res
