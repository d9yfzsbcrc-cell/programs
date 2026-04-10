# Primer ejemplo de simulación de systemas dinámicos de control con el package 'control'
# https://python-control.readthedocs.io/en/0.10.2/examples/python-control_tutorial.html

# Import the packages needed for the examples included in this notebook
import numpy as np
import matplotlib.pyplot as plt

# Import the python-control package
try:
    import control as ct
    print("python-control", ct.__version__)
except ImportError:
    import control as ct

# Define the parameters for the system
m, c, k = 1, 0.1, 2
# Create a linear system
A = np.array([
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [-2*k/m, k/m, -c/m, 0],
    [k/m, -2*k/m, 0, -c/m]
])
B = np.array([[0], [0], [0], [k/m]])
C = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])
D = 0

sys = ct.ss(A, B, C, D, outputs=['q1', 'q2'], name="coupled spring mass")
print(sys)

response = ct.initial_response(sys, X0=[1, 0, 0, 0])
cplt = response.plot()

# Plot the outputs of the system on the same graph, in different colors
t = response.time
x = response.states
plt.plot(t, x[0], 'b', t, x[1], 'r')
plt.legend(['$x_1$', '$x_2$'])
plt.xlim(0, 50)
plt.ylabel('States')
plt.xlabel('Time [s]')
plt.title("Initial response from $x_1 = 1$, $x_2 = 0$");

#plt.savefig('initial_response.pdf')

for X0 in [[1, 0, 0, 0], [0, 2, 0, 0], [1, 2, 0, 0], [0, 0, 1, 0], [0, 0, 2, 0]]:
  response = ct.initial_response(sys, T=20, X0=X0)
  response.plot(label=f"{X0=}")

#plt.savefig('multiple_initial_responses.pdf')

cplt = ct.step_response(sys).plot()

step_info = ct.step_info(sys)
print("Input 0, output 0 rise time = ",
      step_info[0][0]['RiseTime'], "seconds\n")
#step_info

stepresp = ct.step_response(sys)
cplt = stepresp.plot(plot_inputs=True)

#plt.savefig('step_response_with_inputs.pdf')

# Plot the inputs on top of the outputs
cplt = stepresp.plot(plot_inputs='overlay')

#plt.savefig('step_response_overlay.pdf')

# Look at the "shape" of the step response
print(f"{stepresp.time.shape=}")
print(f"{stepresp.inputs.shape=}")
print(f"{stepresp.states.shape=}")
print(f"{stepresp.outputs.shape=}")

T = np.linspace(0, 50, 500)
U1 = np.cos(T)
U2 = np.sin(3 * T)

resp1 = ct.forced_response(sys, T, U1)
resp2 = ct.forced_response(sys, T, U2)
resp3 = ct.forced_response(sys, T, U1 + U2)

# Plot the individual responses
resp1.sysname = 'U1'; resp1.plot(color='b')
resp2.sysname = 'U2'; resp2.plot(color='g')
resp3.sysname = 'U1 + U2'; resp3.plot(color='r');

#plt.savefig('forced_responses.pdf')

# Show that the system response is linear
cplt = resp3.plot(label="G(U1 + U2)")
cplt.axes[0, 0].plot(resp1.time, resp1.outputs[0] + resp2.outputs[0], 'k--', label="G(U1) + G(U2)")
cplt.axes[1, 0].plot(resp1.time, resp1.outputs[1] + resp2.outputs[1], 'k--')
cplt.axes[2, 0].plot(resp1.time, resp1.inputs[0] + resp2.inputs[0], 'k--')
cplt.axes[0, 0].legend(loc='upper right', fontsize='x-small');

#plt.savefig('linearity_check.pdf')

# Show that the forced response from non-zero initial condition is not linear
X0 = [1, 0, 0, 0]
resp1 = ct.forced_response(sys, T, U1, X0=X0)
resp2 = ct.forced_response(sys, T, U2, X0=X0)
resp3 = ct.forced_response(sys, T, U1 + U2, X0=X0)

cplt = resp3.plot(label="G(U1 + U2)")
cplt.axes[0, 0].plot(resp1.time, resp1.outputs[0] + resp2.outputs[0], 'k--', label="G(U1) + G(U2)")
cplt.axes[1, 0].plot(resp1.time, resp1.outputs[1] + resp2.outputs[1], 'k--')
cplt.axes[2, 0].plot(resp1.time, resp1.inputs[0] + resp2.inputs[0], 'k--')
cplt.axes[0, 0].legend(loc='upper right', fontsize='x-small');

#plt.savefig('non_linearity_check.pdf')

# Manual computation of the frequency response
resp = ct.input_output_response(sys, T, np.sin(1.35 * T))

cplt = resp.plot(
    plot_inputs='overlay',
    legend_map=np.array([['lower left'], ['lower left']]),
    label=[['q1', 'u[0]'], ['q2', None]])

# Gain and phase for the simulation above
from math import pi
G = ct.tf(sys)
val = G(1.35j)
print(f"{G(1.35j)=}")
print(f"Gain: {np.absolute(val)}")
print(f"Phase: {np.angle(val)}", " (", np.angle(val) * 180/pi, "deg)")

# Gain and phase at s = 0 (= steady state step response)
print(f"{G(0)=}")
print("Final value of step response:", stepresp.outputs[0, 0, -1])

freqresp = ct.frequency_response(sys)
cplt = freqresp.plot()

#plt.savefig('frequency_response_manual.pdf')

cplt = ct.bode_plot(sys, overlay_outputs=True)

#plt.savefig('bode_plot.pdf')