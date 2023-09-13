import matplotlib.pyplot as plt
import numpy as np

# Listas de nombres de países, población y superficie (datos de ejemplo)
paises = ["Estados Unidos", "Brasil", "México", "Colombia", "Argentina"]
poblacion = [331002651, 212559417, 128932753, 50882891, 45195774]
superficie = [9981930, 85148770, 19643750, 11417480, 27926000]


# Rango de valores para el eje x
x = np.arange(len(paises))
# Ancho de las barras
ancho_barra = 0.35

# Crear el gráfico de barras agrupadas
plt.figure(figsize=(12, 6))
#uso el x y el ancho de barra, pone una barra a la izquierda y la otra a la derecha
plt.bar(x - ancho_barra/2, poblacion, ancho_barra, label='Población', color='blue', alpha=0.6)
plt.bar(x + ancho_barra/2, superficie, ancho_barra, label='Superficie', color='green', alpha=0.6)

plt.xlabel('Países')
plt.ylabel('Valor')
plt.title('Comparación de Población y Superficie por País')
plt.xticks(x, paises, rotation=45)  # Etiquetas de países en el eje x con rotación
plt.legend()

plt.tight_layout()
plt.show()
