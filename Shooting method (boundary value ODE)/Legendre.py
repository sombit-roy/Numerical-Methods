from matplotlib import pyplot as plt
from RK4 import *

def legendre(n):

    N = 101
    epsilon = 0.0001
    a = -0.9999          # x-axis boundary condition 1
    b = 0.9999           # x-axis boundary condition 2
    ya = (-0.9999)**n    # y-axis boundary condition 1
    yb = 0.9999          # y-axis boundary condition 2
    alpha = []
    alpha.append((yb-ya) / (b-a))
    alpha.append(2 * alpha[0])

    def f1(x,y,z):
        return z

    def f2(x,y,z):
        return (2*x*z - n*(n+1)*y) / (1-x**2)

    p = []
    x, y, z = RK4(N,a,b,ya,alpha[0],f1,f2)
    p.append(y[N-1])
    x, y, z = RK4(N,a,b,ya,alpha[1],f1,f2)
    p.append(y[N-1])
    y[N-1] = p[0]
    k = 2

    while (abs(y[N-1] - yb) > epsilon):
    
        alpha.append(alpha[k-2] + (yb-p[k-2]) * (alpha[k-1]-alpha[k-2]) / (p[k-1]-p[k-2]))
        x, y, z = RK4(N,a,b,ya,alpha[k],f1,f2)
        p.append(y[N-1])
        k += 1    

    fig = plt.figure(figsize=(8,8))
    ax = plt.axes()
    ax.plot(x,y)