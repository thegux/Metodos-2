from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral
from math import e

y_generator = lambda x: 1-e**(-2*x)

a=0
b=4

print(simpsons_38_integral(a=a, b=b, n=5, y_generator=y_generator))
print(simpsons_integral(a=a, b=b, y_generator=y_generator))
print(trapezoid_integral(a=a, b=b, y_generator=y_generator))
