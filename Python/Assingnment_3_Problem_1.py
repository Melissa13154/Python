## Problem 1
import numpy as np

#Defining given arrays
A = np.array([[1, 2], [3, 4]]) 
b = np.array([[5], [8]])

#Solving for x
x = np.linalg.solve(A,b)
print(x)