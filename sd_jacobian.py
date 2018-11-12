# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:13:32 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

plt.close('all')

# Reading our values from sd_nullclines.py

a, b = np.genfromtxt('params.txt')

fixed_points = np.genfromtxt('fixed_points.txt')


# Declaring our f and g

x, y = sym.var('x, y')

f = -a*x + 2*x*y
g = b - x**2 - y**2

# Turning our np array into a sym matrix

fixed_points = sym.Matrix(fixed_points)

# Initializing our matrix & jacobian

M = sym.Matrix([f, g])
jac = M.jacobian([x, y])

# Calculating our det and trace

char_poly = jac.det()
determs = np.zeros((4, 1))
trace = np.zeros((4, 1))

for i in range(4):
    vals = jac.subs(x, fixed_points[i, 0]).subs(y, fixed_points[i, 1])
    determs[i] = vals.det()
    trace[i] = vals[0, 0] + vals[1, 1]

print(trace)
print(determs)
x = np.linspace(-8, 8, 100)

textstr = '\n'.join((
    r'$a=%.2f$' % (a, ),
    r'$b=%.2f$' % (b, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

plt.figure(1, figsize=(6, 6))
plt.plot(x, 0.25*x**2, 'k--')
ax = plt.gca()
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i in range(4):
    plt.scatter(int(trace[i]), int(determs[i]), 
             label = r"(x, y) = (%4.1f, %4.1f)" % (fixed_points[i, 0], fixed_points[i, 1]))        
plt.grid()
plt.legend()
ax = plt.gca()
ax.text(0.05, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.savefig("sd_jacobian.png", dpi=300)