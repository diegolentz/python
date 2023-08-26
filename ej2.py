"""Crear un programa donde vamos a declarar un diccionario para guardar los precios de las distintas frutas
. El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final 
de la fruta a partir de los datos guardados en el diccionario. Si la fruta no existe nos dará un error. 
Tras cada consulta el programa nos preguntará si queremos hacer otra consulta."""

diccionario = {"banana":100,"pera":300,"manzana":150,"frutilla":220}
print(diccionario)


resp = input(f"desea consultar presupuesto de verduras? \n").lower()

while resp == "si":
    fruta = input(f"que fruta va a consultar? \n").lower()
    kg = int(input(f"cuantos kg te llevas? \n"))
    
    precio = diccionario[fruta] 
    preciofinal = precio*kg
    
    print(f"el precio final fue de: {preciofinal}\n")
    resp = input(f"desea consultar presupuesto de verduras? \n").lower()

print(f"hasta la proxima")
