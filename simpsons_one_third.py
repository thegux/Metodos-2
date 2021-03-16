import numpy as np

"""
    a is the initial value
    b is the final value
    n is the number of intervals
    y_generator is the function to be integrated
"""

def simpsons_integral(**kwargs):
    #a = 1
    #b = 3
    #n = 2
    a = kwargs.get('a', None)
    b = kwargs.get('b', None)
    n = kwargs.get('n', 2)
    y_generator = kwargs.get('y_generator', None)

    x = kwargs.get('x', None)
    y = kwargs.get('y', None)

    if x is None:
        x = np.linspace(a, b, n+1)
        y = [y_generator(x[i]) for i in range(n+1)]

    vectors_length = len(x)
    if a is None:
        h = x[1] - x[0]
    else:
        h= (b-a)/n
    integral_value = y[0]

    for i in range(2, vectors_length, 2):
        integral_value += 4*y[i-1]
    
    for i in range(3, vectors_length - 1, 2):
        integral_value += 2*y[i-1]
    
    integral_value += y[vectors_length - 1]
    integral_value *= h/3
    return integral_value
