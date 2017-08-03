# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 14:55:21 2017

@author: james
"""

import numpy as np
import matplotlib as plt
import math

def simple():
    x_data = np.linspace(0., 100., 100)

    for x in x_data:
        y = math.cos(x)
        plt.pyplot.scatter(x, y)

    axes = plt.pyplot.gca()
    axes.set_xlabel('x')
    axes.set_ylabel('y')

simple()

