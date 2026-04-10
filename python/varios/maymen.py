#!/usr/bin/python2

##############################################################
# Programa desarrollado por T. Javier Robles Prado           #
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es  #
# Visite http://users.servicios.retecal.es/tjavier           #
##############################################################

#Módulo adivina2, otra variante del juego de adivinar un número
#Esta vez pasamos el rango de la incognita como parámetro

import random

def adv2(n):

    #Obtengamos la incógnita
    x = random.choice(range(n)) + 1

    int = 0
    sel = 0

    while (sel != x):
        int = int + 1

        sel = input("Introduzca número > ")

        if (sel > x):
            print "Prueba uno más pequeño..."
        elif (sel < x) :
            print "Prueba uno más grande..."
        else:
            print "Felicidades, lo has hecho en",int,"intentos"


if __name__=='__main__':
    adv2(n)
    print
    raw_input("pulse Intro >")
else:
    print "Módulo adivina2 importado."
    print "Para ejecutarlo, teclee adivina2.adv2(n), donde n es un numero que vd. elija"
    print "Para recargar despues de cambios teclee reload(adivina2)"

