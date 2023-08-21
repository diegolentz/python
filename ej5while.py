"""5.	Escribe un programa que pida números mientras no se escriba un número negativo. 
El programa terminará emitiendo la suma de los números ingresados."""

numero = float(input("ingrese un número / negativo para terminar \n"))

suma = 0
while numero >= 0:
    suma += numero
    numero = float(input("ingrese un número / negativo para terminar \n"))

print("La suma de los números es:", suma)


