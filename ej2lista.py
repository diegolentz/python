"""Escribe un programa que permita crear una lista de palabras y que,
a continuación, pida una palabra y diga cuántas veces aparece esa
palabra en la lista."""


numPalabras = int(input("Ingrese la cantidad de palabras: "))
lista = []

for i in range(numPalabras):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    lista.append(palabra)

buscar = input("Ingrese la palabra que desea buscar: ")

cantidad = lista.count(buscar)

print("La lista de palabras creada es:")
print(lista)

print(f"La palabra '{buscar}' aparece {cantidad} veces!")
