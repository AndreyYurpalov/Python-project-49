#!/usr/bin/env python3


from brain_games.games import calc
from brain_games.games_engine import engine


def main():
    engine(calc.get_arguments_of_expression_and_answer, calc.QUESTION_OF_GAME)


if __name__ == '__main__':
    main()
