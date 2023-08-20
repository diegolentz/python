"""Escribe un programa que pida dos números enteros y emita la lista de números 
consecutivos que hay entre ellos, de menor a mayor."""


num1 = int(input("ingrese numero 1 \n"))
num2 = int(input("ingrese numero 2 \n"))


if num1 > num2 :
    x = list(range(num2,num1+1))
    print(x)
elif num1<num2 :
    x = list(range(num1,num2+1))
    print(x)
else:
    print(f"deberia ser 1 mayor que el otro")
    