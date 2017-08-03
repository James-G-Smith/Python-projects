# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:34:06 2017

@author: james
"""
        
import math

def main():
    count = 3
    
    while True:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            print(count)
        
        count += 1
main()