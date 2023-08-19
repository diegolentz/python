"""4.	Realiza un programa que dadas una cantidad de segundos los convierta en horas
, minutos y segundos."""

segundosUser = int(input("Ingrese la cantidad de segundos: "))
hora = segundosUser // 3600
segundosRestantes = segundosUser % 3600 #uso el resto para calcular los minutos y segundos
minutos = segundosRestantes // 60 #aca atrapo los minutos
segundos = segundosRestantes % 60 #el resto son los segundos

# Mostrar el resultado
print(f"{segundosUser} segundos equivalen a \n{hora} horas  \n{minutos} minutos  \n{segundos} segundos.")
