import math
from RK44 import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def doublependulum(ang_up,ang_low):
    
    N = 1001
    w = 10

    def f1(t,y1,y2,y3,y4):
        return y3

    def f2(t,y1,y2,y3,y4):
        return y4

    def f3(t,y1,y2,y3,y4):
        return (math.cos(y1-y2) * (-(y3**2)*math.sin(y1-y2) + w*math.sin(y2)) - (y4**2)*math.sin(y1-y2) - 2*w*math.sin(y1)) / (2 - (math.cos(y1-y2))**2)

    def f4(t,y1,y2,y3,y4):
        return (0.5*math.cos(y1-y2) * ((y4**2)*math.sin(y1-y2) + 2*w*math.sin(y1)) + (y3**2)*math.sin(y1-y2) - w*math.sin(y2)) / (1 - 0.5*(math.cos(y1-y2))**2)

    y10 = ang_up * (math.pi/180)     # Initial angle of upper pendulum
    y20 = ang_low * (math.pi/180)    # Initial angle of lower pendulum
    y30 = 0                          # Initial angular velocity of upper pendulum
    y40 = 0.5                        # Initial angular velocity of lower pendulum
    t0 = 0                           # Start time
    tN = 20                          # End time

    t, y1, y2, y3, y4 = RK44(N,t0,tN,y10,y20,y30,y40,f1,f2,f3,f4)

    writer = animation.writers['ffmpeg'](fps=60)

    fig = plt.figure(figsize=(8,4.4))
    ax = plt.axes()

    def animate(i):
        ax.clear()
        ax.plot(math.sin(y1[i]),-math.cos(y1[i]),'o',c='#1f77b4',markersize=10)
        plt.plot(math.sin(y1[i])+math.sin(y2[i]), -math.cos(y1[i])-math.cos(y2[i]),'o',c='#1f77b4',markersize=10)
        plt.plot([math.sin(y1[i]),math.sin(y1[i])+math.sin(y2[i])], [-math.cos(y1[i]),-math.cos(y1[i])-math.cos(y2[i])])
        plt.plot([0,math.sin(y1[i])], [0,-math.cos(y1[i])], c='#1f77b4')
        plt.ylim([-2.2, 0])
        plt.xlim([-2, 2])
    
    ani = animation.FuncAnimation(fig=fig, func=animate, interval=1, frames=1000, repeat=False)
    ani.save('doublependulum.mp4', writer=writer)
    plt.show()