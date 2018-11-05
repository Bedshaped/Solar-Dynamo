# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:35:32 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

def dxdt(x, y):
    return x**2 + x*y - 2*x

def dydt(x, y):
    return x*y**2 + 3*y

def y_1(y):
    return -3/y

def y_2(x):
    return x*0

def x_1(y):
    return y*0

def x_2(x):
    return 2 - x

plt.close('all')

X, Y = np.meshgrid(np.linspace(-2, 4, 100), np.linspace(-2, 4, 100))


DX = dxdt(X, Y)
DY = dydt(X, Y)

# Plot our quiver, streamline and isoclines

plt.figure(1, figsize=(9, 6))
plt.quiver(X[::5, ::5], Y[::5, ::5], DX[::5, ::5], DY[::5, ::5])
plt.streamplot(X, Y, DX, DY)
plt.plot(y_1(Y[:, 0]), Y[:, 0], 'b', linewidth = 3, label = "y-isocline")
plt.plot(X[0, :], y_2(X[0, :]), 'b', linewidth = 3)
plt.plot(x_1(Y[:, 0]), Y[:, 0], 'r', linewidth = 3, label = "x-isocline")
plt.plot(X[0, :], x_2(X[0, :]), 'r', linewidth = 3)
plt.xlim(-2, 4)
plt.ylim(-2, 4)
plt.xlabel("X")
plt.ylabel("Y")

# Add dots for the critical points

plt.plot(-1, 3, 'go', markersize = 10, label = "Stable fixed point")
plt.plot(0, 0, 'yo', markersize = 10, label = "Unstable fixed point")
plt.plot(2, 0, 'yo', markersize = 10)
plt.plot(3, -1, 'yo', markersize = 10)

plt.legend()