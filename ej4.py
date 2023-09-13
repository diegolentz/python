"""4. El propietario de una fábrica electrodomésticos, que opera una línea de producción, tiene dos productos
principales y necesita un gráfico de barras comparativo, de diferentes colores para representar la
producción de cada producto durante 5 días, lunes a viernes. El eje horizontal mostraría los días
y el eje vertical las barras que representan la producción. Como datos tenemos:
prod1 = (20, 35, 30, 35, 27)
prod2 = (25, 32, 34, 20, 25)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
Podría representarse la diferencia de fabricación entre productos en el mismo gráfico?"""


import matplotlib.pyplot as plt
import numpy as np

#listas de productos y dias
prod1 = (20, 35, 30, 35, 27)
prod2 = (25, 32, 34, 20, 25)
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']

# Rango de valores para el eje x
x = np.arange(len(dias))
# Ancho de las barras
ancho_barra = 0.35

# Crear el gráfico de barras agrupadas
plt.figure(figsize=(8, 6))

plt.bar(x - ancho_barra/2, prod1, ancho_barra, label='prod1', color='blue', alpha=0.6)
plt.bar(x + ancho_barra/2, prod2, ancho_barra, label='prod2', color='green', alpha=0.6)

plt.xlabel('Dias')
plt.ylabel('Valor')
plt.title('Comparación semanal de productos')
plt.xticks(x, dias, rotation=45)  # Etiquetas de países en el eje x con rotación
plt.legend()

plt.tight_layout()
plt.show()

