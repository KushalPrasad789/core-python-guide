# =============================================================
# DAY 1 OF PYTHON PROGRAMMING WORKSHOP
# =============================================================

# DECORATORS
# -----------------
def decorator(func):
    def wrapper():
        print('first thing')
        func()
        print('second thing')
    return wrapper

@decorator
def hello():
    print('Hello World')
    
hello()
hello()

# ======================================================

commands = {}

def command(func):
    def wrapper():
        commands[func.__name__] = func
    return wrapper

@command
def hello():
    print('Hello World')
    
@command
def tey():
    print('This is tey')
    
hello()
tey()

commands['hello']() # Prints hello world

print(commands)

print('Hello function: ', hello.__name__)


# ==========================================================
# WAP to take the function name as input from the user and call the function
commands = {}

def command(func):
    def wrapper():
        commands[func.__name__] = func
    return wrapper

@command
def morning():
    print('Good Morning')
    
@command
def afternoon():
    print('Good Afternoon')
    
@command
def evening():
    print('Good Evening')
    
morning()
afternoon()
evening()

# Take input from user
function_name = input('Enter the function you want to call: ')
commands[function_name]() # Call the function

# =====================================================================
# LIBRARIES IN PYTHON
# ----------------------------

# First method
import random

random_num = random.randint(1, 7)
print(random_num)

# ---------------------------------------------------------

# Second method
import random as rd
random_num = rd.randint(1, 7)
print(random_num)

# -------------------------------------------------------------

# Third method
from random import *
random_num = randint(1, 7)
print(random_num)

# --------------------------------

# Fourth method
from random import randint
random_num = randint(1, 7)
print(random_num)

#-------------------------------------------------

# Selection of random item from list
import random

games = ['football', 'cricket', 'tennis', 'badminton', 'basketball']
random_game = random.choice(games)
print(random_game)

# ============================================================================
# GUESS THE NUMBER GAME
# ------------------------
import random

class Game:
    def __init__(self, name):
        self.name = name
        
    def guess_the_number(self):
        print(f'Welcome {name} to GUESS THE NUMBER GAME:')
        print('*' * 35)
        number_to_guess = random.randint(1, 100)
        attempts = 0
        while True:
            user_guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1
            if user_guess < number_to_guess:
                print("❌ Too low!")
            elif user_guess > number_to_guess:
                print("❌ Too high!")
            else:
                print(f"🚩 Congratulations {name}! You've guessed the number in {attempts} attempts.")
                break

name = input('Enter your name: ')
player = Game(name)
player.guess_the_number()

# ==============================================================================================

import random

# random.seed()
random.seed(40)

print(random.randint(0, 34)) # Running multiple times doesn't affect the output


# ==================================================================================================
# os MODULE
# ----------------
import os

# Getting the present working directory
print(os.getcwd()) # Gives the working directory

# Making a new folder
os.mkdir('folder')

# Removing the folder
os.rmdir('folder')

# Changing the directory
os.mkdir('folder') # Creates a new folder
os.chdir('folder') # Changing the directory

# Using the commandline  commands
os.system('') # Write the command line command inside ''

# ======================================================================
# VIRTUAL ENVIRONMENT
# -------------------------
# python -m venv cosmos # To setup the virtual environment named cosmos
# .\cosmos\Scripts\activate.bat # To activate the virtual environment
