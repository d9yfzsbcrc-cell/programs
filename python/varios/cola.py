#!/usr/bin/env python2

##############################################################
# Programa desarrollado por T. Javier Robles Prado           #
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es   #
# Visite http://users.servicios.retecal.es/tjavier           #
##############################################################


# Implementación del TAD COLA en Python

def CrearCola() :

    c=[]
    
    return c

def EsVacia(c):

    return (c==[])

def Poner (cola, elto):

    return cola.insert(0,elto)

def Copiar (cola):

    copia=CrearCola()

    for x in cola:
        
        copia.append(x)

    return copia

def Quitar(cola):

    cola.remove(cola[len(cola)-1])

def Consultar (cola):

    return cola[len(cola)-1]

def Modifica (cola, elto):

    cola[len(cola)-1] = elto
    

