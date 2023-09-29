"""2. Agregar el valor 0 en la posición 5"""


import numpy as np

x = [1,2,3,4,5,6,7]
print(x)

x = np.insert(x,5,0)
print(x)