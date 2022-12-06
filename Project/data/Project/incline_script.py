import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(t, a, b):
    return 1/2*t**2 + a*t + b

data = np.genfromtxt(r'incline_data\small_LR_20.csv', delimiter=',', skip_header=15)
t, gate_val = data[:, 0], data[:, 1]

sample_rate = t.sum() / t[-1]
dt = 1 / sample_rate  # timestep between each sample


"""
Several ways of determining the balls acceleration:

calculate the time a sensor spends in the activated state: t_active = D_ball / v_ball -> plot v(t) give no. of
datapoints equal to no. of sensors. Assumes constant velocity when during active sensor state, which is wrong, but if
the d_ball << l_rail it is a decent approximation.

"""

d_ball = 0.01275  # 2cm
sig_b = 0.00005  # pm 1mm

state_voltage = 2.1

active_samples = t[gate_val > 0]
state_times = np.array([])
for i in range(len(t)-1):
    if (gate_val[i] < state_voltage) & (gate_val[i+1] > state_voltage):
        state_times = np.append(state_times, t[i+1])
    elif (gate_val[i] > state_voltage) & (gate_val[i+1] < state_voltage):
        state_times = np.append(state_times, t[i])

# print(state_times)

active_intervals = state_times[1::2] - state_times[::2]
velocity = d_ball / active_intervals  # m/s

" sig_v^2 = t_active^-2 * sig_b^2 + (d_ball / t_active^2)^2 * (dt / 2)^2"
sig_v = (active_intervals**-2 * sig_b**2 + (d_ball / active_intervals**2)**2 * (dt / 2)**2)**0.5

# print(sig_v)
"""
plt.errorbar(state_times[::2] + active_intervals / 2, velocity, xerr=dt / 2, yerr=sig_v, fmt='.')
plt.ylabel('v [m/s]')
plt.xlabel('t [s]')
"""
gate_pos = np.array([18.7, 36.40, 54.55, 73.45, 91.20]) / 100

popt, cov = curve_fit(func, state_times[::2], gate_pos)


plt.plot(state_times[::2], gate_pos, '.')
x = np.linspace(0, 1, 100)
plt.plot(x, func(x, *popt))
print(*popt)

# print(velocity)
# plt.plot(active_samples, gate_val[gate_val > 0], '.')
plt.show()
