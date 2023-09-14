
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Datos para los conjuntos A y B
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Crear un diagrama de Venn de dos conjuntos
venn2([conjunto_a, conjunto_b], ('Conjunto A', 'Conjunto B'))

# Configurar el título
plt.title("Diagrama de Venn de dos conjuntos")

# Mostrar el diagrama de Venn
plt.show()
