"""Genera una matriz con una distribución normal de 4 por 3."""


import numpy as np

x = np.random.randint(low = 1, high= 32, size =12)
print(x)

x.shape = (4,3)
print(x)

print("2. Calcular la suma por fila y por columna.")
print(np.add.reduce(x))
print(np.add.reduce(x.transpose()))



"""3. Utilizando funciones universales calcular el máximo, el mínimo la media, la desviación estándar, la varianza y los percentiles."""

print(f"max {np.max(x)}" )
print(f"min {np.min(x)}" )
print(f"media {np.mean(x)}")
#  da un numero raro  print(f"media {np.median(x)}")

