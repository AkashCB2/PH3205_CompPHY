# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:44:38 2022

@author: Akash Chandra Behera
"""

import matplotlib.pyplot as plt
import numpy as np
import math

###############
#Parameters
k=0.01 #This is spatial step
h=0.01 #This is temporal step
D=(k**2)/(2*h) #This is given
x=np.arange(-2,2,k) #This is given


###############
#Here, I define the euler scheme 
#It takes in the inital array of parametrs, t_initial, t_final and time step h
#The output is a 2-dim np.array with each i(th) row representing the parameters at i(th) time step 

def eu(x_0,t_i,t_f,h):
    tim=np.arange(t_i,t_f,h)
    x=[x_0] #Initial the Parameters using given condition
    for i in range(1,len(tim)):
        zz=x[i-1]
        oo=[x_0[0]] #This list will be i(th) row, we have x_0[0] here as at the endpoints the euler scheme does not change the function
        #This part calculates the derivative using euler scheme
        for kk in range(1,len(zz)):
            if kk<len(zz)-1:
                jj=0.5*(zz[kk+1]+zz[kk-1])
                oo.append(jj)
            elif kk==len(zz)-1: #This because at the endpoints the euler scheme does not change the function
                oo.append(x_0[-1])
        x.append(np.array(oo))
    return np.array(x)
            
###############
#Here I set the initial value of parameters
def P(x): #P(x,1)
    sig=(2*D)**0.5 #This is thevalue of Sigma at time=1
    return (1.0/(2*math.pi*(sig**2))**(0.5))*math.exp(-x**2/(2*(sig**2)))

#x=np.arange(-2,2,k)
pini=np.frompyfunc(P,1,1) #Convert P to operate on np.array
p_initial=pini(x) #This gives us the inital parameters

################
#p_xt is the function integral i.e. how P evolves in time
p_xt=eu(p_initial,1,20,h)  






#This plots the function at 3 time steps t=1,t=10,t=20
for i in [0,899,1899]:
    #Note p_xt[i,:] gives us the i(th) row of p_xt, which is the heat distribution at time t_i
    plt.plot(x,p_xt[i,:])
plt.legend(['t=1','t=10','t=20']) 
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Evolution of P(x) w.r.t. to Time using Euler Scheme (19MS126)')
plt.show()        



