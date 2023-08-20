"""Escribe un programa que permita crear una lista de palabras y que,
a continuación, pida una palabra y elimine esa palabra de la lista."""

cant = int(input("ingrese la cantidad de palabras: "))
lista = []

for i in range(cant):
    palabra = input(f"ingrese la palabra a insertar {i + 1}: ")
    lista.append(palabra)

eliminar = input("Que palabra desea eliminar? ")
lista.remove(eliminar)

print("la lista despues de eliminar la palabra es:")
print(lista)
