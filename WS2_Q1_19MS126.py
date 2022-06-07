# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 14:00:30 2022

@author: Akash Chandra Behera
"""

#Q1
from numpy import *
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad


def gauss(x):
    return math.exp(-(x**2))
I= quad(gauss, -1, 1) #This is exact value
print(I[0]," is the exact value of the integral (as obtained by Scipy in-built function).")



step=[11,51,101,501,1001,5001]
step_size=[]
error=[] #List of relative error
for i in step: #Follwing lines implement the Simpson rule
    xi,h=linspace(-1,1,i,retstep=True) 
    yi=exp(-(xi**2))
    Simpintg=(h/3.0)*(yi[0]+yi[-1]+(4*sum(yi[1:-1:2]))#This is for odd indexes
                      +(2*sum(yi[2:-1:2])))#This is for even indexes, see slides
    
    err=abs(I[0]-Simpintg) #This abs. error
    relerr=err/I[0]
    print("Calculted value for step size h="+str(h)+" is ", Simpintg, "Percent error is ", (100*relerr))
    step_size.append(h)
    error.append(relerr)
#Plot formatting
plt.title("Simpson rule, step-size vs. error (19MS126)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("Step size")
plt.ylabel("Relative error")
plt.plot(step_size,error)
plt.savefig('19MS126_Plot_WS2_Q1.png')   