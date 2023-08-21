"""Escribe un programa que pida números enteros mientras el usuario ingresa números cada vez más grandes, 
el programa emite en cada iteración el 
número anterior ingresado y finaliza ingresando un número menor."""

anterior = int(input("Ingrese un número: \n"))
actual = int(input("Ingrese otro número entero, debe ser mayor que el anterior para continuar \n"))

while actual > anterior:
    print(f"Número anterior:", anterior)
    anterior = actual
    actual = int(input("Ingrese otro número entero (debe ser mayor que el anterior para continuar): "))

print("Ingresó un número igual o menor al anterior. Terminando programa.")
