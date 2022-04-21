# import your packages
import itertools
import numpy as np
import csv

#0 Kaylen
#1 Victoria
#2 Francesca
#3 Emma
#4 Camille
#5 Alyssa
#6 Mikala
#7 Julia
#8 Nicole
#9 Tori

#A Gio
#B Cam
#C Asaf
#D John
#E Prosper
#F Sam
#G Cameron
#H Morgan
#I Stephen
#J Tyler

#Fixed = [1,2,3,4,5,6,7,8,9,10]
Fixed = [0,1,2,3,4,5,6,7,8,9]

# open a blank file and write the headers
with open('../data/possible_combinations.csv', 'w' , newline="") as writeFile:
    writer = csv.writer(writeFile)
    headers = Fixed
    writer.writerow(headers)

    # calculate the permutations
    permu = list(itertools.permutations('ABCDEFGHIJ', 10))
    
    # print the number of permutations
    print("The total number of possible permutations (at game start) is:", len(permu),"\n")
    
    ##  RULE for MATCHES
    
    # 6 = G
    # 5 = F
    
    ##  RULES for NO MATCH
    
    # 9 != E & Prosper and Tori. No match
    # 7 != D & Jon and Julia no match
    # 9 != C & Asaf and Tori no match
    # 0 != A & Gio and Kaylen no match
    # 1 != B & Victoria and Cam no match
    
    
    ##  GUESSES
    
    g1 =  ('A', 'B', 'C', 'D', 'E','F','G','H','I','J')
    b1 = 3
    
    g2 =  ('A','J','F','E','C','H','G','B','D','I')
    b2 = 3
    
    g3 =  ('A','D','H','E','C','F','G','J','B','I')
    b3 = 4
    
    g4 =  ('A','D','J','B','C','F','G','I','E','H')
    b4 = 4
    
    g5 =  ('J','E','A','B','C','F','G','H','I','D')
    b5 = 4
    
    g6 =  ('E','B','A','D','C','F','G','I','J','H')
    b6 = 4
    
    g7 =  ('D','E','C','A','J','F','G','I','B','H')
    b7 = 4
    
    James_guess = ('C','D','A','E','J','F','G','B','I','H')
    #                   ______________________
    
    print("This is my guess:\n", James_guess,"\n")
    
    # a function for comparing beams
    def comp(x,y):
        output = (list(np.array(x) == np.array(y))).count(True)
        return output
    
    #beam checker    
    comp(James_guess,g7)
    
    index = 0
    
    ## GUESS CHECKS
    
    for l in [g1,g2,g3,g4,g5,g6,g7]:
        print(l,"   ",set(l)==set(['A', 'B', 'C', 'D', 'E','F','G','H','I','J']))
    print("\n")
        
    # loop for beams, matches and no matches
    for n in permu:
        
        # if guess1 and guess2 produce the same number of beams.
        if comp(n,g1) == b1 and comp(n,g2) == b2 and comp(n,g3) == b3 and comp(n,g4) == b4 and comp(n,g5) == b5 and comp(n,g6) == b6 and comp(n,g7) == b7:
            
            # Matches
            if list(n)[6]=="G" and list(n)[5]=="F":
                # guesses
            #if list(n)[6]=="G" and list(n)[5]=="F" and list(n)[4]=="C" and list(n)[3]=="E" and list(n)[2]=="J"  and list(n)[7]=="H":
                
                # No Match
                if list(n)[9]!="E" and list(n)[7]!="D" and list(n)[9]!="C" and list(n)[0]!="A" and list(n)[1]!="B":
                    print(n)
                    # write list to csv
                    writer.writerow(list(n))
                    # if all conditions are satisfied then add 1 to index
                    index = index + 1

print("\n","Number of possible permutations once filtered over known conditions:",index)

                
                
            
