"""2.	En una escuela de 600 alumnos, 100 no estudian ningún idioma extranjero (solo estudian ingles),
450 estudian francés y 50  estudian francés e inglés. ¿Cuántos estudian solo inglés?
"""
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Cantidad total de alumnos en la escuela
total = 600

# Cantidad de alumnos que no estudian ningún idioma extranjero
ingles = 100

# Cantidad de alumnos que estudian francés
frances = 450

# Cantidad de alumnos que estudian francés e inglés
estudian_frances_ingles = 50

# Calcular la cantidad de alumnos que estudian solo inglés
# Usamos la fórmula de Venn: B - (A ∩ B)
estudian_ingles = total - (ingles + frances)

# Crear un diagrama de Venn
venn2(subsets=(ingles, frances, estudian_ingles),
      set_labels=('No Estudian ', 'Estudian Francés o Inglés'))

# Mostrar el diagrama de Venn
plt.title('Diagrama de Venn - Estudiantes de Francés e Inglés')
plt.show()

# Imprimir la cantidad de estudiantes que estudian solo inglés
print(f"Cantidad de estudiantes que estudian solo inglés: {estudian_ingles}")
