"""Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen a una o a otra,
pero sin repetir ninguno. Ejemplo: si recibe los conjuntos 
[1, 2, 1] y [2, 3, 2, 4], devolverá el conjunto [1, 2, 3, 4]."""

conjunto1 = {1,2,1}
conjunto2 = {2,3,2,4}

conjunto3 = conjunto1|conjunto2

print(conjunto3)