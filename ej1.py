"""ESTAS COMILLAS SON PARA PONER
COMENTARIOS DE MAS DE UNA LINEA"""
# PARA COMENTARIOS EN UNA LINEA UTILIZAMOS #

"""tunombre=input("Ingresa tu nombre:")
print(f"Hola {tunombre}!!!")

nombre1=input("ingrese nombre del producto:")
precio1=int(input("ingrese un precio:"))
nombre2=input("ingrese nombre del producto:")
precio2=int(input("ingrese otro precio:"))

# esta es una constante
BONIFICACION = 20

# sumamos los dos precios y su resultado lo guardamos en una variable
precio_total = precio1 + precio2 
print(f"El precio total es: {precio_total}")
print(f"Resultados de la suma de producto {nombre1} y del producto {nombre2}.:")

# concatenar se puede hacer de esta manera con el signo + y en la variable la propiedad str
print ("la suma de los dos productos es:" + str(precio_total))

 VEMOS EL OPERADOR DE ASIGNACION AQUI ABAJO """
"""precio_total += BONIFICACION 
print ("al precio total le incrementamos su valor que tiene la constante:" + str(precio_total))"""

# Prueba el programa guardándolo con un nombre y la extensión .py o .ipynb
bonificacion = 20

nombre = input("ingresa tu nombre:  \n")
print(f"hola {nombre}!!")

prod1 = input("nombre del producto 1 \n")
precio1=int(input("su precio: \n"))
prod2 = input("nombre del producto 2 \n")
precio2=int(input("su precio: \n"))

total = precio1 + precio2

print(f"el total fue de: {total}")
print(f"teniendo en cuenta: {prod1} y {prod2}")

print("la suma de los 2 productos es "+ str(total)) 
total += bonificacion
print("el total + la bonificacion es de : "+ str(total))

