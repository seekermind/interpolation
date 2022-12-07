import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as sc

""" 
# I wanted to compare this with the code i wrote for cubic spline
from cubicSplines import cubicInterpolate
from cubicSplines import cubicInterpolationmatrix """

x = [82.7, 112.5, 140, 151, 159, 168.1, 175.5, 185.2, 198.4, 209.6, 228.8, 237.4, 242.4, 246.5, 250.6, 251.9, 256.4, 261.1, 265.3, 277.1, 285.3, 295.9, 322.6, 348.4, 370.4, 383.7, 393.0, 401.2, 411.5, 423, 450.1, 485.4, 525, 574.7, 641, 727, 819.7, 900, 970, 1136, 1220, 1421, 1923]
y = [1.50, 2.0, 2.45, 2.64, 2.79, 2.96, 3.10, 3.29, 3.52, 3.72, 4.02, 4.11, 4.14, 4.17, 4.19, 4.20, 4.19, 4.17, 4.15, 4.04, 3.92, 3.80, 3.47, 3.20, 3.01, 2.92, 2.83, 2.77, 2.71, 2.63, 2.47, 2.27, 2.09, 1.90, 1.7, 1.48, 1.32, 1.20, 1.10, 0.946, 0.894, 0.765, 0.575]


#this function calculates necessary coefficients, k is order of curve(k=3 for cubic, default=3)
cof = sc.splrep(x, y, k=4, s=0)
x_cs = np.arange(x[0]+0.001, x[-1], 0.01)
# this function interpolates values using coefficient calculated by previous function
y_cs = sc.splev(x_cs, cof)


""" 
# I wanted to compare this with the code i wrote for cubic spline
S = cubicInterpolationmatrix(x, y)
y_my = [cubicInterpolate(i, S, x, y) for i in x_cs]
plt.plot(x_cs, y_my, 'g--', label='my spline') """


plt.plot(x, y, 'bo', label='data')
plt.plot(x_cs, y_cs, 'r-', label='spline')
plt.legend()
plt.show()


