# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 21:27:55 2021

@author: ArnM
"""

class node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        self.level = 1
    def add_child(self,child):
        child.parent = self
        child.level = self.level + 1
        self.children.append(child)
    def print_children(self):
        #print(self.data, self.level)
        print("-"*self.level,self.data)
        for child in self.children:
            child.print_children()

def fun(N):
    if N.level == m-1:
        return
    for child in N.children:
        if child.data == 1:
            child.add_child(node(n-1))
        else:
            child.add_child(node(1))
            child.add_child(node(n-1))
        fun(child)

def mul(N):
    costo = 0
    if N.level == m:
        return N.data
    for child in N.children:
        costo += N.data*mul(child)
    return costo

n = 8
m = 10
root = node(n)
root.add_child(node(1))
root.add_child(node(n-1))

fun(root) #expandir el arbol
root.print_children()

print("resp:",mul(root))