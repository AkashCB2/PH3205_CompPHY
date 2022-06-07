# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 19:11:32 2022

@author: Akash Chandra Behera
"""

#Q2 refined
import numpy as np
import matplotlib.pyplot as plt

la=0
def F(x): #The F at hand
    return -x-la*x**3


st_size = [51,81,101,201] #This corresponds to h=0.2,0.125,0.1,0.05
for jj in st_size:
    time,h=np.linspace(0,10,jj,retstep=True)
    x=[] #position list
    vel=[] #vel list
    E=[] #energy list

    for ti in range(len(time)):
        if ti==0: #this sets initial values
            xi=1
            vi=0
            Ei=0.5+la*(0.25)
        else: #these are the subsequent updates
            v_mid=vel[ti-1] + 0.5*h*(F(x[ti-1]))
            xi=x[ti-1]+h*v_mid
            vi=v_mid+0.5*h*F(xi)
            Ei=0.5*(vi**2)+0.5*(xi**2)+0.25*la*(xi**4)
        #These update the lists
        x.append(xi)
        vel.append(vi)
        E.append(Ei)
    #Make and format the plot
    plt.plot(time,E)

plt.legend(["h=0.2","h=0.125","h=0.1","h=0.05"])
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy vs. Time ($\lambda$=0) 19MS126')
plt.show()