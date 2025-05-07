Quintil = int(input("Ingresa tu quintil de ingresos (1-5): "))

Estudiante = int(input("Eres estudiante. 1) Si    2) No: "))

Hijos = int(input("Tienes hijos?  1) Si     2) No: "))

Edad = int(input("Ingresa tu edad: "))
Beca = 0
Bono_hijo = 0
Bono_edad = 0

if Quintil == 1:
    if Estudiante == 1:
        Beca = 20000
        if Hijos == 1:
            Bono_hijo = 3000
            if Edad < 18:
                Bono_edad = 2000
                
if Quintil == 1:
    if Estudiante == 2:
        Beca = 0
        if Hijos == 2:
            Bono_hijo = 0
            if Edad > 18:
                Bono_edad = 0
if Quintil == 2:
    if Estudiante == 1:
        Beca = 15000
        if Hijos == 1:
            Bono_hijo = 3000
            if Edad < 18:
                Bono_edad = 2000
if Quintil == 2:
    if Estudiante == 2:
        Beca = 0
        if Hijos == 2:
            Bono_hijo = 0
            if Edad > 18:
                Bono_edad = 0
if Quintil == 3:
    if Estudiante == 2:
        Beca = 10000
        if Hijos == 1:
            Bono_hijo = 3000
            if Edad < 18:
                Bono_edad = 2000
if Quintil == 3:
    if Estudiante == 1:
        Beca = 0
        if Hijos == 2:
            Bono_hijo = 0
            if Edad > 18:
                Bono_edad = 0
if Quintil == 4:
    if Estudiante == 1:
        Beca = 5000
        if Hijos == 1:
            Bono_hijo = 3000
            if Edad < 18:
                Bono_edad = 2000
if Quintil == 4:
    if Estudiante == 2:
        Beca = 0
        if Hijos == 2:
            Bono_hijo = 0
            if Edad > 18:
                Bono_edad = 0 
if Quintil == 5:
    if Estudiante == 1 or Estudiante == 2:
        Beca = 2000
        if Hijos == 1:
            Bono_hijo = 3000
            if Edad < 18:
                Bono_edad = 2000
    else:
        print ("error")

Total = (Beca + Bono_hijo + Bono_edad)

print (f"Beca: {Beca} ")
print (f"Bono hijo: {Bono_hijo}")
print (f"Bono edad: {Bono_edad}")
print (f"Total: {Total}")