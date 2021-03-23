import numpy as np

def class_derivative(**kwargs):
    x = kwargs.get('x', None)
    y = kwargs.get('y', [])

    n = len(y) - 1

    #progressive_difference
    dy = np.arange(0, n+1)
    i = 0
    dy[i] = (y[i+1]-y[i])/(x[i+1]-x[i])
    #central difference
    for j in range(1, n):
        dy[j] = (y[j+1]-y[j-1])/(x[j+1]-x[j-1])
    #regressive difference
    dy[n] = (y[n]-y[n-1])/(x[n]-x[n-1])
    
    return dy