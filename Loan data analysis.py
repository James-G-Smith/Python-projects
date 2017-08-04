# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 13:33:54 2017

@author: james
"""

import pandas as pd
import numpy as np
import matplotlib as plt
import csv


df=pd.read_csv("C:\\Users\\james\\OneDrive\\Documents\\Python_Scripts\\Data\\test.csv")
df.head(5)

df.describe()

df["Property_Area"].value_counts()

df["ApplicantIncome"].hist(bins=50)

df.boxplot(column="ApplicantIncome")

df.boxplot(column="ApplicantIncome", by="Education")

