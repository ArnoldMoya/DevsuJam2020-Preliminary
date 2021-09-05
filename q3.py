# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:02:42 2021

@author: Lenovo
"""
l = [1, 2, 3, 4, 3, 4, 5, 6, 5, 6, 7, 8]
def fun(n):
    
    if n == 0: return 1
    if n == 1: return  2
    k =(n - 2)//4
    resto = (n-2) % 2
    base = 2*k+3
    return base + resto
    # for n in range(len(l)):
    #     #n = 4
    #     k =(n - 2)//4
    #     resto = (n-2) % 2
    #     base = 2*k+3
    #     value = base + resto
    #     print(n,k,l[n],value)

print(fun(87123641123172368))