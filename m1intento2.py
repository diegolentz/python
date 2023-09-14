"""
En una comunidad de 100 deportistas se sabe que 30 de ellos entrenan fútbol, 50 entrenan squash 
y 60 entrenan tenis. 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
Si 10 deportistas entrenan los tres deportes 
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""
from matplotlib import pyplot as plt
from matplotlib_venn import venn3,venn3_circles
  


listaFutbol = [10,5,12,1,2]
tuplaSquash = (10,5,20,7,8)
diccionarioTenis = {'uno':10,'dos':20,'tres':12,'cuatro':14,'cinco':4}

def suma(algo):
    suma = 0
    if algo == diccionarioTenis:
        for x in algo.values():
            suma += x
        suma
    else:
        for x in algo:
            suma += x
        suma
    return suma

sumaFutbol = suma(listaFutbol)
sumaSquash = suma(tuplaSquash)
sumaTenis = suma(diccionarioTenis)

print(f"las sumas de los conjuntos es\n")
print(f"{sumaFutbol} para futbol")
print(f"{sumaSquash} para squash")
print(f"{sumaTenis} para tenis")

"""
se verifican las sumas de los conjuntos
"""

#paso todo a set

def pasoSet(algo):
    if algo == diccionarioTenis:
        conver = set()
        for x in algo.values():
            conver.add(x)
        devuelvo = conver
    else:
        devuelvo = set(algo)
    return devuelvo

futbolSet = pasoSet(listaFutbol)
squashSet = pasoSet(tuplaSquash)
tenisSet = pasoSet(diccionarioTenis)

print(f"\nconvertido a set quedaria\n")
print(f"{futbolSet} para futbol")
print(f"{squashSet} para squash")
print(f"{tenisSet} para tenis")

#continuo calculos
""" 22 entrenan tenis y fútbol, 30 entrenan squash y tenis y 15 entrenan squash y fútbol. 
Si 10 deportistas entrenan los tres deportes 

"""
def todoDeporte(x,y,z):
    return (x & y & z)

def cuantos(x,y):
    return x & y

todosDeportes = todoDeporte(futbolSet,squashSet,tenisSet)
tenisFutbol = (cuantos(tenisSet,futbolSet))
squashTenis = (cuantos(squashSet,tenisSet))
squashFutbol = (cuantos(squashSet,futbolSet))

print(f"\nlos que practucan 2 deportes\n")
print(f"{suma(tenisFutbol)} para tenis/futbol")
print(f"{suma(squashTenis)} para squash/tenis")
print(f"{suma(squashFutbol)} para squash/futbol")
print(f"{suma(todosDeportes)} para los que hacen de todo")

"""
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""

def solos(x,y,z):
    return (x-y)&(x-z)

def tenisoFutbol(x,y,z):
    
    return ((y-z)&(y-x))|((x-z)&(x-y)) 

soloTenis = {sum(solos(tenisSet,squashSet,futbolSet))}
soloFutbol = {sum(solos(futbolSet,squashSet,tenisSet))}
soloSquash = {sum(solos(squashSet,futbolSet,tenisSet))}
tenesoFutbol = {sum(tenisoFutbol(tenisSet,futbolSet,squashSet))}

print(f"\nlos que practucan solos 1 deporte\n")
print(f"{soloTenis} para tenis/futbol")
print(f"{soloFutbol} para squash/tenis")
print(f"{soloSquash} para squash/futbol")
print(f"{tenesoFutbol} para tenis o futbol")


def sumaOcupados(soloFutbol, soloTenis, soloSquash, todosDeportes, tenisFutbol, squashFutbol, squashTenis):
    vacio={0}
    vacio.update(soloFutbol)
    vacio.update(soloTenis)
    vacio.update(soloSquash)
    vacio.update(todosDeportes)
    vacio.update(tenisFutbol-todosDeportes)
    vacio.update(squashFutbol-todosDeportes)
    vacio.update(squashTenis-todosDeportes)
    suma = sum(vacio)
    resultado = suma 
    return resultado

universo = 100
ocupados = sumaOcupados(soloFutbol, soloTenis, soloSquash, todosDeportes, tenisFutbol, squashFutbol, squashTenis)
libres = universo - ocupados

print(f"\nvalores\n")
print(f"{universo} universo")
print(f"{ocupados} ocupados")
print(f"{libres} ningun deporte")


plt.figure('parcialito')

diagrama = venn3((1,1,1,1,1,1,1),
                set_labels=("Futbol","Squash","Tenis"))

for x in ("001","010","011","100","101","110","111"):
    diagrama.get_label_by_id(x).set_fontsize(10)
    
diagrama.get_label_by_id("100").set_text(soloFutbol)
diagrama.get_label_by_id("010").set_text(soloSquash)
diagrama.get_label_by_id("001").set_text(soloTenis)
diagrama.get_label_by_id("110").set_text(squashFutbol-todosDeportes)
diagrama.get_label_by_id("101").set_text(tenisFutbol-todosDeportes)
diagrama.get_label_by_id("011").set_text(squashTenis-todosDeportes)
diagrama.get_label_by_id("111").set_text(todosDeportes)


plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universo}",
         size=10)

plt.text(0.30, -0.7,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {libres}",
         size=8)

# Respondemos las preguntas
plt.text(-1.10, -0.20,
         s="Respuestas solicitadas: ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.30,
         s="Entrenan sólo tenis = " + str(soloTenis),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.40,
         s="Entrenan sólo fútbol = " + str(soloFutbol),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.50,
         s="Entrenan sólo squash = " + str(soloSquash),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.60,
         s="Entrenan tenis o fútbol = " + str(tenesoFutbol),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.axis('on')  
plt.title("Deportistas")
plt.show()


