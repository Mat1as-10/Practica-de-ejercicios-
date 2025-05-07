Nombre = (input("Ingresa tu nombre: "))
print(f"Bienvenido {Nombre} en que te puedo ayudar.. Tengo estas opciones para ti: ")

print ("1. Seguros automoviles")

print ("2. Seguros hogar")

print ("3. Seguros medicos")

print ("4. Salir")
Eleccion = int(input("Ingresa tu eleccion (1, 2, 3, 4): "))

if Eleccion == 1:
    print (input("Escribe la patente de tu vehiculo y un agente se contactara contigo ---- Patente: "))
elif Eleccion == 2:
    print (input("Escribe tu direccion y un agente se pondra en contacto contigo ---- Direccion: "))
elif Eleccion == 3:
    print (input("Ingresa tu Isapre, luego un doctor se pondra en contacto contigo ---- Isapre: "))
elif Eleccion == 4:
    print ("Que tengas exclente dia, Gracias por contactarte con nosotros!")
else:
    print ("Codigo invalido..")

