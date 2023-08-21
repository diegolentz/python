"""6.	Escribe un programa que pida un valor límite positivo y a continuación pida números hasta que la suma de los 
números introducidos supere el límite inicial."""

max = float(input("Ingrese un valor maximo: "))
suma = 0

while suma <= max :
    numero = float(input("ingrese un numero: "))
    suma += numero

print("la suma de los numeros introducidos supero el límite inicial de", max)
print(f"alcanzaste a sumar {suma-numero} antes de pasarte")
