import numpy as np
import matplotlib.pyplot as plt
name_list = ['rune', 'riz', 'marcus', 'brage']
time_diff = np.array([])
for name in name_list:
    data = np.genfromtxt(f'timer_output_{name}.dat', delimiter=' 	   ')
    t = data[1:, 1]
    time_diffs = t[1:] - t[:-1]
    time_diff = np.append(time_diff, time_diffs)

H_mass = np.array([3.001, 3.001, 3.012, 3.001]) / 100  # height of pendulum mass [m]
sigma_H_mass = np.array([0.001 for _ in range(4)]) / 100
L = np.array([18.504, 18.504, 18.506, 18.506, 18.504, 18.506, 18.504, 18.504])  # first 4 are before, last 4 after experiment [m]
sigma_L = np.array([1, 2, 1, 1, 1, 1, 1, 1]) / 1000  # [m]


sigma_t = 0.25
sigma_t_diff = 2 * sigma_t

#  weighted mean of H_mass
H_mass_weighted = np.sum(H_mass / sigma_H_mass**2) / np.sum(1 / sigma_H_mass**2)
#  weighted mean of L
L_mean_weighted = np.sum(L / sigma_L**2) / np.sum(1 / sigma_L**2) - H_mass_weighted / 2
sigma_L_weighted = np.sqrt(sigma_L.mean()**2 + sigma_H_mass.mean()**2 / 4)

g_values = L_mean_weighted * (2 * np.pi / time_diff)**2
g_sigma = np.sqrt((2 * np.pi / time_diff)**4 * sigma_L_weighted**2 + (L_mean_weighted * 8 * np.pi**2 / time_diff**3)**2 * sigma_t_diff**2)
g_mean = g_values.mean()
g_mean_sigma = g_sigma.mean() / len(g_sigma)
print(f'g = {g_mean:.3f} $\pm$ {g_mean_sigma:.3f}')

# plt.plot(np.arange(0, len(time_diff), 1), time_diff - np.mean(time_diff), '.')
plt.hist(time_diff - np.mean(time_diff), bins=np.linspace(-0.3, 0.3, 15), density=True)
print(f'bias: {np.mean(time_diff - np.mean(time_diff))}')
plt.show()