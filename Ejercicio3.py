#Construya un programa en Python que permita gestionar un programa simple de ventas para una fonda que presente al usuario los siguientes productos
#Empanadas de pino: $ 2.000
#Empanadas de queso: $ 1.500
#Choripanes: $ 2.500
#Terremotos: $ 1.000
#Por su compra mayor a $ 10.000 recibe un descuento del 25% 
#Por su compra mayor a $ 20.000 recibe un descuento del 40%
#Y finalmente por su compra si es mayor a las dos anteriores tu entrada es gratis 

EMPANADA_PINO = 2000
EMPANADA_QUESO = 1500
CHIRIPANES = 2500
TERREMOTO = 1000

empana_pino = 0
empanada_queso = 0
choripan = 0
terremoto = 0

descuento10 = 0.25
descuento20 = 0.40

total = empana_pino + empanada_queso + choripan + terremoto


while True:

    print ("~~ Bienvenido a nuestra fonda ~~")
    print ("[1] Empanada de pino: $2.000 ")
    print ("[2] Empanada de queso: $1.500 ")
    print ("[3] Choripan: $2.500 ")
    print ("[4] Terremoto: $1.000 ")
    print ("[5] Finalizar compra ")
    
    try:
        entrada = int(input("Ingresa una opcion: "))
        if entrada < 1 or entrada > 5:
            print ("Debes ingresar una alternativa dentro del rango (1 - 4).")
    except ValueError:
        print ("ERROR. SOLO SE ACEPTAN NUMEROS POSITIVOS")
        continue
    try:

        if entrada == 1:
            cantidad_pino= int(input("Cuantas empanadas de pino deseas: "))
            if cantidad_pino <= 0:
                print ("ingresa un numero mayor a 0")
            else:
                empana_pino = cantidad_pino * EMPANADA_PINO
    except ValueError:
        print ("Ingresa un numero positivo")
        continue
    try:
        
        if entrada == 2:
            cantidad_queso = int(input("Cuantas empanadas de queso deseas: "))
            if cantidad_queso <= 0:
                print ("ingresa un numero mayor a 0")
            else:
                empanada_queso = cantidad_queso * EMPANADA_QUESO
    except ValueError:
        print ("Ingresa un numero para la opcion")
        continue
    try:

        if entrada == 3:
            cantidad_choripan = int(input("Cuantos choripanes deseas: "))
            if cantidad_choripan <= 0:
                print ("Ingresa un numero mayor a 0")
            else:
                choripan = cantidad_choripan * CHIRIPANES
    except ValueError:
        print ("imposible cuantificar esa cantidad, ingresa un numero entero.")
        continue
    try:

        if entrada == 4:
            cantidad_terremoto = int(input("Cuantos terremotos deseas: "))
            if cantidad_terremoto <= 0:
                print ("Ingresa una cantidad mayor a 0")
            else:
                terremoto = cantidad_terremoto * TERREMOTO
    except ValueError:
        print ("Imposible cuantificar esa cantidad, ingresa numeros enteros positivos. ")

    
    if entrada == 5:
        if total > 10000:
            descuento = total * (1 - descuento10 )
        elif total > 20000:
            descuento = total * (1 - descuento20)

        total = empana_pino + empanada_queso + choripan + terremoto
        print ("BOLETA")
        print (f"TOTAL: {total * (1 - descuento)} ")
       
       


    
    

       

    
        
