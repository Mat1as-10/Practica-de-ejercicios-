# Entradas del usuario
quintil = int(input("Ingresa tu quintil de ingresos (1-5): "))
estudiante = int(input("¿Eres estudiante? 1) Sí  2) No: "))
hijos = int(input("¿Tienes hijos? 1) Sí  2) No: "))
edad = int(input("Ingresa tu edad: "))

# Inicializamos valores
beca = 0
bono_hijo = 0
bono_edad = 0

# Cálculo de beca según quintil y condición
if quintil == 1 and estudiante == 1:
    beca = 20000
elif quintil == 2 and estudiante == 1:
    beca = 15000
elif quintil == 3 and estudiante == 2:
    beca = 10000
elif quintil == 4 and estudiante == 1:
    beca = 5000
elif quintil == 5:
    beca = 2000  # Aplica para cualquier condición

# Bonos adicionales
if hijos == 1:
    bono_hijo = 3000
if edad < 18:
    bono_edad = 2000

# Total
total = beca + bono_hijo + bono_edad

# Salida
print(f"Beca: ${beca}")
print(f"Bono por hijos: ${bono_hijo}")
print(f"Bono por edad: ${bono_edad}")
print(f"Total a recibir: ${total}")