"""3. Generar otra matriz con la mismas dimensiones de la anterior y concatena ambas."""

import numpy as np

x = np.random.randint(low=1,high=40,size=20)
x.shape = (4,5)
print(x)

y = np.random.randint(low=40,high=80,size=20)
y.shape = (4,5)
print(y)

z = np.concatenate([x,y])
print(z)

print("apilar las matricices horizontalmente")

w = np.hstack((x,y))
print(w)


