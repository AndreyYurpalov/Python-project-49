#!/usr/bin/env python3


from brain_games.games import progression
from brain_games.games_engine import engine


def main():
    engine(progression.get_progression_whit_missing_number_and_answer,
           progression.QUESTION_OF_GAME)


if __name__ == '__main__':
    main()
