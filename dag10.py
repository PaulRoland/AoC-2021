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
    line=line.replace('\n','')
    data.append(line)
f.close()

points={']':57,')':3,'}':1197,'>':25137}
points2={')':1,']':2,'}':3,'>':4}
closes={'(':')','[':']','{':'}','<':'>'}

total_p1=0
total_p2s=list()
for line in data:
    string=''
    valid=True
    for s in line:
        if s in closes:
            string+=s
        elif s==closes[string[-1]]:
            string=string[:-1]
        else:
            total_p1+=points[s]
            valid=False
            break
        
    if valid==True:
        score=0
        closing_string=''
        for s in string[::-1]:
            closing_string+=closes[s]
            score*=5
            score+=points2[closing_string[-1]]
        total_p2s.append(score)
total_p2s.sort()
            
print("Part 1",total_p1)
print("Part 2",total_p2s[len(total_p2s)//2])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))