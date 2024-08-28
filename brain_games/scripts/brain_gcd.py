#!/usr/bin/env python3


from brain_games.games_engine import engine
from brain_games.games.gcd import dic_res, game_cycle


def main():
    engine(dic_res, game_cycle)


if __name__ == '__main__':
    main()
