import random
print("**** Adivina el número ****")

num1 = int(input("Ingresa un número (menor): "))
num2 = int(input("Ingresa un segundo número (mayor): "))

if num1 < num2:
    numero_aleatorio = random.randint(num1, num2)
else:
    print("El primer número debe ser menor que el segundo.")
    exit()

# Primer intento
intento1 = int(input("Ingresa tu primer intento: "))
if intento1 == numero_aleatorio:
    print("¡Felicidades! Has acertado en el primer intento.")
    exit()
elif intento1 < numero_aleatorio:
    print("Tu número es menor.")
elif intento1 > numero_aleatorio:
    print("tu num es mayor")
else:
    print("hubo un error.")

# Segundo intento
intento2 = int(input("Ingresa tu segundo intento: "))
if intento2 == numero_aleatorio:
    print("¡Felicidades! Lo has conseguido en tu segundo intento.")
    exit()
elif intento2 < numero_aleatorio:
    print("Sigue siendo menor.")
else:
    print("Sigue siendo mayor.")

# Tercer intento
intento3 = int(input("Tercer y último intento... ¡vamos, tú puedes!: "))
if intento3 == numero_aleatorio:
    print("¡Uff... lo has conseguido en tu tercer intento!")
else:
    print(f"Has fallado... el número era {numero_aleatorio}.")