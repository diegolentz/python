"""2. Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes,
otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
Si el día ingresado no es ninguno de esos, imprimir otro mensaje."""

dia = input("ingrese el dia \n")
diaMayus = dia.upper()

if diaMayus == 'LUNES':
    print(f"es lunes papu")
elif diaMayus == 'VIERNES':
    print(f"es viernes papu")
elif diaMayus == 'SABADO':
    print(f"es sabado papu")
elif diaMayus == 'DOMINGO':
    print(f"es domingo papu")
else : print(f"en un cumple")
