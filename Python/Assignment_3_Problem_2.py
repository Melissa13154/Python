# Problem 2
import matplotlib.pyplot as plt

def equation(): #Function
    n = 1 #Initalizing n at 1
    sum = 0 #Initalizing sum of all computations at 0
    y = [] #Initalizing the set of all sums for each iteration 
    for n in range(0,1000):
        equ = (-1)**(n+1)*(1/n) #Equation being used to approximate
        sum += equ #Adding the result to the sum of the last result of n - 1
        y.append(sum) #Adding the sum to the end of the list of data points
    
    #Plotting the data points on a range of  0 to 1000
    figure, ax = plt.subplots() 
    ax.axis = ([0,1000, 0,1])
    plt.plot(y)
    plt.show()

equation()




