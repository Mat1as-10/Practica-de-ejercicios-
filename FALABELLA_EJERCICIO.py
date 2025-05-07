Usuarios = {
    "Marco": 1500,
    "Joseluis": 2500,
    "Sebastian" :300
    }

def obtener_niveles(puntos):
    niveles = []

    if puntos >= 1000:
        niveles.append("Nivel Premium (25% de descuento)")
    if puntos >= 500:
        niveles.append("Nivel Oro (10% descuento)")
    if puntos >= 250:
        niveles.append("Premios especiales (audifonos, manos libres, relojes, etc)")

    return niveles

for nombre, puntos in Usuarios.items():
    print(f"Usuario: {nombre}")
    print(f"Puntos acumulados: {puntos}")

    niveles = obtener_niveles(puntos)
    if niveles:
        print ("Niveles alcanzados: ")
        for i, nivel in enumerate(niveles, start=1):
            print (f" Nivel {i}: {nivel}")
    else: 
        print("Aun no ha alcanzado ningun nivel con beneficios. ¡Sifue comprando con nosotros para obtener recompensas!")

    print ("¡Gracias por preferir a Falabella! Sigue comprando y canjea increibles beneficios.")
    print ("-" * 50)