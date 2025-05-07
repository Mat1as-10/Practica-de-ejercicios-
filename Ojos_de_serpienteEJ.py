import random
while True:
    Ojo1 = random.randint (1, 6)
    Ojo2 = random.randint (1, 6)
    Total = (Ojo1 + Ojo2)

    print (f"Dado 1: {Ojo1}, Dado 2: {Ojo2}, Total: {Total}")

    if Total == 2:
        print ("¡Ojos de serpiente!")
        break
    else:
        print ("No, sigue intentando..")

