"""4. Generar un array de 20 elementos enteros, une éste con el anterior en un nuevo eje."""


import numpy as np

x= np.arange(10, 30, 1, dtype = int)
print(x)

y= np.arange(30, 50, 1, dtype = int)
print(y)

matriz = np.stack((x,y), axis = 1)
print(matriz)
