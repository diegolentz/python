"""Escribe un programa que permita crear una lista de palabras y que, a continuación, 
cree una segunda lista igual a la primera, pero al revés (crear una lista distinta)."""

can = int(input("Ingrese la cantidad de palabras: "))
original = []

for i in range(can):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    original.append(palabra)

inversa = []
for palabra in reversed(original):
    inversa.append(palabra)

print("Lista original:")
print(original)
print("Lista inversa:")
print(inversa)
