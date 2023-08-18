"""Construye un programa que permita ingresar 2 tiempos, 
expresados en horas, minutos y segundos, el mismo debe
emitir por pantalla la suma de ambos (también en horas, minutos y segundos)."""

hora1   = int(input("ingrese la  primer hora  \n"))
minuto1 =int(input("ingrese el primer minuto \n"))
segundo1 =int(input("ingrese primer segundo \n"))

hora2   = int(input("ingrese la  segunda hora  \n"))
minuto2 =int(input("ingrese el segundo minuto \n"))
segundo2 =int(input("ingrese segundo segundo \n"))

segundotot = segundo1 + segundo2
minutotot = minuto1 + minuto2
horatot = hora1 + hora2

if segundotot > 59:
    segundotot = segundotot - 60
    minutotot = minutotot + 1
segundotot


if minutotot > 59:
    minutotot = minutotot - 60
    horatot = horatot + 1
segundotot


if horatot > 23:
    print(f"pasaste a 1 dia ")
    horatot - 23
segundotot

print(f"hora total {horatot}\nminutos totales {minutotot} \nsegundos totales {segundotot}")