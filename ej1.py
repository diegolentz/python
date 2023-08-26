"""Diseña un programa que reciba dos conjuntos y devuelva los elementos comunes a ambas, sin repetir ninguno.
Ejemplo: si recibe los conjuntos [1, 2, 1] y [2, 3, 2, 4], devolverá 2.."""

conjunto1 = {1,2,1,4}
conjunto2 = {2,3,2,4,1}


comunes = conjunto1.intersection(conjunto2)
print(comunes)
