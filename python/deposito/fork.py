import os

# Bifurcación del proceso
pid = os.fork()

if pid == 0:
    # Este código se ejecuta en el proceso hijo
    print(f"Hijo: PID {os.getpid()}, Padre: {os.getppid()}")
else:
    # Este código se ejecuta en el proceso padre
    print(f"Padre: {os.getpid()}, Hijo creado con PID: {pid}")
