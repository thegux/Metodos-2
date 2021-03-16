from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral
from gaussian_quadrature import gaussian_quadrature
import sympy as sp
import math

total_radius = 3

y_generator = lambda r : 2*math.pi*r * 2*((1-(r/total_radius))**(1/6))

a = 0
b = total_radius

print(simpsons_integral(a=a,b=b,n=8, y_generator=y_generator))
print(simpsons_38_integral(a=a,b=b,n=9, y_generator=y_generator))
print(gaussian_quadrature(func = y_generator, n = 2, a=a, b=b))