# En la provincia de Bs. As. se realizó una encuesta sobre la posesión de determinados vehículos.
# Los datos obtenidos se agruparon de la siguiente manera:
# En una lista los porcentajes de los que tienen moto = [14, 17, 9, 13, 15, 12]
# En una tupla los porcentajes de los que tienen bicicleta = (17, 8, 9, 7, 10, 11, 12, 4, 12)
# En un diccionario los porcentajes de los que tienen auto = {"Chico":27,"Mediano":17,"Grande":16}
# Como resultado se han obtenido los siguientes datos:
# - 2% no tiene ningún vehículo.
# - 55% tienen los tres vehículos.
# - 2% sólo tienen bicicleta y auto
# - 18% sólo tienen moto y bicicleta
# - 1% sólo auto
# 1. Qué porcentaje de encuestados poseen sólo uno de los vehículos?
# 2. Qué porcentaje sólo tienen moto y auto?
# 3. Qué porcentaje tienen sólo moto?
# 4. Qué porcentaje de tienen sólo bicicleta?

from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles

# 1. Definir variables y estructuras
#paso los datos obtenidos a otra expresion que sirve
lista_moto = [55, 18, 2, 5]
tupla_bici = (55, 18, 2, 15)
diccio_auto = {"Chico":55, "Chico":1, "Grande":2, "electrico":2}

# 2. Funciones de cálculo sobre las estructuras

Universal=232 #->los 230 de la suma de cada conjunto mas los 2 que no tienen ninguno
ninguno=2
los_tres=55
moto_bici=18
bici_auto=2
solo_auto=1

def suma(valores):
    suma = 0
    for elemento in valores:
        suma += elemento
    return suma

sum_moto = suma(lista_moto)
print("El total de personas que  tienen moto es: ", sum_moto)

sum_bici = suma(tupla_bici)
print("El total de personas que tienen bici es: ", sum_bici)

sum_auto = suma(diccio_auto.values())
print("El total de personas que tienen auto es: ", sum_auto)

#convierto todo a set para trabajar con eso

def setx(valores):
    setx = set()
    for elemento in valores:
        setx.add(elemento)
    return setx

moto = setx(lista_moto)
print("Set de moto: ", moto)

bici = setx(tupla_bici)
print("Set de bici: ", bici)

#para los diccionarios paso solo los valores sin las keys
auto = setx(diccio_auto.values()) 
print("Set de auto: ", auto)

#Hago la funcion para chequear cuantos tienen dos vehiculos:
def tienendos(veh1, veh2):
    return (veh1 & veh2)

# 1. Qué porcentaje de encuestados poseen sólo uno de los vehículos?
# 2. Qué porcentaje sólo tienen moto y auto?
# 3. Qué porcentaje tienen sólo moto?
# 4. Qué porcentaje de tienen sólo bicicleta?

moto_auto=tienendos(moto,auto)
print("Porcentaje tienen moto y auto: ", sum(moto_auto))
print("Porcentaje SOLO moto y auto: ", sum(moto_auto) - los_tres) 
solo_motoauto= sum(moto_auto) - los_tres

solo_moto= sum_moto - solo_motoauto - los_tres - moto_bici
print("Porcentaje solo moto: ", solo_moto)

solo_bici= sum_bici - moto_bici - los_tres - bici_auto
print("Porcentaje solo bici: ", solo_bici)

solo_unvehiculo= solo_auto + solo_bici + solo_moto
print("Porcentaje solo un vehiculo:", solo_unvehiculo)

# dibujamos los diagramas
diagram = venn3((1, 1, 1, 1, 1, 1, 1), set_labels=("Moto", "Bicicleta", "Auto"))

# establecemos el tamaanioo de la fuente
for subset in ("111", "110", "101", "100", "011", "010", "001"):
    diagram.get_label_by_id(subset).set_fontsize(10)

# transferimos los resultados de las operaciones
diagram.get_label_by_id('100').set_text(f"{solo_moto}%")
diagram.get_label_by_id('010').set_text(f"{solo_bici}%")
diagram.get_label_by_id('001').set_text(f"{solo_auto}%")
diagram.get_label_by_id('110').set_text(f"{moto_bici}%")
diagram.get_label_by_id('011').set_text(f"{bici_auto}%")
diagram.get_label_by_id('101').set_text(f"{solo_motoauto}%")
diagram.get_label_by_id('111').set_text(f"{los_tres}%")

# marcamos los contornos
c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

# Texto y cantidad universal
plt.text(-0.90, 0.67,
         f"Universal = {Universal} %",
         size=10)

# Texto fuera del conjunto
plt.text(0.40, -0.5,
         f"Fuera\nde los\nconjuntos = {ninguno}%",
         size=8)

# Respondemos las preguntas
plt.text(-1.10, -0.8,
         s=f"Respuestas solicitadas:\nSolo uno de los vehiculos = {solo_unvehiculo}%\nSolo moto y auto =  {solo_motoauto}%\nSolo moto = {solo_moto}%\nSolo bicicleta = {solo_bici}",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))


plt.axis('off')  # Recuadro apagano
plt.title("Vehiculos")
plt.show()