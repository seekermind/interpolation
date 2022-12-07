import matplotlib.pyplot as plt
import numpy as np

def lagrangeInterpolate(x, xi, fi):
    result = 0
    for i in range(len(xi)):
        g = fi[i]
        for j in range(len(xi)):
            if i == j:
                continue
            g *= (x - xi[j])/(xi[i] - xi[j])
        result += g
    return result

x = np.array([0.33,
        1,
        2.2,
        4.7])

f = np.array([107.99,
        93.46,
        85.96,
        75.43])
x1 = [0, 25, 50, 75, 100, 125, 150, 175, 200]
f1 = [10.6, 16, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]


plt.plot(x, f, 'bo', label='experimental data')
xAxis = np.arange(x[0]+0.01,x[-1],0.1)
plt.plot(xAxis, lagrangeInterpolate(xAxis, x, f), 'r--', label='interpolated data')
plt.legend()
plt.show()

