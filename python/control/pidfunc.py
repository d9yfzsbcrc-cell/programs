""" Funciones para el control PID"""


import matplotlib.pyplot as plt 

tsim = 15                  # Tiempo de simulación en segundos
T = 0.1                     # Período de muestreo
numiter = int(tsim/T)-2     # Número de iteraciones para la simulación
u = 1                       # Entrada escalón unitario
entrada = []
error = []
errorc = []
accont = []
salida = []
salcont = []

def simula(ym1, ym2, em1, em2):
    for i in range(numiter):
        y = (1.81*ym1)-(0.817*ym2)+(0.007*em1)+(0.0066*em2)
        e = u - ym1
        entrada.append(u)
        error.append(e)
        salida.append(y)

        # Reasignamos las variables
        em2 = em1
        em1 = e
        ym2 = ym1
        ym1 = y

    

def sim_control(ym1, ym2, em1, em2, acm1, acm2, ec):
    global salcont
    for i in range(numiter):
        ec = u - ym1
        c = acm1+(18.86*ec)-(31.4396*em1)+(12.7663*em2)
        y = (1.81*ym1)-(0.817*ym2)+(0.007*acm1)+(0.0066*acm2)
        #entrada.append(u)
        errorc.append(ec)
        accont.append(c)
        salcont.append(y)

        # Reasignamos las variables
        em2 = em1
        em1 = ec
        acm2 = acm1
        acm1 = c
        ym2 = ym1
        ym1 = y

    
def dibuja(graf):

    #plt.clear()
    ejex = []
    longitud_datos = len(salida)
    for i in range(0, longitud_datos):
        ejex.append(i)

    if graf == 1:
        longitud_datos = len(salida)
        eti_sal = 'Salida'
        eti_ref = 'Referencia'
        color_sal = 'blue'
        color_ref = 'red'
        style_sal = 'solid'
        style_ref = 'solid'
        title_sal = 'Salida sin PID'
        xlabel_sal = f'Muestras (T = {T} seg.)'
        ylabel_sal = 'y(k)'
        ejey_sal = salida
        ejey = entrada 
        plt.figure(figsize=(12, 8))

    if graf == 2:
        longitud_datos = len(salcont)
        eti_sal = 'Salida'
        eti_ref = 'Referencia'
        color_sal = 'blue'
        color_ref = 'red'
        style_sal = 'solid'
        style_ref = 'solid'
        title_sal = 'Salida con PID'
        xlabel_sal = f'Muestras (T = {T} seg.)'
        ylabel_sal = 'y(k)'
        ejey_sal = salcont
        ejey = entrada
        plt.figure(figsize=(12, 8))

    if graf == 3:
        longitud_datos = len(salcont)
        eti_sal = 'Salida sin PID'
        eti_ref = 'Salida con PID'
        color_sal = 'blue'
        color_ref = 'red'
        style_sal = 'solid'
        style_ref = 'solid'
        title_sal = 'Comparacón con/sin PID'
        xlabel_sal = f'Muestras (T = {T} seg.)'
        ylabel_sal = 'y(k)'
        ejey = salcont
        ejey_sal = salida
        plt.figure(figsize=(12, 8))
        plt.plot(ejex, entrada, label='Referencia', color='green', linestyle='solid')


    plt.plot(ejex, ejey_sal, label=eti_sal, color=color_sal, linestyle=style_sal)
    plt.plot(ejex, ejey, label=eti_ref, color=color_ref, linestyle=style_ref)
    plt.title(title_sal)
    plt.xlabel(xlabel_sal)
    plt.ylabel(ylabel_sal)
    plt.legend() # Muestra la leyenda
    plt.grid(True) # Añade una cuadrícula

    # 4. Mostrar la gráfica
    plt.show()        