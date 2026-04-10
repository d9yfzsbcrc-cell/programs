"""
Ejemplo 1: Respuesta al escalón de un sistema discreto
"""

# Import the packages needed for the examples included in this notebook
import numpy as np
import matplotlib.pyplot as plt

# Import the python-control package
try:
    import control as ct
    print("python-control", ct.__version__)
except ImportError:
    import control as ct

# Definición de la fdt del sistema

T = 0.5
num1 = [1]
den1 = [1, -0.5]

sys1 = ct.tf(num1, den1, T)
print(sys1)

resp1 = ct.step_response(sys1)
resp1.plot()
plt.plot(resp1.time, resp1.outputs)
# frequency_response(sys).plot()
# nyquist_response(sys).plot()
# pp.streamlines(sys, limits).plot()
# root_locus_map(sys).plot()