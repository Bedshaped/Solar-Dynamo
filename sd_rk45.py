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
t_max = 4
n = 1000

# Initial values

#initial_vals = [2, 0]

# Using the integrator

plt.figure(1, figsize=(9, 6))

for i in [-2, -1, 0.25, -0.25, 1, 2]:
    for j in [[2.25, 'b-'], [1, 'g-'], [0, 'r-']]:
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




        plt.plot(t, x, j[1], label=r"$x , x_0 = %d$" % initial_vals[0])
        #plt.plot(t, y, j[1], label=r"$y , y_0 = %d$" % initial_vals[1])
    
textstr = '\n'.join((
    r'$a=%.2f$' % (params[0], ),
    r'$b=%.2f$' % (params[1], )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)


