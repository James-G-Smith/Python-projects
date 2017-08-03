# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:42:48 2017

@author: james
"""

from datetime import datetime

now=datetime.now()

mm=str(now.month)
dd=str(now.day)
yyyy=str(now.year)
hour=str(now.hour)
mi=str(now.minute)
ss=str(now.second)


print(mm +"/"+dd+"/"+yyyy)
print(hour+":"+mi+":"+ss)