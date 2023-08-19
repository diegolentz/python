"""4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje
“es vocal”. Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un 
carácter, informarleque no se puede procesar el dato."""

letra = input("ingrese una letra \n").upper()

if len(letra) == 1:
        if letra in 'AEIOU':
            print(f"es vocal")
        else:
            print(f"es consonante")
else:         
            print(f"oprimio mas de una letra")