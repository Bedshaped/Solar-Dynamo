# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:38:57 2018

@author: moreaua2
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

plt.close('all')

def coupledEqns(t, vals, params):
    x, y = vals
    a, b = params
    dxdt = -a*x + 2*x*y
    dydt = b - x**2 - y**2
    
    return np.array([dxdt, dydt])

# Parameters

params = np.genfromtxt('params.txt')

t_0 = 0
t_max = 6
n = 1000

# Initial values

#initial_vals = [2, 0]

# Using the integrator

plt.figure(1, figsize=(9, 6))

color = 0

for i in [-2, -1, 0.25, -0.25, 1, 2]:
    for j in [[2.25, 'b-'], [-1.75, 'g-'], [-2.25, 'r-']]:
        initial_vals = [i, j[0]]
        res = solve_ivp(lambda t, y : coupledEqns(t, y, params),
                        [t_0, t_max],
                        initial_vals,
                        method="RK45",
                        t_eval=np.linspace(t_0, t_max, n))
        
        x = res.y[0]
        y = res.y[1]
        t = res.t

# Plotting


        if (i == -2):
            #plt.plot(t, x, j[1], label=r"x @ $y_0 = %0.2f$" % initial_vals[1])
            plt.plot(t, y, j[1])
        else:
            plt.plot(t, y, j[1])
        

plt.xlabel('t')
plt.ylabel('y')
plt.xlim(0, 6)
plt.ylim(-3, 3)
plt.legend()    
textstr = '\n'.join((
    r'$a=%.2f$' % (params[0], ),
    r'$b=%.2f$' % (params[1], )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax = plt.gca()
ax.text(0.85, 0.15, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)
plt.savefig("sd_rk45.png", dpi=300)


