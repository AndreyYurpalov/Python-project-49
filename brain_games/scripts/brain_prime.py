#!/usr/bin/env python3


from brain_games.games import prime
from brain_games.games_engine import engine


def main():
    engine(prime.get_number_and_answer, prime.QUESTION_OF_GAME)


if __name__ == '__main__':
    main()
