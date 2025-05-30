#Construye un programa en Python que le permita registrar los libros prestados en una biblioteca 
# y que le permita contar cuales fueron prestados por mas de 15 días.
#Primero deben ingresar la cantidad de libros a registrar
#Este numero debe ser entero
#Luego, para cada libro, se debe pedir el titulo de libro y la cantidad de días a prestar. 
#El programa debe indicar si el libro tiene préstamo por mas de 15 días o préstamo por menos de 15 días, al final, 
# se debe mostrar cuantos libros tienen mas de 15 días de préstamo y cuantos no. 
#Todos los datos numéricos deben ser verificados con try except

while True:
    try:
        cantidad_libros_registrar = int(input("Ingresa la cantidad de libros que quieres registrar: "))
        if cantidad_libros_registrar <= 0:
            print ("DEBE SER MAYOR A 0")
            continue
        else:
            break
    except ValueError:
        print ("ingresa numeros enteros positivos para registar la cantidad de libros.")
        continue 

libros = []  # Lista vacía para guardar los libros

try:
    cantidad = int(input("¿Cuántos libros deseas registrar?: "))
    
    for i in range(cantidad):
        print(f"\n Libro {i + 1}:")
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        año = input("Año de publicación: ")

        libro = {
            "Título": titulo,
            "Autor": autor,
            "Año": año}

        libros.append(libro)  # Agregar el libro a la lista

    print("\n✅ Registro completado. Libros guardados:\n")
    for libro in libros:
        print(f"- {libro['Título']} por {libro['Autor']} ({libro['Año']})")

except ValueError:
    print("❌ Error: Debes ingresar un número válido para la cantidad.")




