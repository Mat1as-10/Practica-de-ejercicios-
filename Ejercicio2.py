capacidad_de_estacionamiento = 0
vehiculos_totales_estacionados = 0
recaudacion_total_dia = 0
estacionamientos_disponiles = capacidad_de_estacionamiento - vehiculos_totales_estacionados

AUTOS = 3000
MOTOS = 1500
CAMIONETAS = 4000


autos = 0
motos = 0
camionetas = 0

print ("** ADMINISTRACION **")
while True:
    try:
        capacidad_de_estacionamiento = int(input("Ingrese capacidad del estacionamiento: "))
        if capacidad_de_estacionamiento > 0:
            break
        else:
            print ("Ingresa un numero mayor a 0 ")
            
    except ValueError:
        print ("Ingrese numeros para la capacidad del estacionamiento.")
        continue

while True:
    print (" MENU ")
    print ("[1]. Registrar entrada de vehiculos.")
    print ("[2]. Registrar salida de vehiculos.")
    print ("[3]. Visualizar estado del estacionamiento.")
    print ("[4]. Reporte general del estacionamiento.")
    print ("[5]. Salir")

    try:

        opcion = int(input("Ingrese una opcion (1 - 5): "))
    except ValueError:
        print ("Debe ingresar solo numeros enteros en la opcion.")
        continue

    if opcion == 1:
        
        estacionamientos_utilizados = autos + motos + camionetas

        if estacionamientos_utilizados >= capacidad_de_estacionamiento:
            print ("Estacionamiento lleno.")
            continue

        print ("~~ TIPOS DE VEHICULOS ~~")
        print (f"[1]. AUTOS --  ${AUTOS} / HORA ")
        print (f"[2]. MOTOS -- ${MOTOS} / HORA")
        print (f"[3]. CAMIONETAS -- ${CAMIONETAS} / HORA")

        try:
            tipo_vehiculo = int(input("Que tipo de vehiculo vas a ingresar (1 -- 3): "))
            if tipo_vehiculo < 1 or tipo_vehiculo > 3:
                print ("Opcion invalida. Debes ingresar una opcion dentro del rango ( 1 -- 3 )")
                continue
            if tipo_vehiculo == 1:
                autos += 1
            elif tipo_vehiculo == 2:
                motos += 1
            else:
                camionetas += 1
        except ValueError:
            print ("Ingrese numeros en el tipo de vehiculo.")

    
    elif opcion == 2:
        estacionamientos_utilizados = autos + motos + camionetas
        if estacionamientos_utilizados == 0:
            print ("No hay vehiculos en el estacionamiento.")
            continue 
        
        print ("~~ TIPOS DE VEHICULOS ~~")
        print (f"[1]. AUTOS --  ${AUTOS} / HORA ")
        print (f"[2]. MOTOS -- ${MOTOS} / HORA")
        print (f"[3]. CAMIONETAS -- ${CAMIONETAS} / HORA")

        try:
            tipo_vehiculo = int(input("Ingresa el tipo de vehiculo que deseas sacar: "))
            if tipo_vehiculo < 1 or tipo_vehiculo > 3:
                print ("Ingresa un numero dentro de las opciones validas (1 -- 3)")
                continue
            if tipo_vehiculo == 1 and autos == 0:
                print ("NO HAY AUTOS ESTACIONADOS.")
                continue
            elif tipo_vehiculo == 2 and motos == 0:
                print ("NO HAY MOTOS ESTACIONADAS.")
                continue
            elif tipo_vehiculo == 3 and camionetas == 0:
                print ("NO HAY CAMIONETAS ESTACIONADAS.")
                continue
                
        except ValueError:
            print ("NO puedes ingresar textos, solo puedes ingresa numeros dentro del rango (1 -- 3) en la opcion para sacar vehiculos.")

        try:
            horas_estacionamiento = int(input("Ingrese el tiempo estacionado en horas: "))
            if horas_estacionamiento < 0:
                print ("El tiempo ingresado debe ser mayor a 0 ")
                continue
            if tipo_vehiculo == 1:
                autos -= 1
                pago = horas_estacionamiento * AUTOS
            elif tipo_vehiculo == 2:
                motos -= 1
                pago = horas_estacionamiento * MOTOS
            else: 
                camionetas -= 1
                pago = horas_estacionamiento * CAMIONETAS

            vehiculos_totales_estacionados += 1 
            recaudacion_total_dia += pago               
            
            print ("~~ BOLETA ~~")
            if tipo_vehiculo == 1:
                print ("TIPO DE VEHICULO : AUTO ")
            elif tipo_vehiculo == 2:
                print ("TIPO DE VEHICULO : MOTO ")
            else:
                print("TIPO DE VEHICULO : CAMIOENTAS ")

            print (f"Horas estacionado/a: {horas_estacionamiento} ")
            print (f"Total a pagar: ${pago}")


        except ValueError:
            print ("Error, debe ingresar numeros enteros en el ingreso de horas de estacionamiento (numero entero).")
            continue    
            


    elif opcion == 3:
        estacionamientos_utilizados = autos + motos + camionetas
        estacionamientos_disponiles = capacidad_de_estacionamiento - estacionamientos_utilizados

        print (f"ESTACIONAMIENTOS UTILIZADOS: {estacionamientos_utilizados}")
        print (f"ESTACIONAMIENTOS DISPONIBLES: {estacionamientos_disponiles}")
        print (f"CAPACIDAD MAXIMA DEL ESTACIONAMIENTO: {capacidad_de_estacionamiento}")
        print (f"ESTACIONAMIENTOS UTILIZADOS POR AUTOS: {autos}")
        print (f"ESTACIONAMIENTOS UTILIZADOS POR MOTOS: {motos}")
        print (f"ESTACIONAMIENTOS UTILIZADOS POR CAMIONETAS: {camionetas}")
        
    elif opcion == 4:
        print ("Reporte general del estacionamiento:")
        print (f"Vehiculos totales estacionados en el dia: {vehiculos_totales_estacionados} ")
        print (f"El total recaudado en el dia es de: {recaudacion_total_dia}")
    
    elif opcion == 5:
        print ("Muchas gracias por estacionar con nosotros! que tengas exclenete viaje!")
        break
    else: 
        print ("La opcion ingresada no es valida.")


