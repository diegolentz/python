"""2.	Desarrolla un programa que permita leer 2 valores y que emita por pantalla la suma, la resta
, el producto, la división, el resto, el promedio y el doble producto del primero menos la mitad 
del segundo.     """

numero1 = float(input("ingrese el primer valor \n"))
numero2 = float(input("ingrese el segundo valor \n"))

suma = numero1 + numero2
resta = numero1 - numero2
multi = numero1 * numero2
promedio = (numero1 + numero2)/2
dobleMitad = (numero1*2)-(numero2*0.5)

if numero2 == 0 :
    print(f"no se puede dividir por 0!")
div = numero1 / numero2

print(f"los numeros ingresados fueron {numero1} y {numero2} \n" )
print(f"suma: {suma} \nresta: {resta} \nmultiplicacion: {multi} \npromedio: {promedio} \n2*priomero - segundo/2: {dobleMitad}")