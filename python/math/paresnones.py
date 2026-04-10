#!/usr/bin/python2

##############################################################
# Programa desarrollado por T. Javier Robles Prado           #
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es   #
# Visite http://users.servicios.retecal.es/tjavier           #
##############################################################

#Modulo que implementa el juego de pares y nones

import string 
import rand

def run():

    n = input ("Cuántos juegos quiere jugar >> ")
    a=[]    # Una lista vacia
            # Almacenará una secuencia de 0 y 1 ( victorias y derrotas )
    for x in range(n):
        a.append(jugar_juego())

    estadisticas(a)
    

def imprime(n):
                  #Imprime quién ha ganado

     if (n==0):
         print string.center("Jugador",18)
     else:
         print string.center("Ordenador",18)


def estadisticas(a):


    ganadas = 0
    
    print """PARTIDA       GANADOR""" 
    for x in range(len(a)):
        y = x + 1 
        print string.center(`y`,8),
        imprime(a[x])
        if (a[x]==0):
            ganadas = ganadas + 1
        
    
    porc = ((ganadas * 1.0) / len(a)) * 100

    print "Has ganado el",porc,"% de las partidas."

    

      

def jugar_juego():

# Salida:

# 0 -> gana jugador
# 1 -> gana ordenador

    dec = raw_input("Pares o nones >> ")

   

    #Convenio: pares = 0 y nones = 1

    if (dec[0] == 'p' or dec==[0] == 'P'):
        dec = 0
    else:
        dec = 1

    #Sacar números    
             
    com = rand.choice(range(11))
    dedos = input("Saca dedos >> ")
     

    #Comparamos

    jugada = com + dedos

    print "Has sacado",dedos,"dedos y el ordenador ha sacado",com
    
    if (jugada % 2 == dec) :  
        print "Has ganado"
        return 0
    else:
        print "Perdiste, gana el ordenador"
        return 1



# Ejecutar independientemente el script

if __name__=='__main__':
    run()
    print
    raw_input("pulse Intro >")
else:
    print "Módulo paresnones importado."
    print "Para ejecutarlo, teclee paresnones.run()."
    print "Para recargar despues de cambios teclee reload(paresnones)"

