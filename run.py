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

def rules():
    """
    function to display rules for users
    """
    clear_terminal()
    print(
        """
        Hangman is a word guessing game.\n
        The object of the game is to figure out the unknown word by guessing letters.\n
        If the letter is in the unknown word it will display.\n
        If the guessed letter is not in the unknown word you will lose a try.\n
        You will have 6 tries to guess before you are hanged and lose the game!
        You can choose the different theme of words, M for movies theme, C for cars theme, A for animals theme.\n
        Good luck!
        """)
    input(' ' * 12 + 'Press enter to return to the main menu\n')
    welcome()

def set_theme():
    """
    function to set the theme of the word
    """
    print('\n')
    print('Please select M for movies theme,'.center(80))
    print('C for cars theme and A for animals theme'.center(80))
    theme = False
    while not theme:
        theme_level = input(' '.center(40)).upper()
        if theme_level == 'M':
            theme = True
            lives = 6
        elif theme_level == 'C':
            theme = True
            lives = 6
        elif theme_level == 'A':
            theme = True
            lives = 6
        else:
            print('Please select M, C or A'.center(80))
    return lives
    