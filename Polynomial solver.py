# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:55:21 2017

@author: james
"""

import numpy as np
import matplotlib as plt
import math

PolyC=[1,0,-1,4,0,1,-1]
Poly=np.poly1d(PolyC)

R=np.roots(Poly)

#fig = plt.figure()
#plt.plot(T,R[:,0])
#plt.plot(T,R[:,1])

import matplotlib as pltp
plt.pyplot.plot(R, 'ro')
plt.pyplot.axis([-10,10])
plt.pyplot.show()
print(R)

