import random

Numero1 = int(input("ingresa el primer numero (menor): "))
Numero2 = int(input("ingresa el segundo numero (mayor): "))

if Numero1 < Numero2:
    # Asegurarse de que el rango incluya solo múltiplos de 4
    Minimo = (Numero1 + 3) // 4 * 4  # Primer múltiplo de 4 mayor o igual a Numero1
    Maximo = Numero2 // 4 * 4        # Último múltiplo de 4 menor o igual a Numero2

    if Minimo > Maximo:
        print("No hay múltiplos de 4 en el rango especificado.")
    else:
        Ajustado = random.choice(range(Minimo, Maximo + 1, 4))  # Generar un múltiplo de 4

        Intento1 = int(input("Adivina el numero oculto! Tienes 3 intentos (1-3): "))
        if Intento1 == Ajustado:
            print("Felicidades, acertaste a la primera!!")
        else:
            if Intento1 < Ajustado:
                Pista1 = "El numero es mayor que tu intento."
            else:
                Pista1 = "El numero es menor que tu intento."
            print(Pista1)

            Intento2 = int(input("Segundo intento, Vamos tu puedes (2-3): "))
            if Intento2 == Ajustado:
                print("Felicidades, lo has adivinado en tu segundo intento!!")
            else:
                if Intento2 < Ajustado:
                    Pista2 = "El numero sigue siendo mayor."
                else:
                    Pista2 = "El numero sigue siendo menor."
                print(Pista2)

                Intento3 = int(input("Ultimo intento (3-3): "))
                if Intento3 == Ajustado:
                    print("Felicidades! En el ultimo intento lo has adivinado.")
                else:
                    print(f"Has fallado. El numero era {Ajustado}")

