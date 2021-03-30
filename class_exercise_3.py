from class_derivative_2 import first_derivative
from class_derivative import class_derivative
import matplotlib.pyplot as plt
import numpy as np

x = [87.8, 96.6, 176, 263, 351, 571, 834, 1229, 1624, 2107, 2678, 3308, 4258]
y = [153, 204, 255, 306, 357, 408, 459, 510, 561, 612, 663, 714, 765]

dy = class_derivative(x=x, y=y)

fig, axs = plt.subplots()

axs.plot(x, dy)

# show graph
plt.show()
