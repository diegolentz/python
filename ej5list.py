"""Escribe un programa que permita crear dos listas de palabras y que
, a continuación, elimine de la primera lista los nombres de la segunda lista."""

tam = int(input("Indique el tamaño de la lista: "))
lista1 = []
lista2 = []

for i in range(tam):
    palabra = input("Ingrese la palabra para la primera lista: ")
    lista1.append(palabra)
    
for i in range(tam):
    palabra2 = input("Ingrese la palabra para la segunda lista: ")
    lista2.append(palabra2)
    
for palabra2 in lista2:
    if palabra2 in lista1:
        lista1.remove(palabra2)
             
print("Lista 1 después de eliminar palabras de la Lista 2:")
print(lista1)
print("Lista 2:")
print(lista2)