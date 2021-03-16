from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral
from gaussian_quadrature import gaussian_quadrature

x = [4, 3.95, 3.89, 3.80, 3.60, 3.41, 3.30]
y = [100, 103, 106, 110, 120, 133, 150]

a=0
b=100
n=60

print(simpsons_integral(x=x, y=y, a=a, b=b, n=n))
print(simpsons_38_integral(x=x, y=y,a=a, b=b, n=n))

