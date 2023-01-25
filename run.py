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
    