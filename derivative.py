import numpy as np
import matplotlib.pyplot as plt
from cubicSplines import cubicInterpolationmatrix

def f1(x, dx, S, xi, yi):
    
    if x <= xi[0]:
        i = 0
    elif x >= xi[-1]:
        i = len(xi) - 2
    else:
        i = 0
        while x > xi[i]:
            i += 1
        i -=1
    xdx1, xdx2 = x+dx, x-dx
    fdx1 = (S[i*4][0]*(xdx1**3))+(S[(i*4)+1][0]*(xdx1**2))+(S[(i*4)+2][0]*xdx1)+S[(i*4)+3][0]
    fdx2 = (S[i*4][0]*(xdx2**3))+(S[(i*4)+1][0]*(xdx2**2))+(S[(i*4)+2][0]*xdx2)+S[(i*4)+3][0]
    return (fdx1-fdx2)/(2*dx)
    
if __name__ == "__main__":
    x1 = [0,25,50,75,100,125,150,175,200]
    y1 = [10.6, 16, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]
    S = cubicInterpolationmatrix(x1, y1)
    print(f1(20, 0.1, S, x1, y1))
