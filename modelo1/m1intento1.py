"""
En una comunidad de
100 deportistas se sabe que 
30 de ellos entrenan fútbol,
50 entrenan squash 
60 entrenan tenis.
 
Si 10 deportistas entrenan los tres deportes 
22 entrenan tenis y fútbol,
30 entrenan squash y tenis y 
15 entrenan squash y fútbol. 

1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""

#importo librerias, defino variables
from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

todos = 100
total = 3+15+18+5+12+20+10 #segun pertenencia a conjuntos
ninguno = todos-total

listaFutbol = [10,12,5,1,2]
tuplaSquash = (10,20,5,7,8)
diccionarioTenis = {"uno":10,"dos":12,"tres":20,"cuatro":14,"cinco":4}

#convierto los numeros deseados
#tuplas y listas se pueden sumar de igual manera, hago una generica
def suma(algo):
    suma = 0
    for x in algo:
        suma += x
    return suma

futbol = suma(listaFutbol)
squash = suma(tuplaSquash)

print(f"\nvalores\n")
print(futbol)
print(squash)

def sumT(diccionarioTenis):
    suma = 0
    for x in diccionarioTenis.values():
        suma += x
    return suma

tenis = sumT(diccionarioTenis)
print(tenis)

#convierto a set todo

def convertSet(algo):
#
    if algo == diccionarioTenis:
        conver = set()
        for x in diccionarioTenis.values():
            conver.add(x)
            devuelvo = conver
    else:
        devuelvo = set(algo)
    return devuelvo

futbolSet = convertSet(listaFutbol)
squashSet = convertSet(tuplaSquash)
tenisSet = convertSet(diccionarioTenis)

print(f"\nsets\n")
print(futbolSet)
print(squashSet)
print(tenisSet)

#continua calculos
"""Si 10 deportistas entrenan los tres deportes 
22 entrenan tenis y fútbol,
30 entrenan squash y tenis y 
15 entrenan squash y fútbol. """

def cantidad(x, y):
    return (x & y)

def cant10(x,y,z):
    return (x & y & z)

tenisFutbol = cantidad(tenisSet, futbolSet)
squashTenis = cantidad(squashSet, tenisSet)
squashFutbol = cantidad(squashSet, futbolSet)
todo = cant10(tenisSet,futbolSet,squashSet)

print(f"\nconjuntos\n")
print(tenisFutbol)
print(squashTenis)
print(squashFutbol)
print(todo)

"""
1-¿cuántos entrenan sólo tenis?
2-¿cuántos entrenan sólo fútbol?
3-¿cuántos entrenan sólo squash?
4-¿cuántos entrenan tenis o fútbol?
"""

#calculo los solos
def solo(x, y, z):
    return (x - y) & (x - z)

soloTenis = {sum(solo(tenisSet,futbolSet,squashSet))}
soloFutbol = {sum(solo(futbolSet,tenisSet,squashSet))}
soloSquash = {sum(solo(squashSet,tenisSet,futbolSet))}

print("\nlos solos\n")
print(soloTenis)
print(soloFutbol)
print(soloSquash)

print("\ntenis o futbol\n")

#tenis o futbol
def tenis_o_futbol(tenisSet,futbolSet,squashSet):
    conjunto = ((squashSet-tenisSet)&(squashSet-futbolSet))
    resultado = total - sum(conjunto)
    return resultado
total   

tenisoFutbol = {tenis_o_futbol(tenisSet,futbolSet,squashSet)}
print(tenisoFutbol)

#parte grafica
plt.figure('parcialito')

#se dibuja los diagramas
diagram = venn3((1,1,1,1,1,1,1),
                set_labels=("Futbol","Squash","Tenis"))

#tamanio
for x in ("111","110","101","100","011","010","001"):
    diagram.get_label_by_id(x).set_fontsize(10)
    
#transfiero resultados

diagram.get_label_by_id('100').set_text(soloFutbol)
diagram.get_label_by_id('010').set_text(soloSquash)
diagram.get_label_by_id('001').set_text(soloTenis)
diagram.get_label_by_id('110').set_text(squashFutbol - todo)
diagram.get_label_by_id('101').set_text(tenisFutbol - todo)
diagram.get_label_by_id('011').set_text(squashTenis - todo)
diagram.get_label_by_id('111').set_text(todo)

# agregamos más datos aclaratorios al gráfico


plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {total}",
         size=10)

plt.text(0.30, -0.7,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {ninguno}",
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
         s="Entrenan tenis o fútbol = " + str(tenisoFutbol),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

# Recuadro
plt.axis('on')  
plt.title("Deportistas")
plt.show()