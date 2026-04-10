
# Programa del contrrol de un depósito con threads y tiempo

import threading
import time
import matplotlib.pyplot as plt

# Mutex
lock = threading.Lock()

# Almacenamiento de datos
datos = []

# Definición de variables globales
tiempo = 0.0
volumen = 0

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
            datos.append(volumen)
            print(f"Llenado : volumen = {volumen}")
        time.sleep(1)
        
        
        
def reloj():
    global tiempo, inicio, tiempoej
    while (tiempo<tiempoej):
        fin = time.time()
        tiempo = fin - inicio
        #print(tiempo)
    

th_cont = threading.Thread(target=controldep)
th_alar = threading.Thread(target=alarma)
th_llena = threading.Thread(target=llenado)
th_reloj = threading.Thread(target=reloj)


tiempoej_str = input("Introduce el tiempo de ejecución: ")
caudal_str = input("Introduce el valor del llenado: ")
vaciado_str = input("Introduce el valor del vaciado: ")
umbral_str = input("Introduce el valor de control: ")
peligro_str = input("Introduce el valor de alarma: ")


# Conversiones
tiempoej = float(tiempoej_str)
caudal = int(caudal_str)
vaciado = int(vaciado_str)
umbral = int(umbral_str)
peligro = int(peligro_str)



inicio = time.time()
#print(inicio)


th_reloj.start()
th_llena.start()
th_cont.start()
th_alar.start()

# Esperar a que terminen

th_cont.join()
th_alar.join()
th_llena.join()
th_reloj.join()

final = time.time()
tejec = final - inicio
print (f"Tiempo de ejecución: {tejec}")

print("¡Fin del programa!")

# Representar los datos
longitud_datos = len(datos)
ejex = []
for i in range(0, longitud_datos):
    ejex.append(i)

# print(len(datos))
# print(len(ejex))

plt.figure(figsize=(12, 8)) # Opcional: Define el tamaño de la figura
plt.plot(ejex, datos, label='Volumen de líquido', color='blue', linestyle='solid') # Dibuja la línea

# 3. Personalizar (opcional)
plt.title('Control depósito')
plt.xlabel('Muestras (T = 0.7 seg.)')
plt.ylabel('Volumen (l.)')
plt.legend() # Muestra la leyenda
plt.grid(True) # Añade una cuadrícula

# 4. Mostrar la gráfica
plt.show()        
