"""
Script para graficar los resultados del PID
"""

import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('/home/rafa/Documentos/Programas/python/pid/data_pid.txt', skiprows=1)
i, referencia, error, accontrol, salida = data.T

fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

axs[0].plot(i, referencia, label='Referencia', linewidth=2)
axs[0].plot(i, salida, label='Salida', linewidth=2)
axs[0].set_ylabel('Valor')
axs[0].set_title('Referencia y Salida')
axs[0].legend()
axs[0].grid(True)

axs[1].plot(i, error, label='Error', linewidth=2)
axs[1].plot(i, accontrol, label='Acción de Control', linewidth=2)
axs[1].set_xlabel('Iteración')
axs[1].set_ylabel('Valor')
axs[1].set_title('Error y Acción de Control')
axs[1].legend()
axs[1].grid(True)

plt.tight_layout()
plt.savefig('pid_plot.png')
plt.show()