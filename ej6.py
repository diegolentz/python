"""6.	Un instituto de enseñanza necesita un programa que permita, cada día, procesar observaciones sobre 
las clases de ese día. El instituto dicta clases a estudiantes de distintos niveles y cada nivel tiene clases
en un día de la semana diferente: 
•	los lunes se dicta el nivel inicial, 
•	los martes el nivel intermedio, 
•	los miércoles el nivel avanzado, 
•	los jueves son para práctica y 
•	los viernes para consultas.

a.	Se debe comenzar por solicitar al usuario que ingrese el día (por ejemplo lunes) 
b.	Una vez indicado el día, el usuario necesita poder indicar si ese día se tomaron exámenes, pero sólo si 
se trata de los niveles inicial, intermedio o avanzado, ya que las prácticas y las consultas no tienen exámenes. 
c.	Si hubo exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el programa le mostrará 
el porcentaje de aprobados.
d.	Si el día fue el correspondiente a práctica, el usuario deberá ingresar el porcentaje de asistencia a
clase y el programa le indicará "asistió la mayoría" en caso de que la asistencia sea mayor al 50% o 
"no asistió la mayoría" si no es así.
e.	Si se trata de las consultas y se deberá emitir "Clase de consulta" y solicitar al usuario que ingrese 
la cantidad de alumnos de la clase y el arancel en pesos por cada alumno que consulta, para luego imprimir 
el ingreso total en pesos.

Nota = establece los criterios necesarios, por ejemplo cantidad de alumnos por niveles."""

dia = input("ingrese el dia \n")
dia.lower()

if dia == 'lunes' or dia == 'martes' or dia == 'miercoles':
    examen = input("hubo examen? si/no \n").lower()
    if examen == 'si':
        aprobados = int(input("cuantos aprobaron? \n"))
        desaprobados = int(input("cuantos desaprobaron? \n"))
        proma = (aprobados * (aprobados+desaprobados)) / 100
        promd = (desaprobados * (aprobados+desaprobados)) / 100
        
        print(f"porcentaje de aprobados: {proma}\npordentaje de desaprobados: {promd}")
    else: print(f"zafamos... ja \n")
elif dia == 'jueves':
    asistentes = int(input("ingrese el porcentaje de asistentes \n"))
    if asistentes > 50 :
        print(f"asistio la mayoria \n")
    else : print(f"no asistio la mayoria \n")
elif dia == 'viernes':
    print(f"clase de consultas \n")
    cant = int(input("ingrese la cantidad de alumnos \n"))
    precio = int(input("ingrese el precio de la clase \n"))
    total = cant * precio
    
    print(f"la cantidad recaudada fue de: {total}")
else: print(f"los dias deben ser de lunes a viernes")