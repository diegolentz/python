"""Escribe un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar esa cantidad de 
palabras para crear la lista. Por último, el programa tiene que emitir la lista."""


numPalabras = int(input("Ingrese la cantidad de palabras: \n"))
lista = []

for i in range(numPalabras):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    lista.append(palabra)

print("La lista de palabras creada es:")
print(lista)
