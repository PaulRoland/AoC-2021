# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

hor=0
ver=0
ver2=0
aim=0
f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    n=int(line.split(' ')[1])
    if 'forward' in line:
        hor+=n
        ver2+=aim*n
    elif 'down' in line:
        ver+=n
        aim+=n
    elif 'up' in line:
        ver-=n
        aim-=n
        
    
f.close()



print("Part 1",hor*ver)
print("Part 2",hor*ver2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))