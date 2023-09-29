"""2. Determinar los elementos menores a 5 del array generado en el punto 1."""
import numpy as np

# Genera un array de 10 elementos de tipo float con la parte entera mayor que 1
x = np.random.uniform(1.0, 10.0, 10)

print(x)

print(f"{x} es mayor a 5 {x>5}")