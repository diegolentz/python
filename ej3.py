"""3.	Desarrolla un programa que dada una cierta cantidad de galones, los convierta a 
litros y dada una medida en millas las convierta a metros, ambos con entrada de 
tipo flotante. """

gallon = 3.78   #1 galon = litros
millas = 1.60   #1 milla = km

galones = float(input("introduzca la cantidad de galones \n"))
miyas = float(input("introduzca la cantidad de millas \n"))

totalLitro = round(galones / gallon,2)
totalKm = round(miyas / millas,2)

print(f"{galones} son {totalLitro} lts")
print(f"{miyas} son {totalKm} kms")