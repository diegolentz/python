"""1. Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
No considerar el caso en que ambos números son iguales."""

numero1 = int(input("ingrese el primer numero \n"))
numero2 = int(input("ingrese el segundo numero \n"))

if numero1 > numero2:
      print(f"\nel numero 1 es el mayor")
else: print(f"\nel numero 2 es el mayor")
