""" 8.	Escribe un programa que pida números pares mientras el usuario indique que quiere seguir introduciendo números.
Para indicar que quiere seguir escribiendo números, el usuario deberá contestar ‘S’ o ‘s’ a la pregunta."""


resp = input("Desea introducir un numero par? S/N: ")

while resp.lower() == 's':
    numero = int(input("Ingrese un numero par: "))
    
    if numero % 2 == 0:
        print("Numero par ingresado:", numero)
    else:
        print("El numero ingresado no es par... vuelva a intentarlo \n")
    
    resp = input("Desea introducir otro número par? S/N: ")

print("hasta la proxima!")
