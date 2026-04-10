
# Módulo para adivinar números

import random

def adivina():

    #Se escoge un número entre 1 y 100

    incog = random.choice(range(100)) + 1

    decision = 0
    dist_antes = 0
    intentos = 0

    print("Adivina el número entre 1 y 100 ")

    while decision != incog :

        intentos = intentos + 1
        num = input ("Introduce tu número > ")
        decision = int(num)
        if (decision != incog) :

            #No hemos acertado

            #Veamos como de lejos estamos
            dist_act = abs(incog - decision)

            #Veamos si estamos fr�o o caliente

            if (dist_antes == 0):
                print ("Vuelve a intentarlo... ")
            elif (dist_antes > dist_act):
                print ("Caliente caliente")
            elif (dist_antes < dist_act):
                print ("Frío frío")
            else:
                print ("Estás como estabas")

            dist_antes = dist_act 

        #Fin del if
    #Fin del while

    print ("Felicidades! Lo has hecho en",intentos,"intentos.")


if __name__=='__main__':
    adivina()
    print()
    input("Pulse Intro >")

else:
    print ("Módulo adivina importado.")
    print ("Para ejecutarlo, teclee: adivina.adivina()")
    print ("Para recargar después de cambios al código, teclee reload(adivina)") 