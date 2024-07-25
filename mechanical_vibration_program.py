# -*- coding: utf-8 -*-
"""Mechanical Vibration Program

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18MC3YiJkVphNHzzDaPZfn_OgWYf3tvvp
"""

import math
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Inputs
m = float(input("In kg, what is the mass of the oscillating weight?: "))
c = float(input("In Ns/m, what is the damping coefficient of the damper?: "))
k = float(input("In N/m, what is the spring constant of the spring?: "))
i1 = float(input("In m, what is the initial displacement of the weight from equilibrium?: "))
i2 = float(input("In m/s, what is the initial velocity of the weight?: "))

# Discriminant of Characteristic Equation to Determine Vibration Type
dsc = c * c - 4 * m * k
if c == 0:
    osctype = "Undamped Mechanical Vibration"
    print(f"The system is an {osctype} system.")
else:
    if dsc > 0:
        osctype = "Overdamped Mechanical Vibration"
        print(f"The system is an {osctype} system.")
    elif dsc < 0:
        osctype = "Underdamped Mechanical Vibration"
        print(f"The system is an {osctype} system.")
    elif dsc == 0:
        osctype = "Critically Damped Mechanical Vibration"
        print(f"The system is a {osctype} system.")

# Differential equation solver function
def equation(t, y):
    x, v = y
    dxdt = v
    dvdt = -(c/m) * v - (k/m) * x
    return [dxdt, dvdt]

# Initial conditions
y0 = [i1, i2]

# Time span for the solution
t_span = (0, 10)  # from t=0 to t=10 seconds
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # 1000 time points for evaluation

# Solve the ODE
sol = solve_ivp(equation, t_span, y0, t_eval=t_eval)

# Plotting the results
plt.figure(figsize=(5, 6))
plt.plot(sol.t, sol.y[0], label='Displacement (m)')
plt.plot(sol.t, sol.y[1], label='Velocity (m/s)')
plt.title('Mechanical Vibration System Response')
plt.xlabel('Time (s)')
plt.ylabel('Response')
plt.legend()
plt.grid()
plt.show()
