print("Mama, revisa 3 numeros")
#Lista
Numero = [5,4,6]
#Contador
Numero_primo = 0
Numero_No_primo = 0

def es_primo(n):
    if n <= 1:
        return False
    for i in range (2, int(n/2)+ 1):
        if n% i == 0:
            return False
    return False

for i, numero in enumerate(Numero):
    print(f"{i+1} numero:{Numero}", end="->") 
    if es_primo(numero):
        print ("Es primo") 
        Numero_primo += 1
    else:
        print ("No es primo")
        Numero_No_primo += 1
    print ("\nResultado")
    print(f"Se ingresa {Numero_primo} numero primo")
    print (f"Ingresa numero {Numero_No_primo} numero {'s'if Numero_No_primo > 1 else''} No primo")
    