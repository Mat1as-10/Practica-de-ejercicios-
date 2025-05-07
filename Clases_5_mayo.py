Quintil = int(input("Ingrese su quintil (1-5): "))
Empleabilidad = input("Ingresa tu condicion laboral: ")
Edad = int(input("Ingresa tu edad: "))

Subsidio = 0
Bono = 0

if Quintil in [1, 2]:
    if Empleabilidad == "Desempleado":
        Subsidio = 15000
    elif Empleabilidad == "Empleado":
        Subsidio = 10000
if Quintil == 3:
    if Empleabilidad == "Desempleado":
        Subsidio = 8000
    elif Empleabilidad == "Empleado":
        Subsidio = 6000
if Quintil == 4:
    if Empleabilidad == "Desempleado":
        Subsidio = 0
    elif Empleabilidad == "Empleado":
        Subsidio = 6000
if Quintil == 5:
    Empleabilidad == "Desempleado" or "Empleado"
    Subsidio = 1500

if Quintil in [1, 2]:
    Bono += 2000
    
if Edad >= 60:
    Bono += 3000
    Total = Subsidio + Bono 
print (f"Subsidio: {Subsidio}")
print (f"Bono: {Bono}")
print (f"Total recibido: {Total}")



