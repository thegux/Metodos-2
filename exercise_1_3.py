from scipy import interpolate
import math
import numpy as np

"""
    a = valor inicial de integração
    b = valor final de integração
    n =  número de intervalos
    r = vetor de raios da terra em metros
    rho = vetor de densidade da terra 
"""

a = 0
b = 6370000
n = 11

r = [0, 800000, 1200000, 1400000, 2000000, 3000000, 3400000, 3600000, 4000000, 5000000, 5500000, 6370000]
rho = [13000, 12900, 12700, 12000, 11650, 10600, 9900, 5500, 5300, 4750, 4500, 3300]

x = np.linspace(a, b, n+1)
y_generator = lambda i : rho[i]*4*math.pi*(r[i]**2)

#geramos os valores de y
y = [y_generator(i) for i in range(n+1)]

#calculamos a massa com a regra do trapezio
earth_mass = np.trapz(y, x)


"""
    para a interpolação na letra b
    criamos os novos x, com espaçamento padrão do linspace 50 (xnew)
    realizamos a interpolacao (tck -> ynew)
    e por fim aplicamos no metodo do trapezio para achar a massa (earth_mass_interpolation) 
"""

xnew = np.linspace(0, 6370000, 50)
tck = interpolate.splrep(x, y)
ynew = interpolate.splev(xnew, tck)

earth_mass_interpolation = np.trapz(xnew, ynew)

print(earth_mass)
print(earth_mass_interpolation)

