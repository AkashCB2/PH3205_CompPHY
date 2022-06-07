# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 16:24:44 2022

@author: Akash Chandra Behera
"""

#Q1b
import math
import matplotlib.pyplot as plt
x=float(input("Give x ",))
a=float(input("Give a ",))
b=float(input("Give b ",))

f=a+b*(x**2) #This is our function
f_prime_exact=2*b*x #This is the exact derivative
h=[i*0.01 for i in range(1,10)] #Set steps
err=[] #Empty error list
rel_err=[] #Empty relative error list
if 10>=x and x>=0: #Note our domain is [0,10]
    for i in h:
        f_h=a+b*((x+i)**2)
        f_minus_h=a+b*((x-i)**2)
        f_prime_num=(f_h-f_minus_h)/(2*i) #Numerical value
        error_i=abs((f_prime_num-f_prime_exact)) #Error
        rel_error_i=math.log10(abs((f_prime_num-f_prime_exact)/f_prime_exact)) #Rel. error
        if rel_error_i<-10: #Set tolerance assuming float type 32
            error_i=0
        err.append(error_i)
        rel_err.append(rel_error_i)
else:
    print("Please set x between 0 and 10")
plt.xlabel("Step size")
plt.ylabel("Error")
plt.title("Error vs step size for x="+str(x)+", a="+str(a)+", b="+str(b))
plt.plot(h,err)
print("Relative errors are ",rel_err)
print(err)