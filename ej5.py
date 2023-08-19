"""5.	Escribe un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal, lo almacene en una variable, y muestre por pantalla redondeado 
con dos decimales."""


kg = float(input("ingrese peso en kg \n"))
altura = float(input("ingrese altura en mts \n"))

indiceMasa = round(kg/altura **2,2)

print(f"el indice de masa es: {indiceMasa}")