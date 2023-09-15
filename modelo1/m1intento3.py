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
from matplotlib_venn import venn3, venn3_circles

lista_futbol = [3, 5, 10, 12]
tupla_squash = (10, 20, 15, 5)
diccio_tenis = {"infantil": 12,  "juniors": 10,
                "adolescentes": 20, "adultos": 18}


def suma(algo):
    suma = 0
    if algo == diccio_tenis:
        for x in algo.values():
            suma += x
        suma
    else:
        for x in algo:
            suma += x
        suma
    return suma

sumaFutbol = suma(lista_futbol)
sumaSquash = suma(tupla_squash)
sumaTeenis = suma(diccio_tenis)


print(f"las sumas de los conjuntos es\n")
print(f"{sumaFutbol} lista futbol")
print(f"{sumaSquash} lista squash")
print(f"{sumaTeenis} lista tenis")

#----------------------------------sets---------------------------------

#paso todo a set

def pasoSet(algo):
    if algo == diccio_tenis:
        conver = set()
        for x in algo.values():
            conver.add(x)
        devuelvo = conver
    else:
        devuelvo = set(algo)
    return devuelvo

futbolSet = pasoSet(lista_futbol)
squashSet = pasoSet(tupla_squash)
tenisSet = pasoSet(diccio_tenis)

print(f"\nconvertido a set quedaria\n")
print(f"{futbolSet} para futbol")
print(f"{squashSet} para squash")
print(f"{tenisSet} para tenis")

#----------------------------------calculos---------------------------------
def participaTodo(x,y,z):
    return (x & y & z)

def dosActividades(x,y):
    return x & y

tenisFutbol = dosActividades(tenisSet,futbolSet)
squashTenis = dosActividades(squashSet,tenisSet)
squashFutbol = dosActividades(squashSet,futbolSet)
entrenaTodo = participaTodo(futbolSet,squashSet,tenisSet)

print(f"\nlos que hicieron acts. combinadas o no participaron\n")
print(f"{sum(tenisFutbol)} para tenis/futbol {tenisFutbol}")
print(f"{sum(squashTenis)} para squash/tenis {squashTenis}")
print(f"{sum(squashFutbol)} para squash/futbol {squashFutbol}")
print(f"{sum(entrenaTodo)} para todas las actividades ")

#----------------------------------calculos de solos---------------------------------

def solos(x,y,z):
    return (x-y)&(x-z)

soloTenis = solos(tenisSet,futbolSet,squashSet)
soloSquash = solos(squashSet,futbolSet,tenisSet)
soloFutbol = solos(futbolSet,tenisSet,squashSet)

universo = 100
ocupados = soloTenis | soloSquash | soloFutbol | entrenaTodo | tenisFutbol | squashTenis | squashFutbol
desocupados = universo - suma(ocupados)

tenisoFutbol = suma(ocupados) - suma(soloSquash)

print(f"\ncantidades \n")
print(f"{universo} para total de encuestados") 
print(f"{desocupados} los que no se inscribieron a nada ") 
print(f"{suma(ocupados)} los que no se inscribieron en algo ") 
print(f"\n")
print(f"{suma(soloTenis)} para tenis {soloTenis}")
print(f"{suma(soloSquash)} para squash {soloSquash}")
print(f"{suma(soloFutbol)} para futbol {soloFutbol}") 
print(f"{(tenisoFutbol)} hacen tenis o futbol ") 


#----------------------------------grafico---------------------------------

plt.figure('parcial')

diagrama = venn3((1,1,1,1,1,1,1),
                set_labels=("Futbol","Squash","Tenis"))

for x in ("001","010","011","100","101","110","111"):
    diagrama.get_label_by_id(x).set_fontsize(10)
    
diagrama.get_label_by_id("100").set_text({suma(soloFutbol)})
diagrama.get_label_by_id("010").set_text({suma(soloSquash)})
diagrama.get_label_by_id("001").set_text({suma(soloTenis)})
diagrama.get_label_by_id("110").set_text({suma(squashFutbol - entrenaTodo)})
diagrama.get_label_by_id("101").set_text({suma(tenisFutbol - entrenaTodo)})
diagrama.get_label_by_id("011").set_text({suma(squashTenis - entrenaTodo)})

diagrama.get_label_by_id("111").set_text({suma(entrenaTodo)})

c = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1))

plt.text(-0.90, 0.67,      # Texto y cantidad universal
         f"Universal = {universo}",
         size=10)

plt.text(0.30, -0.7,      # Texto fuera del conjunto
         f"Fuera\nde los\nconjuntos = {desocupados}",
         size=8)

# Respondemos las preguntas
plt.text(-1.10, 0.20,  
         s="Respuestas : ",
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, 0.10,
         s="solo futbol = " + str(sum(soloFutbol)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, 0.00,
         s="solo squash = " + str(sum(soloSquash)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.10,
         s="solo tenis = " + str(sum(soloTenis)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))

plt.text(-1.10, -0.20,
         s="tenis o futbol = " + str(sum(tenisFutbol)),
         size=8,
         ha="left",  # alineación horizontal
         va="bottom",  # alineación vertical
         bbox=dict(boxstyle="square",  # tipo de cuadro
                   ec=(1.0, 0.7, 0.5),
                   fc=(1.0, 0.9, 0.8),))
plt.axis('on')  
plt.title("Deportistas")
plt.show()
