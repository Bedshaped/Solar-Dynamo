# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:38:50 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

plt.close('all')

# Declaring our f and g

x, y = sym.var('x, y')

f = x**2 + x*y - 2*x
g = x*y**2 + 3*y

# Fixed points

fixed_points = sym.Matrix([[-1, 3], [3, -1], [0, 0], [2, 0]])

# Initialize the matrix

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
plt.figure(1, figsize=(6, 6))
plt.plot(x, 0.25*x**2, 'k--')
ax = plt.gca()
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
for i in range(4):
    plt.scatter(int(trace[i]), int(determs[i]), 
             label = r"(x, y) = (%d, %d)" % (fixed_points[i, 0], fixed_points[i, 1]))        
plt.grid()
plt.legend()
