# Funciones necesarias para la simulación del depósito

import time
tiempo = 0.0
tiempoej = 20.0
volumen = 0
caudal = 0
def controldep():
    global tiempo, volumen, umbral, vaciado, datos, lock, tiempoej
    while (tiempo < tiempoej):
        with lock:
            if (volumen > umbral):
                volumen = volumen - vaciado
                print(f"Control: he reducido el volumen a {volumen}")
        time.sleep(0.5)
        
        
def alarma():
    global tiempo, volumen, peligro, lock, tiempoej
    while (tiempo < tiempoej):
        with lock:
            if (volumen > peligro):
                print(f"Alarma: cuidado, el volumen es: {volumen}")
        time.sleep(0.25)
      
def llenado():
    global tiempo, tiempoej, volumen, caudal, lock, tiempoej
    while (tiempo < tiempoej):
        with lock:
            volumen = volumen + caudal
            print(f"Llenado : volumen = {volumen}")
        time.sleep(0.25)
        
               
def reloj():
    global tiempo, inicio, tiempoej
    while (tiempo<tiempoej):
        fin = time.time()
        tiempo = fin - inicio