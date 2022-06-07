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
#Here I declare the derivative functions
#For ease I shall break it into two parts
def derxx(a,b,c,k): #This calculates the numerical double derv w.r.t. x
    xx=(a+c-(2*b))/(k**2)
    return xx

def derP(p): #This part calculates num.derv. for each x value,it takes in as input a list/np.array
    p_dot=[]
    x=np.arange(-2,2,k)
    for i in range(len(x)):
        if i in range(0,len(x)-1):
            ut=D*derxx(p[i+1],p[i],p[i-1],k)
            p_dot.append(ut)
        
        elif i>len(x)-2: #for last values of x at x=2 end I use backward derv
            ut=D*derxx(p[i-3],p[i-2],p[i-1],k)
            p_dot.append(ut)
    return np.array(p_dot)




###############
#This the rk4 function
#It takes in the inital array of parametrs, derivative function, t_initial, t_final and time step h
#The output is a 2-dim np.array with each i(th) row representing the parameters at i(th) time step 
def rk4(x_0,x_der,t_i,t_f,h):
    tim=np.arange(t_i,t_f,h)
    x=[x_0] #Initial the Parameters using given condition
    for i in range(1,len(tim)): #This loop calculates RK4 stages and updates the parameter list
        l1=x_der(x[i-1])
        l2=x_der(x[i-1]+l1*(h/2))
        l3=x_der(x[i-1]+l2*(h/2)) 
        l4=x_der(x[i-1]+(l3*h))
        xi=x[i-1]+(l1+(2*l2)+(2*l3)+l4)*(h/6)
        x.append(xi)
    return np.array(x)

###############
#Here I set the initial value of parameters
def P(x): #P(x,1)
    sig=(2*D)**0.5 #This is thevalue of Sigma at time=1
    return (1.0/(2*math.pi*(sig**2))**(0.5))*math.exp(-x**2/(2*(sig**2)))

#x=np.arange(-2,2,k)
pini=np.frompyfunc(P,1,1) #Convert P to operate on np.array
p_initial=pini(x) #Thgis gives us the inital parameters

################
#p_xt is the function integral i.e. how P evolves in time
p_xt=rk4(p_initial,derP,1,20,h)


###############
#This plots the function at 3 time steps t=1,t=10,t=20
for i in [0,899,1899]:
    #Note p_xt[i,:] gives us the i(th) row of p_xt, which is the heat distribution at time t_i
    plt.plot(x,p_xt[i,:])
plt.legend(['t=1','t=10','t=20']) 
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Evolution of P(x) w.r.t. to Time (19MS126)')
plt.show() 



