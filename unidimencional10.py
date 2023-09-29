"""5. Ordenar el array."""


import numpy as np

# Genera un array de 10 elementos de tipo float con la parte entera mayor que 1
x = np.random.uniform(1.0, 10.0, 10)
print(x)


print(f"ordenado {np.sort(x)}")