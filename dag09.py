# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    data.append(line)
    
f.close()
ncol=len(data[0])
nrow=len(data)

##Part 1
directions= [[0,1],[1,0],[0,-1],[-1,0]]
total_p1=0
basin_start=list()
for row,line in enumerate(data):
    for col,s in enumerate(line):
        lowest=True
        for dr,dc in directions:
            if row+dr<0 or row+dr>=nrow or col+dc<0 or col+dc>=ncol:
                continue
            if data[row][col]>=data[row+dr][col+dc]:
                lowest=False
        
        if lowest==True:
            total_p1+=int(s)+1
            basin_start.append([row,col])


##Part 2
cell_visited=dict()
basin_sizes=list()
for [cr,cc] in basin_start:
    i=0
    heap=[[cr,cc]]
    key=str(cr)+','+str(cc)
    cell_visited.update({key:1})
    size=1
    
    while i<len(heap):
        [cr,cc]=heap[i]
        for dr,dc in directions:
            if cr+dr<0 or cr+dr>=nrow or cc+dc<0 or cc+dc>=ncol:
                continue
            if data[cr+dr][cc+dc]>=data[cr][cc] and data[cr+dr][cc+dc]!='9':
                key=str(cr+dr)+','+str(cc+dc)
                if key in cell_visited:
                    continue
                size+=1
                heap.append([cr+dr,cc+dc])
                cell_visited.update({key:1})
        i+=1
    basin_sizes.append(size)
basin_sizes.sort(reverse=True)
                


print("Part 1",total_p1)
print("Part 2",basin_sizes[0]*basin_sizes[1]*basin_sizes[2])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))