from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral
from gaussian_quadrature import gaussian_quadrature

y_generator = lambda x: 5 + 0.25*x**2

a=0
b=11
n=60

print(trapezoid_integral(a=a,b=b,n=n, y_generator=y_generator))
print(simpsons_integral(a=a,b=b,n=n, y_generator=y_generator))
print(simpsons_38_integral(a=a,b=b,n=n, y_generator=y_generator))
print(gaussian_quadrature(func = y_generator, n = 2, a=a, b=b))
