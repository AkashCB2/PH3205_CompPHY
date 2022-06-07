# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:05:56 2022

@author: Akash Chandra Behera
"""

import numpy as np
import matplotlib.pyplot as plt
lambdA=[0.1,0.5,1] #The list of lambda
for la in lambdA:
    def F(x): #This is the F at hand
        return -x-la*x**3

    time,h=np.linspace(0,10,201,retstep=True) #Here h=0.05
    x=[]
    vel=[]
    E=[]
    #define the velocity verlet
    for ti in range(len(time)):
        if ti==0: #initial condition
                    xi=1
                    vi=0
                    Ei=0.5+la*(0.25)
        else: #non-trivial update
                    v_mid=vel[ti-1] + 0.5*h*(F(x[ti-1]))
                    xi=x[ti-1]+h*v_mid
                    vi=v_mid+0.5*h*F(xi)
                    Ei=0.5*(vi**2)+0.5*(xi**2)+0.25*la*(xi**4)
        #update the counting lists
        x.append(xi)
        vel.append(vi)
        E.append(Ei)
    #make and format plots
    plt.ylabel("Velocity")
    plt.xlabel("Position")
    plt.plot(x,vel)
plt.legend(["$\lambda=0.1$","$\lambda=0.5$","$\lambda=1$"])  
plt.title('Phase space 19MS126')     