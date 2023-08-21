"""Escribe un programa que pida primero dos números enteros (mínimo y máximo) y que después pida números enteros 
situados entre ellos. El programa terminará cuando se escriba un número que no esté
comprendido entre los dos valores iniciales y emitirá la cantidad de números ingresados."""

minimo = int(input("Ingrese el valor mínimo \n") )
maximo = int(input("Ingrese el valor máximo \n") )

ingresados = 0
numero = int(input(f"Ingrese un número entre {minimo} y {maximo} \n"))
print(f" ingrese un número fuera del rango para terminar \n")
while minimo <= numero <= maximo:
    ingresados += 1
    numero = int(input(f"Ingrese un número entre {minimo} y {maximo} \n"))
    print(f" ingrese un número fuera del rango para terminar \n")
    
print("Cantidad de números ingresados:", ingresados)
