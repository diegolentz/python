"""Se encuestaron a 1000 asistentes al centro recreativo "Hoy me divierto" y se obtuvo la siguiente 

a) información:
 230 participaron de juegos y los datos se han recolectado en una tupla: (41,29,58,4,45,37,9,7)
 391 participaron de algún deporte y los datos se recolectaron en un diccionario: 
 {"Voleybol": 10, "Hockey": 87, "Equitación":23, "Ciclismo":81, "Paddle":11, "Fútbol": 45, "Tenis": 37, "Rugby": 9, 
"Básquetbol": 7, "Boxeo": 6, "Natación":75} 
 545 participaron de actividades en la granja y los datos se recolectaron en una lista:
 [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]
b) Por otra parte, se sabe que:
 98 participaron de deportes y juegos.
 152 participaron en juegos y actividades en la granja.
 88 participaron en deportes y actividades en la granja.
 90 prefirieron no participar de las actividades propuestas.
c) Resolver y responder:
 1. Cuántos entrevistados participaron en las 3 propuestas de actividades?
 2. Cuántos entrevistados participaron sólo en deportes y juegos?
 3. Cuántos entrevistados participaron sólo en juegos y actividades en la granja?
 4. Cuántos entrevistados participaron sólo en deportes y actividades en la granja?
 5. Cuántos entrevistados participaron sólo en deportes?
 6. Cuántos entrevistados participaron sólo en juegos?
 7. Cuántos entrevistados participaron sólo en actividades en la granja? 
 8. Cuántos entrevistados participaron sólo en 2 de las 3 propuestas?
d) Graficar con matplotlib_venn

Nota: El ejercicio debe resolverse con variables, estructuras, operaciones de conjuntos, funciones propias y
del lenguaje, etc. No 
se admiten valores literales, salvo en el caso de la asignación del valor universal y en las inicializaciones
de variables. Una vez 
resuelto el ejercicio, sube la solución a la carpeta del campus con nombre y apellido como nombre de archivo.
"""

from matplotlib import pyplot as plt
from matplotlib_venn import venn3,venn3_circles

#----------------------------------suma armado de conjuntos---------------------------------
# 230 participaron de juegos
juegosTupla = (41,29,58,4,45,37,9,7)

#391 participaron de algún deporte 
deporteDiccionario = {"Voleybol": 10, "Hockey": 87, "Equitación":23, "Ciclismo":81, 
                      "Paddle":11, "Fútbol": 45, "Tenis": 37, "Rugby": 9,
                      "Básquetbol": 7, "Boxeo": 6, "Natación":75} 

# 545 participaron de actividades en la granja
granjaLista = [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]


def suma(algo):
    suma = 0
    if algo == deporteDiccionario:
        for x in algo.values():
            suma += x
        suma
    else:
        for x in algo:
            suma += x
        suma
    return suma

cantidadJuegos = suma(juegosTupla)
cantidadDeportes = suma(deporteDiccionario)
cantidadGranja = suma(granjaLista)


print(f"las sumas de los conjuntos es\n")
print(f"{cantidadJuegos} para juegos")
print(f"{cantidadDeportes} para deportes")
print(f"{cantidadGranja} para granja")

#----------------------------------sets---------------------------------

#paso todo a set

def pasoSet(algo):
    if algo == deporteDiccionario:
        conver = set()
        for x in algo.values():
            conver.add(x)
        devuelvo = conver
    else:
        devuelvo = set(algo)
    return devuelvo

juegosSet = pasoSet(juegosTupla)
deportesSet = pasoSet(deporteDiccionario)
granjaSet = pasoSet(granjaLista)

print(f"\nconvertido a set quedaria\n")
print(f"{juegosSet} para juegos")
print(f"{deportesSet} para deportes")
print(f"{granjaSet} para granja")


#----------------------------------calculos---------------------------------
"""b) Por otra parte, se sabe que:
 98 participaron de deportes y juegos.
 152 participaron en juegos y actividades en la granja.
 88 participaron en deportes y actividades en la granja.
 90 prefirieron no participar de las actividades propuestas.
"""
"""Resolver y responder:
 1. Cuántos entrevistados participaron en las 3 propuestas de actividades? listo
 2. Cuántos entrevistados participaron sólo en deportes y juegos? listo
 3. Cuántos entrevistados participaron sólo en juegos y actividades en la granja? listo
 4. Cuántos entrevistados participaron sólo en deportes y actividades en la granja?listo
 """

def participaTodo(x,y,z):
    return (x & y & z)

def dosActividades(x,y):
    return x & y

hizoTodo = participaTodo(deportesSet,juegosSet,granjaSet)
deporteJuego = dosActividades(deportesSet,juegosSet)
juegoGranja = dosActividades(juegosSet,granjaSet)
deporteGranja = dosActividades(deportesSet,granjaSet)

print(f"\nlos que hicieron acts. combinadas o no participaron\n")
print(f"{suma(deporteJuego)} para deporte/juego {deporteJuego}")
print(f"{suma(juegoGranja)} para juego/granja{juegoGranja}")
print(f"{suma(deporteGranja)} para deporte/granja{deporteGranja}")
print(f"{suma(hizoTodo)} para todas las actividades {hizoTodo}")


#----------------------------------calculos de solos---------------------------------
"""
 5. Cuántos entrevistados participaron sólo en deportes?listo
 6. Cuántos entrevistados participaron sólo en juegos?listo
 7. Cuántos entrevistados participaron sólo en actividades en la granja?listo 
 8. Cuántos entrevistados participaron sólo en 2 de las 3 propuestas?listo
"""
 
def solos(x,y,z):
    return (x-y)&(x-z)
def solo_2() :
    return (juegoGranja - hizoTodo) | (deporteGranja - hizoTodo) | (deporteJuego - hizoTodo)

soloDeportes = solos(deportesSet,juegosSet,granjaSet)
soloJuegos = solos(juegosSet,deportesSet,granjaSet)
soloGranja = solos(granjaSet,juegosSet,deportesSet)
universo = 1000
desocupados = 90
dosDeTres = solo_2()

print(f"\nlos que practucan solos 1 deporte\n")
print(f"{universo} para total de encuestados") 
print(f"{desocupados} los que no se inscribieron a nada ") 
print(f"{suma(soloDeportes)} para deportes {soloDeportes}")
print(f"{suma(soloJuegos)} para juegos {soloJuegos}")
print(f"{suma(soloGranja)} para granja {soloGranja}") 
print(f"{suma(dosDeTres)} quienes hicieron 2 de 3 acts {dosDeTres}") 
 
#----------------------------------grafico---------------------------------

plt.figure('parcial')

diagrama = venn3((1,1,1,1,1,1,1),
                set_labels=("Juegos","Deportes","Granja"))

for x in ("001","010","011","100","101","110","111"):
    diagrama.get_label_by_id(x).set_fontsize(10)
    
diagrama.get_label_by_id("100").set_text({suma(soloJuegos)})
diagrama.get_label_by_id("010").set_text({suma(soloDeportes)})
diagrama.get_label_by_id("001").set_text({suma(soloGranja)})
diagrama.get_label_by_id("110").set_text({suma(deporteJuego - hizoTodo)})
diagrama.get_label_by_id("101").set_text({suma(juegoGranja - hizoTodo)})
diagrama.get_label_by_id("011").set_text({suma(deporteGranja - hizoTodo)})
diagrama.get_label_by_id("111").set_text({suma(hizoTodo)})


plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universo}",
         size=10)

plt.text(0.30, -0.7,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {desocupados}",
         size=8)

# Respondemos las preguntas
plt.text(-1.00, 0.20,  
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, 0.10,
         s="3 actividades = " + str({sum(hizoTodo)}),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, 0.00,
         s="deporte / juego = " + str(sum(deporteJuego)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, -0.10,
         s="juegos / granja = " + str(sum(juegoGranja)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, -0.20,
         s="deporte / granja = " + str(sum(deporteGranja)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, -0.30,
         s="solo deporte= " + str(sum(soloDeportes)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.00, -0.40,
         s="solo juegos= " + str(sum(soloJuegos)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))
plt.text(-1.00, -0.50,
         s="solo granja= " + str(sum(soloGranja)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))
plt.text(-1.00, -0.60,
         s=" 2 de 3= " + str(sum(dosDeTres)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.axis('on')  
plt.title("Deportistas")
plt.show()
