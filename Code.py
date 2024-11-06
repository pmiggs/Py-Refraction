import numpy as np
import matplotlib.pyplot as plt
"""
Input values:
"""
N = 2                                # number of indices
theta_init = 15
"""
Given values:
"""
n_N = [1.00, 1.30]
while len(n_N) < N:
    n_New = n_N[0] + 0.30/N
    n_N.insert(0, n_New)
n_N.sort()

y_N = [0, 1]
while len(y_N) <= len(n_N):
    y_New = y_N[0] + 1/len(n_N)
    y_N.insert(0, y_New)
y_N.sort(reverse = True)

x_N = [0]


"""
Solving for theta_N
"""
theta_rad = [np.radians(theta_init)]

for i in range(len(n_N)-1):
    theta_next = np.arcsin(n_N[i] * np.sin(theta_rad[i]) / n_N[i+1])
    theta_rad.append(theta_next)

theta_N = [round(np.degrees(j), 2) for j in theta_rad]

"""
Solving for x_N
"""
for k in range(len(theta_N)):
    x_next = x_N[k] + (y_N[k] - y_N[k+1]) * np.tan(theta_rad[k])
    x_N.append(x_next)
    
"""
Outputs
"""
print("x_N =", x_N)
print("y_N =", y_N)
print("theta_N =", theta_N)

plt.plot(x_N, y_N, marker='.')
plt.show()
