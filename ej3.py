"""Codifica un programa que permita guardar los nombres de alumnos de una clase y las notas que han 
obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario 
cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno. 
El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas 
hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista de alumnos y la nota
media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa 
nos dará un error."""


print(f"bienvenido al sistema de gestion escuelita \n")
alumnos = int(input(f"cuantos alumnos se computaran? \n"))
diccionario = {}

i=0
while i < alumnos :
    nombre = input("nombre del alumno")
    nota = int(input(f"ingrese la nota \n"))
    conjunto = set()
    while nota > 0 :
        conjunto.add(nota)
        nota = int(input(f"ingrese la nota \n"))
    diccionario[nombre] = conjunto
    i+=1
    
        
        
print(diccionario)