import matplotlib.pyplot as plt

# Listas de nombres de países y sus respectivos PIB en millones de dólares
paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador","Guayana","Mexico","Paraguay","Peru","Surinam","Uruguay","Venezuela"]
pib = [440769.2, 29702.8, 2364409.9, 286013.8, 394571.1, 885547.7,4780.6,1309880.9,37260.6,210881.6,4678.2,50532.1,116067.8]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Definir el tamaño de la figura (x/y)

plt.bar(paises, pib, color='red')  # Crear el gráfico de barras

plt.xlabel('Países')  # Etiqueta del eje x
plt.ylabel('PIB (en millones de dólares)')  # Etiqueta del eje y
plt.title('PIB de países latinoamericanos al 15/DIC/2020')  # Título del gráfico

plt.xticks(rotation=45)  # Rotar las etiquetas del eje x para una mejor legibilidad

plt.tight_layout()  # Ajustar el diseño de la figura
plt.show()  # Mostrar el gráfico
