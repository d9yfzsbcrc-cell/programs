#!/usr/bin/env python2


##############################################################
# Programa desarrollado por T. Javier Robles Prado           #
# Informar bugs o sugerencias a tjavier@usuarios.retecal.es   #
# Visite http://users.servicios.retecal.es/tjavier           #
##############################################################


# Solución a la 2ª práctica de EDI. Curso 2002

#---------------------------
# PRODUCTOS (diccionario)

# El elemento (una lista de 3 elementos) será una parte del diccionario de productos cuya clave es el código

# Código = Clave
# 0.-Descripción
# 1.-Cantidad Disponible
# 2.-Cola de espera
#   2.0.- Cliente
#   2.1.- Cantidad
#----------------------------

#----------------------------
# PRODUCTOS SERVIDOS (lista)
#
# El elemento será una tupla de 3 elementos.
#
# 0.- Código
# 1.- Cliente
# 2.- Cantidad servida
#---------------------------

#---------------------------
# PRODUCTOS EN ESPERA (cola)
#
# El elemento será una lista de 2 elementos
#
# 0.- Cliente
# 1.- Cantidad Requerida
#---------------------------

#---------------------------
# PROVEEDORES (lista)
#
# El elemento será una tupla de 4 elementos
#
# 0.- Proveedor
# 1.- Código de Producto
# 2.- Fecha de recepción
# 3.- Cantidad servida
#---------------------------

import cola_py
import sys

from pickle import load, dump
from string import ljust, rjust, center

# Constantes de los productos
DESCRIPCION  = 0
CANTDISP     = 1
COLA         = 2
# Constantes de los productos servidos
CODIGO       = 0
CLIENTE      = 1
CANTSERV     = 2
# Constantes de la cola de espera
COLA_CLIENTE = 0
COLA_CANTREQ = 1
# Constantes de los proveedores
PROV_NOMBRE  = 0
PROV_CODIGO  = 1
PROV_FECHA   = 2
PROV_CANTIDAD= 3
# Constantes del programa
LECTURA      ='r'
ESCRITURA    ='w'

###################################
#GESTIÓN DE PRODUCTOS
###################################

def NuevoProducto (productos,codigo,cantidad,servidos):

# El elemento será una parte del diccionario de productos cuya clave es el código

# Código = Clave
# 0.-Descripción
# 1.-Cantidad Disponible
# 2.-Cola de espera
#   2.0.- Cliente
#   2.1.- Cantidad

    
    #Producto ya existente
    if ExisteCodigo(productos,codigo):

        #No hay clientes en espera
        if cola_py.EsVacia(productos[codigo][COLA]):

            productos[codigo][CANTDISP] = productos[codigo][CANTDISP] + cantidad

        #Hay clientes en espera    
        else :

            ReparteProducto (productos[codigo][COLA],cantidad,codigo,servidos,productos)

        
    #Producto no existente    
    else:       
   
        s = raw_input('Descripción >> ')      
    
        c = cola_py.CrearCola()

        productos [codigo] = [s,cantidad,c]
    
def ExisteCodigo (productos,codigo):

    return productos.has_key(codigo)


def ReparteProducto (cola,cantidad,codigo,servidos,productos):


    while (cantidad != 0 and not (cola_py.EsVacia(cola))):

        necesario = cola_py.Consultar(cola)

        #Satisfacemos petición
        if cantidad >= necesario[COLA_CANTREQ] :

            #Recalculamos stock y actualizamos la cola 
            cantidad = cantidad - necesario[COLA_CANTREQ]
            cola_py.Quitar(cola)

            #Añadimos a servidos
            servidos.append((codigo,necesario[COLA_CLIENTE],necesario[COLA_CANTREQ]))

        #No satisfacemos la petición en su totalidad     
        else :

            #Recalculamos stock y actualizamos la cola 
            nueva_demanda = necesario[COLA_CANTREQ] - cantidad
            cola_py.Modifica(cola,[necesario[COLA_CLIENTE],nueva_demanda])
            
            #Añadimos a servidos
            servidos.append((codigo,necesario[COLA_CLIENTE],cantidad))

            cantidad = 0

    productos[codigo][CANTDISP] = cantidad
    

####################################
#GESTIÓN DE PEDIDOS (clientes)
####################################

#---------------------------
# PROVEEDORES (lista)
#
# El elemento será una tupla de 4 elementos
#
# 0.- Proveedor
# 1.- Código de Producto
# 2.- Fecha de recepción
# 3.- Cantidad servida
#---------------------------

def NuevaEntrega (productos,entregas,servidos):

    nombre = raw_input ('Nombre del proveedor >> ')
    codigo = input ('Código del producto >> ')
    fecha  = raw_input ('Fecha de Recepción >> ')
    cant   = input ('Cantidad >> ')

    
    entregas.append((nombre,codigo,fecha,cant))

    NuevoProducto (productos,codigo,cant,servidos)
    

####################################
#PROGRAMA PRINCIPAL
####################################

def Inicializa():
    tupla =({},[],[])
    return tupla

def PintarMenu():

    print (2*'\n')
    print 'http://users.servicios.retecal.es/tjavier'
    
    print (2*'\n')
    print center('GESTIÓN 2002', 20)
    print (20*'-'),(2*'\n')

    print 'Introduzca número de opción','\n'
    
    print '1.- ','Nuevo pedido de clientes'
    print '2.- ','Nueva entrega de proveedores'
    print '3.- ','Ver Stock'
    print '4.- ','Ver productos con cola de espera'
    print '5.- ','Ver pedidos pendientes'
    print '6.- ','Ver productos servidos a clientes'
    print '7.- ','Ver entregas de proveedores'
    print '8.- ','Salir'

    print (2*'\n')


def ImprimeCabecera (cadena1,cadena2,cadena3,cadena4=''):

    #Para no compartir el valor del argumento por omisión
    if cadena4 =='' :
        cadena4 =''


    if cadena4 != '':
        print (70*'_')
    else:
        print (3*' '),(61*'_')

    print

    print (3*' '),('|'),ljust(cadena1,8),('|'),ljust(cadena2,8),('|'),center(cadena3,35),('|'),

    if cadena4 != '' :
        print ljust(cadena4,12),('|')
    else:
        print '\n'

    if cadena4 != '':
        print (70*'_')
    else:
        print (3*' '),(61*'_') 

def ImprimeCierre (fecha=''):

    #Para no compartir el valor del argumento por omisión
    if fecha =='' :
        fecha =''
        
    if fecha != '':
        print (70*'_')
    else:
        print (3*' '),(61*'_')

    s=' '

    print (2*'\n')
    
    while (s!=''):
        s = raw_input('Presione INTRO para continuar >> ')
    
    
def ImprimeDatos (codigo,cantidad,cadena,fecha=''):

    #Para no compartir el valor del argumento por omisión
    if fecha =='' :
        fecha =''   
    
    
    print (3*' '),('|'),ljust(repr(codigo),8),('|'),ljust(repr(cantidad),8),('|'),ljust(cadena,35),('|'),
    

    if fecha != '' :
        print ljust(fecha,7),('|')
    else:
        print 


 #   if fecha != '':
 #       print (80*'_')
 #   else:
 #       print (3*' '),(66*'_')   
    
def VerStock (productos):
# Se visualizan los productos presentes en el almacén
# No se visualizan colas de espera de productos

    lista = productos.keys()

    ImprimeCabecera ('Código','Cantidad','Descripción')
    for x in lista:

        #No hay cola de espera (nótese que la cantidad disponible puede ser 0
        if cola_py.EsVacia(productos[x][COLA]):
            ImprimeDatos(x,productos[x][CANTDISP],productos[x][DESCRIPCION])

    ImprimeCierre()

def VerProductosConCola (productos):

    lista = productos.keys()

    ImprimeCabecera ('Código','Cantidad','Descripción')
    for x in lista:

        #No hay cola de espera (nótese que la cantidad disponible puede ser 0
        if not cola_py.EsVacia(productos[x][COLA]):
            ImprimeDatos(x,productos[x][CANTDISP],productos[x][DESCRIPCION])

    ImprimeCierre()


def VerColaProducto(productos):
    
    cod = input ('Introduzca Código de producto >> ')
    if ExisteCodigo(productos,cod):
    
        if cola_py.EsVacia(productos[cod][COLA]):
            print 'No hay clientes en cola para el producto de código',cod
        else:
            ImprimeCabecera('Código','Cantidad','Cliente')
            copia =cola_py.Copiar(productos[cod][COLA])
            while not cola_py.EsVacia(copia):
                c = cola_py.Consultar(copia)
                ImprimeDatos(cod,c[COLA_CANTREQ],c[COLA_CLIENTE])
                cola_py.Quitar(copia)

    else :
        print 'No existe el código',cod
    ImprimeCierre()           
        
    
def VerProductosServidos (servidos):
#Se visualizan los pedidos servidos a los clientes

    ImprimeCabecera ('Código', 'Cantidad', 'Cliente')
    for x in range(len(servidos)):
        ImprimeDatos(servidos[x][CODIGO],servidos[x][CANTSERV],servidos[x][CLIENTE])
    ImprimeCierre()
    

def VerEntregas (entregas):
#Se visualizan las entregas de los servidores

    ImprimeCabecera('Código','Cantidad','Proveedor','Fecha')
    for x in range(len(entregas)):
        ImprimeDatos(entregas[x][PROV_CODIGO],entregas[x][PROV_CANTIDAD],entregas[x][PROV_NOMBRE],entregas[x][PROV_FECHA])
    ImprimeCierre('Fecha')  
    
def run (path = ''):
# path será la ruta del archivo con los datos
# Si no se pasa nada, se da la opción de inicializar o cargar

    #Para no compartir el valor del argumento por omisión
    if path =='' :
        path =''   

    if path == '':
        s = raw_input ('Desea inicializar datos (s/n) >> ')
        if s in ['S','s']:
            tupla = Inicializa()

        else:
            done = 0

            while not done :
                path = raw_input('Ruta de acceso >> ')
                try:
                    f = file(path,LECTURA)

                except IOError:
                    print path,': No se ha podido abrir'
                    s = raw_input ('Salir (s/n) >> ')
                    if s in ['S','s']:
                        sys.exit()

                    continue
                done = 1
    else:
        try:
            f = file(path,LECTURA)

        except IOError:
            print path,': No se ha podido abrir'
            sys.exit()
                

    #Archivo abierto
    try:
        tupla = load(f)
    except:
        print 'Error desestibando'
        sys.exit()

               

    #Tenemos en tupla nuestros datos
    #Los desempaquetamos

    productos,servidos,entregas = tupla
    done = 0
        
    while not done:

        #Pintamos Menú
        PintarMenu()

        dec = raw_input('Número de opción >> ')

        if dec[0] =='1':
            NuevoPedido(productos,servidos)

        elif dec[0] =='2':
            NuevaEntrega(productos,entregas,servidos)

        elif dec[0] =='3':
            VerStock(productos)

        elif dec[0] =='4':
            VerProductosConCola(productos)
            
        elif dec[0] =='5':
            VerColaProducto(productos)

        elif dec[0]=='6':
            VerProductosServidos(servidos)

        elif dec[0]=='7':
            VerEntregas(entregas)
            
        elif dec[0] =='8':
            f=file(path,ESCRITURA)
            tupla = (productos,servidos,entregas)
            dump (tupla,f)
            done = 1
            
        else:
            pass
                
            
# Para ejecutar desde la línea de comandos

if __name__ == '__main__':
    if len(sys.argv) == 2:
            run(sys.argv[1])    
    else:
            run()


