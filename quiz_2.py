from gaussian_quadrature import gaussian_quadrature
import sympy as sp
import math

y_generator = lambda x : 1/(1+x**2)

a=-3
b=3

analitic = 2.498091
result = gaussian_quadrature(func = y_generator, n = 6, a=a, b=b)
error = 100 - ((result * 100)/analitic)

print(result)
print(error)
