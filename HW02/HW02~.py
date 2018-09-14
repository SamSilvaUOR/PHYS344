from __future__ import division
from numpy import *
from scipy import *
from  pylab import *
from math import *
import matplotlib.pyplot as plt
import random


#HWO2 Random Walk and 20 Step Random Walk

#CONSTANTS: steps, distance, direction
N=20 #number of steps person takes
d=1 #1 unit per step
direction = [0]*N # needs direction, apply i j k

#LOOP with function
def Walk(n):  #n=the amount of walks that occured
    j = 0 #we set the start position in the y direction to be 0
    Pos_list = [] #generate list of steps
    while j <= n: #loop where j reads for all values of n
        Pos=0 #starting position is at 0
        for i in range(N): #loop will run over all ranges of N, which is 20
            x = randint(0,2) #we want a random step assignment
            if x==0: #we compare x to 0
                x=x+1
            direction[i]=x
            Pos=Pos + d*direction[i]
        Pos_list.append(Pos)
        j=j+1
    return Pos_list

W=Walk(1000)

#DATA COLLECTION
x=linspace(-N,N,21)
x_count=[]
for i in range(N+1):
    c=W.count(2*i-20)
    x_count.append(c)

n=int(N/2 +1)
x2=[0]*n
for i in range(n):
    x2[i]=(2*i)**2

x2_count=[]
for i in range(N+1):
    W[i]=W[i]**2
for j in range(n):
    c=W.count((2*j)**2)
    x2_count.append(c)
print(x2)
print(x2_count)

#PLOTS
figure()
plot(x,x_count)
title("x versus xcount: 20 step Random Walk")
xlabel("Distance Walked")
ylabel("number of times a distance was walked")
show()

figure()
plt.scatter(x2, x2_count)
title("x^2 distribution of random walk")
xlabel("distance walked in x^2")
ylabel("How many times the x^2 happened")
show()


#2-D Walk (Used Tutoring)
def Walk2(n):
    j=0
    Locx_list=[]
    Locy_list=[]
    dir_x=[0]*N
    dir_y=[0]*N
    while j <=n:
        Locx=0
        Locy=0
        for i in range(N):
            x=randint(0,20)
            y=randint(0,20)
            if x==0:
                x=x-1
            if y==0:
                y=y-1
            dir_x[i]=x
            dir_y[i]=y
            Locx=Locx+d*dir_x[i]
            Locy=Locy+d*dir_y[i]
        Locx_list.append(Locx)
        Locy_list.append(Locy)
        j=j+1
    return(Locx_list,Locy_list)
W_2=Walk2(100)
x=W_2[0]
y=W_2[1]

#plot
figure()
plt.scatter(x,y)
show()
