#!/usr/bin/env python
'''Ejemplo del uso de expresiones regulares en Python.'''
__shell_usage__ = ''' Este es un programa de ejemplo. Busca en fichero HTML dado
como argumento, todas las marcas de html y las pone en minusculas y saca el 
resultado por pantalla.'''
__version__ = 'Ejemplo de uso de expresiones regulares'
__author__='Arturo Suelves (arturosa@lycos.es)'
import os,sys
import string,re
def Mm(fentrada):
    flectura=open(fentrada,'r')
    f=flectura.read()
    flectura.close()
    coincidencias1=re.findall("[\n][^<]*[>]",f)
    #Busca todas las marcas html desde el principio de la linea nueva al final
    coincidencias2=re.findall("[<][^>]*[\n]",f)
    #Busca todas las marcas html desde el principio de la linea al final de la linea
    coincidencias3=re.findall("[<].*[>]",f)
    #Busca todas las marcas html que van en una linea
    resultado=f
    for i in coincidencias1:
        busca=re.search(i,resultado)
        if busca:
            p1=busca.start()
            p2=busca.end()
            resultado1=resultado[:p1]
            resultado2=resultado[p2:]
            anadido=string.lower(f[p1:p2])
            resultado=resultado1+anadido+resultado2
    for i in coincidencias2:
        busca=re.search(i,resultado)
        if busca:
            p1=busca.start()
            p2=busca.end()
            resultado1=resultado[:p1]
            resultado2=resultado[p2:]
            anadido=string.lower(f[p1:p2])
            resultado=resultado1+anadido+resultado2
    for i in coincidencias3:
        busca=re.search(i,resultado)
        if busca:
            p1=busca.start()
            p2=busca.end()
            resultado1=resultado[:p1]
            resultado2=resultado[p2:]
            anadido=string.lower(f[p1:p2])
            resultado=resultado1+anadido+resultado2 
    return resultado
if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] != '':
            print (Mm(sys.argv[1]))

 