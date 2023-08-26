"""Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono
(no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere 
insertar más. No se podrán ingresar nombres repetidos."""

resp = input(f"desea ingresar un contacto? \n").lower()
diccionario = {}

while resp == "si":
    nombre = input(f"ingrese nombre \n")
    if nombre in diccionario:
        print(f"el nombre ya existe \n")
        resp = input(f"desea volver a intentarlo? \n").lower()
    else:
        numero = int(input(f"ingresa el numero \n"))
        diccionario[nombre] = numero
        resp = input(f"desea ingresar un contacto? \n").lower()
    
print(f"{diccionario}")
    