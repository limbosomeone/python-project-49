#!/usr/bin/env python3
from brain_games.scripts.games.brain_even import start_even_game
from brain_games.scripts.games.brain_calc import start_calc_game
from brain_games.scripts.games.brain_gcd import start_gcd_game
from brain_games.scripts.games.brain_progression import start_progression_game
from brain_games.scripts.games.brain_prime import start_prime_game
from ..cli import welcome_user
import prompt


def give_game(choice, name):
    if choice == 'brain-even':
        start_even_game(name)
    elif choice == 'brain-calc':
        start_calc_game(name)
    elif choice == 'brain-gcd':
        start_gcd_game(name)
    elif choice == 'brain-progression':
        start_progression_game(name)
    elif choice == 'brain-prime':
        start_prime_game(name)
    else:
        print('Try to enter the game name correctly')


def main():
    name = welcome_user()
    answer = prompt.string('Do you want play to brain-games ? (yes/no) ')
    if answer == 'yes':
        choice = prompt.string(f'Choose game: brain-calc, brain-even, '
                               f'brain-gcd, brain-progression, brain-prime: ')
        give_game(choice, name)
    else:
        print('Come back if you want to play!')


if __name__ == '__main__':
    main()
