# El programa debe comenzar permitiendo ingresar un numero que seria el numero de personas que vas a registrar este numero deberia ser entero.
# Luego se debe registrar cada paciente con sus datos (Nombre, direccion,rut)
# Tambien debe solicitar informacion al paciente, como vacunas que posee, alguna otra enfermedad que padezca y alergias 
# En el caso de no responder alguna pregunta debe decir en un mensaje esquema incompleto 
# Una vez ingresada toda la informacion el programa debe mostrar la informacion obtenida
# Nota importante: cada ingreso debe manejarse con una excepcion 
# Debe preguntar hasta que se cumpla la entrega de la informacion correctamente 
# Por ultimo solicitar un numero para salir y al salir entregar un mensaje de despedida
while True:
    try:
        numero_personas = int(input("Cuantos pacientes deseas ingresar: "))
        if numero_personas <= 0:
            print ("Ingresa un numero sobre 0")
            continue
        elif numero_personas > 0:
            print ("Registro exitoso")
    except ValueError:
        print ("Ingresa Numeros.")
        continue

    
    nombre = input("Nombre: ").lower()
    if nombre.strip() == "": 
        print ("Esquema incompleto")
        continue
      
    try:
        rut = int(input("Rut: "))
        if rut == "":
            print ("Esquema incompleto.")
            continue
    except ValueError:
        print ("Ingresa solo numeros.")
        continue

    try:
        direccion = input("Direccion: ").lower()
        if direccion.strip() == "":
            print ("Esquema incompleto.")
            continue
    except ValueError:
        print ("Ingresa texto.")
        continue

    try:
        enfermedades = input("Tienes alguna enfermedad (SI - NO): ").lower()
        if enfermedades.strip() == "":
            print ("Esquema incompleto.")
            continue
        elif enfermedades.lower() == "si":
            ingreso_enfermedades = input("Ingresa tus enfermedades: ").lower()
            if ingreso_enfermedades.lower() == "":
                print ("Ingresa tus enfermedades.")
                continue
    except ValueError:
        print ("Ingresa texto.")

        try:
            alergias = input("Alergico a algo (SI - NO): ").lower()
            if alergias.strip() == "":
                print ("Esquma incompleto.")
                continue 
            elif alergias.lower() == "si":
                ingreso_alergias = input("Ingresa a que eres alergico: ")
        except ValueError:
            print ("Ingresa texto.")





