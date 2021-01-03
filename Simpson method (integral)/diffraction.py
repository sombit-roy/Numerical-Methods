import math
import numpy as np
import matplotlib.pyplot as plt
from Simpson import *

def f1(t):
    return math.cos((math.pi/2) * t**2)

def f2(t):
    return math.sin((math.pi/2) * t**2)

t = np.linspace(-50,50,5000)
x = [None for _ in range(5000)]
y = [None for _ in range(5000)]
intensity = [None for _ in range(5000)]

for i in range(5000):
    x[i] = Simpson(f1,0,t[i],10000)
    y[i] = Simpson(f2,0,t[i],10000)
    intensity[i] = (0.5-x[i])**2 + (0.5-y[i])**2
    
fig = plt.figure(figsize=(15,15))
ax1 = plt.subplot(2,2,1)
ax1.plot(x,y)
plt.title('Cornu spiral')
ax2 = plt.subplot(2,2,2)
ax2.plot(t,intensity)
plt.title('Diffraction pattern')