#Problem 3
import matplotlib.pyplot as plt

def sums():
    n = 1 #initalizing n and x for the range of imputs
    x = 1
    sum = 0 #initalizing the sum of each iteration for each n
    xsum = [] #creating an array to store each total sum value for every x
    for x in range(0,100): #cycles through 100 values of x
        for n in range(1,100): #for each value of x,cycles through 99 values of n
            equ = ((x)**n)/n #equation given
            sum += equ #adding the current sum to all of the last sums from each iteration
        xsum.append(sum) #adds each result of the sum with the value of x to the end of the inital array after each iteration
    #Plotting the list created (xsum)
    plt.plot(xsum)
    plt.show() 

sums() #calling the function




    