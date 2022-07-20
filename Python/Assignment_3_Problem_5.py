#Problem 5
import sympy as sp
from IPython.display import display

x = sp.symbols('x') #Defining x as a symbol rather than a variable

display(sp.diff((x**3) - ((sp.cos(sp.pi*x)**2)/(2*(x**2)+1)) + (11/3)*(x**2) - 1, x)) #Printing the derivative of the given function


