"""Escribe tres programas que emitan las siguientes secuencias de números:
• En el primer programa, el tipo range() que se utilice en cada bucle debe tener un único argumento. 
• En el segundo programa, el tipo range() que se utilice en cada bucle debe tener dos argumentos. 
• En el tercer programa, el tipo range() que se utilice en cada bucle debe tener tres argumentos.
"""
"""------------------------------------------------------------------------------------------"""

a = int(input("ingrese un numero \n"))
b = list(range(a))
print(b)

"""------------------------------------------------------------------------------------------"""

c = int(input("ingrese un numero inicial \n"))
d = int(input("ingrese un numero final \n"))

if c < d:
    e = list(range(c,d+1))
    print(e)
elif c > d :
    c, d = d, c
    e = list(range(c, d+1))
    print(e)
    
"""------------------------------------------------------------------------------------------"""

f = int(input("Ingrese un número inicial: "))
g = int(input("Ingrese un número final: "))
paso = int(input("Ingrese el valor del paso: "))

if f < g:
    h = list(range(f, g + 1, paso))
    print(h)
elif f > g:
    f, g = g, f
    h = list(range(f, g + 1, paso)) 
    print(h)
