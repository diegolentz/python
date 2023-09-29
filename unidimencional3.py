"""3. Generar un array de 4 números enteros y agregalo al array del punto 1"""

import numpy as np

x= np.arange(10, 20, 2, dtype = int)
print(x)

y= np.arange(20, 30, 2, dtype = int)
print(y)

z = np.concatenate([x,y])
print(z)
