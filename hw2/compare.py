# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 13:03:38 2014

@author: james
"""

def compare(x ,y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

print compare(4,6)