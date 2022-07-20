#Problem 4

import matplotlib.pyplot as plt
import numpy as np

def midpoint(f,a = 0.0, b = 10.0, n = 100):  #defining variables
    total = [] #Initalizing array
    delta_x = (b - a)/n #Distance between each midpoint
    for i in range(n):
        #area = (f((delta_x*i + delta_x*(i+1))/2)*(delta_x)) How to find area of rectangle but dont think its needed?
        height = (f((delta_x*i + delta_x*(i+1))/2)) #Height of function at midpoint
        total.append(height) #Adding each height value to a list
    x = np.arange(a,b, delta_x) #Defining the range of points
    plt.bar(x,total, align='edge', width=delta_x, color='yellow', edgecolor='orange') #Approximation of integral
    plt.plot(x,f(x)) #Given function
    plt.show()


def f(x): #Calling function
    return x**2

midpoint(f)


 








