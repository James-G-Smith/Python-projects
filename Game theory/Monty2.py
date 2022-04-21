# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 12:06:08 2018

@author: james
"""

from random import randint
import time

print("Starting Monty Game...")
time.sleep(2)
print("How many times do you want to play?")
playnumber=int(input())
time.sleep(2)
print("Do you want to swap or not (y/n)?")
yorn=input()
wins=[]
for game in range(0,playnumber):
    car=randint(1, 3)

    guess=randint(1, 3)

    if car==guess:
    
        goat=list(set([1,2,3])-set([car]))[randint(0, 1)]
    
        if yorn=="y":
            wins.append(0)
        if yorn=="n":
            wins.append(1)
        
    if car!=guess:
        goat=list(set([1,2,3])-set([car,guess]))[0]
    
        if yorn=="y":
            newguess=list(set([1,2,3])-set([goat,guess]))
            if car==newguess[0]:
                wins.append(1)
            else:
                wins.append(0)
        if yorn=="n":
            wins.append(0)
    #print(game/playnumber*100)            
print("You won a CAR " + str(sum(wins)/playnumber*100) + "% of the time.")