# Cálculo de los n primeros valores de la serie de Fibonacci
"""Calcula los n primeros valores de la serie de Fibonacci."""

import matplotlib.pyplot as graf
import time
n = 100
salida = []

def fibiter(n): # Escribe n números de Fibonacci
    """Escribe n números de Fibonacci (versión iterativa)."""
    global salida
    a,b = 0,1           #Asignación múltiple      
    for x in range(n):  #Creamos una secuencia 1,2,...,n con range
        #print(b, end = " ")        # Escribimos en una sola línea
        salida.append(b) 
        a, b = b, a+b
    return salida

def fibrec(n):
    """Escribe n números de Fibonacci (versión recursiva)."""
    if (n < 2):
        return n
    else:
                return fibrec(n-1) + fibrec(n-2)

inicio = time.time()

fibiter(n)
#fibrec(n)

fin = time.time()
print(salida)
print(fin - inicio)
# Representamos gráficamente

graf.plot(salida, label = "Evolución serie de Fibonacci")
graf.xlabel("Iteración")
graf.ylabel("Valor")
graf.title("Serie de Fibonacci")
graf.legend()

graf.show()

# plt.show(block=False): En Matplotlib, esto muestra la gráfica pero permite que el script continúe ejecutándose,
# ideal para refrescar datos dentro de un bucle.
# plt.show(block=True) (por defecto): Bloquea hasta que cierras la ventana.
# plt.close(): Es importante para limpiar la ventana anterior si estás actualizando la gráfica dentro de un bucle. 