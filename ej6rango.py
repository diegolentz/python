"""Escribe un programa que pida dos números enteros y emita la lista de números pares 
que hay entre ellos (incluidos ellos mismos si son pares)"""


num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1  # Intercambio variables, quiero dejar el mas chico en num1

if num1 % 2 != 0:
    num1 += 1

pares_entre_numeros = list(range(num1, num2 + 1, 2))

if len(pares_entre_numeros) > 0:
    print("Lista de números pares entre los números ingresados:", pares_entre_numeros)
else:
    print("No hay números pares entre los números ingresados.")
