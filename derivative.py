def derivative(**kwargs):
    '''Compute the difference formula for f'(a) with step size h.

    Parameters
    ----------
    f : function
        Vectorized function of one variable
    a : number
        Compute derivative at x = a
    method : string
        Difference formula: 'forward', 'backward' or 'central'
    h : number
        Step size in difference formula
    It can also receive x and y values.

    Returns
    -------
    float
        Difference formula:
            central: f(a+h) - f(a-h))/2h
            forward: f(a+h) - f(a))/h
            backward: f(a) - f(a-h))/h            
    '''
    f =  kwargs.get('f', None)
    a = kwargs.get('a', None)
    method = kwargs.get('method', 'central')
    h = kwargs.get('h', 0.01)
    x = kwargs.get('x', None)
    y = kwargs.get('y', None)

    if method == 'central':
        if f is None:
            return (y[a + 1] - y[a - 1])/(x[a + 1] - x[a - 1])
        else: 
            return (f(a - 2) - 8*f(a - 1) + 8*f(a+1) - f(a+2))/(12*h)
    elif method == 'forward':
        if f is None:
            return (y[a + 1] - y[a])/(x[a + 1] - x[a])
        else:
            return (f(a + h) - f(a))/h
    elif method == 'backward':
        if f is None: 
            return (y[a] - y[a - 1])/(x[a] - x[a - 1])
        else:
            return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")