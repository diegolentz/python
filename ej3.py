"""3.c. Se necesita obtener el promedio simple de un estudiante a partir de
sus tres notas parciales N1, N2 y N3."""


print(f"se ingresaran 3 notas y se calculara su promedio \n")

i = 0

nota1 = int(input("ingrese la nota 1 \n"))
nota2 = int(input("ingrese la nota 2 \n"))
nota3 = int(input("ingrese la nota 3 \n"))


promedio = ((nota1 + nota2 + nota3)/3)

print(f"su promedio fue de: {promedio}")

if promedio > 6 : 
    print(f"pasastes")
print(f"ripiastes")
