"""Diseña un programa que facilite el trabajo con conjuntos. Recuerda que un conjunto es una lista
en la que no hay elementos repetidos. Debes implementar: 

• lista_a_conjunto(lista): Devuelve un conjunto con los mismos elementos que hay en lista
    pero sin repeticiones. (Ejemplo: lista_a_conjunto([1,1,3,2,3])
    devolverá la lista [1, 2, 3] (aunque también se acepta como equivalente cualquier permutación de esos 
    mismos elementos, como [3,1,2] o [3,2,1]). 
• union(A, B): devuelve el conjunto resultante de unir los conjuntos A y B. 
• interseccion(A, B): devuelve el conjunto cuyos elementos pertenecen a A y a B.
• diferencia(A, B): devuelve el conjunto de elementos que pertenecen a A y no a B. 
•iguales(A, B): devuelve cierto si ambos conjuntos tienen los mismos elementos, y falso en caso contrario."""

lista = [1,1,3,2,3]
listb = [2,3,2,4]
#1
conjuntoa = set(lista)
conjuntob = set(listb)

print(conjuntoa)
print(conjuntob)
#2
conjuntoc = conjuntoa | conjuntob
print(conjuntoc)
#3
conjuntod = conjuntoa & conjuntob
print(conjuntod)
#4
conjuntoe = conjuntoa - conjuntob
print(conjuntoe)
#5
conjuntof = conjuntoa == conjuntob
print(f"son iguales papu? \n{conjuntof}")