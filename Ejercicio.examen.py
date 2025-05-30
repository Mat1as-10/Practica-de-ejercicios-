# El susuario debe ingresar una temperatura en un rango de -50 a 50 grados centigrdos
# Dado que el usuario pueda ingresar cualquier dato (incluos cadena de texto), se puede usar manejo de excepcion para evitar que el programa se detenga
# 1. si el dato ingresado no es numero entero, el programa debe mostrar el siguiente mensaje: ERROR: DEBE INGRESAR UN NUMERO ENTERO VALIDO Y REPETIR HASTA QUE SEA VALIDO
# 2. si el usuario ingresa un numero entero fuera del rango informarle al usuario ERROR: TEMPERATURA FUERA DEL RANGO PERMITIDO EL RANGO ES DE -50 A 50 GRADOS CENTIGRADOS 
# hasta que el usuario ingresebien el dato
# 3. si el usuario introduce los datos correctamente temperatura registrada exitosamente 
# debe tener una opcion para solicitar la salida del programa, al salir del programa debe mostrar un mensaje que diga "cierre del programa hasta luego!"
while True:
    try:
        entrada = input("Ingrese la temperatura en un rango de (-50 - 50) o escriba 'salir' para terminar: ").strip()
        if entrada.lower() == "salir":  # Verifica si el usuario quiere salir
            print("CIERRE DEL PROGRAMA, HASTA LUEGO.")
            break
        temperatura = int(entrada)  # Convierte la entrada a entero si no es "salir"
        if -50 <= temperatura <= 50:
            print("Temperatura registrada con éxito.")
            break
        else:
            print("ERROR: TEMPERATURA FUERA DEL RANGO PERMITIDO. EL RANGO ES DE -50 A 50 GRADOS CENTÍGRADOS.")
    except ValueError:
        print("ERROR: DEBE INGRESAR UN NÚMERO ENTERO VÁLIDO O LA PALABRA 'SALIR'.")




