import random

Num1 = int(input("Ingresa un número (menor): "))
Num2 = int(input("Ingresa un número (mayor): "))

if Num1 < Num2:
    Numero_aleatorio = random.randint(Num1, Num2)
    Adivina = round(Numero_aleatorio / 5) * 5

    Intento1 = int(input("Primer intento - (1-4): "))
    if Intento1 == Adivina:
        print("Felicidades, has acertado.")
    else:
        if Intento1 < Adivina:
            Pista1 = "El número es mayor"
        else:
            Pista1 = "El número es menor"
        print(Pista1)

        Intento2 = int(input("Segundo intento - (2-4): "))
        if Intento2 == Adivina:
            print("Felicidades, has acertado en el segundo intento!")
        else:
            if Intento2 < Adivina:
                Pista2 = "El número sigue siendo mayor"
            else:
                Pista2 = "El número sigue siendo menor"
            print(Pista2)

            Intento3 = int(input("Tercer intento - (3-4): "))
            if Intento3 == Adivina:
                print("Felicitaciones, has acertado en el tercer intento!")
            else:
                if Intento3 < Adivina:
                    Pista3 = "Sigue siendo mayor"
                else:
                    Pista3 = "Sigue siendo menor"
                print(Pista3)

                Intento4 = int(input("Último intento - (4-4): "))
                if Intento4 == Adivina:
                    print("Uf, en el último intento has acertado... ¡Suerte!")
                else:
                    print(f"Fallaste, el número era: {Adivina}")
else:
    print("El primer número debe ser menor.")
