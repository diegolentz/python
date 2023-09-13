import matplotlib.pyplot as plt

# Listas de nombres de países y sus respectivos PIB en millones de dólares
paises = ["Argentina", "Bolivia", "Brasil", "Chile", "Colombia", "Ecuador", "Guyana", "Mexico", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
pib = [440769.2, 29702.8, 2364409.9, 286013.8, 394571.1, 885547.7,4780.6,1309880.9,37260.6,210881.6,4678.2,50532.1,116067.8]


plt.figure(figsize=(10, 10))

desfase = [0.1 if pais == 'Argentina' else 0 for pais in paises]
plt.pie(pib ,labels = paises , autopct='%1.1f%%', explode = desfase)

plt.title('Distribución del PIB de países latinoamericanos al 15/DIC/2020')

plt.axis('equal')  # Aspecto igual para que el gráfico sea un círculo

plt.tight_layout()  # Ajustar el diseño de la figura
plt.show()  # Mostrar el gráfico
