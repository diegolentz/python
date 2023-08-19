"""5. Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto 
debe ser divisible por 4 y no debe ser divisible por 100,
excepto que también sea divisible por 400."""


ano = int(input("ingrese un ano \n"))

if ano % 4 == 0 and ano % 4 == 0 or ano % 400 == 0:
    print(f"es viciesto")  
else: print(f"no es viciesto")