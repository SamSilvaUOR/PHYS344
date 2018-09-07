#PHYS344 HW01
#Stern-Gerlach Model

#IMPORTS
from __future__ import division
from pylab import *
from numpy import *
from math import *
from scipy import *
import matplotlib.pyplot as plt
import random

#CONSTANTS
N = 1000000
i = 0
p_list = []
diff_list = [] #per tutoring

p = random.randint(0,1) #Stern-Gerlach only has two outputs

#LOOP
while i < N:
    i = i + 100
    p = random.randint(0,1)
    p_list.append(p)
    p0 = p_list.count(0)
    p1 = p_list.count(1)
    diff = abs(p1 - p0)  #used to plot differences (per tutoring)
    diff_list.append(diff)

#MODEL/GRAPH
x = linspace(0,1000000,10000)
figure()
plot(x,diff_list)
show()

#NOTES: the lines of code for the differences within the loop portion, were derived during tutoring




