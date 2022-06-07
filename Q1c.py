# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 12:13:56 2022

@author: Akash Chandra Behera
"""
#Q1c
import matplotlib.pyplot as plt
import math
import pandas as p
x=[i for i in range(1,11)]
#print(x)   #Just for testing
h=[10**-i for i in range(1,7)]
#The following will be useful for making table
mytab1=p.DataFrame({}, index = ['h = '+str(i) for i in h]) #This generates a table of calculated value of second derivative
mydata=p.DataFrame({}, index = ['h = '+str(i) for i in h]) #This generates a table of realtive errors

#print(h)   #Just for testing
for i in x :
    zz=[]
    jj=[]
    jj2=[]
    for j in h:
        f=math.exp(i)
        f_second_derv_exact=math.exp(i) #Derivative of expo is expo itself
        f_second_derv_num=(math.exp(i+j)+math.exp(i-j)-2*f)/j**2 #This the numerical second derivative value
        rel_error_i=math.log10(abs((f_second_derv_num-f_second_derv_exact)/f_second_derv_exact)) #this gives relative error
        abs_error_i=abs((f_second_derv_num-f_second_derv_exact)) #This gives absolute error
        zz.append(f_second_derv_num) #update the numeric value list
        jj2.append(abs_error_i) #update absolute error list
        jj.append(rel_error_i) #update relative error list
    #Next lets plot the error vs step size for a given x
    plt.xscale('log') #Set the axis to log
    plt.yscale('log')
    plt.plot(h,jj2) #Make the plot
    plt.title("x="+str(i)+" (Note the axes are in log scale)") #Set good tite
    plt.xlabel("Step size") #set labels
    plt.ylabel("Error (in log scale)")
    plt.savefig("19MS126_x="+str(i)+'.png') #save plot
    plt.clf() #clear figure window
    #print("For x = "+str(i), jj) #Just for testing
    mydata["x = "+str(i)]=jj #Update pandas database
    mytab1["x = "+str(i)]=zz

newrow = p.Series(data=[math.exp(i) for i in x],index=mytab1.columns, name="Exact value") #Add exact value row
mytab1=mytab1.append(newrow)
print(mydata) #Print the tables
print(mytab1)
#From here we get that h=0.0001 or 10^-4 is the optimal step size
