# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:48:13 2014

@author: james
"""

def check_fermat(a,b,c,d):
    if a^d + b^d == c^d:
        return 'true'
    else:
        return 'false'
        
print check_fermat(2,4,5,7)

