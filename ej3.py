"""3. Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
Según el candidato elegido (A, B ó C)  se le debe imprimir el mensaje “Usted ha votado por el partido
[color que corresponda al candidato elegido]”. Si el usuario ingresa una opción que no corresponde a 
ninguno de los candidatos disponibles, indicar “Opción errónea”."""

print("elija su voto:")
print("A - Candidato A por el partido rojo")
print("B - Candidato B por el partido verde")
print("C - Candidato C por el partido azul")

voto = input("Elija su candidato (A/B/C): ").upper()

if voto == 'A':
    print("votaste el partido rojo.")
elif voto == 'B':
    print("votaste el partido verde.")
elif voto == 'C':
    print("votaste el partido azul.")
else:
    print("Opción errónea.")
