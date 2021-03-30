from euler_dr import euler_dr
import matplotlib.pyplot as plt

fun = lambda u, v : 1-v

[x, y] = euler_dr(0, 0, 0.5, 8, fun)

fig, axs = plt.subplots()

axs.plot(x, y)

# show graph
plt.show()