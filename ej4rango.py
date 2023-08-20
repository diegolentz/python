"""Escribe un programa que pida dos números enteros
(el segundo mayor que el primero) y emita listas de números 
consecutivos al derecho y al revés."""


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número (mayor que el primero): "))


while num2 <= num1:
    print("El segundo número debe ser mayor que el primero.")
    num2 = int(input("Ingrese el segundo número entero (mayor que el primero): "))

listaDerecha = list(range(num1, num2 + 1))
listaReves = list(range(num2, num1 - 1, -1))

print("Lista de números consecutivos al derecho:", listaDerecha)
print("Lista de números consecutivos al revés:", listaReves)
