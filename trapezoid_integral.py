import numpy as np

"""
    function for calculating integrals using the trapezoid method
    x is a vector of independent variables
    y is a vector of dependent variables
    a is the initial value
    b is the final value
    n is the number of intervals
    y_generator is the function to be integrated
"""

def trapezoid_integral(a, b, n, y_generator):
    #a = 1
    #b = 3
    #n = 2
    #y_generator = lambda x: 1/x

    h = (b-a)/n
        
    x = np.linspace(a, b, n+1)
    y = [y_generator(x[i]) for i in range(n+1)]

    interval = x[1] - x[0]
    vectors_length = len(x)
    
    integral_value = y[0]

    for i in range(2, vectors_length):
        integral_value += 2*y[i - 1]
    
    integral_value += y[vectors_length - 1]
    integral_value *= h/2
    return integral_value

