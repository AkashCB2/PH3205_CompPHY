# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:46:57 2022

@author: Akash Chandra Behera
"""

#Q1
import matplotlib.pyplot as plt
import numpy as np

x=[] #position list
vel=[] #velocity list
acc=[] #acceleration list
gamma=4 #This is damping constant, for ease of coding I have set to 4 (critically damped), this can be changed as per will
k=1 #This is spring constant, for ease of coding I have set to 1, this can be changed as per will
m=4 #This is mass, for ease of coding I have set to 4, this can be changed as per will
jj=1001 #This is no. of steps, 1001 means h=0.1
time,h=np.linspace(0,100,jj,retstep=True)
x_int=0 #initial position (can be changed to any value as per wish)
v_int=1 #initial velocity (can be changed to any value as per wish)

for ti in range(jj):
    if ti==0:
        xi=x_int
        vi=v_int
        ai=-(gamma*vi)/m - (k*xi)/m
    else:
        #These are the Runge-Kutta Stages
        l1=h*acc[ti-1]
        l2=0.5*(h*acc[ti-1]+l1)
        l3=0.5*(h*acc[ti-1]+l2)
        l4=h*(acc[ti-1]+l3)
        
        k1=h*vel[ti-1]
        k2=0.5*(h*vel[ti-1]+k1)
        k3=0.5*(h*vel[ti-1]+k2)
        k4=h*(vel[ti-1]+k3)
        
        xi=x[ti-1]+(1.0/6.0)*(k1+k4+(2*(k2+k3))) #Position update
        vi=vel[ti-1]+(1.0/6.0)*(l1+l4+(2*(l2+l3))) #Velocity update
        ai=-(gamma*vi)/m - (k*xi)/m
    #update the lists of x,vel,acc
    x.append(xi)
    vel.append(vi)
    acc.append(ai)
plt.title("$\gamma$="+str(gamma)+"(Critically-damped condition, m=4, k=1) 19MS126") #The damped statement is changed as per need
plt.xlabel("Time")
plt.ylabel("Position")
plt.plot(time,x)
#For other gammas, I used to other .py files to get the plots, I have attached these in the plots folder


