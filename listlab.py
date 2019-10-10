# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:07:45 2019

@author: pkuma
"""

def list4(a,b,c,d):
    """Identify whether a,b,c,d are integers or floats, and if so, then to determine and return the max of those four numbers, if not, then to return a list of the inputs.""" 
    if (type(a)==float or type(a)==int) and (type(b)==float or type(b)==int) and (type(c)==float or type(c)==int) and (type(d)==float or type(d)==int) :
        list=[a,b,c,d]
        return max(list)
        
    else: 
        list = [a,b,c,d]
        return list 
print(list4(5,4,3,2))