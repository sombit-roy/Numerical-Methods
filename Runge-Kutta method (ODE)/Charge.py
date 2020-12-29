from RK44 import *
from matplotlib import pyplot as plt

def charge(E, B):    

    def f1(t,y1,y2,y3,y4):
        return y3

    def f2(t,y1,y2,y3,y4):
        return y4

    def f3(t,y1,y2,y3,y4):
        return (q/m) * (E - B*y4)

    def f4(t,y1,y2,y3,y4):
        return (q/m) * (B*y3)

    N = 10001     # number of iterations
    m = 1         # mass of particle
    q = 1         # charge of particle
    y10 = 0       # initial x position 
    y20 = 0       # initial y position
    y30 = 1       # initial x velocity
    y40 = 0       # initial y velocity
    t0 = 0        # start time
    tN = 20       # end time
    z0 = 0        # initial z position
    zdot0 = 1     # initial z velocity

    t, y1, y2, y3, y4 = RK44(N, t0, tN, y10, y20, y30, y40, f1, f2, f3, f4)
    z = [_*zdot0 + z0 for _ in t]
    
    fig = plt.figure(figsize=(8,8))
    ax = plt.axes(projection='3d')
    ax.plot3D(y1, y2, z)
