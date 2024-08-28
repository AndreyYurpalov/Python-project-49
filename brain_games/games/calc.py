import random


dic_res = dict()
dic_res['question'] = 'What is the result of the expression?'


def game_cycle():
    sp_arguments = [random.randint(1, 15) for _ in range(2)]
    actions = ('+', '-', '*')
    action = random.choice(actions)
    if action == '+':
        correct_answer = sp_arguments[0] + sp_arguments[1]
    elif action == '-':
        correct_answer = sp_arguments[0] - sp_arguments[1]
    else:
        correct_answer = sp_arguments[0] * sp_arguments[1]
    dic_res['correct_answer'] = str(correct_answer)
    number = f'{sp_arguments[0]} {action} {sp_arguments[1]}'
    dic_res['number'] = number
    return dic_res
