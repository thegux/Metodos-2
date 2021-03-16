from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral
from gaussian_quadrature import gaussian_quadrature
import numpy as np
import sympy as sp
import math

x = sp.Symbol('x')

y_generator = lambda x : (1 - sp.diff(221.5 - 20.97*math.cosh(x/30.38))**2)**(1/2)

a=-91.21
b=91.21

print(simpsons_integral(a=a,b=b,n=8, y_generator=y_generator))
print(simpsons_38_integral(a=a,b=b,n=9, y_generator=y_generator))
print(gaussian_quadrature(func = y_generator, n = 2, a=a, b=b))

