"""1. Generar una matriz de números enteros aleatorios de 4 por 5."""


import numpy as np

x = np.random.randint(low=1,high=40,size=20)
x.shape = (4,5)
print(x)

"""Dividir por 3 la columna 2"""
print("\ndivide 3 la columna 2")
x[:,2] = x[:,2]/3.0
print(x)

"""3. Tranponer la matriz."""

print("\nmatriz traspuesta\n")
print(x.transpose())


print("\nmatriz ordenada\n")
"""ordenar la matriz"""
print(np.sort(x))
