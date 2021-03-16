def gaussian_quadrature(func, **kwargs):
    """
        function to be integrated by the gaussian quadrature method
        with order n of a function 'func'
    """

    n = kwargs.get('n', 2)
    a = kwargs.get('a', -1)
    b = kwargs.get('b', 1)    

    c = [[1, 1, 0, 0, 0, 0],
         [0.5555556, 0.8888889, 0.5555556, 0, 0, 0],
         [0.3478548, 0.6521452, 0.6521452, 0.3478548, 0, 0],
         [0.2369269, 0.4786287, 0.5688889, 0.4786287, 0.2369269, 0],
         [0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245]
         ]
    x = [
        [-0.577350269, 0.577350269, 0, 0, 0, 0],
        [-0.7774596669, 0, 0.7774596669, 0, 0, 0],
        [-0.861136312, -0.339981044, 0.339981044, 0.861136312, 0, 0],
        [-0.90619846, -0.538469310, 0, 0.538469310, 0.90619846, 0],
        [-0.932469514, -0.661209386, -0.238619186,
            0.238619186, 0.661209386, 0.932469514]
    ]
    
    for i in range(len(x)):
        for j in range(len(x[i])):
            x[i][j] = x_generator(x[i][j], a, b)
   
    dx_constant = (b-a)/2

    I = 0
    for i in range(0, n):
        I += c[n - 2][i]*func(x[n - 2][i])*dx_constant
    
    return I


#changing integration limits
def x_generator(x_val, a, b):
    if x_val == 0: 
        return 0 
    else: 
        auxVal = ((a+b)/2) + ((b-a)/2)*x_val
        return auxVal