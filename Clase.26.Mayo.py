#Se solicita desarrollar un programa en Python que permita calcular el área de varios triángulos.
#Para esto se le solicita al usuario cuantos triángulos desea procesar.
#Luego, por cada triangulo, se debe ingresar la base y la altura, ambos valores positivos y reales (Es decir, pueden tener decimales).
#El Area de un triangulo se calcula con la siguiente formula 
#AREA = BASE * ALTURA / 2 
#Si su usuario ingresa un valor invalido se debe mostrar un mensaje de ERROR 
 
while True:
    try:
        cantidad_triangulos = int(input("ingresa cuantos triangulos quieres calcular: "))
        if cantidad_triangulos <= 0:
            print ("ingresa un numero positivo")
        else:
            for i in range (1, cantidad_triangulos + 1):
                print (f"\nTriangulo {i}")
                try:
                    base = float(input("Ingresa la base: "))
                    altura = float(input("Ingresa la altura: "))
                    if base <= 0 or altura <= 0:
                        print ("ingresa un numero valido.")
                    else:
                        area = base * altura /2
                        print (f"el area de un el triangulo {i} es: {area}")
                        break
                except ValueError:
                    print("ERROR")
    except ValueError:
        print("ingresa un numero entero.")

    