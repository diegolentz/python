"""Escribe un programa que calcule el factorial de un número cualquiera que se ingresa por teclado."""

numero = int(input("ingrese el numero que desee conocer su factorial \n"))

suma = 1

for i in range(1,numero+1):
    suma *= i
    
print(suma)