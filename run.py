"""
Project 3 for Code Istitute
"""
import random
import os
import words
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

MOVIES_LEVEL = words.movies_words
CARS_LEVEL = words.cars_words
ANIMALS_LEVEL = words.animals_words
 
def clear_terminal():
    """
    function to clean terminal
    """
    os.system(('cls' if os.name == 'nt' else 'clear'))
    title()

def title():
    """
    function to display the title
    """
    print(
        """
        ░▒█░▒█░█▀▀▄░▒█▄░▒█░▒█▀▀█░▒█▀▄▀█░█▀▀▄░▒█▄░▒█
        ░▒█▀▀█▒█▄▄█░▒█▒█▒█░▒█░▄▄░▒█▒█▒█▒█▄▄█░▒█▒█▒█
        ░▒█░▒█▒█░▒█░▒█░░▀█░▒█▄▄▀░▒█░░▒█▒█░▒█░▒█░░▀█
        """
    )

def welcome():
    """
    function to display title with navigation to start the game or read rules
    """
    clear_terminal()
    print('\n')
    print(' 1 PLAY GAME '.center(80))
    print(' 2 HOW TO PLAY '.center(80))
    print('\n' * 4)
    while True:
        player_choice = input(' ' * 28 + 'Select 1 or 2: ')
        if player_choice == '1':
            start_game()
        elif player_choice == '2':
            rules()
        else:
            print('Please select 1 or 2'.center(77))
            print('\n')

