#!/usr/bin/env python
# coding: utf-8

# In[27]:


#End Sem Project
#Members:- Abhishek Kumar, Jishnu N, Mathew George K
            

#importing libraries reqiured
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#giving x and y values and creating grid
x = np.linspace(-29, 29, 400)
y = np.linspace(-19, 19, 400)
x, y = np.meshgrid(x, y)

#reading csv file as Data Frame
coeffs = pd.read_csv("data.csv", header=0, sep=",")

#Taking values from Data Frame
a = coeffs.loc[0].at['a']
b = coeffs.loc[0].at['b']
c = coeffs.loc[0].at['c']
d = coeffs.loc[0].at['d']
e = coeffs.loc[0].at['e']
f = coeffs.loc[0].at['f']

#creating axes
def axes():
    plt.axhline(0, alpha=.1)
    plt.axvline(0, alpha=.1)
    
    
axes()
plt.contour(x, y, (a*x**2 + b*y**2+ c*x + d*y + e*x*y), [-f], colors='b', alpha=.5)

plt.show()

