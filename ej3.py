"""3.	En una escuela de 500 estudiantes, hay:

- 125 estudiantes inscriptos en Álgebra II, 
- 275 estudiantes que practican deportes y 
- 52 estudiantes que están inscriptos en Álgebra II y practican deportes. 

Crea un diagrama de Venn para ilustrar esta información."""

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Cantidad total de estudiantes
total = 500

# Estudiantes inscritos en Álgebra II
algebra = 125

# Estudiantes que practican deportes
deportes = 275

# Estudiantes inscritos en Álgebra II y que practican deportes
algebra_deportes = 52

# Calcular estudiantes que solo hacen una actividad
soloAlgebra = algebra - algebra_deportes 
soloDeportes = deportes - algebra_deportes 

# Calcular estudiantes que no hacen ninguna de las dos actividades
#ningunaActividad = total - (algebra + deportes + algebra_deportes)

# Crear un diagrama de Venn
venn2(subsets=(soloAlgebra, soloDeportes,algebra_deportes),
      set_labels=('Álgebra II', 'Deportes'))

# Mostrar el diagrama de Venn
plt.title('Diagrama de Venn - Estudiantes en Álgebra II y Deportes')
plt.show()
