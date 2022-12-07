import matplotlib.pyplot as plt
import numpy as np


def polyFit(x, y, degree):
    summationX = np.zeros((2 * degree))
    summationXY = np.zeros((degree + 1))

    for i in range(2 * degree):
        for xi in x:
            summationX[i] += xi**(i + 1)
    for i in range(degree + 1):
        for xi, yi in zip(x, y):
            summationXY[i] += yi * xi**i

    coefficient_matrix = np.zeros((degree + 1, degree + 1))

    l = degree * 2
    for i in range(degree + 1):
        ii = l
        for j in range(degree + 1):
            coefficient_matrix[i][j] += [summationX[ii - 1]]
            ii = ii - 1
        l = l - 1

    coefficient_matrix[-1][-1] = len(x)
    constant_matrix = np.flip(summationXY)

    coefficients = np.linalg.solve(coefficient_matrix, constant_matrix)

    def polynomial(X):
        Y = 0
        for j, c in enumerate(np.flip(coefficients)):
            Y += c * X**j
        return Y

    return polynomial


x = [1, 4, 7, 11, 15, 20, 30, 50, 77, 92, 100]
y = [5, 20, 52, 121, 228, 403, 903, 2504, 5929, 8464, 10005]

fit = polyFit(x, y, 2)

xfit = np.arange(0, 100, 0.1)
yfit = fit(xfit)

plt.plot(x, y, 'bo', label='data points')
plt.plot(xfit, yfit, 'r--', label='Polynomial Fit')
plt.xlabel("x axis ")
plt.ylabel("y axis")
plt.title("Least Square Method")
plt.legend()
plt.show()
