# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
herds_east=set()
herds_south=set()
for row,line in enumerate(f):
    line=line.replace('\n','')
    for col,s in enumerate(line):
        key=str(row)+','+str(col)
        if s=='v':
            herds_south.add(key)
        if s=='>':
            herds_east.add(key)
f.close()
nrow=row+1
ncol=col+1

moving=True
steps=0
#print(herds_east)
while moving==True:
    steps+=1
    moving=False
    moves=list()
    
    #consider east
    for key in herds_east:
        cr,cc=[int(d) for d in key.split(',')]
        key2=str(cr)+','+str((cc+1)%ncol)
        
        if key2 not in herds_east and key2 not in herds_south :
            moves.append([key,key2])
            moving=True
            
    for key1,key2 in moves:
        herds_east.remove(key1)
        herds_east.add(key2)
    
    #consider south
    moves=list()
    for key in herds_south:
        cr,cc=[int(d) for d in key.split(',')]
        key2=str((cr+1)%nrow)+','+str(cc)
        
        if key2 not in herds_east and key2 not in herds_south :
            moves.append([key,key2])
            moving=True
            
    for key1,key2 in moves:
        herds_south.remove(key1)
        herds_south.add(key2)
        
    #moving=False
        
    #consider south


print("Part 1",steps)
print("Part 2")
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))