"""Escribe un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número
mientras no sea mayor que el primero. El programa termina y emitirá los números."""

primero = int(input("escriba un numero \n"))
segundo = int(input("escriba otro numero \n"))

while  segundo < primero :
    segundo = int(input("escriba un numero mayor al primero \n"))

print(f"el primer numero es {primero} \n")    
print(f"el segundo numero es {segundo} \n")    

