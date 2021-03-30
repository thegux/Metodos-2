from class_derivative import class_derivative
import numpy as np
import matplotlib.pyplot as plt
from class_derivative_2 import second_derivative

x = np.arange(4, 8.2, 0.2)
y = [-5.87, -4.23, -2.55, -0.89, 0.67, 2.09, 3.31, 4.31, 5.06, 5.55,  5.78, 5.77,
     5.52, 5.08, 4.46, 3.72, 2.88, 2.00, 1.10, 0.23, -0.59]


velocity = class_derivative(x=x, y=y)

acceleration = class_derivative(x=x, y=velocity)
acceleration2 = second_derivative(x=x, y=y)


fig, axs = plt.subplots(3)

axs[0].plot(x, y)
axs[0].set(ylabel='distancia')

axs[1].plot(x, velocity)
axs[1].set(ylabel='velocidade')

axs[2].plot(x, acceleration2)
axs[2].set(ylabel='aceleração', xlabel='tempo')


# show graph
plt.show()


