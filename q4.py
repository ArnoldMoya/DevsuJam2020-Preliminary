# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 10:25:47 2021

@author: Lenovo
"""

letters = 'MNOQ'

def fun_cod(n):
    r = []
    resto = n % len(letters)
    if n == 0: return []

    if resto == 0: resto = len(letters)
    #print(n,resto,n-resto)
    
    if n-resto != 0:
        r =fun_cod((n-resto)//len(letters)) + [resto]
    else:
        r.append(resto)
    return r

def fun(n):
    r = fun_cod(n)
    #print(r)
    return  ''.join([letters[n-1] for n in r ])

    
print(fun(22421))