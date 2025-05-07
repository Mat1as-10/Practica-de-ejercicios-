Quintil = int(input("Ingresa el nivel de tu quintil (1-3): "))
Empleabilidad = int(input("Estas -- 1) Empleado    2) Desempleado  : "))
Edad = int(input("Ingresa tu edad: "))

Subsidio = 0
Bono_Edad = 0

if Quintil == 1 or 2 and Empleabilidad == 2 and Edad < 18:
    Subsidio = 50000 
    Bono_Edad = 15000
else: 
    if Quintil == 1 or 2 and Empleabilidad == 1 and Edad > 18:
        Subsidio = 0 
        Bono_Edad = 0

        if Quintil == 3 and Empleabilidad == 2 and Edad < 18:
            Subsidio = 25000 
            Bono_Edad = 8000
        else:
            Subsidio = 2000 
            Bono_Edad = 0

Total = Subsidio + Bono_Edad

print (f"Subsidio: {Subsidio}")
print (f"Bono Edad: {Bono_Edad}")
print (f"El total es: {Total}")
