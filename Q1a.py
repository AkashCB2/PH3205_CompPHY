# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:12:09 2022

@author: Akash Chandra Behera
"""
#Q1a
#import numpy as np
import math
import matplotlib.pyplot as plt
x=float(input("Give x ",))
if x>10 or 0>x:
    print("Please input a number between 0 and 10")
else:
    a=float(input("Give a ",))
    b=float(input("Give b ",))
    f=a+b*(x**2)
    f_prime_exact=2*b*x
    h=[i*0.01 for i in range(1,10)] #Generate a list of step sizes
    err=[]  #List for absolute error
    rel_err=[] #List for relative error
    if x<10:     #We use forward formula for x<10
        for i in h:
            f_h=a+b*((x+i)**2)
            f_prime_num=(f_h-f)/i
            error_i=abs((f_prime_num-f_prime_exact))
            rel_error_i=math.log10(abs((f_prime_num-f_prime_exact)/f_prime_exact))
            err.append(error_i)
            #err.append(error_i)
            rel_err.append(rel_error_i)
    elif x==10:  #We use backward formula for x=10
        for i in h:
            f_h=a+b*((x-i)**2)
            f_prime_num=(f-f_h)/i
            error_i=abs((f_prime_num-f_prime_exact))
            rel_error_i=math.log10(abs((f_prime_num-f_prime_exact)/f_prime_exact))
            err.append(error_i)
            rel_err.append(rel_error_i)
            
    plt.xlabel("Step size")
    plt.ylabel("Absolute error")
    plt.title("Plot for x = "+str(x)+", a = "+str(a)+", b = "+str(b) )
    plt.plot(h,err)
    
    print("Relative errors are ",rel_err, "corresponding to step size", h)
    

