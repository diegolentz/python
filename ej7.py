"""7. Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros no se cobran hasta finales de año y se te suman al balance final de tu cuenta de ahorros.
Escribe un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros. 
El programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer año.
Redondea cada cantidad a dos decimales."""


ingreso = float(input("cuanto dinero desea depositar: \n"))

interes = 0.04

primerAno = round((ingreso * interes) + ingreso, 2)
segundoAno = round((primerAno * interes) + primerAno, 2)
tercerAno = round((segundoAno * interes) + segundoAno, 2)

print(f"el primer ano obtuvo {primerAno} \nel segundo ano obtuvo {segundoAno} \nel tercer ano obtuvo {tercerAno}")