"""Diseña un programa que reciba dos conjuntos y devuelva los elementos que pertenecen al 
primero pero no al segundo, sin repetir ninguno. Ejemplo: si recibe las listas [1, 2, 1] y [2, 3, 2, 4]
, devolverá la lista [1]."""


conjunto1 = {1,2,1}
conjunto2 = {2,3,2,4}

conjunto3= conjunto1 - conjunto2
print(conjunto3)