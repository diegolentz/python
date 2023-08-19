"""6. Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la 
empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de 
los payasos y muñecas 
que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. 
Escribe un programa que lea 
el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del 
paquete que será enviado."""

cantp = int(input("ingrese la cantidad de payasos vendidos \n"))
cantm = int(input("ingrese la cantidad de munecas vendidas \n"))

cantp *= 112
cantm *= 75

print(f"el peso de los payasos es de {cantp} y de las munecas {cantm}\nen total {cantm+cantp}")