# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 15:08:12 2017

@author: james
"""


import random

def roll(sides=6):
    num_rolled=random.randint(1,sides)
    return num_rolled

def main():
    sides=6
    rolling=True
    while rolling:
        roll_again = input("Ready to roll? ENTER=Roll. Q=Quit.")
        if roll_again.lower()!="q":
            num_rolled=roll(sides)
            print("You rolled a", num_rolled)
        else:
            rolling=False
            print("Thanks for playing.")
main()
