"""5.	Crea un diagrama de Venn para ilustrar la información siguiente acerca de los subconjuntos M y N 
en el universo U:

n(M) = 89; n(N ) = 103; n(M ∪ N ) = 130; n(U ) = 178

Solución: De nuevo, comenzaremos en el medio de la intersección. Debemos determinar cuántos elementos
hay en la intersección. Consideremos que cuando agregamos elementos M a los elementos en N, agregamos
los elementos de la intersección 2 veces. Esto sucede porque se cuentan en el conjunto M y también 
en N. Observaste que:

- n(M) + n(N ) = 89 + 103 = 192

mientras el:

- n(M ∪ N ) = 130

Hemos contado 2 veces los 62 (192-130) elementos en M ∩ N. Ahora podemos poner este número en el
diagrama y resolver como en el ejemplo anterior."""

import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Cantidad de elementos en M
n_m = 89

# Cantidad de elementos en N
n_n = 103

# Cantidad de elementos en la unión de M y N
n_union = 130

# Calcular la cantidad de elementos en la intersección entre M y N
n_intersection = n_m + n_n - n_union

# Crear un diagrama de Venn
venn2(subsets=(n_m - n_intersection, n_n - n_intersection, n_intersection), set_labels=('M', 'N'))

# Mostrar el diagrama de Venn
plt.title('Diagrama de Venn - Conjuntos M y N')

plt.text(0.28, -0.65, 
         s="Fuera de\nlos conjuntos = " + str('178-(27+62+41)=48'),
         size=10)

plt.show()
