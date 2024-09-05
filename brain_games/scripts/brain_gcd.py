#!/usr/bin/env python3


from brain_games.games import gcd
from brain_games.games_engine import engine


def main():
    engine(gcd.get_numbers_and_answer, gcd.QUESTION_OF_GAME)


if __name__ == '__main__':
    main()
