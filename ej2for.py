"""Escribe un programa que le permita realizar la suma de los primeros 
N números impares. El N debe ingresarse por teclado."""

numero = int(input("Ingrese cuántos números impares desea sumar: "))
suma = 0
impares = 1

for i in range(numero):
    suma += impares
    impares += 2

print("La suma de los primeros", numero, "números impares es:", suma)
