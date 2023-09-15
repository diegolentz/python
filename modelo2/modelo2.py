"""Se encuestaron a 1000 asistentes al centro recreativo "Hoy me divierto" y se obtuvo la siguiente información:
a)
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
from matplotlib_venn import venn3, venn3_circles

tupla_juegos = (41,29,58,4,45,37,9,7)
dicc_deportes = {"Voleybol": 10, "Hockey": 87, "Equitación":23, "Ciclismo":81, "Paddle":11, "Fútbol": 45, "Tenis": 37, "Rugby": 9, 
"Básquetbol": 7, "Boxeo": 6, "Natación":75} 
lista_granja = [65,14,25,29,12,1,17,18,45,37,6,41,19,8,2,90,103,13]

# Compruebo las cantidades

# Personas que participaron de juegos
def suma_j(j) :
    suma = 0
    for i in j :
        suma += i
    return suma
suma_juegos = suma_j(tupla_juegos)
print(f"Personas que participaron de juegos: {suma_juegos}")

# Personas que participaron de algún deporte
def suma_d(d) :
    suma = 0
    for i in d.values() :
        suma += i
    return suma
suma_deportes = suma_d(dicc_deportes)
print(f"Personas que participaron de deportes: {suma_deportes}")

# Personas que participaron de actividades de granja
def suma_g(g) :
    suma = 0
    for i in g :
        suma += i
    return suma
suma_granja = suma_g(lista_granja)
print(f"Personas que participaron de actividades de granja: {suma_granja}")

universo = 1000
ninguno = 90

# Pasamos la tupla a set
def juegos_a_set(j) :
    set_j = set()
    for i in j :
        set_j.add(i)
    return set_j
set_juegos = juegos_a_set(tupla_juegos)
print(f"Conjunto de juegos: {set_juegos}")

# Diccionario a set
def deportes_a_set(d) :
    set_d = set()
    for i in d.values() :
        set_d.add(i)
    return set_d
set_deportes = deportes_a_set(dicc_deportes)
print(f"Conjunto de deportes: {set_deportes}")

# Lista a set
def granja_a_set(g) :
    set_g = set()
    for i in g :
        set_g.add(i)
    return set_g
set_granja = granja_a_set(lista_granja)
print(f"Conjunto de actividades de granja: {set_granja}")

# Solo juegos y deportes
def juegos_dep(j, d) :
    jd = j & d
    suma = 0
    for i in jd :
        suma += i
    return suma
juegos_deportes = juegos_dep(set_juegos, set_deportes)
print(f"Hacen sólo juegos y deportes: {juegos_deportes}")

# Solo juegos y granja
def juegos_granjas(j, g) :
    jg = j & g 
    suma = 0
    for i in jg :
        suma += i
    return suma
juegos_granja = juegos_granjas(set_juegos, set_granja)
print(f"Hacen sólo juegos y actividades de granja: {juegos_granja}")

# Solo deportes y granja
def deportes_granjas(d, g) :
    dg = d & g 
    suma = 0
    for i in dg :
        suma += i
    return suma
deportes_granja = deportes_granjas(set_deportes, set_granja)
print(f"Hacen sólo deportes y actividades de granja: {deportes_granja}")

# Personas que participaron de las tres actividades
def tres_act(j,d,g) :
    jdg = j & d & g
    suma = 0
    for i in jdg :
        suma += i
    return suma
tres_actividades = tres_act(set_juegos, set_deportes, set_granja)
print(f"Personas que participaron de las tres actividades: {tres_actividades}")

# Solo juegos 
def solo_j(j,d,g) :
    j = (j - d) & (j - g)
    suma = 0
    for i in j :
        suma += i
    return suma
solo_juegos = solo_j(set_juegos, set_deportes, set_granja)
print(f"Personas que hacen solo juegos: {solo_juegos}")

# Solo deportes
def solo_d(d,j,g) :
    d = (d - j) & (d - g)
    suma = 0
    for i in d :
        suma += i
    return suma
solo_deportes = solo_j(set_deportes, set_juegos, set_granja)
print(f"Personas que hacen solo deportes: {solo_deportes}")

# Solo actividades de granja
def solo_g(g,j,d) :
    g = (g - d) & (g - j)
    suma = 0
    for i in g :
        suma += i
    return suma
solo_granja = solo_j(set_granja, set_juegos, set_deportes)
print(f"Personas que hacen solo granja: {solo_granja}")

# Dos de las 3 propuestas
def solo_2() :
    return juegos_granja + deportes_granja + juegos_deportes

# Diagrama
plt.figure("Parcial")

d = venn3({"100":1, "010":1, "001": 1, "110":1, "101":1, "011":1, "111":1}, set_labels=("Juegos", "Deportes", "Granja"))
venn3_circles(subsets=(1,1,1,1,1,1,1), linewidth=1, color="black")

d.get_label_by_id("100").set_text(solo_juegos)
d.get_label_by_id("010").set_text(solo_deportes)
d.get_label_by_id("001").set_text(solo_granja)
d.get_label_by_id("110").set_text(juegos_deportes)
d.get_label_by_id("101").set_text(juegos_granja)
d.get_label_by_id("011").set_text(deportes_granja)
d.get_label_by_id("111").set_text(tres_actividades)

plt.text(-1.10, 0.70,
 s="Universo = " + str(f"{universo}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(0.54, -0.70,
 s="Fuera del conjunto = " + str(f"{ninguno}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.30, -0.20,
 s="Respuestas: ",
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.30,
 s="Participaron en las 3 propuestas: " + str(f"{tres_actividades}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.40,
 s="Participaron sólo en deportes y juegos: " + str(f"{juegos_deportes}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.50,
 s="Participaron sólo en juegos y actividades en la granja: " + str(f"{juegos_granja}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.60,
 s="Participaron sólo en deportes y actividades en la granja: " + str(f"{deportes_granja}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.70,
 s="Participaron sólo en deportes: " + str(f"{solo_deportes}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.80,
 s="Participaron sólo en juegos: " + str(f"{solo_juegos}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.80,
 s="Participaron sólo en actividades de granja: " + str(f"{solo_granja}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.text(-1.3, -0.80,
 s="Participaron sólo en 2 de las 3 propuestas: " + str(f"{solo_2()}"),
 size=10,
 ha="left", 
 va="bottom", 
 bbox=dict(boxstyle="square", 
 ec=(1.0, 0.7, 0.5),
 fc=(1.0, 0.9, 0.8),))

plt.show()