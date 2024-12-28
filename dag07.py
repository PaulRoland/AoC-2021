# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    numbers=[int(d) for d in line.split(',')]
    
f.close()

mindist1=10**99
best1=10*99
for i in range(0,1200):
    dist=0
    for number in numbers:
        dist+=abs(number-i)
    
    if dist<mindist1:
        mindist1=dist
        best=i


mindist2=10**99
best2=10*99
for i in range(0,1200):
    dist=0
    for number in numbers:
        n=abs(number-i)
        dist+=n*(n+1)/2
        print(number,i,dist)
    print(i,dist)
    if dist<mindist2:
        mindist2=dist
        best2=i        



print("Part 1",mindist1)
print("Part 2",mindist2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))