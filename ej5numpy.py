"""5. Convertir el array anterior en una matriz de 5 x 5."""

import numpy as np

x = np.random.rand(25)
print(x)


x.shape = (5,5)
print(x)