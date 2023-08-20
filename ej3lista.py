"""Escribe un programa que permita crear una lista de palabras y que,
a continuación, pida dos palabras y sustituya la primera (que debe estar en la lista) 
por la segunda. Emitir la lista."""

numPalabras = int(input("ingrese la cantidad de palabras: "))
lista = []

for i in range(numPalabras):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    lista.append(palabra)

palabra1 = input("Ingrese la palabra que desea sustituir: ")
palabra2 = input("Ingrese la palabra que desea insertar en la lista: ")

if palabra1 in lista:
    indice = lista.index(palabra1)
    lista[indice] = palabra2
    print("Palabra sustituida exitosamente.")
else:
    print("La primera palabra no esta en la lista.")

print("La lista de palabras actualizada es:")
print(lista)
