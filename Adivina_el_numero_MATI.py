# Desarrolla un programa en python que permita generar un numero aleatorio 
# Dentro de un rango definido por el usuario y ajustarlo dividiendolo por 4 
# Luego, el usuario deberia adivinar el numero en un maximo de intentos de 3
# Condiciones del juego: 
# 1. Ingreso de dato: 
# A) El usuario ingresa dos numeros entero que presentan el rango numerico 
# B) El primer número debe ser menor al segundo 
# 2. Generacion de números aleatorios 
# A) Se elige un numero aleatorio dentro de un rango ingresado
# B) El numero se ajusta dividiendolo entre 4 y redondeandolo al multilplo de 4 mas cercano 
# 3. Intentos del usuario
# A) Primero intento: Si el usuario acierta se muestra un mensaje de felicitacion
# B) Segundo intento: Si el usuario no acierta se le indica si el numero es mayor o menor 
# C) Tercer intento: Si no acierta nuevamente se le da otra pista 
# D) Resultado final: Si no acierta en los tres intentos el programa muestra el mensaje "perdiste, el número era..."
# E) importar libreria random

import random
print ("Bienvenido a la ruleta de la suerte, deberas ingresar dos numeros enteros el primero menor que el segundo! Veamos si adivinas!!")

Numero_menor = int(input("Ingresa el primer numero del rango (menor): "))
Numero_mayor = int(input("Ingresa el segundo numero del rango (mayor): "))

if Numero_menor < Numero_mayor:
    Numero_aleatorio = random.randint(Numero_menor, Numero_mayor)
    Ajustado = round(Numero_aleatorio / 4) * 4

    Intento1 = int(input("Adivina el numero (intento 1-3): "))
    if Intento1 == Ajustado:
        print (" Felicitaciones! Adivinaste el numero!")
    else:
        if Intento1 < Ajustado:
            Pista1 = "El numero es mayor que tu intento"
        else:
            Pista1 = "El numero es menor que tu intento"
            print(f"{Pista1}")

            Intento2 = int(input("Intenta nuevamente (intento 2-3): "))
            if Intento2 == Ajustado:
                print (" Bien echo! Has adivinado el numero en el segundo intento!")
            else: 
                if Intento2 < Ajustado:
                    Pista2 = "El numero sigue siendo mayor"
                else:
                    Pista2 = "El numero sigue siendo menor"
                    print (Pista2)
            Intento3 = int(input("Ultimo intento (3-3): "))
            if Intento3 == Ajustado:
                print ("Muy bien! has acertado en el ultimo intento! Felicidades!!")
            else:
                print (f"Perdiste, el numero era {Ajustado}") 

else:
    print ("Error.")                       
