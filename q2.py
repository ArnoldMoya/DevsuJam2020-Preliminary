# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:48:05 2021

@author: Lenovo
"""

numbers = [0,7,1,-10,2,-4,-1,3,-2,10,-2,-6,-9,9,1,10,3,-2,0,9,6,-5,10,-10,-2,-5,-5,7,-6,-10,2,2,-5,-3,8,0,3,4,-2,-9,-8,-1,-5,-9,-3,-10,7,-3,-9,4,0,1,0,-9,-8,6,-5,1,-6,-1,0,9,-10,-9,-4,5,5,5,-1,-9,1,-7,-5,-4,0,7,-7,0,6,7,8,-2,0,-6,-6,-2,2,5,0,-4,6,-6,10,-8,-5,-5,7,0,7,-9]

def fun(numbers):
    difN = []
    for n in numbers:
        if not n in difN: difN.append(n)
    
    sumas = {m:sum([n for n in numbers if n != m])for m in difN}
    lower = min(sumas,key=sumas.get)
    choice = max([n for n in difN if sumas[n] == sumas[lower] ])
    return choice

print(fun(numbers))