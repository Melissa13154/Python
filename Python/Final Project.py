#Cards

import numpy as np
import itertools as it
import matplotlib.pyplot as plt
import random

def counting():
        #Creating the deck of cards
        for k in range(10000):  #Gathering data for 1000 seperate hands 
            deck = list(it.product(range(1,14),['Spade','Heart','Diamond','Club'])) 
            random.shuffle(deck)
            hand = [] #intializing hand
            for n in range(5): #Dealing the cards
                hand.append((deck[n][0]))

            
            #Checking for any quad
            check_quad = list(it.combinations(hand,4)) #Generating every combination with length 4 from hand

            quads = [] #intializing variables
            num = 0
            for i in check_quad: #Conditional statement to check for 4 equal cards
                    if check_quad[num][0] == check_quad[num][1] == check_quad[num][2] == check_quad[num][3]: 
                        quads.append((check_quad[num][0],check_quad[num][1],check_quad[num][2],check_quad[num][3]))
                    num += 1
            amt_quad=len(quads) #taking the length of the list to count the amount of 4 of a kind
            global quad_total #global variable to plot value out of function
            quad_total+=amt_quad #Adding length of list value for every iteration 
            

            #Checking for any triples
            check_triple = list(it.combinations(hand,3)) #Generating every combination with length 3 from hand
            triples = [] #Initalizing variables used
            num = 0
            for i in check_triple: #Conditional statment for three of a kind
                    if check_triple[num][0] == check_triple[num][1] == check_triple[num][2]: 
                        triples.append((check_triple[num][0],check_triple[num][1],check_triple[num][2]))
                    num += 1
            amt_triple=len(triples)
            global triple_total
            triple_total += amt_triple

        
            #Checking for any pairs
            """The same idea for pairs but altered to accomodate 2 cards"""
            check_pair = list(it.combinations(hand,2))
            pairs = [] 
            num = 0
            for i in check_pair:
                if check_pair[num][0] == check_pair[num][1]:
                    pairs.append((check_pair[num][0], check_pair[num][1]))
                num += 1
            amt_pair=len(pairs)
            global pair_total
            pair_total+=amt_pair


pair_total = 0 #initalizing the variables used for the data set plotted 
triple_total = 0
quad_total = 0

counting() #calling the function

totals = [pair_total,triple_total,quad_total] #Creating data set
print(totals)
x = np.arange(3) #Three bars for bar graph
plt.bar(x,totals, color='blue', edgecolor='orange') 
plt.xticks(x,["Pairs", "Three-of-a-kinds", "Four-of-a-kinds"])
plt.ylabel("Frequency")
plt.xlabel("Match Type")
plt.show()

     






