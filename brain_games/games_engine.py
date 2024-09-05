import prompt
from brain_games.games.cli import welcome_user


ATTEMPT = 3


def engine(game, quest):
    name = welcome_user()
    print(quest)
    for _ in range(ATTEMPT):
        question, correct_answer = game()
        print(f'Question: {question}')
        your_answer = prompt.string("Your answer: ")
        if str(your_answer) == str(correct_answer):
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
