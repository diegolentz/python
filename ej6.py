"""6. Traza un gráfico de dispersión (puntos) de los siguientes datos que representan las calificaciones de dos grupos de
deportistas dentro de un rango (eje x). Identifica los valores de cada grupo con un color distinto.
grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
"""

import matplotlib.pyplot as plt

grupo1 = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
grupo2 = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
rango = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Crear el gráfico de dispersión para el grupo1
plt.scatter(rango, grupo1, label='Grupo 1', color='blue', marker='o')

# Crear el gráfico de dispersión para el grupo2
plt.scatter(rango, grupo2, label='Grupo 2', color='red', marker='x')

# Agregar etiquetas y título al gráfico
plt.xlabel('Rango')
plt.ylabel('Calificaciones')
plt.title('Gráfico de Dispersión de Calificaciones de Dos Grupos de Deportistas')

# Agregar una leyenda para identificar los grupos
plt.legend()

# Mostrar el gráfico
plt.grid(True)
plt.show()
