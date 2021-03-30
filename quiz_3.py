from derivative import derivative
import numpy as np
import math 

def f(x):
    return math.sin(0.5*(x**(1/2)))/x

point = 1
h = 0.2
derivative(f=f, a=point, h=h)
#print()