""" 2. Agregar una nueva columna y una fila a la matriz anterior."""

import numpy as np

x = np.random.randint(low=1,high=40,size=12)
print(x)

x.shape = (3,4)
print(x)

x = np.append(x,[[1],[1],[1]], axis= 1)
x = np.append(x,[[2,2,2,2,2]], axis= 0)

print(x)




