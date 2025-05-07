# Desarrolla un programa en python que permite calcular el subsidio de gas segun el quintil de ingreso al que pertenece la familia del solicitante y sus codiciones laborales
# Condiciones socieconomicas:
# Quintil de ingreso hay 5 quintiles en total (1. igual menos ingreso, 5 igual mayor ingreso)
# Condiciones laborales:
# Se considera si la persona esta empleada o desempleada. 
# Condiciones del subsidio de gas: 
# Quintil / Condicion laboral / Subsidio de gas.  
# Primer dato a ingresar: 1 o 2; Condicion desempleado; 10.000
# Segundo dato: 1 o 2; Empleado; le corresponde 8.000
# Tercer dato: 3; desempleada; le pertenece un sibsidio de 6.000 
# Cuarto dato: 4; Empleado; Subsidio de 4.000
# Quinto dato: 4 o 5; Cualquiera; Subsidio de 1.500  
# Bono adicionales: si el solicitante pertenece al quintil 1 o 2 recibira un bono adicional de 2.000 pesos, si ademas tiene mas de 65 años recibira un bono extra de 3.000

print ("Bienvenido al calculo de subsidio de gas segun tu ingreso.")
Empleabilidad = int(input("Estas 1) Empleado o 2) Desempleado: "))
Quintil  = int(input("Ingresa tu quintil de ingreso (1-5): "))
Edad = int(input("Ingresa tu edad: "))

Subsidio = 0 
Bono = 0

if Quintil == 1 or 2: 
    if Empleabilidad == 2: 
        Subsidio = 10000
elif Quintil == 1 or 2:
    if Empleabilidad == 1:
        Subsidio = 8000
elif Quintil == 3: 
    if Empleabilidad == 2:
        Subsidio = 6000
elif Quintil == 4:
    if Empleabilidad == 1:
        Subsidio = 4000
elif Quintil == 4 or 5:
    if Empleabilidad == 1 or 2:
        Subsidio = 1500
else: 
    print ("Error.")

if Quintil == 1 or Quintil == 2:
    Bono = 2000
    if Edad > 65:
        Bono = Bono + 3000

Subsidio_total = Subsidio + Bono

print (f"Subsidio base: {Subsidio}")
print (f"Bono obtenido: {Bono}")
print (f"Subsidio final: {Subsidio_total}")