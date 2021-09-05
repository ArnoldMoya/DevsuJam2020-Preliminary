# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 15:17:16 2021

Distance from right top to left bottom
@author: Lenovo
"""

m = [[1, 5,1],
     [4,-1,2],
     [4, 1,2],
     [8,-2,1]
     ]

m = [[22,-7,1,-10,8,21,-10,-11,2,1,3,15,-23,-13,8,9,21,1,-3,-25,14,-21,-14,5,-20,10,5,15,-10,25,9,-15,5,6,6,5,2,16,24,-4,5,9,-8,-5,17,-10,11,1,10,10],[-14,0,-2,-11,18,4,25,14,-9,10,2,-8,5,25,-14,17,24,18,21,10,2,18,8,25,23,-7,-1,-4,9,-11,9,17,7,-21,2,22,9,-17,-17,13,25,-11,-13,5,-20,-12,-16,0,-22,3],[1,7,24,-10,-21,-2,-10,9,-3,0,18,22,-23,-21,23,9,23,4,-16,3,2,16,7,-25,1,-2,-5,-4,17,-14,11,10,8,7,-23,-11,21,11,22,8,18,-18,-1,-18,-13,-18,-4,14,5,-5],[-15,-17,10,13,1,15,-3,23,-2,-10,-4,-8,-18,-23,-25,-13,14,0,12,1,18,-11,-10,9,-16,1,12,17,7,-21,-22,-6,-16,12,-7,20,17,-24,0,-25,-12,20,-15,-18,-12,-8,7,0,-3,16],[-23,-13,16,18,-21,8,-5,11,21,13,-22,-24,-25,0,-15,-14,-4,-23,-1,20,-19,-1,6,7,-15,25,-6,-21,24,23,19,-1,9,17,1,1,-14,-4,20,-9,-22,10,10,-4,0,-15,0,13,25,-20],[7,24,19,2,-18,-17,0,-11,4,-22,-11,-25,1,14,24,1,6,0,19,-15,-22,-23,22,-25,-22,19,0,-14,9,21,-20,5,-5,-16,-9,-14,-23,-4,-16,-9,12,-2,-22,17,-23,-7,-6,-2,2,-18],[23,22,-22,0,-7,21,1,25,20,10,14,18,1,13,-2,-3,17,15,1,20,22,8,8,5,-3,-21,-13,6,12,9,-8,-5,14,-1,16,0,-9,6,14,13,-19,-19,-5,18,5,-25,25,-25,15,-17],[-5,1,-8,13,10,9,-8,-22,10,-25,-8,-12,1,23,15,19,4,6,5,22,-12,-25,11,13,20,6,-11,19,-14,-16,-13,-12,1,-17,3,-15,-14,-18,-22,16,-24,-17,6,15,13,16,19,21,-24,-12],[-25,-9,10,-21,-12,-3,-10,-20,10,-22,-10,-20,22,-13,5,24,-22,24,23,-5,17,-11,-7,-22,0,-1,-18,10,-12,-22,0,-21,3,-24,-8,12,13,-2,4,9,-4,10,-18,-23,20,10,23,14,-8,3],[24,10,24,9,25,16,-1,-22,-10,-5,-21,3,-13,17,-21,20,-8,19,-19,-22,-22,-21,20,-19,21,-15,-7,3,-14,1,1,-11,-19,-17,15,-12,0,-21,-5,-22,25,12,3,24,25,21,-20,-5,7,-9],[-9,-25,24,19,0,-16,22,24,0,-8,24,-24,-9,5,-24,12,18,6,12,-21,15,8,-9,-17,-9,-24,-13,-22,-22,11,-17,23,-6,-5,-14,-25,-2,-18,25,6,16,8,-17,16,-14,19,23,15,-7,18],[3,19,-3,-2,9,-14,-2,14,10,0,-19,14,20,-24,19,25,-24,-7,11,23,-11,-24,24,-2,-18,-16,6,-7,-11,2,12,8,9,12,10,-3,-25,24,2,17,-21,-20,9,-8,-23,3,15,22,-14,21],[22,2,-3,11,-2,-23,-11,18,0,-9,25,-9,0,-10,0,-1,23,0,21,8,-9,25,-18,12,13,21,1,-8,22,-25,14,-23,-15,-5,-3,-18,-2,0,-11,21,-12,-7,25,15,19,-15,-2,20,13,-16],[24,21,8,20,16,-9,18,-11,18,-11,11,17,-8,16,6,-11,8,1,7,-13,-6,3,-3,18,21,-21,25,-5,-6,4,-15,-13,12,11,-6,8,-7,-10,0,-23,-11,-14,-3,-3,-7,-7,-19,19,2,2],[-19,-10,9,4,4,-17,8,11,23,-12,13,7,-3,11,9,-13,7,-2,9,13,8,-18,-4,14,24,20,22,5,3,-4,3,-1,-8,15,5,4,9,13,1,15,10,-7,24,-8,-23,-3,-23,3,15,10],[11,21,-22,-11,-6,11,-16,-2,17,-23,14,-13,-19,17,-3,-24,-9,-22,-19,-24,-22,8,3,-6,-6,18,1,-3,-11,-9,22,9,-18,17,-19,6,19,13,17,4,20,21,18,20,11,9,24,-12,1,-4],[-17,16,23,-13,-7,7,25,-7,-4,1,-3,-13,-22,9,2,-21,11,11,1,2,4,0,-23,1,-4,10,23,-25,17,19,8,-6,-1,2,-20,21,14,22,-14,-13,7,-15,10,-17,23,-21,6,-2,18,-14],[15,12,-12,-10,9,-9,21,-23,-8,15,-24,-2,24,24,-21,-22,-6,19,-8,-15,0,-17,-25,-3,-9,-15,-17,-25,-20,11,25,0,-5,-1,-3,4,6,12,1,16,-3,-11,-21,17,-5,-7,21,14,23,-7],[-2,2,7,-15,-15,-12,-5,-8,0,25,7,5,13,-14,-8,-24,-18,16,18,3,-18,4,-24,-19,-2,-11,-4,-4,16,-12,-4,-19,6,-9,11,-23,7,-2,18,-16,12,9,-18,-14,-25,8,6,2,9,-15],[-17,-19,16,3,-20,-17,6,-9,-19,4,-16,-24,-5,0,21,-12,20,-22,-6,-18,24,21,13,-17,0,-1,5,7,-15,-14,-25,3,23,3,2,18,12,13,-25,20,-22,-25,11,-5,5,23,0,-16,-21,-16],[-22,16,-4,24,-17,-13,20,-18,11,-9,-25,-19,-5,16,0,6,-16,2,4,21,19,23,-23,21,25,25,16,16,-5,-13,-22,12,13,14,17,-21,-10,-6,-21,-11,-14,6,-20,25,13,-25,14,16,12,7],[-14,-20,6,20,-2,25,-15,25,-13,15,1,-24,-8,-22,-18,14,-9,10,-16,11,-18,4,23,-15,-25,6,0,-15,7,1,7,-18,19,14,6,16,15,-13,24,10,-21,-24,2,-13,0,-23,0,-13,24,-12],[10,5,21,-24,-5,4,0,23,15,19,-6,9,-11,12,10,-7,23,6,0,0,5,19,-3,-6,-8,18,20,-7,-6,-16,-20,15,4,25,8,9,0,12,9,-10,-12,5,-25,4,-16,-7,13,-14,-24,-4],[-4,10,18,-12,-25,-3,-3,-1,-2,25,-2,-9,8,22,-23,19,-11,10,2,25,14,-11,-1,24,-23,12,-9,12,-9,10,-6,0,16,1,2,-12,-15,-8,-1,0,0,10,17,4,-11,3,-23,-1,-23,-23],[3,-24,-10,-23,-1,13,-10,24,-20,-1,12,-25,-3,10,-25,-12,15,-1,23,2,-15,19,-5,11,14,-2,14,25,-7,-3,-24,3,-1,-6,-22,16,0,-13,0,-4,-5,-14,-16,12,3,7,-17,-9,-16,12],[17,10,7,-5,2,-14,14,16,11,2,1,12,5,-12,-4,-3,16,12,-18,-4,20,-6,-12,-12,1,-3,25,-16,-23,-8,0,4,-19,16,17,9,-25,-7,-7,-21,-13,21,7,19,23,0,1,14,9,-10],[-3,6,-7,9,-11,15,5,4,-10,10,1,17,-8,14,22,-22,7,13,-6,-20,-9,17,24,-5,7,17,17,13,12,20,7,0,16,0,16,19,21,-17,-19,-2,-20,-13,-16,0,17,-5,10,-3,-12,-18],[0,23,4,-7,20,-9,16,22,7,3,-12,8,-11,12,-7,2,-24,21,-19,10,-14,0,-1,25,3,-14,-7,8,0,-20,15,-9,18,14,-8,-10,-25,22,-24,3,3,-7,-2,13,-24,-10,15,18,13,0],[4,-2,11,0,24,-23,22,18,11,24,-18,15,9,14,-17,-3,-4,9,-22,-10,-13,11,3,20,4,8,4,18,-15,0,-24,7,18,1,0,18,16,21,-10,19,13,20,6,-1,-13,-19,-18,18,-20,22],[-6,-25,-20,-1,-12,-2,-12,12,-17,14,24,13,-20,-25,-23,-22,7,12,3,-10,2,-7,6,16,-12,6,-2,1,-11,0,-2,-15,-1,5,7,5,0,-24,-8,23,5,-13,-21,-9,20,17,-23,7,25,-9],[-6,-10,-7,16,24,9,-23,12,0,-14,0,2,-16,-17,-19,-2,-2,-14,-7,-23,8,7,-4,-3,-22,23,-14,-22,21,-16,-11,-20,-24,19,-25,10,-9,-3,8,-5,1,-25,19,23,-15,8,7,-24,6,4],[-3,-18,-20,-12,-7,20,17,2,-20,-10,12,-19,19,-1,8,22,-17,20,-3,-24,0,-21,-15,-18,-1,0,-9,12,-9,-24,-22,-18,-1,-9,10,19,3,1,-19,22,-6,-23,0,15,11,-8,21,13,21,-5],[23,-22,-15,2,14,-25,-8,5,-2,-5,-6,6,18,-7,18,-1,-25,6,8,-24,-9,-13,24,24,-17,18,-5,2,11,21,20,-12,-11,-20,0,-12,-13,7,2,-25,19,1,-9,-14,14,1,-15,17,-18,-11],[-8,4,12,7,1,-16,24,4,-6,1,2,22,-23,9,16,-4,15,0,-11,15,9,-10,11,18,-1,-10,-23,10,18,-16,-15,-24,23,18,15,10,-10,0,-24,0,-8,17,10,25,-20,6,0,10,4,-18],[14,9,-21,21,-6,24,-12,22,0,18,-9,-3,9,-22,-11,-20,24,5,-21,-23,-9,-16,14,9,-6,20,-3,17,-19,17,1,25,-21,-18,-10,0,-4,-6,14,-14,-25,16,-22,-25,0,-24,-3,-2,20,0],[1,10,20,25,-5,25,12,-9,12,-16,14,-18,11,-3,11,-10,18,-11,17,6,-23,10,25,9,11,24,-11,-7,1,11,18,-1,20,-14,4,17,-13,-2,-11,2,13,-19,23,-16,11,-22,-11,-18,-13,-24],[17,15,15,-5,-5,5,-16,18,-12,-8,16,12,-23,10,9,10,16,-11,15,-4,12,22,-21,11,-10,14,24,6,-16,10,-18,-4,-24,24,-24,-22,4,3,18,-4,22,10,-17,-16,12,15,-21,-20,-13,2],[-5,7,10,-19,10,-5,-25,19,23,14,20,-19,22,-23,-24,1,-10,1,-7,-19,-18,-8,15,-13,7,6,15,-13,-15,14,0,14,3,15,-11,25,14,17,-10,-12,-11,-14,-4,-22,9,1,-20,-6,-10,-12],[-12,-19,-23,-25,23,-16,23,25,12,9,-7,-1,-6,0,17,12,-15,15,-9,-4,2,-14,20,7,8,13,-12,-16,-13,-15,-9,8,-3,-7,-15,9,15,23,10,-16,14,-24,-6,0,-16,0,15,-21,22,16],[0,-24,-13,-11,-17,19,-24,-7,22,-16,22,-17,0,14,22,-21,-16,-7,25,10,13,-6,-14,0,-1,-23,4,17,18,-25,5,6,6,25,-12,23,-16,-16,0,-9,-8,21,12,-18,22,-24,7,-20,-16,22],[-10,8,25,6,-7,-6,-22,-9,-1,10,-5,20,16,-22,-11,17,-20,-12,-13,-24,22,19,-4,25,7,1,-3,7,5,-13,-1,-5,16,18,-15,-3,18,-16,-6,-23,-25,-4,12,-23,-16,-2,-19,1,-10,7],[-25,-5,15,0,23,-22,16,-13,-10,4,-7,-13,9,3,-18,-9,-4,-7,-10,14,16,-21,5,19,-1,-6,0,-19,19,25,-13,24,11,-16,14,0,16,12,10,-10,18,-12,-8,2,-18,-6,19,-13,2,-19],[-5,9,-14,7,3,-13,-19,9,-14,-24,-20,-13,15,14,-5,7,-10,21,18,6,-15,0,13,-19,23,-8,-22,-23,8,-4,4,15,21,-4,-10,-5,23,-4,-15,13,8,10,-19,-23,-1,-14,-9,-9,12,-8],[12,-6,-25,12,22,2,-21,13,20,-21,14,10,-3,10,-10,25,13,0,17,-22,2,17,13,4,4,-18,3,-2,22,25,0,-10,13,-14,-8,22,21,9,2,-2,17,14,17,7,4,-13,-7,-12,0,7],[2,-24,17,0,-18,-21,-3,15,0,6,-25,-8,21,12,15,-19,-21,1,-22,19,14,21,25,2,-12,-25,24,0,25,3,14,7,-10,-18,14,-19,25,19,-21,17,-10,13,-7,-2,7,4,16,-3,-16,-22],[-21,-9,10,-9,-18,-16,-14,20,-10,-9,-7,-9,0,7,10,-15,6,0,12,13,11,-24,14,6,-9,0,-14,21,-25,-25,20,5,23,16,19,8,-19,-12,-16,-13,-6,12,23,22,-22,20,16,-11,22,-21],[19,13,24,2,0,-22,10,-14,6,-14,-10,18,-5,11,10,-2,21,-10,19,2,16,23,19,-16,9,-22,6,-6,19,18,-5,-17,11,-2,16,-3,-3,19,8,-8,-12,25,5,-2,12,-12,2,-11,22,-1],[23,-19,0,-19,4,-4,21,-11,-20,22,8,12,16,-24,-3,11,12,-25,-2,-1,-3,-20,-20,-6,3,16,-8,-10,-25,-4,7,15,9,15,9,-9,12,10,10,-25,11,17,-17,16,-13,9,3,-24,-3,1],[-2,-8,17,5,0,3,0,24,16,-19,6,-4,-2,2,-22,0,-7,-16,17,-3,2,-18,6,-7,1,-20,-21,-24,16,9,-17,0,-24,0,-15,5,8,-18,16,-8,12,19,-21,-23,-19,18,15,-25,18,11],[-22,-20,-19,-16,12,7,15,10,-14,17,23,6,9,1,14,4,22,13,4,5,-11,-16,-16,-21,1,24,7,5,-19,16,10,-19,2,5,4,-21,6,4,4,25,20,-21,-23,13,1,11,22,22,20,15]]

m = [row[::-1] for row in m]

M = len(m)
N = len(m[0])

#boxes = [(i,j) for i in range(M) for j in range(N)]
values = [[-200 for j in range(N)] for i in range(M) ]

for i in range(M):
    for j in range(N):
        if i == 0 and j == 0:
            values[0][0] = m[0][0]
        if i < M - 1:
            if values[i][j] + m[i+1][j] > values[i+1][j]:
                values[i+1][j] = values[i][j] + m[i+1][j]
        if j < N - 1:
            if values[i][j] + m[i][j+1] > values[i][j+1]:
                values[i][j+1] = values[i][j] + m[i][j+1]
                
print(values[M-1][N-1])