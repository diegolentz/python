"""
Escribe un programa que pida números decimales mientras el usuario escriba número mayores que el primero.
"""
primero = float(input("Ingrese el primer número decimal: \n"))
actual = float(input("Ingrese un número decimal mayor que el primero para continuar: \n"))

while actual > primero:
    actual = float(input(" otro número decimal mayor que el primero para continuar: \n"))

print("Ingresó un número menor o igual al primer número. Terminando el programa. \n")
