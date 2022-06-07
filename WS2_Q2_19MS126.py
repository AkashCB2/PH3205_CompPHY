# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 12:29:05 2022

@author: Akash Chandra Behera
"""

#Q2
import matplotlib.pyplot as plt
import math


tru_val=5216.9264773230244801 #From Wolfram alpha
print("Exact value of integral (as obtained by Wolfram apha) is ", tru_val)

def f(x):
    return ((math.exp(4+4*x))*(4+4*x)) #Quadrature function
err=[]
n=[2,3,4,5]
#integ is the integral value calculated by  Gaussian quad method
for i in n:
    if i==2:
        integ=f(1/(3**0.5))+f(-1/(3**0.5)) 
    if i==3:
        integ=(f(0)*(8/9))+(f((3/5)**0.5)*(5/9))+(f(-(3/5)**0.5)*(5/9))
    if i==4: #In n=4 and n=5, p's are for points and o's for weights
        o1=(18+30**0.5)/36
        p1=((3/7)-(2/7)*((6/5)**0.5))**0.5
        o2=(18+30**0.5)/36
        p2=((3/7)+(2/7)*((6/5)**0.5))**0.5
        o3=(18-30**0.5)/36
        integ=(f(p1)*(o1))+(f(-p1)*(o2))+(f(-p2)*(o3))+(f(p2)*(o3))
    if i==5:
        p1=0.0
        o1=128.0/225
        p2=(1.0/3)*((5-2*((10.0/7)**0.5))**0.5)
        o2=(322+13*(70**0.5))/900
        p3=(1.0/3)*((5+2*((10.0/7)**0.5))**0.5)
        o3=(322-13*(70**0.5))/900
        integ=(f(p1)*o1)+(f(p2)*o2)+(f(-p2)*o2)+(f(p3)*o3)+(f(-p3)*o3)
    p=abs(tru_val-integ) #Absolute error
    p_rel=p/tru_val #rel. error
    err.append(p_rel)
    percent=100*(p/tru_val)
    print("Value of integral for n="+str(i)+" is ", integ, " And error is ",percent,"%.")
    
    #print(p)
#The formatting of plot
plt.title("Gaussian Quadrature method (19MS126)")
plt.ylabel("Relative Error")
plt.xlabel("n")
plt.yscale('log') #rel. error plotted in log scale
plt.plot(n,err)
#plt.savefig('19MS126_Plot_WS2_Q2.png')

