from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral

x=[1,2,3.25, 4.5,6,7,8,9, 9.5, 10]
y=[5,6,5.5,7, 8.5, 8,6,7,7,5]

print(simpsons_integral(x=x, y=y))
print(simpsons_38_integral(x=x, y=y))
print(trapezoid_integral(x=x, y=y))
