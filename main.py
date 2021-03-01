"""
Calcular sueldo semanal, incluyendo pago por horas dobles
"""

# Entradas
horas = eval(input("Introduzca las horas trabajadas: "))
tarifa = eval(input("Introduzca la tarifa horaria: "))
		
# Proceso
if horas <= 48:
    # Puras horas sencillas
	sueldo1 = horas * tarifa
	horas2 = 0
	sueldo2 = 0
else:
	sueldo1 = 48 * tarifa
	horas2 = horas - 48
	sueldo2 = horas2 * tarifa * 2

sueldoT = sueldo1 + sueldo2
	
# Salidas

print("Horas extras:  ", horas2)
print("Sueldo extra:  ", sueldo2)
print("Sueldo total:  ", sueldoT)
