# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:59:23 2018

@author: james
"""

from random import randint
import time

print("Starting Monty Game...")
time.sleep(2)
print("Chosing door number for car...")
time.sleep(2)


car=randint(1, 3)
print("Choose one of the following doors: |1| |2| |3|")
guess=int(input(""))

if car==guess:
    
    goat=list(set([1,2,3])-set([car]))[randint(0, 1)]
    print("There is a goat behind door number |" + str(goat) + "|")
    time.sleep(2)
    print("Do you want to swap (y/n)?")
    yorn=input()
    time.sleep(2)
    if yorn=="y":
        print("Sorry. You have won a GOAT. Enjoy!")
    if yorn=="n":
        print("You have won a CAR. Congratulations!")
        
if car!=guess:
    goat=list(set([1,2,3])-set([car,guess]))[0]
    print("There is a goat behind door number |" + str(goat) + "|")
    time.sleep(2)
    print("Do you want to swap (y/n)?")
    yorn=input()
    time.sleep(2)
    if yorn=="y":
        newguess=list(set([1,2,3])-set([goat,guess]))
        if car==newguess[0]:
            print("You have won a CAR. Congratulations!")
        else:
            print("Sorry. You have won a GOAT. Enjoy!")
    if yorn=="n":
        print("Sorry. You have won a GOAT. Enjoy!")

