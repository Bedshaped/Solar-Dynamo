# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 10:30:16 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x, y, params):
    a, b = params
    return - a*x + 2*x*y

def g(x, y, params):
    a, b = params
    return b - x**2 - y**2

def y_1(y, params):
    a, b = params
    return np.sqrt(b - y**2)

def y_2(x, params):
    a, b = params
    return np.sqrt(b - x**2)

def x_1(y, params):
    return y*0

def x_2(x, params):
    a, b = params
    return 0.5*a

plt.close('all')

# Parameters

a, b = 4, 4

np.savetxt('params.txt', [a, b], fmt='%4.6f')

X, Y = np.meshgrid(np.linspace(-5, 5, 100), np.linspace(-5, 5, 100))


DX = f(X, Y, [a, b])
DY = g(X, Y, [a, b])


# Plot our quiver, streamline and isoclines

textstr = '\n'.join((
    r'$a=%.2f$' % (a, ),
    r'$b=%.2f$' % (b, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

plt.figure(1, figsize=(9, 6))
plt.quiver(X[::5, ::5], Y[::5, ::5], DX[::5, ::5], DY[::5, ::5])
plt.streamplot(X, Y, DX, DY)
plt.plot(y_1(Y[:, 0], [a, b]), Y[:, 0], 'b', linewidth = 3, label = "y-isocline")
plt.plot(-1*y_1(Y[:, 0], [a, b]), Y[:, 0], 'b', linewidth = 3)
plt.plot(X[0, :], y_2(X[0, :], [a, b]), 'b', linewidth = 3)
plt.plot(X[0, :], -1*y_2(X[0, :], [a, b]), 'b', linewidth = 3)
plt.plot(x_1(Y[:, 0], [a, b]), Y[:, 0], 'r', linewidth = 3, label = "x-isocline")
plt.plot(X[0, :], np.full(X[0, :].shape, x_2(X[0, :], [a, b])), 'r', linewidth = 3)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel("X")
plt.ylabel("Y")

# Add dots for the critical points

ix = np.roots([-1, 0, -0.25*a**2 + b])
iy = np.roots([-1, 0, b])

for i in range(2):
    if not (np.iscomplex(ix[i])):
        plt.plot(ix[i], 0.5*a, 'go', markersize = 10)
plt.plot(10, 10, 'go', markersize = 10, label = "Stable fixed point")
if (a < b):  
    plt.plot(0, iy[0], 'yo', markersize = 10)
else:
    plt.plot(0, iy[0], 'go', markersize = 10)
plt.plot(0, iy[1], 'yo', markersize = 10, label = "Unstable fixed point")
plt.legend()
ax = plt.gca()
ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

fixed_points = np.array([[ix[0], 0.5*a], [ix[1], 0.5*a], [0, iy[0]], [0, iy[1]]])

np.savetxt('fixed_points.txt', fixed_points)

    



