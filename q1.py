# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 09:21:03 2021

@author: Lenovo
"""

text = "uepnzleaiogoxbvdcwalayckdzfzxdvddexcofcjlujrzofzolxmigtogtslkwwuxdilwmdjlpaqufnvuuufvhcmwpjqhlchtmqzrijwajbqzwrtzcmbwjvzfdhgunizgddehprykgvbpohccigzyvhintlpwotuvvlzrqicnavvnxfteduomtdjlwqyxbridegazizo"
subText = "egazizo"

def fun(text,subText):
    if not subText in text: return -1
    left = text.index(subText)
    rigth = text[::-1].index(subText[::-1])
    return min(left,rigth)
    
print(fun(text,subText))