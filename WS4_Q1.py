# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:26:12 2022

@author: Akash Chandra Behera
"""

#Q1 REFINED

import matplotlib.pyplot as plt
import numpy as np


###############
#This the rk4 function
#It takes in the inital array of parametrs, derivative function, t_initial, t_final and time step h
#The output is a 2-dim np.array with each i(th) row representing the parameters at i(th) time step 
def rk4(x_0,x_der,t_i,t_f,h):
    tim=np.arange(t_i,t_f,h)
    x=[x_0]
    #This calculates my rk4 stages and updates parameter list
    for i in range(1,len(tim)):
        l1=x_der(x[i-1])
        l2=x_der(x[i-1]+l1*(h/2))
        l3=x_der(x[i-1]+l2*(h/2)) 
        l4=x_der(x[i-1]+(l3*h))
        xi=x[i-1]+(l1+(2*l2)+(2*l3)+l4)*(h/6)
        x.append(xi)
    return np.array(x)

###############
#Here I declare the derivative function
def dervR(a):
    pp=[]
    pp.append(10*(a[1]-a[0]))
    pp.append(a[0]*(28-a[2])-a[1])
    pp.append(a[0]*a[1]-a[2]*(8.0/3))
    return np.array(pp)


###############
#Here I set the initial value of parameter
x_0=np.array([0,1,0])


################
#k3 is the function integral
k3=rk4(x_0,dervR,0,100,0.001)
#Note k3 is a 2-dim np array with each i(th) row consiting of (x,y,z) at t_i time 

time=np.arange(0,100,0.001)

######
#This bit is to plot x vs z
plt.plot(k3[:,0],k3[:,2]) 
plt.xlabel('x')
plt.ylabel('z')
plt.title('Lorenz attractor x vs z (19MS126)')


#Following is to plot y vs t, uncomment to use 
'''

plt.plot(time,k3[:,1])
plt.xlabel('Time')
plt.ylabel('y')
plt.title('Lorenz attractor y vs t (19MS126)')
'''



#Following is to plot the attractor in 3d, uncomment to use
'''
ax = plt.axes(projection ='3d')
ax.plot3D(k3[:,0],k3[:,1],k3[:,2],'green')
ax.set_ylabel("Y")
ax.set_xlabel("X")
ax.set_zlabel("Z")
ax.set_title('Lorenz Attractor (19MS126)')
plt.show()
'''