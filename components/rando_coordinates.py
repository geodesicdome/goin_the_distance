"""Generates random coordinate pairs"""
# The line below allows us to use the function randint
from random import randint

def prints_random_number():
    """Prints a random number"""
    # randint returns a random integer, we are giving it 0 & 10, so it'll return
    # a random integer between 0 - 10 (https://docs.python.org/2/library/random.html#random.randint)
    print randint(0,10)

prints_random_number()
