""" Depósito de agua con control de nivel y alarma"""

# Importamos el módulo de threads y el de gestón de tiempo 
import threading
import time

# Creamos un mutex mediante el método Lock()
lock = threading.Lock()

# Inicializamos variables globales
tiempo = 0.0
volumen = 0
inicio = 0

# Introducimos los parámetros de ls simulación (se leen como cadenas de caracteres)

tiempoej = int(input("Introduce el tiempo de ejecución: "))
caudal = int(input("Introduce el valor del llenado: "))
vaciado = int(input("Introduce el valor del vaciado: "))
umbral = int(input("Introduce el valor de control: "))

# Ejemplo de lectura segura para detectar que la entrada es un float
try:
    peligro = int(input("Introduce el valor de alarma: "))
    # print(f"El número es: {peligro}")
except ValueError:
    print("Error: Por favor introduce un valor numérico válido.")


# tiempoej_str = 120
# caudal_str = 5
# vaciado_str = 10
# umbral_str = 13
# peligro_str = 21

# # Convertimos los datos leídos a float
# tiempoej = float(tiempoej_str)
# caudal = int(caudal_str)
# vaciado = int(vaciado_str)
# umbral = int(umbral_str)
# peligro = int(peligro_str)

# Asegurarnos de que 'lock' existe y es un threading.Lock válido antes de usarlo
try:
    _tmp = lock
    if not (hasattr(lock, '__enter__') and hasattr(lock, '__exit__')):
        lock = threading.Lock()
except NameError:
    lock = threading.Lock()

# Definimos las funciones a ejecutar por los threads
# Utilizamos un retardo con el tiempo de ejecución periódica para cada tarea

def controldep():
    global tiempo, volumen, umbral, vaciado, datos, lock
    while (tiempo < tiempoej):
        with lock:
            if (volumen > umbral):
                volumen = volumen - vaciado
                print(f"Control: he reducido el volumen a {volumen}")
        time.sleep(2)
        
        
def alarma():
    global tiempo, volumen, peligro, lock
    while (tiempo < tiempoej):
        with lock:
            if (volumen > peligro):
                print(f"Alarma: cuidado, el volumen es: {volumen}")
        time.sleep(1)
      
def llenado():
    global tiempo, tiempoej, volumen, caudal, lock
    while (tiempo < tiempoej):
        with lock:
            volumen = volumen + caudal
            print(f"Llenado : volumen = {volumen}")
        time.sleep(1)
        
               
def reloj():
    global tiempo, inicio, tiempoej
    while (tiempo<tiempoej):
        fin = time.time()
        tiempo = fin - inicio

# Asignamos las funciones a ejecutar a los distintos threads
th_cont = threading.Thread(target=controldep)
th_alar = threading.Thread(target=alarma)
th_llena = threading.Thread(target=llenado)
th_reloj = threading.Thread(target=reloj)

# Medimos tiempo de inicio de la simulación
inicio = time.time()

# Lanzamos los threads
th_reloj.start()
th_llena.start()
th_cont.start()
th_alar.start()

# Esperamos la finalización de cada thread
th_cont.join()
th_alar.join()
th_llena.join()
th_reloj.join()

# Calculamos el tiempo total de ejecución como curiosidad
final = time.time()
tejec = final - inicio
print (f"Tiempo de ejecución: {tejec}")