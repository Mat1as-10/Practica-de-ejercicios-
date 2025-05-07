Palabra = input("Ingresa una palabra:")
Vocales = "aeiouAEIOU"
Contador = 0

for letra in Palabra:
    if letra in Vocales:
        Contador += 1

print (f"La palabra {Palabra} tiene {Contador} vocales")
