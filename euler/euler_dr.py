def euler_dr(x_initial, y_initial, step, x_final, fun):
    """
        Retornando um vetor de [x, y]
    """
    i = 0
    y = []
    x = []
    dydt = []
    x.insert(i, x_initial)
    y.insert(i, y_initial)

    while x[i] < x_final:
        dydt.insert(i, fun(x[i], y[i]))
        x.insert(i+1, x[i] + step)
        y.insert(i+1, y[i] + step*dydt[i])
        i += 1
    return [x,y]

