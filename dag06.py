# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

mem = dict()
def new_fishes(n,days):
    total=1
    key=str(n)+','+str(days)
    if key in mem: return mem[key]
    
    while days>0:
        days-=1
        if n==0:
            total+=new_fishes(8,days)
            n=7
        n-=1
    
    mem.update({key:total})
    return total

f = open("input.txt", "r")
numbers=[int(d) for d in re.findall(r'\d+',f.readline())]
f.close()

total_p1=0
total_p2=0
for number in numbers:
    total_p1+=new_fishes(number,80)
    total_p2+=new_fishes(number,256)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))