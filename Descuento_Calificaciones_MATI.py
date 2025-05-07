def descuento ():
    
    Nombre = (input("Bienvenido ingresa tu nombre: "))
    Nota = float(input(f"Bienvenido {Nombre}, ingresa tu calificacion: "))

    if Nota >= 6.0:
        print ("Felicitaciones, as obtenido un descuento del 20%")
    elif Nota >= 5.0:
        print ("Bien, has obtenido un descuento del 15%")
    elif Nota >= 4.0:
        print ("Has aprobado y tienes un descuento del 5%")
    elif Nota <= 3.9:
        print ("Has reprobado, sigue intentandolo...")
    else:
        print ("No identificable.")


descuento()
