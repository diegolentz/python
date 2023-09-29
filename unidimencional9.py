"""4. Crear una función lambda que devuelva los elementos del array elevados al cubo."""

import numpy as np

# Genera un array de 10 elementos de tipo float con la parte entera mayor que 1
x = np.random.uniform(1.0, 10.0, 10)
print(x)

cubo = lambda x:pow(x,3)

print(f"array {(x)}    cubo {cubo(x)}")