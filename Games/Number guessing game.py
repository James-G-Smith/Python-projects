# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 16:36:52 2017

@author: james
"""

import random


number=random.randint(1,100)
guesses=0
win=False

while guesses<6:
        guess=int(input("Your guess?"))
        guesses+=1
            
            
        if guess>number:
            print("Your guess was too high", 6-guesses, "remaining")
                
        elif guess<number:
            print("Your guess was too low", 6-guesses, "remaining")
        else:
                    
            print("Nailed it. Thanks for playing.")
            win=True
            guesses=0

if win==False:
    print("Sorry")
