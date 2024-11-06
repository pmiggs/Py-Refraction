import numpy as np
import matplotlib.pyplot as plt
"""
Given values:
"""
n_N = [1.00, 1.30]
theta_init = 15
y_N = [0, 1, 1/len(n_N)]
x_N = [0]

"""
Solving for y_N
"""
while len(y_N) <= len(n_N):
    y_N.append(y[-1] + 1/len(n_N))
y_N.sort(reverse = True)

"""
Solving for theta_N
"""
theta_rad = [np.radians(theta_init)]

for i in range(len(n_N)-1):
    theta_next = np.arcsin(n_N[i] * np.sin(theta_rad[i]) / n_N[i+1])
    theta_rad.append(theta_next)

theta_N = [round(np.degrees(j)) for j in theta_rad]

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

plt.plot(x_N, y_N, marker='o')
plt.show()
