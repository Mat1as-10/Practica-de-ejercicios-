Quintil = int(input("Ingresa tu Quintil de ingresos (1-5): "))
Empleabilidad = int(input(" 1) Empleado  2) Desempleado: "))
Edad = int(input("Ingresa tu edad: "))

Subsidio = 0
Bono = 0
Bono_adicional = 0

if Quintil == 1 or 2:
    Bono = 2000
    if Empleabilidad == 2:
        Subsidio = 15000
        if Edad > 65:
            Bono_adicional = 3000
if Quintil == 1 or 2:
    Bono = 2000
    if Empleabilidad == 1:
        Subsidio = 10000
        if Edad > 65:
            Bono_adicional = 3000

if Quintil == 3:
    Bono = 0
    if Empleabilidad == 2:
        Subsidio = 8000
        if Edad > 65:
            Bono_adicional = 3000
    if Empleabilidad == 1:
        Subsidio = 0
        if Edad > 65:
            Bono_adicional = 3000

if Quintil == 4:
    Bono = 0
    if Empleabilidad == 1:
        Subsidio = 6000
        if Edad > 65: 
            Bono_adicional = 3000
    if Empleabilidad == 2:
        Subsidio = 0
        if Edad > 65:
            Bono_adicional = 3000

if Quintil == 5:
    Bono = 0
    if Empleabilidad == 1 or 2:
        Subsidio = 1500
        if Edad > 65:
            Bono_adicional = 3000 


Subsidio_total = Subsidio + Bono + Bono_adicional

print (f"Subsidio: {Subsidio}")
print (f"Bono: {Bono}")
print (f"Bono Especial: {Bono_adicional}")
print (f"Subsidio final: {Subsidio_total}")