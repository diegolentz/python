"""Escribe un programa que pida la cantidad de números positivos que se tienen que ingresar y
    a continuación pida números hasta que se hayan ingresado la cantidad de números indicada."""

cantidad = int(input("Ingrese la cantidad de números que desea mostrar: \n"))
ingresos = 0

ingresados = []

while ingresos < cantidad:
    numero = int(input("Ingrese un número positivo: \n"))
    while numero < 0:
        print("Opción inválida, debe ser un número positivo. \n")
        numero = int(input("Ingrese un número positivo: \n"))
    
    ingresados.append(numero)
    ingresos += 1

print("Números ingresados:", ingresados)
