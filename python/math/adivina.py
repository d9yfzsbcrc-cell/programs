#!/usr/bin/python2

##############################################################
# Programa desarrollado por T. Javier Robles Prado           #
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es   #
# Visite http://users.servicios.retecal.es/tjavier           #
##############################################################

# Modulo adivina3, el ordenador adivina un numero dado por el usuario
# en un rango tambien dado por el usuario.

print "Modulo adivina3 importado."
print "Para ejecutarlo, teclee: adivina3.adv3(n,rango)"
print "Para recargar despues de cambios al codigo, teclee reload(adivina3)"

def adv3(n,rango):

    int = 0
    busqueda = 0   
    inf,sup = 0, rango

    if (n > rango):
        print """El primer argumento ha de ser menor que el segundo.
Se intercambiaran sus valores."""
        aux=n
        n=rango
        rango=n
    
 
    while (n != busqueda) :
        
        busqueda = (inf + sup) / 2
        int = int + 1

        if ( n > busqueda ):
            inf = busqueda + 1
        elif (n < busqueda):
            sup = busqueda - 1
        else:
            print "Numero encontrado en",int,"intentos."
                       
