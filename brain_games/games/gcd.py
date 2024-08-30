import random


dic_res = dict()
dic_res['question'] = 'Find the greatest common divisor of given numbers.'


def game_cycle():
    sp_arguments = [random.randint(1, 12) for _ in range(2)]
    sp_arguments.sort()
    answer = [sp_arguments[0] // (i + 1) for i in range(sp_arguments[0])
              if sp_arguments[0] % (i + 1) == 0]
    control_answer = [sp_arguments[1] // answer[i] for i in range(len(answer))
                      if sp_arguments[1] % answer[i] == 0]
    correct_answer = sp_arguments[1] // min(control_answer)
    dic_res['correct_answer'] = str(correct_answer)
    dic_res['number1'] = sp_arguments[0]
    dic_res['number2'] = sp_arguments[1]
    return dic_res
