from euler_dr import euler_heun
import matplotlib.pyplot as plt

fun = lambda u, v : -0.1*(v-10)

[x, y] = euler_heun(0, 100, 0.5, 60, fun)

fig, axs = plt.subplots()

axs.plot(x, y)

# show graph
plt.show()