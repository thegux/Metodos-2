from trapezoid_integral import trapezoid_integral
from simpsons_one_third import simpsons_integral
from simpsons_three_eigths import simpsons_38_integral

y_generator = lambda x: x

x=[336, 294.4, 266.4, 260.8, 260.5, 249.6, 193.6, 165.6]
y=[0.5,2,3,4,6,8,10, 11]

a=336
b=165.6

print(simpsons_integral(x=x, y=y, a=a, b=b))
print(simpsons_38_integral(x=x, y=y, a=a, b=b))
print(trapezoid_integral(x=x, y=y))