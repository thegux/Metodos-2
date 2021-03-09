from trapezoid_integral import trapezoid_integral
from sympsons_one_third import sympsons_integral

y_generator = lambda x: 5 + 0.25*x**2

a=0
b=11
n=1

print(trapezoid_integral(a,b,n, y_generator))
print(sympsons_integral(a,b,n, y_generator))
