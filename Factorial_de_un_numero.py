#Escribir una función que reciba un número entero positivo y devuelva su factorial.
import math

def factorial():
    while True:
        numero = int(input("Ingresa un numero para devolverte su factorial: "))
        print (math.factorial(numero))
        pregunta = input("Deseas consultar otro numero? (SI - NO): ").upper()
        if pregunta == "SI":
            return factorial()
        else:
            print ("Cerrando programa...!")
            break

factorial()
     