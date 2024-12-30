# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import numpy as np
start_time = time.time_ns()


def shortest_path(grid):
    directions=[[0,1],[1,0],[0,-1],[-1,0]]
    nrow=len(grid)
    ncol=len(grid[0])
    start_r=0
    start_c=0
    end_r=nrow-1
    end_c=ncol-1
    
    heap=[[start_r,start_c,0]]
    i=0
    min_scores=np.ones((nrow,ncol))*10**9

    while i<len(heap):
        cr,cc,cur_score=heap[i]
        i+=1
        if cur_score>min_scores[cr,cc]:
            continue

        if cr==end_r and cc==end_c:
            continue
    
        #Nieuwe paden
        for [dr,dc] in directions:
            if cr+dr>=nrow or cr+dr<0 or cc+dc>=ncol or cc+dc<0:
                continue
            new_score=cur_score+int(grid[cr+dr][cc+dc])
            if new_score<min_scores[cr+dr][cc+dc]:
                min_scores[cr+dr][cc+dc]=new_score
                heap.append([cr+dr,cc+dc,new_score])
                
    return int(min_scores[end_r][end_c])
    

f = open("input.txt", "r")
map1=list()

for row,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    line_data=''
    for col,s in enumerate(line):
        line_data+=s
    map1.append(line_data)
f.close()

###Part 1
total_p1=shortest_path(map1)
        
### Part 2
#Extend the map
map2=list()
for ro in range(0,5):
    for row,line in enumerate(map1):
        new_line=''
        for co in range(0,5):
            for col,s in enumerate(line):
                new_line+=str((int(s)+ro+co-1)%9+1)
        map2.append(new_line)
total_p2=shortest_path(map2)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))