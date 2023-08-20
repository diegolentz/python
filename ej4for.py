"""Muestre los N primeros números de la secuencia de Fibonacci,
siendo n un dato entero"""


numero = int(input("Ingrese la cantidad de números de la secuencia de Fibonacci que desea mostrar: "))

fibonacci = [0, 1]

for i in range(2, numero):
    proximo = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(proximo)

print(f"Los primeros {numero} números de la secuencia de Fibonacci son:")
print(fibonacci)
