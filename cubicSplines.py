import matplotlib.pyplot as plt
import numpy as np

def cubicInterpolationmatrix(xi, yi):
    
    n = len(xi)
    A = np.zeros(((4*(n-1)),(4*(n-1))))
    B = np.zeros((4*(n-1),1))

    r = 0
    for i in range(n-1):
        p = 3
        for j in range((4*i),((4*i)+4)):
            A[r][j] = xi[i]**p 
            p -=1
        B[r] = yi[i]
        r += 1

    for i in range(n-1,0,-1):
        p = 3
        for j in range((i*4)-4, (i*4)):
            A[r][j] = xi[i]**p
            p -= 1
        B[r] = yi[i]
        r +=1

    for i in range(1,n-1):
        p = 3 
        for j in range(((i-1)*4), ((i-1)*4)+3):
            A[r][j] = p*(xi[i]**(p-1))
            p -= 1
        p = 3
        for j in range(((i-1)*4)+4, ((i-1)*4)+7):
            A[r][j] = -p*(xi[i]**(p-1))
            p -= 1
        r += 1

    for i in range(1,n-1):
        p = 3
        for j in range(((i-1)*4), ((i-1)*4)+2):
            A[r][j] = 2*p*(xi[i]**(p//2))
            p -= 2
        p = 3
        for j in range(((i-1)*4)+4, ((i-1)*4)+6):
            A[r][j] = -2*p*(xi[i]**(p//2))
            p -= 2
        r += 1

    A[r][0] = 6*xi[0]
    A[r][1] = 2
    r +=1
    A[r][-2] = 6*xi[n-1]
    A[r][-1] = 2

    S = np.linalg.solve(A,B)
    return S

def cubicInterpolate(x, S, xi, yi):
    if x <= xi[0]:
        i = 0
    elif x >= xi[-1]:
        i = len(xi) - 2
    else:
        i = 0
        while x > xi[i]:
            i += 1
        i -=1
    return (S[i*4][0]*(x**3))+(S[(i*4)+1][0]*(x**2))+(S[(i*4)+2][0]*x)+S[(i*4)+3][0]

if __name__ == "__main__":
    x1 = np.array([0.33,
        1,
        2.2,
        4.7])

    y1 = np.array([107.99,
        93.46,
        85.96,
        75.43])

    x11 = [0,25,50,75,100,125,150,175,200]
    y11 = [10.6, 16, 45, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]
    plt.plot(x1,y1,'bo')

    S = cubicInterpolationmatrix(x1, y1)
    xAxis = np.arange(x1[0]-5, x1[-1]+5, 1)
    yAxis = [cubicInterpolate(i, S, x1, y1) for i in xAxis]

    plt.plot(xAxis, yAxis, 'r--')
    plt.show()
