"""5. Un grupo de amigos, decidieron registrar durante 6 días, cuántas tazas ingerían de café, té y agua.
Con esos datos, necesitan un gráfico de barras apiladas para visualizar quién ingiere más líquidos y quién menos.
cafe = np.array([5, 5, 7, 6, 7, 4])
te = np.array([1, 2, 0, 2, 1, 3])
agua = np.array([10, 0, 14, 12, 15, 13])
nombres = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']
Podrían representarse los datos anteriores con un diagrama de cajas?
"""

import matplotlib.pyplot as plt
import numpy as np

nombres = ['María', 'Pablo', 'Ema', 'Franco', 'Estefanía', 'Pedro']
cafe = np.array([5, 5, 7, 6, 7, 4])
te = np.array([1, 2, 0, 2, 1, 3])
agua = np.array([10, 0, 14, 12, 15, 13])

# Definir los parámetros del gráfico
N = len(nombres)
barWidth = 0.5
xloc = np.arange(N)

# Crear el gráfico de barras apiladas
plt.bar(xloc, cafe, width=barWidth, label='Café')
plt.bar(xloc, te, bottom=cafe, width=barWidth, label='Té')
plt.bar(xloc, agua, bottom=cafe + te, width=barWidth, label='Agua')

# Añadir etiquetas, título, marcas de verificación y leyenda
plt.ylabel('Litros')
plt.xlabel('Nombres')
plt.title('Consumo de Bebidas')
plt.xticks(xloc, nombres)
plt.yticks(np.arange(0, 41, 5))
plt.legend()

# Mostrar el gráfico
plt.show()
