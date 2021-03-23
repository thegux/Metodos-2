import numpy as np

def first_derivative(**kwargs):
    x = kwargs.get('x', None)
    y = kwargs.get('y', [])

    n = len(y) - 1
    i = 0
    h = x[i+1]-x[i]
    #progressive_difference
    dy = np.arange(0, n+1)
    dy[i] = ((-3*y[i]) + (4*y[i+1]) - y[i+2])/(2*h) #(y[i+1]-y[i])/h
    #central difference
    for j in range(1, n-1):
        dy[j] = (y[j+1]-y[j-1])/(2*h)
    #regressive difference
    dy[n] = (y[n-2] - 4*x[n-1] + 3*x[n])/(2*h) #(y[n]-y[n-1])/h
    
    return dy

def second_derivative(**kwargs):
    x = kwargs.get('x', None)
    y = kwargs.get('y', [])

    n = len(y) - 1
    i = 0
    h = x[i+1]-x[i]
    #progressive_difference
    dy = np.arange(0, n+1)  
    dy[i] = (2*y[i] - 5*y[i+1] + 4*y[i+2] - y[i+3])/(h**2) #(y[i+1]-y[i])/h

    #central difference
    for j in range(1, n):
        dy[j] = (y[j-1] - 2*y[j] +  y[j+1])/(h**2)
    #regressive difference

    dy[n] = (-y[n-3] + 4*y[n-2] - 5*y[n-1]+2*y[n])/(h**2)
    
    return dy