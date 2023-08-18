"""3.d. Desarrolla un algoritmo que permita, dados ciertos centímetros como
entrada de tipo flotante, emitir por pantalla su equivalencia en pies (enteros) 
y en pulgadas (flotante, con 3 decimales)."""

print(f"se convertiran cm -> pies y pulgadas \n")

pie = 30.48
pulgada = 2.54

medida = float(input("ingrese la medida en cm \n"))

pie = round(medida/pie,3)
pulgada = round(medida/pulgada,3)

print(f"en pies son {pie} \n en pulgadas {pulgada}")

