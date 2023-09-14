"""6.	Crea un diagrama de Venn para representar la información siguiente y responder las preguntas: 
En una encuesta a 15 estudiantes secundarios, se descubrió que: 
•	80 estudiantes tienen laptops.
•	110 estudiantes tienen celulares.
•	125 estudiantes tienen iPod
•	50 estudiantes tienen los tres objetos.


•	62 estudiantes tienen una laptop y un celular.
•	58 estudiantes tienen una laptop y un iPod.
•	98 estudiantes tienen un celular y un iPod.
Responde:
a. ¿Cuántos estudiantes tienen solo un celular?
b. ¿Cuántos estudiantes no tienen ninguno de los objetos mencionados?
c. ¿Cuántos estudiantes tienen un iPod y una laptop, pero no un celular?
"""
#hay que mirar los calculos pero esta...


import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Cantidad total de estudiantes encuestados
total_estudiantes = 15

# Cantidad de estudiantes que tienen laptops
estudiantes_laptop = 80

# Cantidad de estudiantes que tienen celulares
estudiantes_celular = 110

# Cantidad de estudiantes que tienen iPod
estudiantes_ipod = 125

# Cantidad de estudiantes que tienen los tres objetos
estudiantes_tres_objetos = 50



# Cantidad de estudiantes que tienen una laptop y un celular
estudiantes_laptop_celular = (62 - estudiantes_tres_objetos)

# Cantidad de estudiantes que tienen una laptop y un iPod
estudiantes_laptop_ipod = (58 - estudiantes_tres_objetos)

# Cantidad de estudiantes que tienen un celular y un iPod
estudiantes_celular_ipod = (98 - estudiantes_tres_objetos)


lap = estudiantes_tres_objetos + estudiantes_laptop_ipod  + estudiantes_laptop_celular
cel = estudiantes_tres_objetos + estudiantes_celular_ipod + estudiantes_laptop_celular
ipo = estudiantes_tres_objetos + estudiantes_celular_ipod + estudiantes_laptop_ipod

# Crear un diagrama de Venn
venn3(subsets= (estudiantes_laptop - lap,
                estudiantes_celular - cel,
                estudiantes_ipod - ipo,
                estudiantes_laptop_celular,
                estudiantes_celular_ipod,
                estudiantes_laptop_ipod,
                estudiantes_tres_objetos),
      set_labels=('Laptop', 'Celular', 'iPod'))

# Mostrar el diagrama de Venn
plt.title('Diagrama de Venn - Estudiantes y Sus Dispositivos')
plt.show()


