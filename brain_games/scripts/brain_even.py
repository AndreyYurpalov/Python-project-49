#!/usr/bin/env python3


from brain_games.games import even
from brain_games.games_engine import engine


def main():
    engine(even.get_random_num_and_answer, even.QUESTION_OF_GAME)


if __name__ == '__main__':
    main()
