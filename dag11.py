# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import numpy as np

grid = list()
f = open("input.txt", "r")
for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    new_row=list()
    for col,n in enumerate(line):
        new_row.append(int(n))
    grid.append(new_row)
f.close()

grid = np.array(grid)
nrow=len(grid)
ncol=len(grid[0])

directions=[[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
n_flashes=0
step=0
while True:
    #Increase energy with one
    step+=1
    grid+=1
    
    #check flashing
    heap=list()
    for row,line in enumerate(grid):
        for col,n in enumerate(line):
            if n>9: heap.append([row,col])

    flashed=np.zeros((nrow,ncol))
    i=0
    while i<len(heap):
        [cr,cc]=heap[i]
        i+=1
        #Check flashing
        if grid[cr,cc]<=9 or flashed[cr,cc]==1: #Locatie flashed niet of heeft al geflashed
            continue
        #Count flashes and update this location
        flashed[cr,cc]=1
        n_flashes+=1
        grid[cr,cc]=0
        
        for [dr,dc] in directions:
            if cr+dr>=nrow or cr+dr<0 or cc+dc>=ncol or cc+dc<0:
                continue
            if flashed[cr+dr,cc+dc]==1:
                continue
            grid[cr+dr,cc+dc]+=1
            if grid[cr+dr,cc+dc]>9: #New flashing
                heap.append([cr+dr,cc+dc])
    if step==99:
        total_p1=n_flashes
    if 0 not in flashed:
        break
    
print("Part 1",total_p1)
print("Part 2",step)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))