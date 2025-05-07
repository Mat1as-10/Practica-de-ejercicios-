import random

print("=== Juego de Adivinanza Ajustada ===")

# Paso 1: Ingreso del rango
numero1 = int(input("Ingresa el primer número (menor): "))
numero2 = int(input("Ingresa el segundo número (mayor): "))

if numero1 < numero2:
    # Paso 2: Generación del número aleatorio
    numero_aleatorio = random.randint(numero1, numero2)
    ajustado = round(numero_aleatorio / 4) * 4

    # Paso 3: Intentos del usuario
    intento1 = int(input("Adivina el número ajustado (intento 1 de 3): "))
    if intento1 == ajustado:
        print("¡Felicitaciones! Adivinaste el número.")
    else:
        if intento1 < ajustado:
            pista1 = "El número es mayor que tu intento."
        else:
            pista1 = "El número es menor que tu intento."
        print(f"{pista1}")

        intento2 = int(input("Intenta nuevamente (intento 2 de 3): "))
        if intento2 == ajustado:
            print("¡Bien hecho! Lo lograste en el segundo intento.")
        else:
            if intento2 < ajustado:
                pista2 = "El número sigue siendo mayor."
            else:
                pista2 = "El número sigue siendo menor."
            print(pista2)

            intento3 = int(input("Último intento (intento 3 de 3): "))
            if intento3 == ajustado:
                print("¡Justo a tiempo! Adivinaste en el último intento.")
            else:
                print("Perdiste, el número era:", ajustado)
else:
    print("Error: el primer número debe ser menor que el segundo.")